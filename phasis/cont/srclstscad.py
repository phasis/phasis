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
    return SrcScad(parent,cnt)

#---------------------------------------------------------------------------
class SrcScad(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        #self.SetTitle(cnt[0])
        Nid = wx.NewId()
        self.CnAz=prnt.CnAz
        #self.font=self.GetFont()
        #self.__FRM__ = prnt
        
        
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)

        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0))
        self.pnl.SetFont(self.font)  
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,110),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        self.lc.InsertColumn(0, _("Num."),width=wx.DLG_SZE(self.pnl, 30,-1).width)
        self.lc.InsertColumn(1, _("Data Scad."),width=wx.DLG_SZE(self.pnl, 42,-1).width)
        self.lc.InsertColumn(2, _("Tipo Scad."),width=cfg._COLSZ0_) #width=wx.DLG_SZE(self.pnl, 45,-1).width)
        self.lc.InsertColumn(3, _("Condizioni di pagamento"),width=cfg._COLSZ0_) #width=wx.DLG_SZE(self.pnl, 85,-1).width)
        self.lc.InsertColumn(4, _("Ragione Sociale"),width=wx.DLG_SZE(self.pnl, 70,-1).width)
        self.lc.InsertColumn(5, _("D/A"),width=wx.DLG_SZE(self.pnl, 18,-1).width)
        self.lc.InsertColumn(6, _("Totale"),width=wx.DLG_SZE(self.pnl, 40,-1).width)
        self.lc.InsertColumn(7, _("Stato"),width=wx.DLG_SZE(self.pnl, 52,-1).width)
        self.lc.InsertColumn(8, _("Data Doc."),width=wx.DLG_SZE(self.pnl, 38,-1).width)
        self.lc.InsertColumn(9, _("Tipo Doc."),width=cfg._COLSZ0_) #width=wx.DLG_SZE(self.pnl, 70,-1).width)
        self.lc.InsertColumn(10, _("Num. Doc."),width=cfg._COLSZ0_) #width=wx.DLG_SZE(self.pnl,38,-1).width)

        #self.lc.SetFont(self.font)
        # < diegom 
        rowlc = 0
        anno = self.cnt[0]


        
        #valueSql= tbl,tipoDoc
 
        sql = " select * from scad WHERE anno = '" + anno + "' order by data_scad_int DESC"
        
        # > diegom
        
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            rows = cr.fetchall()
            #print rows
            for row in rows:
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()   
                    self.lc.InsertStringItem(rowlc, str(row[0]))
                    self.lc.SetStringItem(rowlc, 1, str(row[2]))
                    self.lc.SetStringItem(rowlc, 2, str(row[3]))

                    self.lc.SetStringItem(rowlc, 3, str(row[4]))
                    self.lc.SetStringItem(rowlc, 4, row[7])
                    self.lc.SetStringItem(rowlc, 5, str(row[12]))
                    self.__MDI__.CnvVM(row[13])
                    totale=self.__MDI__.val
                    self.lc.SetStringItem(rowlc, 6, totale)
                    if row[14]=="R":
                        self.lc.SetStringItem(rowlc, 7, "Registrato")
                    elif row[14]=="S":
                        self.lc.SetStringItem(rowlc, 7, "Saldato")

                    self.lc.SetStringItem(rowlc, 8, str(row[9]))
                    self.lc.SetStringItem(rowlc, 9, str(row[10]))
                    if row[11]!=0: self.lc.SetStringItem(rowlc, 10, str(row[11]))

                    self.lc.SetItemData(0,0)
        except StandardError, msg:
            self.__MDI__.MsgErr("lstscad","RmpLc Error %s " % (msg))
        if not rows: self.Message("Dati non presenti",self.ttl) 
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
        self.cnt[2](self)   
        self.Destroy() 
        
    def OnListSelect(self, event):
        self.currentItem = event.m_itemIndex


