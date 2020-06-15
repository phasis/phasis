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
    return LstVend(parent,cnt)

#---------------------------------------------------------------------------
class LstVend(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        #wx.Frame.__init__(self, id = wx.NewId(), name = '',
        #      parent = prnt, pos = wx.Point(0, 0), 
        #      style = wx.DEFAULT_FRAME_STYLE , title = cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        Nid = wx.NewId()
        self.ttl = cnt[0]
        self.tipodoc = cnt[1]
        self.tcpart = "C"
        #self.ottl = "Gestione Documenti"
        self.tbl = "docu1"
        self.tblart = "articoli"
        self.rec = cnt[2]
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        self.CMD = cnt[5]
        #self.SetClientSize(wx.Size(600, 400))
        #self.font = self.GetFont()
        self.__MDI__ =  wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz = self.__MDI__.GetConnAZ()
        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon =  self.__MDI__.GetDataC()
        
        self.pnl = wx.Panel(id = wx.NewId(), name = 'panel',
              parent = self, pos = wx.Point(0, 0),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)#, size = wx.Size(680, 400))
        self.pnl.SetFont(self.font)
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,120),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,130), 
              wx.DLG_SZE(self.pnl , 335,-1))
        wx.StaticText(self.pnl , -1, _("Rag. Soc.:"), 
              wx.DLG_PNT(self, 25,142))
        self.rs = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 70,140), 
	      wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.crs = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 175,140), wx.DLG_SZE(self.pnl , 12,12))
        wx.StaticText(self.pnl , -1, _("Cod. Articolo:"), 
              wx.DLG_PNT(self, 25,157))
        self.cod = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 70,155), 
	      wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)
        self.ccod = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 175,155), wx.DLG_SZE(self.pnl , 12,12))
        self.TIPO_DOC = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 210,140), 
              wx.DLG_SZE(self.pnl, 125,-1), [],
	      wx.CB_DROPDOWN | wx.CB_SORT | wx.TE_PROCESS_ENTER)
        self.vTIPO_DOC =  wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,90))
        self.rbEVA = wx.RadioButton(self.pnl, Nid, cfg.vcEVA,
              wx.DLG_PNT(self.pnl, 210,155), 
              wx.DLG_SZE(self.pnl, 60,10), wx.RB_GROUP )
        self.rbNOEVA = wx.RadioButton(self.pnl, Nid, cfg.vcNOEVA,
              wx.DLG_PNT(self.pnl, 275,155), wx.DLG_SZE(self.pnl, 65,10))
        self.stt_doc = wx.TextCtrl(self.pnl, -1, "E", 
              wx.DLG_PNT(self.pnl, 285,137))  
        self.ok = wx.Button(self.pnl , Nid, cfg.vcok, 
              wx.DLG_PNT(self.pnl , 210,170), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 275,170), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFocus()
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        #self.SetFont(self.font)
        
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
        #self.lc.Bind(wx.EVT_LIST_KEY_DOWN, self.DblClick)
        self.ccod.Bind(wx.EVT_BUTTON, self.FndDoc)
        self.crs.Bind(wx.EVT_BUTTON, self.FndDoc)
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        #self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick)
        self.cod.Bind(wx.EVT_TEXT_ENTER, self.FndDoc)
        self.rs.Bind(wx.EVT_TEXT_ENTER, self.FndDoc)
        self.TIPO_DOC.Bind(wx.EVT_COMBOBOX, self.SelTIPO_DOC)
        self.rbEVA.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.rbNOEVA.Bind(wx.EVT_RADIOBUTTON, self.RadioB)     
        
        self.vTIPO_DOC.SetValue(cfg.tipodoc_lst)
        self.SelCOMBO(self)
        self.Start(self)

    def Start(self, event):        
        self.vTIPO_DOC.Enable(False)
        self.vTIPO_DOC.Show(False)
        self.vTIPO_DOC.SetValue(self.vTIPO_DOC.GetValue())
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Num Doc"))
        self.lc.InsertColumn(1, _("Vs. Data"))
        self.lc.InsertColumn(2, _("Cod. Anag"))
        self.lc.InsertColumn(3, _("Rag. Soc.1 Cognome"))
        self.lc.InsertColumn(4, _("Rag. Soc.2 Nome"))
        self.lc.InsertColumn(5, _("Cod. Age"))
        self.lc.InsertColumn(6, _("Data Doc"))
        self.lc.InsertColumn(7, _("Tipo Doc"))
        self.lc.InsertColumn(8, _("Anno"))        
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self, 37,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 50,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 90,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self, 90,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self, 30,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self, 50,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(8, wx.DLG_SZE(self, 30,-1).width)
        #self.lc.SetFont(self.font)
        self.stt_doc.Show(False)
        if self.vTIPO_DOC.GetValue()=='B1':
            self.rbNOEVA.SetValue(True)
            self.stt_doc.SetValue("C")
            self.rbEVA.Show(True)
            self.rbNOEVA.Show(True)
        else:
            self.stt_doc.SetValue("E")
            self.rbEVA.Show(False)
            self.rbNOEVA.Show(False)
        if self.cod.GetValue()=='' or self.cod.GetValue()=='None':
            self.FndSelDoc(self)
            self.rs.SetFocus()
        else:
            self.FndSelDocCodArt(self)
            self.cod.SetFocus()
        self.RadioB(self)

    def RadioB(self, evt):
        if (self.rbEVA.GetValue()==True):
            self.stt_doc.SetValue("E")
            self.rs.SetFocus()
        if (self.rbNOEVA.GetValue()==True):
            self.stt_doc.SetValue("C")
            self.rs.SetFocus()
            
    def SelCOMBO(self, evt):      
        vTIPO_DOC = self.vTIPO_DOC.GetValue()
        self.TIPO_DOC.Clear()      
        sql = " select * from tabgen "
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)                 
            while (1):
                row = cr.fetchone () 
                if row==None: 
                    break          
                if (row[0]=="TIPODOC"):
                    if (row[1]==vTIPO_DOC):self.sTIPO_DOC = row[2]
                    self.TIPO_DOC.Append(row[2],row[1])
            self.TIPO_DOC.Append('Lista Completa','FF')   ##########
            if ('FF'==vTIPO_DOC):self.sTIPO_DOC = 'Lista Completa'    #########
        except StandardError, msg:
            self.__MDI__.MsgErr("lstvend","SelCOMBO Error %s" % (msg))
        self.CnAz.commit()
        cntTIPO_DOC = 0
        cntTIPO_DOC = self.TIPO_DOC.FindString(self.sTIPO_DOC)
        self.TIPO_DOC.Select(cntTIPO_DOC)
       
    def SelTIPO_DOC(self, evt):
        self.Sel(evt)
        self.vTIPO_DOC.SetValue(self.cb_val)
        if self.vTIPO_DOC.GetValue()=='B1':
            self.rbEVA.Show(True)
            self.rbNOEVA.Show(True)
        else:
            self.rbEVA.Show(False)
            self.rbNOEVA.Show(False)
        self.FndDoc(self)
            
    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str =  evt.GetString()
        evt.Skip()

    def CnvNone(self, evt):
        if(evt==None or evt=="None" or evt==0):self.val = ""
        else:self.val = evt
        
    def FndDoc(self, evt):
        self.Start(self)

    def FndSelDocCodArt(self, evt):        
        rowlc = 0
        val = self.cod.GetValue().upper()
        stt_doc = self.stt_doc.GetValue() #"C"
        tipodoc = self.vTIPO_DOC.GetValue()#self.tipodoc
	sql = """ select tdoc ,aaaa, ndoc, ddoc, cod_cf, rag_soc1, rag_soc2,
	          vsdata,cod_age from
       		 (select num_doc as ndoc, datadoc as ddoc, anno as aaaa, 
		  tipo_doc as tdoc from  docu2  
                  where cod like '%s' and anno = '%s' and tipo_doc = '%s' ),
		  docu1  
                  where docu1.num_doc = ndoc and docu1.anno = aaaa 
		  and docu1.tipo_doc = tdoc """
        valueSql = '%'+val+'%',self.annoc,tipodoc
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()
                    tipo_doc = str(row[0])
                    anno = str(row[1])       
                    num_doc = str(row[2])
                    data_doc = str(row[3])
                    cod_cf = str(row[4])
                    ragsoc1 = str(row[5]).title()
                    ragsoc2 = str(row[6]).title()
                    vsdata = str(row[7])
                    self.CnvNone(row[7])
                    vsdata = self.val  
                    codage = str(row[8])
                    self.lc.InsertStringItem(rowlc, num_doc)    
                    self.lc.SetStringItem(rowlc, 1, vsdata)
                    self.lc.SetStringItem(rowlc, 2, cod_cf)
                    self.lc.SetStringItem(rowlc, 3, ragsoc1)
                    self.lc.SetStringItem(rowlc, 4, ragsoc2)
                    self.lc.SetStringItem(rowlc, 5, codage)
                    self.lc.SetStringItem(rowlc, 6, data_doc)
                    self.lc.SetStringItem(rowlc, 7, tipo_doc)
                    self.lc.SetStringItem(rowlc, 8, anno)
                    self.lc.SetItemData(0,0)                  
        except StandardError, msg:
            self.__MDI__.MsgErr("lstvend","FndSelDocCodArt Error %s" % (msg))
        self.CnAz.commit()
         
    def FndSelDoc(self, evt):        
        rowlc = 0
        val = self.rs.GetValue().title()
        stt_doc = self.stt_doc.GetValue() #"C"
        tipodoc = self.vTIPO_DOC.GetValue()#self.tipodoc
        valueSql = '%'+val+'%', tipodoc, self.annoc, stt_doc
        valueSql1 = '%'+val+'%', self.annoc, stt_doc
        sql = """ select * from docu1 
	          where rag_soc1 like '%s' and tipo_doc = '%s' and anno = '%s' 
		  and stt_doc = '%s' order by rag_soc1 asc """
        sql1 = """ select * from docu1 
	          where rag_soc1 like '%s' and anno = '%s' 
		  and stt_doc = '%s' order by num_doc asc """
        try:
            cr = self.CnAz.cursor ()
            if tipodoc!='FF' :cr.execute(sql % valueSql) 
            else: cr.execute(sql1 % valueSql1)
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()      
                    num_doc = str(row[2])
                    vsdata = str(row[16])
                    self.CnvNone(row[16])
                    vsdata = self.val  
                    data_doc = str(row[3])
                    cod_cf = str(row[4]).title()
                    ragsoc1 = str(row[5]).title()
                    ragsoc2 = str(row[6]).title()
                    codage = str(row[18]).title()
                    tipo_doc = str(row[0]).title()
                    anno = str(row[1])                    
                    self.lc.InsertStringItem(rowlc, num_doc)    
                    self.lc.SetStringItem(rowlc, 1, vsdata)
                    self.lc.SetStringItem(rowlc, 2, cod_cf)
                    self.lc.SetStringItem(rowlc, 3, ragsoc1)
                    self.lc.SetStringItem(rowlc, 4, ragsoc2)
                    self.lc.SetStringItem(rowlc, 5, codage)
                    self.lc.SetStringItem(rowlc, 6, data_doc)
                    self.lc.SetStringItem(rowlc, 7, tipo_doc)
                    self.lc.SetStringItem(rowlc, 8, anno)
                    self.lc.SetItemData(0,0)         
        except StandardError, msg:
            self.__MDI__.MsgErr("lstvend","FndSelDoc Error %s" % (msg))
        self.CnAz.commit()
        self.currentItem = 0

    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal()==wx.ID_OK:
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
        #ottl = self.ottl
        #Dir = "vend"
        #Mod = "vendite"
        rec = (self.lc.GetItemText(self.currentItem))
        tbl = self.getColTxt(self.currentItem,7)
        #AggMenu = self.AggMenu
        #IDMENU = self.IDMENU    
        #self.CMD(rec, Dir, Mod, ottl, tbl)
        self.CMD(3001,rec,tbl)       
        #self.AggMenu(True,self.IDMENU)
        #self.Destroy()

    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)

