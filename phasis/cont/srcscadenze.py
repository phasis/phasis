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

ttl=''

def create(parent,cnt):
    return srcscadenze(parent,cnt)

#---------------------------------------------------------------------------
class srcscadenze(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        self.SetTitle(cnt[0])
        Nid = wx.NewId()
        self.CnAz=prnt.CnAz
        #self.font=self.GetFont()
        self.__FRM__ = prnt
        
        
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)

        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0))
        self.pnl.SetFont(self.font)  
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,110),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        self.lc.InsertColumn(0, _("Valore"))
        self.lc.InsertColumn(1, _("Descrizione"))        
        self.lc.InsertColumn(2, "") 
        self.lc.InsertColumn(3, _("Contropartita"))     
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self,  70,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self,  100,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self,  0,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self,  50,-1).width)
        #self.lc.SetFont(self.font)
        rowlc=0
        cod=self.cnt[4]
        vCF=self.cnt[5]
        valueSql = cod,vCF
        sql = " SELECT * FROM scadenze WHERE cod = '%s' AND val1 = '%s' AND val2 = 'S' ORDER BY descriz DESC "
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()
                    cod=str(row[0])
                    valore = str(row[1])
                    descriz = str(row[2])
                    vCF = str(row[3])
                    self.lc.InsertStringItem(rowlc, valore)
                    self.lc.SetStringItem(rowlc, 1, descriz)
                    self.lc.SetStringItem(rowlc, 2, cod)
                    self.lc.SetStringItem(rowlc, 3, vCF)
                    self.lc.SetItemData(0,0)
        except StandardError, msg:
            self.__FRM__.MsgErr("srcscadenze"," Fnd Error %s " % (msg)) 
        self.CnAz.commit()
        self.currentItem = 0
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,115), 
              wx.DLG_SZE(self.pnl , 300,-1))
        #self.pnl.SetFont(self.font)
        self.ok = wx.Button(self.pnl , Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl , 195,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc=wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 255,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        
        self.canc.SetFocus()
        #self.SetFont(self.font)
        box_sizer = wx.BoxSizer(wx.VERTICAL)
        box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        self.SetAutoLayout(1)
        self.SetSizer(box_sizer)
        box_sizer.Fit(self)
        
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.DblClick)       
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnListSelect)
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.DblClick)

    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    def Ok(self, event):
        self.DblClick(self.currentItem)
        
    def Close(self, event):
        self.Destroy() 
              
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

    def DblClick(self, event):
        self.cnt[1].SetValue(self.getColTxt(self.currentItem, 0))   
        self.cnt[2].SetValue(self.getColTxt(self.currentItem, 1))
        self.cnt[5] = self.getColTxt(self.currentItem, 3)      
        self.cnt[3](self)   
        self.Destroy() 
        
    def OnListSelect(self, event):
        self.currentItem = event.m_itemIndex


