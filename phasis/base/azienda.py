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


def create(parent,cnt):
    return Azienda(parent,cnt)
 
class Azienda(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.ttl=cnt[0]
        tcpart=cnt[1].upper()
        #self.tblanag="aziende"
        self.tcpart=tcpart
        self.rec=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        
        self.__MDI__= wx.GetApp().GetPhasisMdi()
       
        self.font=self.__MDI__.font
        self.SetFont(self.font)

        
        #self.font=self.GetFont()
        self.color=self.GetBackgroundColour()        
        #self.tblage="agenti"
        Nid = wx.NewId()
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0), size = wx.DLG_SZE(self,680/2,370/2), #size=wx.Size(680, 370),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        self.ntbk = wx.Notebook(id=wx.NewId(), name='notebook',
            parent=self.pnl, pos = wx.DLG_PNT(self.pnl, 10/2,120/2),#pos=wx.Point(10, 120), 
            size = wx.DLG_SZE(self.pnl,cfg.NTBKH1TUTTI/2,cfg.NTBKV1TUTTI/2),style = 0)
          #size=wx.Size(cfg.NTBKH1TUTTI,cfg.NTBKV1TUTTI),style=0)
        self.ntbk.SetFont(self.font) 
        
        self.pnl1 = wx.Panel(id=wx.NewId(), name='panel0',
              parent=self.ntbk, pos=wx.Point(0, 0), size = wx.DLG_SZE(self.pnl,600/2,220/2)) #size=wx.Size(600, 220))
        self.pnl1.SetFont(self.font)
        
        self.pnl2 = wx.Panel(id=wx.NewId(), name='panel1',
              parent=self.ntbk, pos=wx.Point(0, 0), size = wx.DLG_SZE(self.pnl,600/2,220/2)) #size=wx.Size(600, 220))
        self.pnl2.SetFont(self.font)
        
        self.pnl0 = wx.Panel(id=wx.NewId(), name='panel2',
              parent=self.ntbk, pos=wx.Point(0, 0), size = wx.DLG_SZE(self.pnl,600/2,220/2)) #size=wx.Size(600, 220))
        self.pnl0.SetFont(self.font)
                        
        self.ntbk.AddPage(imageId=-1, page=self.pnl0, select=True, 
            text=_(' Sede Legale'))       
                
        self.ntbk.AddPage(imageId=-1, page=self.pnl1, select=False,
            text=_(' Sede Ammnistrativa '))
        
        self.ntbk.AddPage(imageId=-1, page=self.pnl2, select=False,
            text=_(' Contabile ed Altro'))
        
        #self.pnl.SetFont(self.font)
        #self.pnl1.SetFont(self.font)
        #self.pnl2.SetFont(self.font)
        #self.pnl0.SetFont(self.font)
        #self.ntbk.SetFont(self.font)
        
        self.t_cpart = wx.TextCtrl(self.pnl, -1, "", 
            wx.DLG_PNT(self.pnl, 275,37))
        
        self.lcodcf = wx.StaticText(self.pnl, -1, _("Codice :"), 
            wx.DLG_PNT(self.pnl, 5,7))
        self.lcodcf.SetFont(self.font)
        
        self.codcf = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,5), wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT))
        self.codcf.SetFont(self.font)
        
        self.ccodcf=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl, 110,5),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        self.lragsoc1 = wx.StaticText(self.pnl, -1,_("Rag. Sociale ( Cognome ) :"),
            wx.DLG_PNT(self.pnl, 5,22))
        self.lragsoc1.SetFont(self.font)
        
        self.ragsoc1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 5,35), 
            wx.DLG_SZE(self.pnl, 120,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)    
        self.ragsoc1.SetFont(self.font)
        
        self.cragsoc1=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl, 130,35),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        wx.StaticText(self.pnl, -1, _("( Nome ) :"), wx.DLG_PNT(self.pnl, 150,22)).SetFont(self.font)
        
        self.ragsoc2 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 150, 35), wx.DLG_SZE(self.pnl, 110,cfg.DIMFONTDEFAULT))          
        self.ragsoc2.SetFont(self.font)
        
        wx.StaticText(self.pnl0, -1, _("Indirizzo :"), wx.DLG_PNT(self.pnl0, 5,7)).SetFont(self.font)
        
        self.indiriz = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,5), wx.DLG_SZE(self.pnl0, 210,cfg.DIMFONTDEFAULT))
        self.indiriz.SetFont(self.font)
        
        wx.StaticText(self.pnl0, -1, _("Citta` :"), wx.DLG_PNT(self.pnl0, 5,22)).SetFont(self.font)
        
        self.zona = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,20), wx.DLG_SZE(self.pnl0, 100,cfg.DIMFONTDEFAULT))
        self.zona.SetFont(self.font)
        
        wx.StaticText(self.pnl0, -1, _("CAP :"), wx.DLG_PNT(self.pnl0, 150,22)).SetFont(self.font)
        
        self.cap = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 175, 20), wx.DLG_SZE(self.pnl0, 35,cfg.DIMFONTDEFAULT))
        self.cap.SetFont(self.font)
        
        wx.StaticText(self.pnl0, -1, _("PR :"), wx.DLG_PNT(self.pnl0, 215,22)).SetFont(self.font)
        
        self.pr = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 235, 20), wx.DLG_SZE(self.pnl0, 20,cfg.DIMFONTDEFAULT))
        self.pr.SetFont(self.font)
        
        self.ltabi = wx.StaticText(self.pnl0, -1, _("Telefono :"), 
            wx.DLG_PNT(self.pnl0, 5,37))
        self.ltabi.SetFont(self.font)
        
        self.tabi = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,35), wx.DLG_SZE(self.pnl0, 85,cfg.DIMFONTDEFAULT))
        self.tabi.SetFont(self.font)
        wx.StaticText(self.pnl0, -1, _("Fax :"), wx.DLG_PNT(self.pnl0, 140,37))
        self.fax = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 170, 35), wx.DLG_SZE(self.pnl0, 85,-1))
        self.fax.SetFont(self.font)


        #self.lmob = wx.StaticText(self.pnl0, -1, "Mobile :", 
        #    wx.DLG_PNT(self.pnl0, 140,37))
        #self.lmob.SetFont(self.font)
        
        #self.mob = wx.TextCtrl(self.pnl0, Nid, "",
        #      wx.DLG_PNT(self.pnl0, 170, 35), wx.DLG_SZE(self.pnl0, 85,cfg.DIMFONTDEFAULT))
        #self.mob.SetFont(self.font)
        
        wx.StaticText(self.pnl0, -1, _("Localita` :"), wx.DLG_PNT(self.pnl0, 5,52)).SetFont(self.font)
        
        self.localit = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,50), wx.DLG_SZE(self.pnl0, 85,cfg.DIMFONTDEFAULT))
        self.localit.SetFont(self.font)
        
        wx.StaticText(self.pnl0, -1, _("Stato :"), wx.DLG_PNT(self.pnl0, 140,52)).SetFont(self.font)
        
        self.stato = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 170, 50), wx.DLG_SZE(self.pnl0, 85,cfg.DIMFONTDEFAULT))
        self.stato.SetFont(self.font)
        
        wx.StaticText(self.pnl0, -1, _(" EMail :"), wx.DLG_PNT(self.pnl0, 5,67)).SetFont(self.font)
        
        self.email = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,65), wx.DLG_SZE(self.pnl0, 120,cfg.DIMFONTDEFAULT))
        self.email.SetFont(self.font)
        
        wx.StaticText(self.pnl0, -1, _(" Url :"), wx.DLG_PNT(self.pnl0, 5,82)).SetFont(self.font)
        
        self.web = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,80), wx.DLG_SZE(self.pnl0, 120,cfg.DIMFONTDEFAULT))
        self.web.SetFont(self.font)
        
        wx.StaticText(self.pnl1, -1, _("Indirizzo :"), wx.DLG_PNT(self.pnl1, 5,7)).SetFont(self.font)
        
        self.indiriz1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,5), wx.DLG_SZE(self.pnl1, 210,cfg.DIMFONTDEFAULT))  
        self.indiriz1.SetFont(self.font)
        
        wx.StaticText(self.pnl1, -1, _("Citta`:"), wx.DLG_PNT(self.pnl1, 5,22)).SetFont(self.font)
        
        self.zona1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,20), wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))
        self.zona1.SetFont(self.font)
        
        wx.StaticText(self.pnl1, -1, _("CAP :"), wx.DLG_PNT(self.pnl1, 150,22)).SetFont(self.font)
        
        self.cap1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 175, 20), wx.DLG_SZE(self.pnl1, 35,cfg.DIMFONTDEFAULT))
        self.cap1.SetFont(self.font)
        
        wx.StaticText(self.pnl1, -1, _("PR :"), wx.DLG_PNT(self.pnl1, 215,22)).SetFont(self.font)
        
        self.pr1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 235, 20), wx.DLG_SZE(self.pnl1, 20,cfg.DIMFONTDEFAULT))
        self.pr1.SetFont(self.font)
        
        wx.StaticText(self.pnl1, -1, _("Localita` :"), wx.DLG_PNT(self.pnl1, 5,37)).SetFont(self.font)
        
        self.localit1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,35), wx.DLG_SZE(self.pnl1, 85,cfg.DIMFONTDEFAULT))
        self.localit1.SetFont(self.font)
        
        wx.StaticText(self.pnl1, -1, _("Stato :"), wx.DLG_PNT(self.pnl1, 140,37)).SetFont(self.font)
        
        self.stato1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 170, 35), wx.DLG_SZE(self.pnl1, 85,cfg.DIMFONTDEFAULT))
        self.stato1.SetFont(self.font)
        
        self.ltuff = wx.StaticText(self.pnl1, -1, _("Telefono :"), 
            wx.DLG_PNT(self.pnl1, 5,52))
        self.ltuff.SetFont(self.font)
        
        self.tuff = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,50), wx.DLG_SZE(self.pnl1, 85,cfg.DIMFONTDEFAULT))
        self.tuff.SetFont(self.font)
        
        #wx.StaticText(self.pnl1, -1, "Fax :", wx.DLG_PNT(self.pnl1, 140,52)).SetFont(self.font)
        #self.fax = wx.TextCtrl(self.pnl1, Nid, "",
        #      wx.DLG_PNT(self.pnl1, 170, 50), wx.DLG_SZE(self.pnl1, 85,cfg.DIMFONTDEFAULT))
        #self.fax.SetFont(self.font)

        wx.StaticText(self.pnl1, -1, _("Mobile :"), 
              wx.DLG_PNT(self.pnl1, 140,52))
        self.mob = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 170, 50), wx.DLG_SZE(self.pnl1, 85,-1))

        wx.StaticText(self.pnl2, -1, _("P.IVA :"), wx.DLG_PNT(self.pnl2, 5,22)).SetFont(self.font)
        
        self.piva = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 35,20), wx.DLG_SZE(self.pnl2, 85,cfg.DIMFONTDEFAULT))
        self.piva.SetFont(self.font)
        
        wx.StaticText(self.pnl2, -1, _("C.F. :"), wx.DLG_PNT(self.pnl2, 140,22)).SetFont(self.font)
        
        self.codfisc = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 165,20), wx.DLG_SZE(self.pnl2, 85,cfg.DIMFONTDEFAULT))
        self.codfisc.SetFont(self.font)
        
        wx.StaticText(self.pnl2, -1, _("Paese:"), wx.DLG_PNT(self.pnl2, 5,40))
        self.paese = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 5,50), wx.DLG_SZE(self.pnl2, 20,-1))
        wx.StaticText(self.pnl2, -1, _("Cod.C:"), wx.DLG_PNT(self.pnl2, 28,40))
        self.cod_c = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 28,50), wx.DLG_SZE(self.pnl2, 20,-1))
        wx.StaticText(self.pnl2, -1, _("CIN:"), wx.DLG_PNT(self.pnl2, 51,40))
        self.cin = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 52,50), wx.DLG_SZE(self.pnl2, 10,-1))
        wx.StaticText(self.pnl2, -1, _(" ABI :"), wx.DLG_PNT(self.pnl2, 70,40))
        self.abi = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 70,50), wx.DLG_SZE(self.pnl2, 40,-1))
        wx.StaticText(self.pnl2, -1, _(" CAB :"), wx.DLG_PNT(self.pnl2, 115,40))
        self.cab = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 115,50), wx.DLG_SZE(self.pnl2, 40,-1))
        wx.StaticText(self.pnl2, -1, _(" C/C:"), wx.DLG_PNT(self.pnl2, 160,40))
        self.ncc = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 160,50), wx.DLG_SZE(self.pnl2, 80,-1))
        wx.StaticText(self.pnl2, -1, _(" Banca :"), wx.DLG_PNT(self.pnl2, 5,65))
        self.banca = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 5,75), wx.DLG_SZE(self.pnl2, 235,-1))
        
        wx.StaticText(self.pnl2, -1, _("Riferimento Azienda:"), wx.DLG_PNT(self.pnl2, 10,95)).SetFont(self.font)
        
        self.nsrif = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 90,95), wx.DLG_SZE(self.pnl2, 120,cfg.DIMFONTDEFAULT))
        self.nsrif.SetFont(self.font)
        
        self.new = wx.Button(self.pnl, Nid, cfg.vcnew, 
            wx.DLG_PNT(self.pnl, 285,20), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.new.SetFont(self.font)
        
        self.ok = wx.Button(self.pnl, Nid, cfg.vcok, 
            wx.DLG_PNT(self.pnl, 285,20), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))               
        self.ok.SetFont(self.font)
        
        self.inte = wx.Button(self.pnl, Nid, cfg.vcint, 
            wx.DLG_PNT(self.pnl, 285,35), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV)) 
        self.inte.SetFont(self.font)
        
        self.canc = wx.Button(self.pnl, Nid, cfg.vccanc, 
            wx.DLG_PNT(self.pnl, 285,35), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFont(self.font)
        
        self.modi = wx.Button(self.pnl, Nid, cfg.vcmodi, 
            wx.DLG_PNT(self.pnl, 285,50), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))      
        self.modi.SetFont(self.font)
        
        self.dele = wx.Button(self.pnl, Nid, cfg.vcdele,
            wx.DLG_PNT(self.pnl, 285,50), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.dele.SetFont(self.font)
        
        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
            wx.DLG_PNT(self.pnl, 285,65),
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa.SetFont(self.font)
        
        
        #self.SetFont(self.font)
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)
        
        self.ok.Bind(wx.EVT_BUTTON, self.Save)
        self.new.Bind(wx.EVT_BUTTON, self.New)  
        self.inte.Bind(wx.EVT_BUTTON, self.IntAnag) 
        self.modi.Bind(wx.EVT_BUTTON, self.Modi)      
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.dele.Bind(wx.EVT_BUTTON, self.CntrDele)
        self.ccodcf.Bind(wx.EVT_BUTTON, self.FndCodCF)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.codcf.Bind(wx.EVT_TEXT_ENTER, self.FndCodCF)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.ragsoc1.Bind(wx.EVT_CHAR, self.EvtChar)
        self.indiriz.Bind(wx.EVT_TEXT_ENTER, self.zonaSF)
        self.zona.Bind(wx.EVT_TEXT_ENTER, self.capSF)
        self.cap.Bind(wx.EVT_TEXT_ENTER, self.prSF)
        self.pr.Bind(wx.EVT_TEXT_ENTER, self.localitSF)
        self.localit.Bind(wx.EVT_TEXT_ENTER, self.tabiSF)
        self.tabi.Bind(wx.EVT_TEXT_ENTER, self.mobSF)
        self.mob.Bind(wx.EVT_TEXT_ENTER, self.pivaSF)
        self.piva.Bind(wx.EVT_TEXT_ENTER, self.codfiscSF)
        self.ragsoc2.Bind(wx.EVT_TEXT_ENTER, self.FndAnagIs)
        ## EVT_KILL escluso per assertion failed: (GTK_WIDGET_HAS_FOCUS (entry))
        ##self.cap.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_cap)
        ##self.tabi.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_tabi)
        ##self.mob.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_mob)
        ##self.tuff.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_tuff)
        ##self.fax.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_fax)
        ##self.piva.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_piva)
        ##self.codfisc.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_codfisc)
        ##self.pr.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_pr)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.Bind(wx.EVT_CLOSE, self.Close)    
        self.AT_Aziende()
        self.Start(self)

    def AT_Aziende(self):
        sql = """ select paese from aziende """	
        try:
            cr =  fdb.CnDBAZ.cursor ()
            cr.execute(sql)
            row = cr.fetchone()
        except StandardError, msg:
            dlg = wx.MessageDialog(self, 
                _("Aggiornamento della tabella ......"), 
                _("Aggiornamento Tabella "), wx.ID_OK | wx.ICON_INFORMATION)
            if dlg.ShowModal()==wx.ID_OK: dlg.Destroy()	    
            import at_aziende
            self.AggMenu(True,self.IDMENU )
            wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        fdb.CnDBAZ.commit()

    def Stampa(self, evt):
        pass
        
    def Start(self, evt):
        self.DelTxt(self)
        self.OffTxt(self)
        self.dele.Enable(False)
        self.dele.Show(False) # aggiunto per errore visualizzione mac
        self.stampa.Enable(False)
        self.modi.Enable(False)
        self.new.Show(True)
        self.new.Enable(False)
        self.ok.Show(False)
        self.inte.Show(False)
        self.codcf.Enable(True)
        self.ccodcf.Enable(True)
        self.ragsoc1.Enable(True)
        self.ragsoc1.SetFocus()
        self.cragsoc1.Enable(True)
        self.t_cpart.Enable(False)
        self.t_cpart.Show(False)
        if (self.rec!=""):
            self.codcf.SetValue(self.rec)
            self.FndCodCF(self)
    def indirizSF(self, evt):
        self.indiriz.SetFocus()
    def zonaSF(self, evt):
        self.zona.SetFocus()
    def capSF(self, evt):
        self.cap.SetFocus()
    def prSF(self, evt):
        self.pr.SetFocus()
    def localitSF(self, evt):
        self.localit.SetFocus()
    def tabiSF(self, evt):
        self.tabi.SetFocus()
    def mobSF(self, evt):
        self.mob.SetFocus()
    def pivaSF(self, evt):
        self.piva.SetFocus()
    def codfiscSF(self, evt):
        self.codfisc.SetFocus()
        

            
    def IntAnag(self, evt):
        self.rec=""
        self.Start(self)
        self.canc.Show(True)
        self.new.Show(True)
        self.ok.Show(False)
        self.dele.Show(False)
        self.stampa.Enable(False)

        
    def FndSel(self, evt):
        row=evt
        self.t_cpart.SetValue(str(row[0]))
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.indiriz.SetValue(str(row[6]).title())  
        self.cap.SetValue(str(row[7]))       
        self.zona.SetValue(str(row[8]).title())
        self.localit.SetValue(str(row[9]).title())  
        self.pr.SetValue(str(row[10]).strip().upper())
        self.stato.SetValue(str(row[11]).title())
        self.tabi.SetValue(str(row[18]))
        self.mob.SetValue(str(row[20]))
        self.tuff.SetValue(str(row[19]))
        self.fax.SetValue(str(row[21]))
        self.piva.SetValue(str(row[25]).strip())
        self.codfisc.SetValue(str(row[24]).strip().upper())
        self.email.SetValue(str(row[23]))
        self.web.SetValue(str(row[22]))
        self.indiriz1.SetValue(str(row[12]).title())
        self.zona1.SetValue(str(row[14]).title())
        self.localit1.SetValue(str(row[15]).title())
        self.cap1.SetValue(str(row[13]))       
        self.pr1.SetValue(str(row[16]).strip().upper())
        self.stato1.SetValue(str(row[17]).title())
        self.banca.SetValue(str(row[26]).title())
        # paese cod_c cin
        self.abi.SetValue(str(row[28]).strip())
        self.cab.SetValue(str(row[29]).strip())
        self.ncc.SetValue(str(row[27]).strip())
        self.paese.SetValue(str(row[37]))
        self.cod_c.SetValue(str(row[38]))
        self.cin.SetValue(str(row[39]))
	
        self.nsrif.SetValue(str(row[5]))
        self.OffTxt(self)
        self.modi.Enable(True)
        self.modi.SetFocus()
        self.canc.Show(False)
        self.inte.Show(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(False)
        self.dele.Show(False)
        self.stampa.Enable(False)

            
    def NewTxt(self, evt):
        self.OnTxt(self) 
        self.codcf.Enable(False)
        self.ccodcf.Enable(False)
        self.ragsoc1.SetFocus()
        self.cragsoc1.Enable(False)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.dele.Show(False)
        
    def ModiTxt(self, evt):
        self.OnTxt(self)
        self.modi.Enable(False)
        self.inte.SetFocus()
        self.ok.Enable(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.dele.Show(False)
        self.dele.Enable(False)
        
        
    def SaveTxt(self, evt):
        self.OffTxt(self)
        self.inte.SetFocus()
        self.ok.Show(False)
        self.new.Show(True)
        self.dele.Show(False)
        self.dele.Enable(False)

    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()
        
    def OffTxt(self, evt):
        self.codcf.Enable(False)
        self.ccodcf.Enable(False)
        self.ragsoc1.Enable(False)
        self.ragsoc2.Enable(False)
        self.cragsoc1.Enable(False)
        self.indiriz.Enable(False)
        self.zona.Enable(False)
        self.pr.Enable(False)
        self.cap.Enable(False)
        self.localit.Enable(False)
        self.stato.Enable(False)
        self.indiriz1.Enable(False)
        self.zona1.Enable(False)
        self.pr1.Enable(False)
        self.localit1.Enable(False)
        self.stato1.Enable(False)
        self.cap1.Enable(False)  
        self.tabi.Enable(False)
        self.mob.Enable(False)
        self.tuff.Enable(False)
        self.fax.Enable(False)
        self.piva.Enable(False)
        self.codfisc.Enable(False)
        self.email.Enable(False)
        self.web.Enable(False)

        self.nsrif.Enable(False)
        self.abi.Enable(False)
        self.cab.Enable(False)
        self.ncc.Enable(False)
        self.banca.Enable(False)
        #modifica banca
        self.paese.Enable(False)
        self.cod_c.Enable(False)
        self.cin.Enable(False)
        self.cntr=""

    def OnTxt(self ,evt):
        self.ragsoc1.Enable(True)
        self.ragsoc2.Enable(True)
        self.cragsoc1.Enable(True)
        self.indiriz1.Enable(True)
        self.zona.Enable(True)
        self.pr.Enable(True)
        self.cap.Enable(True)
        self.localit.Enable(False)
        self.stato.Enable(False)
        self.indiriz.Enable(True)
        self.zona1.Enable(True)
        self.pr1.Enable(True)
        self.cap1.Enable(True)
        self.localit1.Enable(True)
        self.stato1.Enable(True)
        self.tabi.Enable(True)
        self.mob.Enable(True)
        self.tuff.Enable(True)
        self.fax.Enable(True)
        self.piva.Enable(True)
        self.codfisc.Enable(True)
        self.email.Enable(True)
        self.web.Enable(True)
        self.localit.Enable(True)
        self.stato.Enable(True)
        self.nsrif.Enable(True)
        self.abi.Enable(True)
        self.cab.Enable(True)
        self.ncc.Enable(True)
        self.banca.Enable(True)
        #modifica banca
        self.paese.Enable(True)
        self.cod_c.Enable(True)
        self.cin.Enable(True)
        
    def DelTxt(self, evt):
        self.codcf.SetValue('')
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.indiriz.SetValue('')
        self.zona.SetValue('')
        self.cap.SetValue('')
        self.pr.SetValue('')
        self.localit.SetValue('')
        self.stato.SetValue('')
        self.indiriz1.SetValue('')
        self.zona1.SetValue('')
        self.cap1.SetValue('')
        self.pr1.SetValue('')
        self.localit1.SetValue('')
        self.stato1.SetValue('')
        self.tabi.SetValue('')
        self.mob.SetValue('')
        self.tuff.SetValue('')
        self.fax.SetValue('')
        self.piva.SetValue('')
        self.codfisc.SetValue('')
        self.email.SetValue('')
        self.web.SetValue('')
        self.abi.SetValue('')
        self.cab.SetValue('')
        self.ncc.SetValue('')
        self.banca.SetValue('')
        self.nsrif.SetValue('')
        # modifica banca
        self.paese.SetValue('')
        self.cod_c.SetValue('')
        self.cin.SetValue('')
	
        self.t_cpart.SetValue(self.tcpart)
        
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        dlg.ShowModal()
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
          
    def SetFcs(self, evt):
        evt.Skip()
        
    def KillFcs_cap(self, evt):          
        vcap=self.cap.GetValue()
        if (vcap!=""):
            if (vcap.isdigit()!= True):
                self.Message(_("CAP ") + cfg.msgdatono,self.ttl)
                self.cap.SetFocus()
            else:self.pr.SetFocus()
        #evt.Skip()

    def KillFcs_tabi(self, evt):
        vtabi=self.tabi.GetValue()
        if (vtabi!=""):
            if (vtabi.isdigit()!= True ):
                self.Message(_("Tel. ") + cfg.msgdatono,self.ttl)
                self.tabi.SetFocus()
                
    def KillFcs_codcf(self, evt):
        vcodcf=self.codcf.GetValue()
        if (vcodcf==""):
            self.Message(cfg.msgnocod,self.ttl)
            self.codcf.SetFocus()
            
    def KillFcs_mob(self, evt):
        vmob=self.mob.GetValue()
        if (vmob!=""):
            if (vmob.isdigit()!= True ):
                self.Message(_("Mob. ")+cfg.msgdatono ,self.ttl)
                self.mob.SetFocus()
            
    def KillFcs_fax(self, evt):
        vfax=self.fax.GetValue()
        if (vfax!=""):
            if (vfax.isdigit()!= True):
                self.Message(_("Fax ") + cfg.msgdatono,self.ttl)
                self.fax.SetFocus()
            
    def KillFcs_tuff(self, evt):
        vtuff=self.tuff.GetValue()
        if (vtuff!=""):
            if (vtuff.isdigit()!= True):
                self.Message(_("Tel. ") + cfg.msgdatono,self.ttl)
                self.tuff.SetFocus()

    def KillFcs_pr(self, evt):
        vpr=self.pr.GetValue()
        if (vpr!=""): 
            if (vpr.isalpha()!= True):
                self.Message(_("PR ") + cfg.msgdatono,self.ttl)
                self.pr.SetFocus()
                
    def KillFcs_codfisc(self, evt):
        vcodfisc=self.codfisc.GetValue()
        if (vcodfisc!=""):
            if (vcodfisc.isalnum()!= True):
                self.Message(_("Cod. Fisc. ") + cfg.msgdatono,self.ttl)
                self.codfisc.SetFocus()

    def KillFcs_piva(self, evt):
        vpiva=self.piva.GetValue()
        if (vpiva!=""):
            if (vpiva.isdigit()!= True):
                self.Message(_("P.IVA ") + cfg.msgdatono,self.ttl)
                self.piva.SetFocus()
                
    #Funzioni tasti-------------------------------------------
    def Close(self, evt):
        #print self.IDMENU 
        if (self.ragsoc2.GetValue()!="" or self.ragsoc1.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgesci, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
                self.AggMenu(True,self.IDMENU )
                wx.GetApp().GetPhasisMdi().CloseTabObj(self)
                #self.Destroy()   
            else:
                dlg.Destroy() 
        else:
            self.AggMenu(True,self.IDMENU )
            wx.GetApp().GetPhasisMdi().CloseTabObj(self)
            #self.Destroy() 
                 
    def Modi(self, evt):
        dlg = wx.MessageDialog(self, msgmodi_anag, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.ModiTxt(self)
            self.cntr="modi"
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()
 
    def New(self, evt):
        # Funzione Nuovo
        self.DelTxt(self)
        self.cntr="new"
        self.NewTxt(self)
        tcpart = self.t_cpart.GetValue().upper()
        sql = """ select max(cod) from aziende where t_cpart = "%s" """
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql % tcpart)
            while (1):
                row=cr.fetchone()
                if row == None:
                    break
                if (row[0] == None) : self.codcf.SetValue('1')
                if (row[0] != None) : self.codcf.SetValue(str(int(row[0])+1))
        except StandardError, msg:
            print "Azienda Error %s" % (msg)
        fdb.CnDBAZ.commit()
     
    def Save(self, evt):
        # Funzione Salva
        vcntr=self.cntr
        vtabi=self.tabi.GetValue()
        vmob=self.mob.GetValue()
        vfax=self.fax.GetValue()
        vtuff=self.tuff.GetValue()
        vpr=self.pr.GetValue()
        vpr1=self.pr1.GetValue()
        if vpr=="":vpr="--"
        if vpr1=="":vpr1="--"
        
        vcodfisc=self.codfisc.GetValue()
        vpiva=self.piva.GetValue()
        vcodcf=self.codcf.GetValue()
        vragsoc1=self.ragsoc1.GetValue().strip().title() 
        
        if (vcodcf.isdigit()!= True ):
            self.Message(cfg.msgdatono,self.ttl)
        if (vragsoc1==""):
            self.Message(cfg.msgcmp_null,self.ttl)
            self.ragsoc1.SetFocus()
        else:
            self.SaveTxt(self)
            vtcpart=self.t_cpart.GetValue().strip().upper()        
            vcodcf=self.codcf.GetValue().strip()
            vragsoc2=self.ragsoc2.GetValue().strip().title() 
            vragsoc1=self.ragsoc1.GetValue().strip().title()  
            vindiriz=self.indiriz.GetValue().strip().title()
            vzona=self.zona.GetValue().strip().title()
            vlocalit=self.localit.GetValue().strip().title()
            vcap=self.cap.GetValue().strip()              
            vpr=self.pr.GetValue().strip().upper()
            if vpr=="":vpr="--"
            vstato=self.stato.GetValue().title()
            vtabi=self.tabi.GetValue().strip()        
            vfax=self.fax.GetValue().strip()      
            vmob=self.mob.GetValue().strip()
            vtuff=self.tuff.GetValue().strip()       
            vemail=self.email.GetValue().strip()
            vweb=self.web.GetValue().strip()
            vpiva=self.piva.GetValue().strip()
            vcodfisc=self.codfisc.GetValue().strip().upper()
            vindiriz1=self.indiriz1.GetValue().strip().title()
            vzona1=self.zona1.GetValue().strip().title()
            vlocalit1=self.localit1.GetValue().strip().title()
            vcap1=self.cap1.GetValue().strip()           
            vpr1=self.pr1.GetValue().strip().upper()
            if vpr1=="":vpr1="--"
            vstato1=self.stato1.GetValue().strip().title()
            vbanca=self.banca.GetValue().strip().title()
            vabi=self.abi.GetValue().strip()            
            vcab=self.cab.GetValue().strip()
            vncc=self.ncc.GetValue().strip()
            # modifica banca
            vpaese = self.paese.GetValue().strip().upper()
            vcod_c = self.cod_c.GetValue().strip()
            vcin = self.cin.GetValue().strip().upper()
            vcodbar="" 
            
            vnsrif=self.nsrif.GetValue().strip().title()
            if vnsrif=='' : vnsrif=vragsoc1 #vself.nsrif.GetValue().strip().title()
            vrea='' #self.rea.GetValue().strip()
            vmastro=""
            if vmastro == "" : vmastro=0          
            vcampo1=""
            vcampo2=""
            vscad_da=""
            vscad_a=""    
            vcod_div="EU"  
            vfrm1modi = vcodbar,vragsoc1,vragsoc2,vnsrif
            vfrm1 = vtcpart,int(vcodcf),vcodbar,vragsoc1,vragsoc2,vnsrif 
            vfrm2 = vindiriz,vcap,vzona,vlocalit,vpr,vstato 
            vfrm3 = vindiriz1,vcap1,vzona1,vlocalit1,vpr1,vstato1 
            vfrm4 = vtabi,vtuff,vmob,vfax,vweb,vemail 
            vfrm5 = vcodfisc,vpiva,vbanca,vncc,vabi,vcab,vscad_da,vscad_a, 
            vfrm6 = vmastro,vcod_div,vrea,vcampo1,vcampo2,vpaese,vcod_c,vcin 
            vfrm6modi = vmastro,vcod_div,vrea,vcampo1,vcampo2,vpaese,vcod_c,vcin,int(vcodcf),vtcpart 
            valueSql = vfrm1+vfrm2+vfrm3+vfrm4+vfrm5+vfrm6
            valueSql_modi = vfrm1modi+vfrm2+vfrm3+vfrm4+vfrm5+vfrm6modi
            if(vcntr=="new"):
                try:
                    cr = fdb.CnDBAZ.cursor()
                    sql = """ insert into aziende
                              values("%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s") """

                    cr.execute(sql % valueSql)
                except StandardError, msg:
                    print "Azienda Error %s" % (msg)
                fdb.CnDBAZ.commit()
            if(vcntr=="modi"):
                try:
                    cr = fdb.CnDBAZ.cursor()
                    sql = """ update aziende set
                              codbar = "%s", rag_soc1 = "%s", rag_soc2 = "%s", 
                              nsrif = "%s", indiriz = "%s", cap = "%s", 
			      zona = "%s", localit = "%s", pr = "%s", 
			      stato = "%s", indiriz1 = "%s", cap1 = "%s", 
			      zona1 = "%s", localit1 = "%s", pr1 = "%s", 
                              stato1 = "%s", tel_abit = "%s", tel_uff = "%s", 
                              mobile = "%s", fax = "%s", web = "%s", 
			      e_mail = "%s", codfisc = "%s", piva = "%s", 
			      banca = "%s", num_cc = "%s", abi = "%s", 
			      cab = "%s", scad_da = "%s", scad_a = "%s",  
                              mastro = "%s", cod_div = "%s",  
			      rea = "%s", campo1 = "%s", campo2 = "%s",
			      paese = "%s", cod_c = "%s", cin = "%s"
			      where cod = "%s" and t_cpart = "%s" """
			      
                    cr.execute(sql % valueSql_modi)
                except StandardError, msg:
                    print "Azienda Error %s" % (msg)
                fdb.CnDBAZ.commit()

    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgnodele_anag, self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr=""
            dlg.Destroy()
            
    def Dele(self, evt):
        # Funzione Elimina    
        dlg = wx.MessageDialog(self, cfg.msgdele_anag,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.cntr="dele"
            cod = self.codcf.GetValue()
            sql = """ delete from aziende 
                      where cod = "%s" and t_cpart = "%s" """
            valueSql = int(cod), self.tcpart
            try:
                cr = fdb.CnDBAZ.cursor ()
                cr.execute(sql % valueSql)
            except StandardError, msg:
                print "Azienda Error %s" % (msg)
            fdb.CnDBAZ.commit()
            self.IntAnag(self)
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()
       

    def FndAnagIs(self, evt):
        cnt_rec=0
        val1=self.ragsoc1.GetValue().strip()
        val2=self.ragsoc2.GetValue().strip()
        if (val1!="" and val2!="" and self.cntr=="new"):
            sql = """ select * from aziende where rag_soc1 = "%s"
                      and rag_soc2 = "%s" and t_cpart = "%s" """
            valueSql = val1.title(), val2.title(), self.tcpart
            try:
                cr = fdb.CnDBAZ.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                print "Azienda Error %s" % (msg)
            fdb.CnDBAZ.commit()
            if (cnt_rec==1 and cnt_rec<2):
                self.Message(cfg.msgdatosi,self.ttl)
                self.cntr=""
                self.FndSel(row)
            elif (cnt_rec>1):
                import SrcAnag
                control = [self.tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
                win = SrcAnag.create(self,control) 
                win.Centre(wx.BOTH)
                win.Show(True)
                
    def FndAnag(self, evt): 
         # Funzione cerca
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec=0
            val=self.ragsoc1.GetValue()
            cod=self.codcf.GetValue()
            sql = """ select * from aziende where t_cpart = "%s"
                      and rag_soc1 like "%s" order by rag_soc1 desc """
            valueSql = self.tcpart, '%'+val.title()+'%'
            try:
                cr = fdb.CnDBAZ.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                print "Azienda Error %s" % (msg)
            fdb.CnDBAZ.commit()        
            if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
            elif (cnt_rec==1 and cnt_rec<2): self.FndSel(row)
            elif (cnt_rec>1):
                import SrcAnag
                control = [self.tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
                win = SrcAnag.create(self,control) 
                win.Centre(wx.BOTH)
                win.Show(True)
            else:
                self.ragsoc2.SetFocus()
  
    def FndCodCF(self, evt):
         ## Funzione cerca codCF
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec=0
            cod=self.codcf.GetValue()
            if cod == "" :cod=0
            elif (cod.isdigit()!= True): cod=0
            sql = """ selcet * from aziende where cod = "%s"
                      and t_cpart =  "%s" """
            valueSql = int(cod), self.tcpart
            try:
                cr = fdb.CnDBAZ.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                print "Azienda Error %s" % (msg)
            fdb.CnDBAZ.commit()       
            if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
            elif (cnt_rec==1 and cnt_rec<2): self.FndSel(row)

