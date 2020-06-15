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

ttl=_("Scheda Articoli")

def create(parent,cnt):
    return Scheda_Art(parent,cnt)

#---------------------------------------------------------------------------
class Scheda_Art(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        self.cnt = cnt
        self.ttl=ttl
        Nid = wx.NewId()
        self.CnAz=prnt.CnAz
        #self.font=self.GetFont()
        self.annoc = prnt.annoc
        self.datacon = prnt.datacon
        self.CnAz = prnt.CnAz
        self.font = self.GetFont()
        self.__FRM__ = prnt.__MDI__
        self.__CMD__ = prnt.__MDI__.CMD

        self.__MDI__= wx.GetApp().GetPhasisMdi()
       
        self.font=self.__MDI__.font
        self.SetFont(self.font)


        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              	parent=self, pos=wx.Point(0, 0))
        self.pnl.SetFont(self.font)  

        self.lbcodart=wx.StaticText(self.pnl, -1, _("Codice :"), 
              wx.DLG_PNT(self.pnl, 5,7))
        self.lbcodart.SetFont(self.font)
        
        self.codart = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 55,5), 
            wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT))
        self.codart.SetFont(self.font)
        
        self.ccodart=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl, 120,5),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))

        wx.StaticText(self.pnl, -1, _("BarCode :"), 
              wx.DLG_PNT(self.pnl, 140,7)).SetFont(self.font)
        
        self.codbar = wx.TextCtrl(self.pnl, Nid, "",
       	      wx.DLG_PNT(self.pnl, 180, 5), 
            wx.DLG_SZE(self.pnl, 75,cfg.DIMFONTDEFAULT))
        self.codbar.SetFont(self.font)
        
        self.ccodbar=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl, 260,5),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        wx.StaticText(self.pnl, -1, _("Descrizione :"), 
              wx.DLG_PNT(self.pnl, 5,22)).SetFont(self.font)
        
        self.descriz = wx.TextCtrl(self.pnl, Nid, "",
            wx.DLG_PNT(self.pnl, 55,20), wx.DLG_SZE(self.pnl, 200,cfg.DIMFONTDEFAULT))                    
        self.descriz.SetFont(self.font)
        
        self.cdescriz=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...",
            wx.DLG_PNT(self.pnl, 260,20),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        wx.StaticText(self.pnl, -1, _("Costo :"), wx.DLG_PNT(self.pnl, 5,37)).SetFont(self.font)
        
        self.costo = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 55, 35), 
            wx.DLG_SZE(self.pnl, 58,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.costo.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Prezzo :"), wx.DLG_PNT(self.pnl, 115,37)).SetFont(self.font)
        
        self.prezzo1 = wx.TextCtrl(self.pnl, Nid, "",
            wx.DLG_PNT(self.pnl, 155, 35),
            wx.DLG_SZE(self.pnl, 58,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.prezzo1.SetFont(self.font)
        
        self.lbum = wx.StaticText(self.pnl, -1, _("UM :"), 
              wx.DLG_PNT(self.pnl, 240,37))
        self.lbum.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Q.ta`  Dare :"), 
              wx.DLG_PNT(self.pnl, 5,52)).SetFont(self.font)
        
        self.qt_car = wx.TextCtrl(self.pnl, Nid, "",
            wx.DLG_PNT(self.pnl, 55, 50), 
            wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.qt_car.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Q.ta` Avere :"), 
              wx.DLG_PNT(self.pnl, 100,52)).SetFont(self.font)
        
        self.qt_sca = wx.TextCtrl(self.pnl, Nid, "",
            wx.DLG_PNT(self.pnl, 140, 50), 
            wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.qt_sca.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Q.ta` Saldo :"), 
              wx.DLG_PNT(self.pnl, 187,52)).SetFont(self.font)
        
        self.qt_sal = wx.TextCtrl(self.pnl, Nid, "",
            wx.DLG_PNT(self.pnl, 230, 50),
            wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.qt_sal.SetFont(self.font)
        
        self.lc = wx.ListCtrl(self.pnl , Nid, 
            wx.DLG_PNT(self.pnl, 5,80), 
            wx.DLG_SZE(self.pnl , 330,50), 
            wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        self.lc.SetFont(self.font)
        
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,145),  
              wx.DLG_SZE(self.pnl , 340,-1))
        
        #self.pnl.SetFont(self.font)
        self.ok = wx.Button(self.pnl , Nid, cfg.vcconf, 
            wx.DLG_PNT(self.pnl , 195,160), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.ok.SetFont(self.font)
        
        self.canc=wx.Button(self.pnl , Nid, cfg.vccanc, 
            wx.DLG_PNT(self.pnl , 255,160), 
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
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.DblClick)
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        
        self.Start(self)

    def Start(self, evt):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Numero"))
        self.lc.InsertColumn(1, _("Data mov."))
        self.lc.InsertColumn(2, _("Causa mag."))
        self.lc.InsertColumn(3, _("Q.ta` carico"))
        self.lc.InsertColumn(4, _("Q.ta` scarico"))
        self.lc.InsertColumn(5, _("Prezzo"))
        self.lc.InsertColumn(6, _("Totale"))
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self, 30,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 45,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 45,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 50,-1).width)        
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self,  50,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self,  60,-1).width)
        self.codbar.Enable(False)
        self.codart.Enable(False)
        self.descriz.Enable(False)
        self.ccodbar.Enable(False)
        self.ccodart.Enable(False)
        self.cdescriz.Enable(False)
        self.costo.Enable(False)
        self.prezzo1.Enable(False)
        self.codart.SetValue(self.cnt[0])
        self.descriz.SetValue(self.cnt[1])
        self.costo.SetValue(self.cnt[2])
        self.prezzo1.SetValue(self.cnt[3])
        self.qt_car.Enable(False)
        self.qt_sca.Enable(False)
        self.qt_sal.Enable(False)
        self.FndMovCodArt(self)

    def FndMovCodArt(self, evt):   
        ## Funzione Cerca Articolo    
        rowlc=0
        cod=self.codart.GetValue().upper()
        try:
            cr = self.CnAz.cursor ()
            sql = """ SELECT ANNO,NUM_MOV,DATAMOV,CAUMA,QT,COSTO_UN,
                      TOT_RIGA, UM FROM
                    movmag WHERE COD like '%s' and ANNO = '%s' """
            valueSql = cod, self.annoc
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            qt_cart=0
            qt_scat=0
            um = ''
            for row in rows:            
                for rowlc in range(1):                    
                    row_lc = self.lc.GetItemCount()      
                    anno = str(row[0])
                    nummov = str(row[1])
                    datamov = str(row[2])
                    cauma= str(row[3])
                    qt =  float(row[4])
                    qt_car=0
                    qt_sca=0
                    um = str(row[7])
                    if (cauma=="801" or cauma=="802") : 
                        qt_car = qt
                    elif (cauma=="901" or cauma=="902") :
                        qt_sca = qt
                    qt_cart+=qt_car
                    qt_scat+=qt_sca
                    self.__FRM__.CnvVM5(qt_car)
                    qtcar=self.__FRM__.val  
                    self.__FRM__.CnvVMQT(qt_sca)
                    qtsca=self.__FRM__.val  
                    self.__FRM__.CnvVMQT(str(row[5]))
                    costo_un = self.__FRM__.val  
                    self.__FRM__.CnvVMQT(str(row[6]))
                    tot_riga = self.__FRM__.val  
                    self.lc.InsertStringItem(rowlc, nummov)    
                    self.lc.SetStringItem(rowlc, 1, datamov)
                    self.lc.SetStringItem(rowlc, 2, cauma)
                    self.lc.SetStringItem(rowlc, 3, qtcar)
                    self.lc.SetStringItem(rowlc, 4, qtsca)
                    self.lc.SetStringItem(rowlc, 5, costo_un)
                    self.lc.SetStringItem(rowlc, 6, tot_riga)
                    self.lc.SetItemData(0,0)   
        except StandardError, msg:
            print "FndMovCodArt Error %s" % (msg)
        self.CnAz.commit()
        if (qt_cart==""):qt_cart=0
        if (qt_scat==""):qt_scat=0
        self.__FRM__.CnvVMQT(qt_cart)
        vqtcar=self.__FRM__.val      
        self.__FRM__.CnvVMQT(qt_scat)
        vqtsca=self.__FRM__.val     
        self.__FRM__.CnvVMQT(qt_cart-qt_scat)
        vqtsal=self.__FRM__.val 
        self.__FRM__.CnvVMQT('0')
        vnull = self.__FRM__.val
        if (vqtcar==""):vqtcar = vnull
        if (vqtsca==""):vqtsca = vnull
        if (vqtsal==""):vqtsal = vnull
        self.qt_car.SetValue(vqtcar)
        self.qt_sca.SetValue(vqtsca)
        self.qt_sal.SetValue(vqtsal)
        self.lbum.SetLabel("U.M.:  " + um)
 
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
        #ttl = "Gestione Movimenti"
        #Dir = "maga"
        #Mod = "movmag"
        idmenu=5001
        tbl = "movmag"
        rec=(self.lc.GetItemText(self.currentItem))
        self.__CMD__(idmenu,rec,tbl)
        #self.__CMD__(rec, Dir, Mod, ttl, tbl)       
        self.Destroy()
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)

