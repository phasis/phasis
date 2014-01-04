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
import cfg

ttl=_("Testo")

def create(parent,cnt):
    return Testo(parent,cnt)

#---------------------------------------------------------------------------
class Testo(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        
        self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        
        self.cnt = cnt	
        ctesto = cnt[0]
        Nid = wx.NewId()
        #self.font=self.GetFont()
        self.__MDI__= wx.GetApp().GetPhasisMdi()
       
        self.font=self.__MDI__.font
        self.SetFont(self.font)

        
        self.pnl = wx.Panel(id=100, name='panel',
              	parent=self, pos=wx.Point(0, 0)) #, size=wx.Size(680, 400))
        #testo wdim = 0 x 40 caratteri
        #      wdim = 95 x 70 caratteri
        wdim = 10
        self.pnl.SetFont(self.font)
        
        self.dtesto = wx.TextCtrl(self.pnl , -1,"",
                wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 120+wdim,100),
                wx.TE_MULTILINE )
        self.dtesto.SetFont(self.font)
        
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,115), 
              wx.DLG_SZE(self.pnl , 115+wdim,-1))
        
        self.ok = wx.Button(self.pnl , -1, cfg.vcconf, 
              wx.DLG_PNT(self.pnl , 30+wdim,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
        self.ok.SetFont(self.font)
        
        self.canc=wx.Button(self.pnl , -1, cfg.vccanc,
              wx.DLG_PNT(self.pnl , 80+wdim,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
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
        #self.Bind(wx.EVT_LEFT_DCLICK, self.DblClick, self.ctesto)
        self.Bind(wx.EVT_CLOSE, self.Close)
               
    def Ok(self, evt):
        self.cnt[0].SetValue(self.dtesto.GetValue())  
        self.cnt[1](self)    
        self.Destroy() 
        
    def Close(self, evt):
        self.Destroy() 
                      
    
        

