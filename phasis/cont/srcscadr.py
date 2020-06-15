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

ttl=_("Ricerca Documenti")

def create(parent,cnt):
    return srcscadr(parent,cnt)

#---------------------------------------------------------------------------
class srcscadr(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        #self.tipo_doc = cnt[0]
        #print self.cnt
        vTIPO_SCAD = cnt[0].GetValue()
        anno = cnt[1]		
        data_scad_int = cnt[2]
        data_scad_int_A = cnt[6] 
        vCF = cnt[4]
        num_doc= cnt[5]
        print "srcscadr"
    
        #data_doc = cnt[3].GetValue()		
        #stt_doc = cnt[5]
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
        self.lc.InsertColumn(0, _("Data Scad"))
        self.lc.InsertColumn(1, _("Anno"))
        self.lc.InsertColumn(2, _("Tipo Scad"))
        self.lc.InsertColumn(3, _("Rag. Soc.1 Cognome"))
        self.lc.InsertColumn(4, _("Rag. Soc.2 Nome"))
        self.lc.InsertColumn(5, _("Num. Scad."))

        self.lc.SetColumnWidth(0, wx.DLG_SZE(self, 40,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 60,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 95,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self, 90,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self, 30,-1).width)
        #self.lc.SetFont(self.font)
        rowlc=0
        val=""
        sql = """ select * from scad 
                  where tipo_scad = "%s" 
                  and t_cpart = "%s" 
                  and data_scad_int >= "%s" 
                  and data_scad_int <= "%s"
                  order by data_scad_int desc """
        valueSql =  vTIPO_SCAD, vCF, int(data_scad_int),int(data_scad_int_A)

        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()    
                    data_scad = str(row[2])
                    anno = str(row[1])
                    tipo_scad = str(row[3])
                    ragsoc1 = str(row[7]).title()
                    ragsoc2 = str(row[8]).title()
                    num_scad = str(row[0])
                                  
                    self.lc.InsertStringItem(rowlc, data_scad)
                    self.lc.SetStringItem(rowlc, 1, anno)    
                    self.lc.SetStringItem(rowlc, 2, tipo_scad)
                    self.lc.SetStringItem(rowlc, 3, ragsoc1)
                    self.lc.SetStringItem(rowlc, 4, ragsoc2)
                    self.lc.SetStringItem(rowlc, 5, num_scad)                     
                    self.lc.SetItemData(0,0)
        except StandardError, msg:
            self.__FRM__.MsgErr("srcscadr"," srcscad Error %s" % (msg))
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
        self.cnt[2]=self.getColTxt(self.currentItem, 1)  	
        self.cnt[5].SetValue(self.getColTxt(self.currentItem, 5))
        self.cnt[3](self)   
        self.Destroy() 
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)
