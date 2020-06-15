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
import cfg
import copyright

def create(parent,cnt):
    return Info(parent,cnt)

#---------------------------------------------------------------------------
class Info(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id = wx.NewId(), name = '',
              parent = prnt, pos = wx.Point(0, 0),  size = (200,-1),
              style = wx.SYSTEM_MENU, title = copyright.longversion)
              #style = wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP, title = copyright.longversion)
        self.SetIcon(wx.Icon(cfg.path_img + "/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.AggMenu = cnt[3]
        #self.IDMENU = cnt[4]
        Nid = wx.NewId()
        #self.font = self.GetFont()
        #self.SetClientSize(wx.Size(300, 360))
        self.Center(wx.BOTH)            
        #self.pnl = wx.Panel(id = wx.NewId(), name = 'panel',
        #      	parent = self)#, pos = wx.Point(0, 0))
        png = wx.Image((cfg.path_img + "splash.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        immagine=wx.StaticBitmap(self, -1, png)#, 
              #(5,5),
              #wx.DLG_SZE(self.pnl, png.GetWidth(), png.GetHeight()))
              #wx.Size(png.GetWidth(), png.GetHeight()))
        #self.SetFont(self.font) 
        
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        self.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False)) #modifica
        self.font = self.GetFont() #modifcia

        self.SetBackgroundColour(wx.NamedColour('white'))
        testo=wx.StaticText(self, -1, copyright.copyright)# , 
              #wx.DLG_PNT(self.pnl, 10, 100))
        self.canc = wx.Button(self, Nid, cfg.vcclose)#, 
              #wx.DLG_PNT(self.pnl , 170, 190), 
              #wx.DLG_SZE(self.pnl, cfg.btnSzeLH, cfg.btnSzeV))
        
        for x in self.GetChildren(): x.SetFont(self.font)

        
        self.canc.SetFocus()
        #self.SetFont(self.font)
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(immagine, 0, wx.ALIGN_CENTER | wx.ADJUST_MINSIZE | wx.ALL, 20)
        sizer_1.Add(testo, 0, wx.ALIGN_CENTER | wx.ADJUST_MINSIZE | wx.LEFT | wx.RIGHT, 20)
        sizer_1.AddSpacer((-1,20))
        sizer_1.Add(self.canc, 0, wx.ALIGN_CENTER | wx.ADJUST_MINSIZE | wx.ALL, 20)
        #sizer_1.AddSpacer((-1,10))
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        
        
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
        #box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(0)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)
        
        
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.Bind(wx.EVT_CLOSE, self.Close)
        
    def Close(self, event):
        #self.AggMenu(True,self.IDMENU)
        #wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        self.Destroy() 
              

