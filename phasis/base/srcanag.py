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
import fdb
import sys

ttl = _("Ricerca Anagrafica")

def create(parent,cnt):
    return SrcAnag(parent,cnt)

#---------------------------------------------------------------------------
class SrcAnag(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id = wx.NewId(), name = '',
              parent = prnt, pos = wx.Point(10, 50), size = wx.DefaultSize,
              style = wx.DEFAULT_FRAME_STYLE, title = ttl)
        self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        
        #self.font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False)#self.GetFont()
        #self.font=wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
        #y=wx.ScreenDC().MaxY()
        #if y>=1200 : numfont=16
        #elif y>=1024 : numfont=14
        #else : numfont=12
        #if cfg.FONTFISSO!=0 : numfont=cfg.FONTFISSO
        #self.font.SetPointSize(numfont)
        #self.SetFont(self.font)
        self.__MDI__=wx.GetApp().GetPhasisMdi()
        self.font=self.__MDI__.font
        self.SetFont(self.font) 
        
        
        self.cnt = cnt	
        tcpart = cnt[0]
        if (tcpart=="Z"):
            fdb.CnDBAZ
            self.tblanag = "aziende"
        if (tcpart=="C" or tcpart=="F" or tcpart=="V" or tcpart=="T"):
            self.CnAz = prnt.CnAz
            self.tblanag = "anag"
        if (tcpart=="A"):
            self.CnAz = prnt.CnAz
            self.tblanag = "agenti"
        self.tcpart = tcpart
        Nid = wx.NewId()
        #self.font = self.GetFont()
        self.__FRM__ = prnt.__MDI__
        self.pnl = wx.Panel(id = wx.NewId(), name = 'panel',
              	parent = self, pos = wx.Point(0, 0))
        self.pnl.SetFont(self.font)
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,110),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        self.lc.SetFont(self.font)
        
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Rag. Soc.1 Cognome"))
        self.lc.InsertColumn(2, _("Rag. Soc.2 Nome"))
        self.lc.InsertColumn(3, _("Indirizzo"))
        self.lc.InsertColumn(4, _("Telefono"))
        self.lc.InsertColumn(5, _("Mobile"))
        self.lc.InsertColumn(6, _("Ufficio"))
        self.lc.InsertColumn(7, _("Fax"))
        
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self,  30,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self,  70,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self,  70,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self,  100,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self,  0,-1).width)
        #self.lc.SetFont(self.font)
        
        rowlc = 0
        cod = self.cnt[1].GetValue().upper()
        val = self.cnt[2].GetValue().upper()
        valueSql = '%'+val.title()+'%', self.tcpart
        ## Funzione cerca
        if self.tblanag=='agenti' :
            sql = """ SELECT * FROM agenti 
                      WHERE rag_soc1 like '%s' AND  t_cpart = '%s'  
                      ORDER BY rag_soc1 DESC """
        elif self.tblanag=='aziende' :
            sql = """ SELECT * FROM aziende 
                      WHERE rag_soc1 like '%s' AND  t_cpart = '%s'  
                      ORDER BY rag_soc1 DESC """
        else:
            sql = """ SELECT * FROM anag 
                      WHERE rag_soc1 like '%s' AND  t_cpart = '%s'  
                      ORDER BY rag_soc1 DESC """
        try:
            if self.tcpart=="Z" :cr = fdb.CnDBAZ.cursor ()
            else: cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()      
                    t_cpart = str(row[0])
                    cod = str(row[1])
                    ragsoc1 = str(row[3]).title()
                    ragsoc2 = str(row[4]).title()
                    indiriz = str(row[6]).title()
                    tel_abi = str(row[18])
                    tel_uff = str(row[19])
                    mobile = str(row[20])
                    fax = str(row[21])
                    self.lc.InsertStringItem(rowlc, cod)    
                    self.lc.SetStringItem(rowlc, 1, ragsoc1)
                    self.lc.SetStringItem(rowlc, 2, ragsoc2)
                    self.lc.SetStringItem(rowlc, 3, indiriz)
                    self.lc.SetStringItem(rowlc, 4, tel_abi)
                    self.lc.SetStringItem(rowlc, 5, mobile)
                    self.lc.SetStringItem(rowlc, 6, tel_abi)
                    self.lc.SetStringItem(rowlc, 7, fax)
                    self.lc.SetItemData(0,0)
                    #self.lc.SetItemFont(rowlc,self.font)
        except StandardError, msg:
            self.__FRM__.MsgErr("SrcAnag"," Cerca Error %s"  % (msg))
        if self.tcpart=="Z" :fdb.ClDBAZ.commit()    
        else: self.CnAz.commit()     
        self.currentItem = 0
        #wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,115), 
        #      wx.DLG_SZE(self.pnl , 300,-1))
        self.ok = wx.Button(self.pnl , Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl , 195,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.ok.SetFont(self.font)
        self.canc = wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 255,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFont(self.font)
        self.canc.SetFocus()
        #self.SetFont(self.font)
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
        self.cnt[1].SetValue(self.lc.GetItemText(self.currentItem))
        self.cnt[2].SetValue(self.getColTxt(self.currentItem, 1))     
        self.cnt[3](self)   
        self.Destroy() 
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)


