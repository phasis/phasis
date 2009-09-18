# Copyright (C) 2003 - 2007  See Open - http://www.seeopen.it/
# Author: Massimo Gerardi <m.gerardi@mgsoft.it>
#
# Released under the terms of the GNU General Public License
# (version 2 or above)
#
# See COPYING for details.
#
#   www.phasis.it - info@phasis.it
#

import wx
#from wxPython.wx import *
#import wx.lib.buttons as buttons #import *
from cfg import *
import cfg
ttl=_("Ricerca Articoli")

def create(parent,cnt):
    return Cerca_Art(parent,cnt)

#---------------------------------------------------------------------------
class Cerca_Art(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        self.ttl=ttl
        self.tblart=self.cnt[0]
        self.CnAz = prnt.CnAz
        #self.font = self.GetFont()
        self.__FRM__ = prnt.__MDI__
        
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              	parent=self, pos=wx.Point(0, 0))
        self.pnl.SetFont(self.font)  
        
        self.lc = wx.ListCtrl(self.pnl , -1,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,110),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)

        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Descriz"))
        self.lc.InsertColumn(2, _("UM"))
        self.lc.InsertColumn(3, _("TG"))        
        self.lc.InsertColumn(1, _("Descriz"))
        self.lc.InsertColumn(2, _("UM"))
        self.lc.InsertColumn(3, _("TG"))
        self.lc.InsertColumn(4, _("Prezzo1"))
        self.lc.InsertColumn(5, _("Prezzo2"))
        self.lc.InsertColumn(6, _("Costo"))
        self.lc.InsertColumn(7, _("BarCode"))			
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self,  65,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 150,-1).width) 
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 20,-1).width)        
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self,  60,-1).width)     
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self,  0,-1).width) 
      
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,115), 
              wx.DLG_SZE(self.pnl , 300,-1))
        #self.pnl.SetFont(self.font)
        self.ok = wx.Button(self.pnl , -1, cfg.vcconf, 
              wx.DLG_PNT(self.pnl , 195,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc=wx.Button(self.pnl , -1, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 255,120), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.descriz_art = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 5, 120), 
              wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.descriz_art.SetFont(self.font)
        self.cdescriz_art = wx.BitmapButton(self.pnl, -1, png,
            wx.DLG_PNT(self.pnl, 95,120),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))

        #self.cdescriz_art=wx.Button(self.pnl , -1, "Cerca", 
              #wx.DLG_PNT(self.pnl , 95,120), 
              #wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))

        
        
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
        self.cdescriz_art.Bind(wx.EVT_BUTTON, self.OnListSelectDesc)       
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.DblClick)       
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnListSelect)
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.DblClick)
        self.descriz_art.Bind(wx.EVT_TEXT_ENTER, self.OnListSelectDesc)

        val=self.cnt[2].GetValue().upper()
        cod=self.cnt[1].GetValue().upper()
        valore = [val,cod]
        self.Start(valore)

    def Start(self, valore):  
        self.ClearLC(self) 
        val = valore[0] 
        cod = valore[1] 
        #self.lc.SetFont(self.font)
        rowlc=0

        sql = """ SELECT * FROM articoli 
                  WHERE descriz like '%s' ORDER BY descriz """
        if val == "":
            sql = """ SELECT * FROM articoli 
                      WHERE cod like '%s' ORDER BY descriz """
            val = cod
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % ('%'+val+'%'))
            rows = cr.fetchall()
            for row in rows:
                for rowlc in range(1):
                    rowlc = self.lc.GetItemCount()     
                    codart = row[0]
                    codbar = row[1]
                    descriz = row[2]
                    UM = str(row[3])
                    if (row[4]==None): tg=""
                    else: tg = str(row[4])
                    self.lc.InsertStringItem(rowlc, codart)    
                    self.lc.SetStringItem(rowlc, 1, descriz)
                    self.lc.SetStringItem(rowlc, 2, UM)
                    self.lc.SetStringItem(rowlc, 3, tg)
                    self.lc.SetStringItem(rowlc, 7, codbar)
                    self.__FRM__.CnvVMPZ(row[5])
                    price1=self.__FRM__.val
                    self.__FRM__.CnvVMPZ(row[6])
                    price2=self.__FRM__.val
                    self.__FRM__.CnvVMPZ(row[7])
                    costo=self.__FRM__.val
                    self.lc.SetStringItem(rowlc, 4, price1)
                    self.lc.SetStringItem(rowlc, 5, price2)
                    self.lc.SetStringItem(rowlc, 6, costo)           
        except StandardError, msg:
            self.__FRM__.MsgErr("scrart"," Cerca Articoli Error %s"  % (msg))
        self.CnAz.commit()       
        self.currentItem = 0

    def ClearLC(self, evt):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Descriz"))
        self.lc.InsertColumn(2, _("UM"))
        self.lc.InsertColumn(3, _("TG"))
        self.lc.InsertColumn(4, _("Prezzo1"))
        self.lc.InsertColumn(5, _("Prezzo2"))
        self.lc.InsertColumn(6, _("Costo"))
        self.lc.InsertColumn(7, _("BarCode"))			
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self,  65,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 150,-1).width) 
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 20,-1).width)        
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self,  60,-1).width)     
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self,  0,-1).width) 
        #self.lc.SetFont(self.font) 

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
        self.cnt[1].SetValue(self.lc.GetItemText(self.currentItem))
        self.cnt[2].SetValue(self.getColTxt(self.currentItem, 1))
        self.cnt[3](self)       
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Descriz"))
        self.lc.InsertColumn(2, _("UM"))
        self.lc.InsertColumn(5, _("TG"))
        self.lc.InsertColumn(3, _("Imponibile"))
        self.lc.InsertColumn(4, _("Prezzo"))
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self,  50,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 145,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 20,-1).width)        
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self,  60,-1).width)
        #self.lc.SetFont(self.font)
        #self.Destroy() 
        
    def OnListSelect(self, event):
        self.currentItem = event.m_itemIndex
 
    def OnListSelectDesc(self, event):
        val = self.descriz_art.GetValue()
        valore = val,""
        self.Start(valore)

