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
    return Inventa(parent,cnt)

#---------------------------------------------------------------------------
class Inventa(wx.ScrolledWindow):
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
        self.tipoord =cnt[1]
        self.tcpart="M"
        #self.ottl="Gestione Movimenti"
        self.tbl="movmag"
        self.tblart="articoli"
        self.rec=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]   
        #self.font=self.GetFont()
        self.color=self.GetBackgroundColour()
        Nid = wx.NewId()
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz=self.__MDI__.GetConnAZ()
        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon= self.__MDI__.GetDataC()
        self.dzDatiAzienda= self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0), size = wx.DLG_SZE(self,600/2,400/2), #size=wx.Size(600, 400),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,130),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,140), 
              wx.DLG_SZE(self.pnl , 335,-1))
        wx.StaticText(self.pnl , -1, _("Cod. Articolo:"), 
              wx.DLG_PNT(self, 15,152))
        self.cod = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 70,150), 
              wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.ccod=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 175,150),
              wx.DLG_SZE(self.pnl , 12,12))     
        self.canc = wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 210,150), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.int = wx.Button(self.pnl, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 275,150), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))		      
        self.canc.SetFocus()
        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 275,165), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))        
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
        self.int.Bind(wx.EVT_BUTTON, self.Start)          
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.ccod.Bind(wx.EVT_BUTTON, self.FndInv)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnListSelect)	
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.cod.Bind(wx.EVT_TEXT_ENTER, self.FndInv)
        
        self.Start(self)

    def Stampa(self, evt):   
        anno=self.annoc 
        tipo_doc='INV'
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,  
              tipo = tipo_doc,
              parametriSql = ("801", "301", anno, "901","901", anno),
              datiazienda = self.dzDatiAzienda,
              anteprima = True )

    def Start(self, event):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Descrizione"))
        self.lc.InsertColumn(2, _("Q.ta` Saldo"))
        self.lc.InsertColumn(3, _("Valore"))
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self, 60,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 120,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 60,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 100,-1).width)
        font=self.GetFont()
        self.lc.SetFont(font)
        self.FndSelInv(self)
        self.int.Enable(False)
        self.canc.Enable(True)  	
        self.cod.SetFocus()

    def FndInv(self, evt):
        self.Start(self)


    def FndSelInv(self, evt):
        if self.cod.GetValue()=='' or self.cod.GetValue()=='None': xcod='N'
        else : xcod = 'Y'
        rowlc = 0
        cod = self.cod.GetValue().upper()
        anno = self.annoc
        annoa = anno
        sql = """ select cod, descriz, um, ifnull(sum(qt),0) as qt, 
                  ifnull(sum(costo),0) as valore from
                  (select cod, descriz, um, sum(qt) as qt, 
                  sum(costo_un) as costo from movmag 
                  where (cauma="%s" or cauma="%s") and anno="%s" group by cod 
                  union
                  select cod, descriz, um,  (-(sum(qt))) as qt,  
                  sum(costo_un) as costo from movmag  
                  where (cauma = "%s" or cauma = "%s") and anno = "%s" group by cod)
                  group by cod order by descriz """
        valueSql = "801", "301", anno, "901","901", anno
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):                    
                    row_lc = self.lc.GetItemCount()      
                    cod = str(row[0])
                    descriz = str(row[1])
                    um = str(row[2])
                    self.__MDI__.CnvVMQT(row[3])
                    qt = str(self.__MDI__.val)
                    self.__MDI__.CnvVMPZ(row[4])
                    valore = str(self.__MDI__.val)
                    if qt == '' : 
                       qt = "--" 
                       valore = "--"
                    if xcod=='N':
                        self.lc.InsertStringItem(rowlc, cod)    
                        self.lc.SetStringItem(rowlc, 1, descriz)
                        self.lc.SetStringItem(rowlc, 2, qt)
                        self.lc.SetStringItem(rowlc, 3, valore)
                        self.lc.SetItemData(0,0)  
                    if xcod=='Y'  and self.cod.GetValue().upper()==cod :
                        self.lc.InsertStringItem(rowlc, cod)    
                        self.lc.SetStringItem(rowlc, 1, descriz)
                        self.lc.SetStringItem(rowlc, 2, qt)
                        self.lc.SetStringItem(rowlc, 3, valore)
                        self.lc.SetItemData(0,0)   
        except StandardError, msg:
            self.__MDI__.MsgErr("inventa","FndSelInv Error %s " % (msg))
        self.CnAz.commit()

    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
                    
    def Close(self, event):
        self.AggMenu(True,self.IDMENU)
        wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        #self.Destroy()
              
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()
       
    def LstAct(self, event):
        self.cod.SetValue(self.lc.GetItemText(self.currentItem))
        self.FndInv(self)
        self.int.Enable(True)
        self.canc.Enable(False)
        self.cod.SetValue("")
        self.int.SetFocus()

    def OnListSelect(self, event):
        self.currentItem = event.m_itemIndex
