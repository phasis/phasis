# -*- coding: iso-8859-1 -*-
#
#  Copyright (C) 2001 - 2020 Massimo Gerardi all rights reserved.
#
#  Author: Massimo Gerardi massimo.gerardi@gmail.com
#
#  Copyright (c) 2020 Qsistemi.com.  All rights reserved.
#
#  Viale Giorgio Ribotta, 11 (Roma)
#  00144 Roma (RM) - Italy
#  Phone: (+39) 06.87.163
#  
#
#  Si veda file COPYING per le condizioni di software.
#
#   www.qsistemi.com - italy@qsistemi.com

 

import wx
from cfg import *
import cfg


def create(parent,cnt):
    return LstMov(parent,cnt)

#---------------------------------------------------------------------------
class LstMov(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        #wx.Frame.__init__(self, id=wx.NewId(), name='',
        #      parent=prnt, pos=wx.Point(0, 0), 
        #      style=wx.DEFAULT_FRAME_STYLE , title=cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.SetClientSize(wx.Size(600, 400))
        self.cnt = cnt
        Nid = wx.NewId()
        self.ttl=cnt[0]
        self.tipomov =cnt[1]
        self.tcpart = "M"
        #self.ottl = "Gestione Movimenti"
        self.rec = cnt[2]
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        self.CMD = cnt[5]
        self.__MDI__=wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz = self.__MDI__.GetConnAZ()
        self.annoa = self.__MDI__.GetAnnoC()
        self.datacon = self.__MDI__.GetDataC()
        self.dzDatiAzienda = self.__MDI__.dzDatiAzienda
        #self.font = self.GetFont()         
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0), size = wx.DLG_SZE(self,600/2,400/2), #size=wx.Size(600, 400),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,130),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,140), 
              wx.DLG_SZE(self.pnl , 335,-1))
        wx.StaticText(self.pnl , -1, _("Desc. Articolo:"), 
              wx.DLG_PNT(self, 25,152))
        # < diegom num_mov rimane nome ma diventa descrizione articolo
        self.num_mov = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 70,150), 
              wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT))
        self.cnum_mov=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 175,150),
              wx.DLG_SZE(self.pnl , 12,12))
        wx.StaticText(self.pnl , -1, _("Cod. Articolo:"), 
              wx.DLG_PNT(self, 25,167))
        self.cod = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 70,165), 
              wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT))
        self.ccod=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 175,165),
              wx.DLG_SZE(self.pnl , 12,12))
        self.ok = wx.Button(self.pnl , Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl , 210,150), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc=wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 275,150), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFocus()
        #self.SetFont(self.font)
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)
        
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.DblClick)
        self.ccod.Bind(wx.EVT_BUTTON, self.FndMov)
        self.cnum_mov.Bind(wx.EVT_BUTTON, self.FndMov)
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        self.cod.Bind(wx.EVT_TEXT_ENTER, self.FndMov)
        self.num_mov.Bind(wx.EVT_TEXT_ENTER, self.FndMov)
        
        self.Start(self)

    def Start(self, event):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Anno"))
        self.lc.InsertColumn(1, _("Numero"))
        self.lc.InsertColumn(2, _("Data"))
        self.lc.InsertColumn(3, _("Causale"))
        self.lc.InsertColumn(4, _("Codice"))
        self.lc.InsertColumn(5, _("Descrizione"))
        self.lc.InsertColumn(6, _("UM"))
        self.lc.InsertColumn(7, _("Qt"))
        self.lc.InsertColumn(8, _("Prezzo"))
        self.lc.InsertColumn(9, _("Cod. Mag"))
        self.lc.InsertColumn(10, _("Cod. CF"))
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 60,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self, 60,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self, 120,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(8, wx.DLG_SZE(self, 60,-1).width)
        self.lc.SetColumnWidth(9, wx.DLG_SZE(self, 30,-1).width)
        self.lc.SetColumnWidth(10, wx.DLG_SZE(self, 30,-1).width)
        #self.lc.SetFont(self.font)
        if self.cod.GetValue()=='' or self.cod.GetValue()=='None':
            self.FndSelMov(self)
            self.num_mov.SetFocus()
        else:
            self.FndSelMovCodArt(self)
            self.cod.SetFocus()

    def FndMov(self, evt):
        self.Start(self)

    def FndSelMovCodArt(self, evt): 
        ## Funzione Cerca Articolo
        rowlc = 0
        val = self.cod.GetValue().upper()
        anno = self.annoa
        sql = """ select ANNO,NUM_MOV,DATAMOV,CAUMA,COD_MAG,CFM,COD,
                  DESCRIZ,UM,QT,COSTO_UN from movmag  
                  where cod like '%s' and anno = '%s' """
        valueSql = '%'+val+'%', anno
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):                    
		    row_lc = self.lc.GetItemCount()      
                    anno = str(row[0])
                    nummov = str(row[1])
                    datamov = str(row[2])
                    cauma= str(row[3])
                    codmag = str(row[4])
                    cfm = str(row[5])
                    cod = str(row[6])
                    descriz = row[7]
                    um = str(row[8])
                    qt = str(row[9])
                    costo_un = str(row[10])
                    self.lc.InsertStringItem(rowlc, anno)    
                    self.lc.SetStringItem(rowlc, 1, nummov)
                    self.lc.SetStringItem(rowlc, 2, datamov)
                    self.lc.SetStringItem(rowlc, 3, cauma)
                    self.lc.SetStringItem(rowlc, 4, cod)
                    self.lc.SetStringItem(rowlc, 5, descriz)
                    self.lc.SetStringItem(rowlc, 6, um)
                    self.lc.SetStringItem(rowlc, 7, qt)
                    self.lc.SetStringItem(rowlc, 8, costo_un)
                    self.lc.SetStringItem(rowlc, 9, codmag)
                    self.lc.SetStringItem(rowlc, 10, cfm)
                    self.lc.SetItemData(0,0)   
        except StandardError, msg:
            self.__MDI__.MsgErr("lstmov","FndSelMovCodArt Error %s " % (msg))
        self.CnAz.commit()
          

    # < diegom Modifica funzione per ricerca descrizione articolo invece che num_mov
    def FndSelMov(self, evt): 
        ## Funzione Cerca Movine
        rowlc = 0
        vnum_mov = self.num_mov.GetValue()
        #print vnum_mov
        if vnum_mov=="" :
            sql = " select * from movmag where anno = '%s' order by num_mov asc "
            valueSql = self.annoa
        else:
            sql = " select * from movmag where descriz like '%s' and anno = '%s' order by num_mov asc "
            valueSql = '%'+vnum_mov+'%', self.annoa
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()      
                    anno = str(row[0])
                    nummov = str(row[1])
                    datamov = str(row[2])
                    cauma= str(row[3])
                    codmag = str(row[4])
                    cfm = str(row[5])
                    cod = str(row[8])
                    descriz = row[11]
                    um = str(row[12])
                    qt = str(row[14])
                    costo_un = str(row[15])
                    self.lc.InsertStringItem(rowlc, anno)    
                    self.lc.SetStringItem(rowlc, 1, nummov)
                    self.lc.SetStringItem(rowlc, 2, datamov)
                    self.lc.SetStringItem(rowlc, 3, cauma)
                    self.lc.SetStringItem(rowlc, 4, cod)
                    self.lc.SetStringItem(rowlc, 5, descriz)
                    self.lc.SetStringItem(rowlc, 6, um)
                    self.lc.SetStringItem(rowlc, 7, qt)
                    self.lc.SetStringItem(rowlc, 8, costo_un)
                    self.lc.SetStringItem(rowlc, 9, codmag)
                    self.lc.SetStringItem(rowlc, 10, cfm)
                    self.lc.SetItemData(0,0)
        except StandardError, msg:
            self.__MDI__.MsgErr("lstmov","FndSelMov Error %s " % (msg))
        self.CnAz.commit()
        self.currentItem = 0

    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
            
    def Ok(self, event):
        self.DblClick(self.currentItem)
        
    def Close(self, event):
        self.AggMenu(True,self.IDMENU)
        wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        #self.Destroy()
              
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

    def DblClick(self, event):
        #ottl=self.ottl
        #Dir="maga"
        #Mod="movmag"
        tbl="movmag"
        rec=(self.getColTxt(self.currentItem, 1))
        #AggMenu=self.AggMenu
        #IDMENU=self.IDMENU
        #print rec, Dir, Mod, ottl, tbl
        #self.CMD(rec, Dir, Mod, ottl, tbl)       
        self.CMD(5001,rec,tbl)  
        #self.AggMenu(True,self.IDMENU)
        #self.Destroy()
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)

