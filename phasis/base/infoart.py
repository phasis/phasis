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
    return Info_Art(parent,cnt)

#---------------------------------------------------------------------------
class Info_Art(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        self.ttl=ttl
        Nid = wx.NewId()
        self.CnAz = prnt.CnAz
        self.font = self.GetFont()
        self.annoc = prnt.annoc
        self.datacon = prnt.datacon
        
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.__FRM__ = prnt.__MDI__
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0))#, size=wx.Size(540, 260))
        self.pnl.SetFont(self.font)  
        
        self.lbcodart = wx.StaticText(self.pnl, -1, _("Codice :"), 
            wx.DLG_PNT(self.pnl, 5,7))
        self.lbcodart.SetFont(self.font)
        
        self.codart = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 80,5), wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT))
        self.codart.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Descrizione :"), wx.DLG_PNT(self.pnl, 5,22)).SetFont(self.font)
        
        self.descriz = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 80,20), wx.DLG_SZE(self.pnl, 190,cfg.DIMFONTDEFAULT))                    
        self.descriz.SetFont(self.font)
        
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,35), 
              wx.DLG_SZE(self.pnl , 270,-1))
        
        self.lbgia = wx.StaticText(self.pnl, -1, _("Giacenza :"), 
              wx.DLG_PNT(self.pnl, 5,42))
        self.lbgia.SetFont(self.font)
        
        self.qt_gia = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 80, 40), 
              wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.qt_gia.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, "+", wx.DLG_PNT(self.pnl, 150,42)).SetFont(self.font)
        
        self.lbordc = wx.StaticText(self.pnl, -1, _("Ordini clienti :"), 
              wx.DLG_PNT(self.pnl, 5,57))
        self.lbordc.SetFont(self.font)
        
        self.qt_oc = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 80, 55), 
              wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.qt_oc.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, "-", wx.DLG_PNT(self.pnl, 150,57)).SetFont(self.font)
        
        self.lbordf = wx.StaticText(self.pnl, -1, _("Ordini fornitori :"), 
              wx.DLG_PNT(self.pnl, 5,72))
        self.lbordf.SetFont(self.font)
        
        self.qt_of = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 80, 70), 
              wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.qt_of.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, "+", wx.DLG_PNT(self.pnl, 150,72)).SetFont(self.font)
        
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5, 85), 
              wx.DLG_SZE(self.pnl , 150,-1))
        
        self.lbdisp = wx.StaticText(self.pnl, -1, _("Disponibilita` :"), 
              wx.DLG_PNT(self.pnl, 5,92))
        self.lbdisp.SetFont(self.font)
        
        self.qt_dis = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 80, 90), 
              wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.qt_dis.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, "=", wx.DLG_PNT(self.pnl, 150,92)).SetFont(self.font)
        
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,110), 
              wx.DLG_SZE(self.pnl , 270,-1))
        
        #self.pnl.SetFont(self.font)
        
        self.canc=wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 160,120), 
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
        self.Start(self)


    def Start(self, evt):
        self.codart.Enable(False)
        self.descriz.Enable(False)
        self.codart.SetValue(self.cnt[0])
        self.descriz.SetValue(self.cnt[1])
        self.qt_oc.Enable(False)
        self.qt_of.Enable(False)
        self.qt_gia.Enable(False)
        self.qt_dis.Enable(False)
        self.FndInfoCodArt(self)

    def FndInfoCodArt(self, evt):   
        ## Funzione Cerca Articolo     
        cod=self.codart.GetValue().upper()
        qt_cart=0
        qt_scat=0
        #sqldb.sql_qtord
        sql =  """ SELECT sum(QT_ORD) as QT_ORD
                    FROM ordi2 
                WHERE ANNO = '%s' AND TIPO_ORD = '%s' AND COD = '%s' """
        valueSql = self.annoc,"OC",cod
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            row = cr.fetchone()
            vqtoc = row[0]
            if vqtoc==None : vqtoc = 0.0
        except StandardError, msg:
            print "FndInfoCodArt Error %s" % (msg)
        self.CnAz.commit()
        sql =  """ SELECT sum(QT_ORD) as QT_ORD
                    FROM ordi2 
                WHERE ANNO = '%s' AND TIPO_ORD = '%s' AND COD = '%s' """
        valueSql = self.annoc,"OF",cod        
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            row= cr.fetchone()
            vqtof = row[0]
            if vqtof==None : vqtof = 0.0
        except StandardError, msg:
            print "FndInfoCodArt Error %s" % (msg)
        self.CnAz.commit()
        um = '  '
        sql = """ SELECT ANNO,NUM_MOV,DATAMOV,CAUMA,QT,COSTO_UN,
                  TOT_RIGA, UM FROM
                movmag WHERE COD like '%s' and ANNO = '%s' """
        valueSql = cod, self.annoc
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cauma = str(row[3])
                qt = float(row[4])
                qt_car = 0.0
                qt_sca = 0.0
                if (cauma=="801" or cauma=="802"):qt_car = qt
                elif (cauma=="901" or cauma=="902"):qt_sca = qt
                qt_cart+=qt_car
                qt_scat+=qt_sca
                um = str(row[7])               
        except StandardError, msg:
            print "FndInfoCodArt Error %s" % (msg)
        self.CnAz.commit()
        vqtgia=qt_cart-qt_scat
        vqtdis=vqtgia-vqtoc+vqtof
        self.__FRM__.CnvVMQT(vqtoc)
        vqtoc = self.__FRM__.val  
        self.__FRM__.CnvVMQT(vqtof)
        vqtof = self.__FRM__.val  
        self.__FRM__.CnvVMQT(vqtgia)
        vqtgia = self.__FRM__.val  
        self.__FRM__.CnvVMQT(vqtdis)
        vqtdis = self.__FRM__.val
        self.__FRM__.CnvVMQT('0')
        vnull = self.__FRM__.val
        if (vqtoc==""):vqtoc = vnull
        if (vqtof==""):vqtof = vnull
        if (vqtgia==""):vqtgia = vnull
        if (vqtdis==""):vqtdis = vnull
        self.qt_oc.SetValue(vqtoc)
        self.qt_of.SetValue(vqtof)
        self.qt_gia.SetValue(vqtgia)
        self.qt_dis.SetValue(vqtdis)
        self.lbgia.SetLabel(_("Giacenza:")+"             " + um)
        self.lbordc.SetLabel(_("Ordini clienti:")+"       " + um)
        self.lbordf.SetLabel(_("Ordini fornitori:")+"    " + um)
        self.lbdisp.SetLabel(_("Disponibilita`:")+"      " + um)
             
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
        
    def Close(self, event):
        self.Destroy() 

