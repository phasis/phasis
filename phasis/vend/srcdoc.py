# -*- coding: iso-8859-1 -*-
#
#  Copyright (C) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 
#                2008, 2009, 2010, 2011, 2012, 2013 
#                2014 Massimo Gerardi all rights reserved.
#
#  Author: Massimo Gerardi massimo@gerardi.mobi
#
#  Copyright (c) 2013 Qsistemi.com.  All rights reserved.
#
#  Via Michele Rosi 184 - Aranova (Roma)
#  00050 Aranova (Roma) - Italy
#  Numero Telefono: +39 06 99.344.718
#  Numero Fax: +39 06 99.334.718
#
#  Si veda file COPYING per le condizioni di software.
#
#   www.qsistemi.com - info@qsistemi.com
#


import wx
from cfg import *
import cfg

ttl=_("Ricerca Documenti")

def create(parent,cnt):
    return SrcDoc(parent,cnt)

#---------------------------------------------------------------------------
class SrcDoc(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        #self.tipo_doc = cnt[0]
        #print self.cnt
        vTIPO_DOC = cnt[0].GetValue()
        anno = cnt[1].GetValue()		
        num_doc = cnt[2].GetValue()
        stt_doc = cnt[5]
        Nid = wx.NewId()
        self.CnAz = prnt.CnAz
        #self.font = self.GetFont()
        self.__FRM__ = prnt.__MDI__ 
        
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0), 
              size = wx.DLG_SZE(self,540/2,260/2)) #, #size=wx.Size(540, 260))
        self.pnl.SetFont(self.font)  
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 300,100),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)        
        self.lc.InsertColumn(0, _("Tipo Doc"))
        self.lc.InsertColumn(1, _("Num Doc"))
        self.lc.InsertColumn(2, _("Data Doc"))
        self.lc.InsertColumn(3, _("Rag. Soc.1 Cognome"))
        self.lc.InsertColumn(4, _("Rag. Soc.2 Nome"))
        self.lc.InsertColumn(5, _("Rag. Soc.2 Nome"))
        self.lc.InsertColumn(6, _("Anno"))
        self.lc.InsertColumn(7, _("Cod. Anag"))
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 60,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 95,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self, 90,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self, 20,-1).width)	
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self, 30,-1).width)
        #self.lc.SetFont(self.font)
        rowlc=0
        val=""
        if num_doc!="" and stt_doc=="":
            sql = """ select * from docu1 
                    where num_doc = "%s" and tipo_doc like "%s"  
                    and anno = "%s" """
            valueSql = int(num_doc), '%%', anno
        elif num_doc=="" and stt_doc=="" :
            sql = """ select * from docu1 
                    where num_doc like "%s" and tipo_doc = "%s"  
                    and anno = "%s" """
            valueSql = '%%', vTIPO_DOC, anno
        elif stt_doc!="" :
            sql = """ select * from docu1 
                    where num_doc like "%s" and tipo_doc = "%s"  
                    and anno = "%s" and stt_doc = "%s" """
            valueSql = '%%', vTIPO_DOC, anno, stt_doc
    
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()      
                    num_doc = str(row[2])
                    vsdata = str(row[16])
                    data_doc = str(row[3])
                    cod_cf = str(row[4]).title()
                    ragsoc1 = str(row[5]).title()
                    ragsoc2 = str(row[6]).title()
                    tel = str(row[5])
                    mob = str(row[6])
                    codage = str(row[18]).title()
                    tipo_doc = str(row[0]).title()
                    anno = str(row[1]).title()                      
                    stt_doc = str(row[66])                     
                    self.lc.InsertStringItem(rowlc,tipo_doc)
                    self.lc.SetStringItem(rowlc, 1, num_doc)    
                    self.lc.SetStringItem(rowlc, 2, data_doc)
                    self.lc.SetStringItem(rowlc, 3, ragsoc1)
                    self.lc.SetStringItem(rowlc, 4, ragsoc2)                    
                    self.lc.SetStringItem(rowlc, 5, stt_doc)
                    self.lc.SetStringItem(rowlc, 6, anno)
                    self.lc.SetStringItem(rowlc, 7, cod_cf)
                    self.lc.SetItemData(0,0)
        except StandardError, msg:
            self.__FRM__.MsgErr("srcdoc"," SrcDoc Error %s" % (msg))
        self.CnAz.commit()
        self.currentItem = 0
        wx.StaticLine(self.pnl , -1, 
              wx.DLG_PNT(self.pnl , 5,115),  wx.DLG_SZE(self.pnl , 300,-1))
        wx.StaticLine(self.pnl , -1, 
              wx.DLG_PNT(self.pnl , 5,115), wx.DLG_SZE(self.pnl , 300,-1))
        self.ok = wx.Button(self.pnl , Nid, cfg.vcconf,
              wx.DLG_PNT(self.pnl , 195,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
        self.canc=wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 255,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
        self.canc.SetFocus()
        #self.SetFont(self.font)
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        
        box_sizer = wx.BoxSizer(wx.VERTICAL)
       	box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        self.SetAutoLayout(1)
        self.SetSizer(box_sizer)
        box_sizer.Fit(self)
        
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.DblClick)
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        self.Bind(wx.EVT_CLOSE, self.Close)
               
    def Ok(self, event):
        self.DblClick(self.currentItem)
        
    def Close(self, event):
        self.Destroy() 
              
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

    def DblClick(self, event):    
        self.cnt[6].SetValue(self.lc.GetItemText(self.currentItem)) 
        self.cnt[2].SetValue(self.getColTxt(self.currentItem, 1))  	
        self.cnt[3].SetValue(self.getColTxt(self.currentItem, 2))
        self.cnt[4](self)   
        self.Destroy() 
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)
