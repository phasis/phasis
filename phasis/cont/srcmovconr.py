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
    return srcmovconr(parent,cnt)

#---------------------------------------------------------------------------
class srcmovconr(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        print "srcmovconr"
        self.cnt = cnt
        #self.tipo_doc = cnt[0]
        #print self.cnt
        anno = cnt[0]		
        data_int = cnt[1] 
        data_int_A = cnt[5]
        vCF = cnt[3]
        num_doc= cnt[4].GetValue()
     
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
        self.lc.InsertColumn(0, _("Data Mov"))
        self.lc.InsertColumn(1, _("Anno"))
        self.lc.InsertColumn(2, _("Num. Mov."))
        self.lc.InsertColumn(3, _("D/A"))
        self.lc.InsertColumn(4, _("Importo"))
        self.lc.InsertColumn(5, _("Cod."))
        self.lc.InsertColumn(6, _("Causale"))
        self.lc.InsertColumn(7, _("Cod."))
        self.lc.InsertColumn(8, _("Operazione"))
        self.lc.InsertColumn(9, _("Controp."))
        self.lc.InsertColumn(10, _("Totale Doc."))

        self.lc.SetColumnWidth(0, wx.DLG_SZE(self, 45,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 25,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 45,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self, 55,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self, 25,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self, 80,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self, 25,-1).width)
        self.lc.SetColumnWidth(8, wx.DLG_SZE(self, 80,-1).width)
        self.lc.SetColumnWidth(9, wx.DLG_SZE(self, 50,-1).width)
        self.lc.SetColumnWidth(10, wx.DLG_SZE(self, 55,-1).width)

        #self.lc.SetFont(self.font)
        rowlc=0
        val=""
        sql = """ select * from movcon 
                  where t_cpart = "%s" 
                  and data_int >= "%s" 
                  and data_int <= "%s" 
                  order by data_int asc """
        valueSql =  vCF, int(data_int), int(data_int_A)

        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:            
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()    
                    data_mov = str(row[12])
                    if data_mov=="  /  /    ": data_mov = str(row[2])
                    anno = str(row[0])
                    num_mov = str(row[1])
                    DA = str(row[17])
                    importo = str(row[8])
                    codcau = str(row[6])
                    causale = str(row[7])
                    codop = str(row[15])
                    operazione = str(row[29])
                    t_cpart = str(row[31])
                    totale = str(row[16])
                    self.lc.InsertStringItem(rowlc, data_mov)
                    self.lc.SetStringItem(rowlc, 1, anno)    
                    self.lc.SetStringItem(rowlc, 2, num_mov) 
                    self.lc.SetStringItem(rowlc, 3, DA)    
                    self.lc.SetStringItem(rowlc, 4, importo)
                    self.lc.SetStringItem(rowlc, 5, codcau)    
                    self.lc.SetStringItem(rowlc, 6, causale)
                    self.lc.SetStringItem(rowlc, 7, codop)    
                    self.lc.SetStringItem(rowlc, 8, operazione) 
                    self.lc.SetStringItem(rowlc, 9, t_cpart)
                    self.lc.SetStringItem(rowlc, 10, totale)

                    self.lc.SetItemData(0,0)
        except StandardError, msg:
            self.__FRM__.MsgErr("srcmovconr"," srcmovconr Error %s" % (msg))
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
        self.cnt[0]=self.getColTxt(self.currentItem, 1)  	
        self.cnt[4].SetValue(self.getColTxt(self.currentItem, 2))
        self.cnt[2](self)   
        self.Destroy() 
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)
