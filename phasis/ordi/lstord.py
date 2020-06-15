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
    return LstOrd(parent,cnt)

#---------------------------------------------------------------------------
class LstOrd(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        self.cnt = cnt
        Nid = wx.NewId()
        self.ttl = cnt[0]
        self.tipoord = cnt[1]
        self.tcpart="C"
        #self.ottl="Ordini Clienti"
        if self.tipoord=='OF':
            self.tcpart = "F"
            #self.ottl = "Ordini Fornitori"
        self.tbl = "ordi1"
        self.tblart = "articoli"
        self.rec = cnt[2]
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        self.CMD = cnt[5]
        #self.font = self.GetFont()
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz = self.__MDI__.GetConnAZ()
        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon = self.__MDI__.GetDataC()
        self.dzDatiAzienda = self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,130),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        wx.StaticLine(self.pnl , -1, 
              wx.DLG_PNT(self.pnl , 5,140), 
              wx.DLG_SZE(self.pnl , 335,-1))
        wx.StaticText(self.pnl , -1, _("Rag. Soc.:"), 
              wx.DLG_PNT(self, 25,152))
        self.ragsoc = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 70,150), 
              wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT),
              wx.TE_PROCESS_ENTER)
        self.cragsoc = wx.BitmapButton(self.pnl, -1, png,
              wx.DLG_PNT(self.pnl , 175,150),
              wx.DLG_SZE(self.pnl , 12,12))
        wx.StaticText(self.pnl , -1, _("Cod. Articolo:"),  
              wx.DLG_PNT(self, 25,167))
        self.cod = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 70,165), 
              wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT),
              wx.TE_PROCESS_ENTER)
        self.ccod=wx.BitmapButton(self.pnl, -1, png,
              wx.DLG_PNT(self.pnl , 175,165),
              wx.DLG_SZE(self.pnl , 12,12))
        self.rbEVA = wx.RadioButton(self.pnl, Nid, cfg.vcEVA,
              wx.DLG_PNT(self.pnl, 210,165), 
              wx.DLG_SZE(self.pnl, 60,10))
        self.rbNOEVA = wx.RadioButton(self.pnl, Nid, cfg.vcCONF,
              wx.DLG_PNT(self.pnl, 275,165), 
              wx.DLG_SZE(self.pnl, 60,10) )
        self.rbPRE = wx.RadioButton(self.pnl, Nid, cfg.vcPREV,
              wx.DLG_PNT(self.pnl, 275,175), 
              wx.DLG_SZE(self.pnl, 60,10))
        self.stt_ord = wx.TextCtrl(self.pnl, -1, "C", 
              wx.DLG_PNT(self.pnl, 285,137))  
        self.ok = wx.Button(self.pnl , Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl , 210,150), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 275,150), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFocus()
        #self.SetFont(self.font)
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)
        
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.DblClick)
        self.ccod.Bind(wx.EVT_BUTTON, self.FndOrd)
        self.cragsoc.Bind(wx.EVT_BUTTON, self.FndOrd)
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        self.cod.Bind(wx.EVT_TEXT_ENTER, self.FndOrd)
        self.ragsoc.Bind(wx.EVT_TEXT_ENTER, self.FndOrd)
        self.rbEVA.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.rbNOEVA.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.rbPRE.Bind(wx.EVT_RADIOBUTTON, self.RadioB)  
        
        self.rbEVA.SetValue(False)
        self.rbNOEVA.SetValue(True)
        self.rbPRE.SetValue(False)
        self.Start(self)


    def Start(self, event):
        if self.tipoord=="OC" or self.tipoord=="OF" :        
            self.rbEVA.Show(True)
            self.rbNOEVA.Show(True)
            self.rbPRE.Show(False)
            self.rbEVA.SetValue(False)
            self.rbNOEVA.SetValue(True)
            self.rbPRE.SetValue(False)
            self.stt_ord.SetValue('C')

        if self.tipoord=="PC" or self.tipoord=="PF" :        
            self.rbEVA.Show(False)
            self.rbNOEVA.Show(False)
            self.rbPRE.Show(False)
            self.rbEVA.SetValue(False)
            self.rbNOEVA.SetValue(False)
            self.rbPRE.SetValue(True)
            self.stt_ord.SetValue('P')
        self.stt_ord.Show(False)
        self.stt_ord.Enable(False)
        self.ClearLC(self)
        if self.cod.GetValue()=='' or self.cod.GetValue()=='None':
            self.FndSelOrd(self)
            self.ragsoc.SetFocus()
        else:
            self.FndSelOrdCodArt(self)
            self.cod.SetFocus()
        #self.RadioB(self)

    def ClearLC(self, event):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Num Ord"))
        self.lc.InsertColumn(1, _("Data Ord"))
        self.lc.InsertColumn(2, _("Tipo"))
        self.lc.InsertColumn(3, _("Ragione Sociale ( Cognome Nome)"))
        self.lc.InsertColumn(4, _("Vs. Data"))
        self.lc.InsertColumn(5, _("Anno"))
        self.lc.InsertColumn(6, _("Telefono"))
        self.lc.InsertColumn(7, _("Mobile"))
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 150,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self, 30,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self, 60,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self, 60,-1).width)
        #self.lc.SetFont(self.font)

    def CnvNone(self, evt):
        if(evt==None or evt=="None" or evt==0):self.val=""
        else:self.val=evt
        
    def RadioB(self, evt):
        if (self.rbEVA.GetValue()==True):
            self.stt_ord.SetValue("E")
            self.ragsoc.SetFocus()
        elif (self.rbNOEVA.GetValue()==True):
            self.stt_ord.SetValue("C")
            self.ragsoc.SetFocus()
        elif (self.rbPRE.GetValue()==True):
            self.stt_ord.SetValue("P")
            self.ragsoc.SetFocus()
        self.FndOrd(self)
            
    def FndOrd(self, evt):
        self.ClearLC(self)
        if self.cod.GetValue()=='':
            self.FndSelOrd(self)
            self.ragsoc.SetFocus()
        else:
            self.FndSelOrdCodArt(self)
            self.cod.SetFocus()

    def FndSelOrdCodArt(self, evt):        
        rowlc=0
        cod = self.cod.GetValue()
        stt_ord = self.stt_ord.GetValue() 
        sql = """ select tord, aaaa, nord, data_ord, cod_cf, rag_soc1,rag_soc2,
                  vsdata, cod_age, vsord from
                  (select num_ord as nord , anno as aaaa, tipo_ord as tord 
                  from  ordi2  
                  where cod like "%s" and anno = "%s" and tipo_ord = "%s" ),
                  ordi1 
                  where ordi1.num_ord = nord and ordi1.anno = aaaa 
                  and ordi1.tipo_ord = tord """
        valueSql = "%" + cod +"%", self.annoc, self.tipoord
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()
                    tipo_ord = row[0]
                    anno = str(row[1])       
                    num_ord = str(row[2])
                    data_ord = str(row[3])
                    #cod_cf = str(row[4])
                    ragsoc1 = row[5]
                    ragsoc2 = row[6]
                    vsdata = str(row[7])
                    self.CnvNone(row[7])
                    vsdata = self.val  
                    #codage = str(row[8])
                    #vsord = str(row[9])
                    self.lc.InsertStringItem(rowlc, num_ord)
                    self.lc.SetStringItem(rowlc, 1, data_ord)
                    self.lc.SetStringItem(rowlc, 2, tipo_ord)
                    self.lc.SetStringItem(rowlc, 3, ragsoc1 + " " + ragsoc2)
                    self.lc.SetStringItem(rowlc, 4, vsdata)
                    self.lc.SetStringItem(rowlc, 5, anno)
                    self.lc.SetStringItem(rowlc, 6, telefono)
                    self.lc.SetStringItem(rowlc, 7, mobile)
                    self.lc.SetItemData(0,0)                  
        except StandardError, msg:
            self.__MDI__.MsgErr("lstord"," FndSelOrdCodArt Error %s " % (msg))
        self.CnAz.commit()
          
        
    def FndSelOrd(self, evt):        
        rowlc = 0
        ragsoc = self.ragsoc.GetValue()
        stt_ord = self.stt_ord.GetValue()
        print self.tipoord
	if self.tipoord=='OC' or self.tipoord=='PC':
            sql = """ select * from ordi1 where rag_soc1 like "%s" 
	              and tipo_ord=="%s" or tipo_ord=="%s" 
		      and anno = "%s" and stt_ord = "%s" 
                      order by num_ord desc """
            valueSql = "%" + ragsoc + "%", "OC", "PC", self.annoc, stt_ord 
	if self.tipoord=='OF' or self.tipoord=='PF':
            sql = """ select * from ordi1 where rag_soc1 like "%s" 
	              and (tipo_ord=="%s" or tipo_ord=="%s") 
		      and anno = "%s" and stt_ord = "%s" 
                      order by num_ord desc """
            valueSql = "%" + ragsoc + "%", "OF", "PF", self.annoc, stt_ord 
	else:	
	    sql = """ select * from ordi1 where rag_soc1 like "%s" 
                      and tipo_ord = "%s"
                      and anno = "%s" and stt_ord = "%s" 
                      order by num_ord desc """
            valueSql = "%" + ragsoc + "%", self.tipoord, self.annoc, stt_ord

        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
	    print sql % valueSql
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()      
                    num_ord = str(row[2])
                    self.CnvNone(row[24])
                    vsord =self.val
                    self.CnvNone(row[25])
                    vsdata=self.val     
                    data_ord = str(row[3])
                    cod_cf = str(row[4])
                    ragsoc1 = row[5]
                    ragsoc2 = row[6]
                    tel = str(row[5])
                    mob = str(row[6])
                    codage = str(row[18])
                    tipo_ord = row[0]
                    anno = str(row[1])                    
                    self.lc.InsertStringItem(rowlc, num_ord)
                    self.lc.SetStringItem(rowlc, 1, data_ord)
                    self.lc.SetStringItem(rowlc, 2, tipo_ord)
                    self.lc.SetStringItem(rowlc, 3, ragsoc1 + " " + ragsoc2)
                    self.lc.SetStringItem(rowlc, 4, vsdata)
                    self.lc.SetStringItem(rowlc, 5, anno)
                    self.lc.SetStringItem(rowlc, 6, telefono)
                    self.lc.SetStringItem(rowlc, 7, mobile)
                    self.lc.SetItemData(0,0)
        except StandardError, msg:
            self.__MDI__.MsgErr("lstord"," FndSelOrd Error %s " % (msg))
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
        tbl = self.tipoord 
        if self.tipoord=="OC": idmenu=6001 #ordini clienti
        elif self.tipoord=="PC": idmenu=6005 #offerte clienti
        elif self.tipoord=="OF": idmenu=6012 #ordini fornitori
        elif self.tipoord=="PF": idmenu=6021 #offerte fornitori
        rec = (self.lc.GetItemText(self.currentItem))
        self.CMD(idmenu,rec,tbl)
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)


