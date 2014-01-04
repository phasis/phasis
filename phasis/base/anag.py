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
import string 
from cfg import *
import cfg

def create(parent,cnt):
    return Anag(parent,cnt)
 
class Anag(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #wx.Frame.__init__(self, id = wx.NewId(), name = '',
        #      parent = prnt, pos = wx.Point(0, 0), size = wx.DefaultSize,  
        #      style = wx.DEFAULT_FRAME_STYLE, title = cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img + "/null.ico", wx.BITMAP_TYPE_ICO))

        self.font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False)
        #self.SetClientSize(wx.Size(600, 370))       
        y=wx.ScreenDC().MaxY()
        if y>=1200 : numfont=16
        elif y>=1024 : numfont=14
        else : numfont=12
        if cfg.FONTFISSO!=0 : numfont=cfg.FONTFISSO
        self.font.SetPointSize(numfont)
        self.SetFont(self.font)
        
        self.ttl = cnt[0]
        self.ttldest = _(" Anagrafica spedizioni ") 
        tcpart = cnt[1].upper()
        if (tcpart=="C" or tcpart=="F" or tcpart=="V" or tcpart=="T"):
            self.tblanag = "anag"
        if (tcpart=="A"):self.tblanag = "agenti"
        self.tcpart = tcpart
        self.rec = cnt[2]
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]

        self.font = self.GetFont()
        self.color = self.GetBackgroundColour()      
        Nid = wx.NewId()
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        
        #self.font=self.__MDI__.font
        #self.SetFont(self.font) 
        
        self.CnAz = self.__MDI__.GetConnAZ()
        self.annoc=self.__MDI__.GetAnnoC() 
        self.datacon= self.__MDI__.GetDataC()
        self.dzDatiAzienda= self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id = wx.NewId(), name = 'panel',
              parent = self, pos = wx.Point(0, 0), size = wx.DLG_SZE(self,680/2,370/2),#size = wx.Size(680, 370),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        #self.pnl.SetBackgroundColour(self.__MDI__.backcolmod)
        
        self.ntbk = wx.Notebook(id = wx.NewId(), name = 'notebook',
              parent = self.pnl, pos = wx.DLG_PNT(self.pnl, 10/2,120/2), #wx.Point(10, 120),
              size = wx.DLG_SZE(self.pnl,cfg.NTBKH1TUTTI/2,cfg.NTBKV1TUTTI/2),style = 0)
            #size = wx.Size(cfg.NTBKH1,cfg.NTBKV1),style = 0)
        #self.ntbk.SetFont(self.font)
        self.ntbk.SetFont(self.font)
        #self.pnl.SetBackgroundColour(self.__MDI__.backcolmod)
        
        self.pnl0 = wx.Panel(id = wx.NewId(), name = 'panel0',
              parent = self.ntbk, pos = wx.Point(0, 0), size = wx.DLG_SZE(self.pnl,600/2,220/2))#size = wx.Size(600, 220))
        self.pnl0.SetFont(self.font)
        
        self.pnl1 = wx.Panel(id = wx.NewId(), name = 'panel1',
              parent = self.ntbk, pos = wx.Point(0, 0), size = wx.DLG_SZE(self.pnl,600/2,220/2))#size = wx.Size(600, 220))
        self.pnl1.SetFont(self.font)
        
        self.pnl2 = wx.Panel(id = wx.NewId(), name = 'panel2',
              parent = self.ntbk, pos = wx.Point(0, 0), size = wx.DLG_SZE(self.pnl,600/2,220/2))#size = wx.Size(600, 220))
        self.pnl2.SetFont(self.font)
        
        self.pnl3 = wx.Panel(id = wx.NewId(), name = 'panel3',
              parent = self.ntbk, pos = wx.Point(0, 0), size = wx.DLG_SZE(self.pnl,600/2,220/2))#size = wx.Size(600, 220))
        self.pnl3.SetFont(self.font)
        
        self.ntbk.AddPage(imageId = -1, page = self.pnl2, select = True, 
            text = _(' Sede Legale')+' (1)')       
        self.ntbk.AddPage(imageId = -1, page = self.pnl0, select = False, 
            text = _(' Sede Ammnistrativa')+' (2)')
        self.ntbk.AddPage(imageId = -1, page = self.pnl1, select = False, 
            text = _(' Contabile')+' (3)')
        self.ntbk.AddPage(imageId = -1, page = self.pnl3, select = False,
            text = _(' Altro')+' (4)')
        
        #self.pnl.SetFont(self.font)
        #self.pnl0.SetFont(self.font)
        #self.pnl1.SetFont(self.font)
        #self.pnl2.SetFont(self.font)
        #self.pnl3.SetFont(self.font)
        #self.ntbk.SetFont(self.font)

        self.t_cpart = wx.TextCtrl(self.pnl, -1, "", 
            wx.DLG_PNT(self.pnl, 275,37))
        self.lcodcf = wx.StaticText(self.pnl, -1, "Codice :", 
            wx.DLG_PNT(self.pnl, 5,7))
        self.codcf = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,5), 
              wx.DLG_SZE(self.pnl, 60,-1),wx.TE_PROCESS_ENTER)
        self.ccodcf = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl, 110,5),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lragsoc1 = wx.StaticText(self.pnl, -1,"Ragione Sociale 1 ( Cognome ) :",
            wx.DLG_PNT(self.pnl, 5,22))
        self.ragsoc1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 5,35), 
            wx.DLG_SZE(self.pnl, 140,-1),wx.TE_PROCESS_ENTER)    
        self.cragsoc1 = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl, 262,35),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl, -1, "Ragione Sociale 2 ( Nome ) :", wx.DLG_PNT(self.pnl, 150,22))
        self.ragsoc2 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 150, 35), wx.DLG_SZE(self.pnl, 110,-1))          
        wx.StaticText(self.pnl0, -1, "Indirizzo :", wx.DLG_PNT(self.pnl0, 5,7))
        self.indiriz1 = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,5), wx.DLG_SZE(self.pnl0, 210,-1))      
        wx.StaticText(self.pnl0, -1, "Citta`:", wx.DLG_PNT(self.pnl0, 5,22))
        self.zona1 = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,20), wx.DLG_SZE(self.pnl0, 100,-1))
        wx.StaticText(self.pnl0, -1, "CAP :", wx.DLG_PNT(self.pnl0, 150,22))
        self.cap1 = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 175, 20), wx.DLG_SZE(self.pnl0, 35,-1))
        wx.StaticText(self.pnl0, -1, "PR :", wx.DLG_PNT(self.pnl0, 215,22))
        self.pr1 = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 235, 20), wx.DLG_SZE(self.pnl0, 20,-1))
        #self.ltabi = wx.StaticText(self.pnl0, -1, "Tel. Abit. :", 
        #      wx.DLG_PNT(self.pnl0, 5,37))
        #self.tabi = wx.TextCtrl(self.pnl0, Nid, "",
        #      wx.DLG_PNT(self.pnl0, 45,35), wx.DLG_SZE(self.pnl0, 85,-1))
        wx.StaticText(self.pnl0, -1, "Localita`:", wx.DLG_PNT(self.pnl0, 5,37))
        self.localit1 = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,35), wx.DLG_SZE(self.pnl0, 85,-1))
        wx.StaticText(self.pnl0, -1, "Stato :", wx.DLG_PNT(self.pnl0, 140,37))
        self.stato1 = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 170, 35), wx.DLG_SZE(self.pnl0, 85,-1))
        self.ltuff = wx.StaticText(self.pnl0, -1, "Telefono :", 
            wx.DLG_PNT(self.pnl0, 5,52))
        self.tuff = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 45,50), wx.DLG_SZE(self.pnl0, 85,-1))

        wx.StaticText(self.pnl0, -1, "Mobile :", 
              wx.DLG_PNT(self.pnl0, 140,52))
        self.mob = wx.TextCtrl(self.pnl0, Nid, "",
              wx.DLG_PNT(self.pnl0, 170, 50), wx.DLG_SZE(self.pnl0, 85,-1))

        #wx.StaticText(self.pnl0, -1, "Fax :", wx.DLG_PNT(self.pnl0, 140,52))
        #self.fax = wx.TextCtrl(self.pnl0, Nid, "",
        #      wx.DLG_PNT(self.pnl0, 170, 50), wx.DLG_SZE(self.pnl0, 85,-1))

        self.lcodage = wx.StaticText(self.pnl1, -1, "", wx.DLG_PNT(self.pnl1, 5,7))
        self.codage = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 50, 5), wx.DLG_SZE(self.pnl1, 40,-1))
        self.ccodage = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
            wx.DLG_PNT(self.pnl1, 92,5),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc1age = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 106, 5), wx.DLG_SZE(self.pnl1, 70,-1))
        wx.StaticText(self.pnl1, -1, "Listino:", wx.DLG_PNT(self.pnl1, 5,7))
        self.lst = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 35,5), wx.DLG_SZE(self.pnl1, 20,-1))
        self.clst = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl1, 58,5),
            wx.DLG_SZE(self.pnl1,cfg.btnSzeSH,cfg.btnSzeV))	      
        #self.lsc1 = wx.StaticText(self.pnl1, -1, "", wx.DLG_PNT(self.pnl1, 180,7))
        #self.sc1 = wx.TextCtrl(self.pnl1, Nid, "0",
              #wx.DLG_PNT(self.pnl1, 220,5), wx.DLG_SZE(self.pnl1, 30,-1))	      
        wx.StaticText(self.pnl1, -1, "P.IVA :", wx.DLG_PNT(self.pnl1, 5,22))
        self.piva = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 35,20), wx.DLG_SZE(self.pnl1, 85,-1))
        wx.StaticText(self.pnl1, -1, "C.F. :", wx.DLG_PNT(self.pnl1, 140,22))
        self.codfisc = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 165,20), wx.DLG_SZE(self.pnl1, 85,-1))
        ##self.lsc2 = wx.StaticText(self.pnl1, -1, "Sc % :", wx.DLG_PNT(self.pnl1, 5,37))
        ##self.sc2 = wx.TextCtrl(self.pnl1, Nid, "0",
              ##wx.DLG_PNT(self.pnl1, 35,35), wx.DLG_SZE(self.pnl1, 30,-1))	      
        wx.StaticText(self.pnl1, -1, "Cond.Pagam. :", wx.DLG_PNT(self.pnl1, 70,37))
        self.PAGAM = wx.ComboBox(self.pnl1, Nid,"",
              wx.DLG_PNT(self.pnl1, 130,35), 
            wx.DLG_SZE(self.pnl1, 120,-1),[],wx.CB_DROPDOWN | wx.CB_SORT )
        self.vPAGAM = wx.TextCtrl(self.pnl1, -1, "", wx.DLG_PNT(self.pnl1, 85,37))                                           
        self.lcodage.Show(False)
        self.codage.Show(False)
        self.ccodage.Show(False)
        self.ragsoc1age.Show(False)
        ##self.lsc1.Show(False)            
        ##self.sc1.Show(False)
        ##self.lsc2.Show(False)
        ##self.sc2.Show(False)           
        #self.lsc2.Show(True)
        wx.StaticText(self.pnl1, -1, "Paese:", wx.DLG_PNT(self.pnl1, 5,50))
        self.paese = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 5,60), wx.DLG_SZE(self.pnl1, 20,-1))
        wx.StaticText(self.pnl1, -1, "Cod.C:", wx.DLG_PNT(self.pnl1, 28,50))
        self.cod_c = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 28,60), wx.DLG_SZE(self.pnl1, 20,-1))
        wx.StaticText(self.pnl1, -1, "CIN:", wx.DLG_PNT(self.pnl1, 51,50))
        self.cin = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 52,60), wx.DLG_SZE(self.pnl1, 10,-1))
        wx.StaticText(self.pnl1, -1, " ABI :", wx.DLG_PNT(self.pnl1, 70,50))
        self.abi = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 70,60), wx.DLG_SZE(self.pnl1, 40,-1))
        wx.StaticText(self.pnl1, -1, " CAB :", wx.DLG_PNT(self.pnl1, 115,50))
        self.cab = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 115,60), wx.DLG_SZE(self.pnl1, 40,-1))
        wx.StaticText(self.pnl1, -1, " C/C:", wx.DLG_PNT(self.pnl1, 160,50))
        self.ncc = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 160,60), wx.DLG_SZE(self.pnl1, 80,-1))
        wx.StaticText(self.pnl1, -1, " Banca :", wx.DLG_PNT(self.pnl1, 5,75))
        self.banca = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 5,85), wx.DLG_SZE(self.pnl1, 235,-1))
        wx.StaticText(self.pnl3, -1, " Note :", wx.DLG_PNT(self.pnl3, 5,5))
        self.note = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 5,15), 
            wx.DLG_SZE(self.pnl3, 250,20), wx.TE_MULTILINE)
        wx.StaticText(self.pnl3, -1, "Cod. Spedizione :", 
            wx.DLG_PNT(self.pnl3, 5,38))
        self.codcf1 = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 5,48), wx.DLG_SZE(self.pnl3, 60,-1))
        self.ccoddest = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
            wx.DLG_PNT(self.pnl3, 70,48),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl3, -1, "Destinatario :", 
            wx.DLG_PNT(self.pnl, 90,38))
        self.ragsoc3 = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 90,48), wx.DLG_SZE(self.pnl3, 120,-1))
        self.modidest = wx.Button(self.pnl3, Nid, "&Nuovo", 
            wx.DLG_PNT(self.pnl3, 215,48),
            wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
        self.cancdest = wx.Button(self.pnl3, Nid, "Annul&la", 
            wx.DLG_PNT(self.pnl3, 215,63),
            wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
        wx.StaticText(self.pnl3, -1, "Ns Riferimento :", 
            wx.DLG_PNT(self.pnl3, 5,72))
        self.nsrif = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 90,70), wx.DLG_SZE(self.pnl3, 120,-1))

        # fax e mail di contatto per invio documenti
        wx.StaticText(self.pnl3, -1, "Fax invio documenti:", 
	      wx.DLG_PNT(self.pnl3, 5,85))
        self.faxd = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 5,95), wx.DLG_SZE(self.pnl3, 85,-1))
        wx.StaticText(self.pnl3, -1, " EMail invio documenti :", 
	      wx.DLG_PNT(self.pnl3, 120,85))
        self.emaild = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 120,95), wx.DLG_SZE(self.pnl3, 120,-1))

        #self.reg_def = wx.TextCtrl(self.pnl1, Nid, "",
        #wx.DLG_PNT(self.pnl1, 250,75), wx.DLG_SZE(self.pnl1, 20,-1))
        wx.StaticText(self.pnl2, -1, "Indirizzo :", wx.DLG_PNT(self.pnl2, 5,7))
        self.indiriz = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 45,5), wx.DLG_SZE(self.pnl2, 210,-1))
        wx.StaticText(self.pnl2, -1, "Citta :", wx.DLG_PNT(self.pnl2, 5,22))
        self.zona = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 45,20), wx.DLG_SZE(self.pnl2, 100,-1))
        wx.StaticText(self.pnl2, -1, "CAP :", wx.DLG_PNT(self.pnl2, 150,22))
        self.cap = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 175, 20), wx.DLG_SZE(self.pnl2, 35,-1))
        wx.StaticText(self.pnl2, -1, "PR :", wx.DLG_PNT(self.pnl2, 215,22))
        self.pr = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 235, 20), wx.DLG_SZE(self.pnl2, 20,-1))
        self.ltabi = wx.StaticText(self.pnl2, -1, "Telefono :", 
            wx.DLG_PNT(self.pnl2, 5,37))
        self.tabi = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 45,35), wx.DLG_SZE(self.pnl2, 85,-1))
        wx.StaticText(self.pnl2, -1, "Fax :", wx.DLG_PNT(self.pnl2, 140,37))
        self.fax = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 170, 35), wx.DLG_SZE(self.pnl2, 85,-1))

        #self.lmob = wx.StaticText(self.pnl2, -1, "Mobile :", 
        #    wx.DLG_PNT(self.pnl2, 140,37))
        #self.mob = wx.TextCtrl(self.pnl2, Nid, "",
        #      wx.DLG_PNT(self.pnl2, 170, 35), wx.DLG_SZE(self.pnl2, 85,-1))
	
        wx.StaticText(self.pnl2, -1, "Localita` :", 
            wx.DLG_PNT(self.pnl2, 5,52))
        self.localit = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 45,50), wx.DLG_SZE(self.pnl2, 85,-1))
        wx.StaticText(self.pnl2, -1, "Stato :", wx.DLG_PNT(self.pnl2, 140,52))
        self.stato = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 170, 50), wx.DLG_SZE(self.pnl2, 85,-1))
        wx.StaticText(self.pnl2, -1, " EMail :", wx.DLG_PNT(self.pnl2, 5,67))
        self.email = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 45,65), wx.DLG_SZE(self.pnl2, 120,-1))
        wx.StaticText(self.pnl2, -1, " Url :", wx.DLG_PNT(self.pnl2, 5,82))
        self.web = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 45,80), wx.DLG_SZE(self.pnl2, 120,-1))
        self.sbox = wx.StaticBox(self.pnl2, Nid, " ",
              wx.DLG_PNT(self.pnl2, 170,60), wx.DLG_SZE(self.pnl2, 80,35))
        self.rbCONFER = wx.RadioButton(self.pnl2, Nid, "Confermato",
              wx.DLG_PNT(self.pnl2, 180,70), 
            wx.DLG_SZE(self.pnl2, 60,10))
        self.rbPREVIS = wx.RadioButton(self.pnl2, Nid, "Previsione",
              wx.DLG_PNT(self.pnl2, 180,80), 
            wx.DLG_SZE(self.pnl2, 60,10))
        self.precon = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 280,100))    
        #self.provv = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 280,100))
        #self.provv_ma = wx.TextCtrl(self.pnl, -1, "", 
        #     wx.DLG_PNT(self.pnl, 280,100))
        self.new = wx.Button(self.pnl, Nid, cfg.vcnew, 
            wx.DLG_PNT(self.pnl, 285,20), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.ok = wx.Button(self.pnl, Nid, cfg.vcok, 
            wx.DLG_PNT(self.pnl, 285,20), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))               
        self.inte = wx.Button(self.pnl, Nid, cfg.vcint, 
            wx.DLG_PNT(self.pnl, 285,35), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV)) 
        self.canc = wx.Button(self.pnl, Nid, cfg.vccanc, 
            wx.DLG_PNT(self.pnl, 285,35), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.modi = wx.Button(self.pnl, Nid, cfg.vcmodi, 
            wx.DLG_PNT(self.pnl, 285,50), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))      
        self.dele = wx.Button(self.pnl, Nid, cfg.vcdele, 
            wx.DLG_PNT(self.pnl, 285,50), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
            wx.DLG_PNT(self.pnl, 285,65), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.scheda = wx.Button(self.pnl, Nid, cfg.vcscheda, 
            wx.DLG_PNT(self.pnl, 285,80), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))

        #self.SetFont(self.font)
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)
        self.pnl.SetFont(self.font)
        self.pnl0.SetFont(self.font)
        self.pnl1.SetFont(self.font)
        self.pnl2.SetFont(self.font)
        self.pnl3.SetFont(self.font)
        self.ntbk.SetFont(self.font)        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)


        self.rbCONFER.Bind(wx.EVT_RADIOBUTTON,self.RadioB)
        self.rbPREVIS.Bind(wx.EVT_RADIOBUTTON,self.RadioB)
        self.ok.Bind(wx.EVT_BUTTON,self.Save)
        self.new.Bind(wx.EVT_BUTTON,self.New)  
        self.inte.Bind(wx.EVT_BUTTON,self.IntAnag) 
        self.modi.Bind(wx.EVT_BUTTON,self.Modi)      
        self.canc.Bind(wx.EVT_BUTTON,self.Close)
        self.dele.Bind(wx.EVT_BUTTON,self.CntrDele)
        self.ccodcf.Bind(wx.EVT_BUTTON,self.FndCodCF)
        self.cancdest.Bind(wx.EVT_BUTTON,self.CancDest)
        self.modidest.Bind(wx.EVT_BUTTON,self.ModiDest)
        self.ccoddest.Bind(wx.EVT_BUTTON,self.FndCodCFDest)
        self.ccodage.Bind(wx.EVT_BUTTON,self.FndAge)
        self.cragsoc1.Bind(wx.EVT_BUTTON,self.FndAnag)
        self.codage.Bind(wx.EVT_TEXT_ENTER,self.FndAge)
        self.codcf.Bind(wx.EVT_TEXT_ENTER,self.FndCodCF)
        self.codcf1.Bind(wx.EVT_TEXT_ENTER,self.FndCodCFDest)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER,self.FndAnag)
        #self.ragsoc1.Bind(wx.EVT_TEXT,self.FndAnag)
        self.ragsoc1.Bind(wx.EVT_CHAR,self.EvtChar)
        self.indiriz.Bind(wx.EVT_TEXT_ENTER,self.zonaSF)
        self.zona.Bind(wx.EVT_TEXT_ENTER,self.capSF)
        self.cap.Bind(wx.EVT_TEXT_ENTER,self.prSF)
        self.pr.Bind(wx.EVT_TEXT_ENTER,self.localitSF)
        self.localit.Bind(wx.EVT_TEXT_ENTER,self.tabiSF)
        self.tabi.Bind(wx.EVT_TEXT_ENTER,self.mobSF)
        self.mob.Bind(wx.EVT_TEXT_ENTER,self.pivaSF)
        self.piva.Bind(wx.EVT_TEXT_ENTER,self.codfiscSF)
        self.ragsoc2.Bind(wx.EVT_TEXT_ENTER,self.FndAnagIs)
        self.cap.Bind(wx.EVT_KILL_FOCUS,self.KillFcs_cap)
        self.tabi.Bind(wx.EVT_KILL_FOCUS,self.KillFcs_tabi)
        self.mob.Bind(wx.EVT_KILL_FOCUS,self.KillFcs_mob)
        self.tuff.Bind(wx.EVT_KILL_FOCUS,self.KillFcs_tuff)
        self.fax.Bind(wx.EVT_KILL_FOCUS,self.KillFcs_fax)
        self.piva.Bind(wx.EVT_KILL_FOCUS,self.KillFcs_piva)
        self.codfisc.Bind(wx.EVT_KILL_FOCUS,self.KillFcs_codfisc)
        self.pr.Bind(wx.EVT_KILL_FOCUS,self.KillFcs_pr)
        self.PAGAM.Bind(wx.EVT_COMBOBOX,self.SelPAGAM)
        self.stampa.Bind(wx.EVT_BUTTON,self.Stampa)
        self.Bind(wx.EVT_CLOSE,self.Close)    
        self.Bind(wx.EVT_CHAR,self.EvtCharS)    
        self._locked = False
        self.Start(self)

    #<daniele> 
    def Stampa(self, evt): 
        codcf = self.codcf.GetValue()
        if self.tcpart=="C" : tipodoc = 'sanagc'
        if self.tcpart=="F" : tipodoc = 'sanagf'
        if self.tcpart=="A" : tipodoc = 'sanaga'   
        if self.tcpart=="V" : tipodoc = 'sanagv'      
        import skprint
        valueSql = self.tcpart, codcf
        skprint.stampaDoc(
              conn = self.CnAz , #connessione
              tipo = tipodoc, #tipo documento e parametro
              parametriSql = valueSql,
              #datiazienda = self.dzDatiAzienda,
              anteprima = True )
    #</daniele>                            

    def Start(self, evt):
        #self.AggMenu(False,self.IDMENU)
        self.DelTxt(self)
        self.OffTxt(self)
        self.dele.Enable(False)
        self.dele.Show(False) # aggiunto per errore visualizzione mac
	self.scheda.Enable(False)
        self.stampa.Enable(False)
        self.modi.Enable(False)
        self.new.Show(True)
        self.ok.Show(False)
        self.inte.Show(False)
        self.codcf.Enable(True)
        self.ccodcf.Enable(True)
        self.ragsoc1.Enable(True)
        self.ragsoc1.SetFocus()
        self.cragsoc1.Enable(True)
        self.t_cpart.Enable(False)
        self.t_cpart.Show(False)
        self.precon.Enable(False)
        self.ragsoc1age.Enable(False)
        self.precon.Show(False)
        self.precon.SetValue("C")
        if self.vPAGAM.GetValue()=="":
            self.vPAGAM.SetValue("PAG23")
            self.sPAGAM = ""
        self.PAGAM.Enable(False)
        self.vPAGAM.Enable(False)
        self.vPAGAM.Show(False)
        self.SelCOMBO(self)
        self.cntr = ""
        if (self.rec!=""):
            self.codcf.SetValue(self.rec)
            self.FndCodCF(self)
        self.note.SetBackgroundColour(self.color)
        self.rbCONFER.SetValue(True)
        self.rbPREVIS.SetValue(False)


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
        
    def SelRadioB(self, evt):
        if (self.precon.GetValue()=="C"):
            self.rbCONFER.SetValue(True)
            self.rbPREVIS.SetValue(False)
        elif (self.precon.GetValue()=="P"):
            self.rbCONFER.SetValue(False)
            self.rbPREVIS.SetValue(True)       
        elif (self.precon.GetValue()==""):
            self.precon.SetValue("C")
            self.rbCONFER.SetValue(True)
            self.rbPREVIS.SetValue(False)

    def RadioB(self, evt):
        if (self.rbCONFER.GetValue()==True):
            self.precon.SetValue("C")
        elif (self.rbPREVIS.GetValue()==True):
            self.precon.SetValue("P")
            
    def IntAnag(self, evt):
        self.rec = ""
        self.Start(self)
        self.canc.Show(True)
        self.new.Show(True)
        self.ok.Show(False)
        self.dele.Show(False)
        self.stampa.Enable(False)

    def FndSelAge(self, evt):
        row = evt
        self.codage.SetValue(str(row[0]))
        self.ragsoc1age.SetValue(str(row[1]).title())
        self.sc1.SetFocus()
        
    def FndSel(self, evt):
        row = evt
        self.t_cpart.SetValue(str(row[0]))
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.indiriz.SetValue(str(row[6]).title())         
        self.zona.SetValue(str(row[8]).title())
        self.localit.SetValue(str(row[9]).title())   
        cap = string.zfill(str(row[7]).strip(),5)
        if cap=="00000" : cap  = ""
        self.cap.SetValue(cap)
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
        cap1 = string.zfill(str(row[13]).strip(),5)
        if cap1=="00000" : cap1  = ""
        self.cap1.SetValue(cap1)
        self.pr1.SetValue(str(row[16]).strip().upper())
        self.stato1.SetValue(str(row[17]).title())
        self.banca.SetValue(str(row[26]).title())
	# paese cod_c cin
        self.abi.SetValue(str(row[28]).strip())
        self.cab.SetValue(str(row[29]).strip())
        self.ncc.SetValue(str(row[27]).strip())
        if (self.tblanag=="anag"):
            ##self.__MDI__.CnvVM(str(row[30]))                                   
            ##self.sc1.SetValue(self.__MDI__.val)                   
            ##self.__MDI__.CnvVM(str(row[31]))
            ##self.sc2.SetValue(self.__MDI__.val)           
            self.codage.SetValue(str(row[38]))
            self.codcf1.SetValue(str(row[39]))
            if row[39]=='' or row[39]==None:self.codcf1.SetValue('')
            if self.codcf1.GetValue()!="":self.FndCodCFDest(self)
            self.vPAGAM.SetValue(str(row[42]))
            self.precon.SetValue(str(row[47]))
            self.SelRadioB(self)
            self.note.SetValue(str(row[48])) 
	    # modifica banca
            #self.campo1.SetValue(str(row[49])) 
	    #self.campo2.SetValue(str(row[50]))
	    self.paese.SetValue(str(row[51]))
	    self.cod_c.SetValue(str(row[52]))
	    self.cin.SetValue(str(row[53]))
	    self.faxd.SetValue(str(row[54]))
	    self.emaild.SetValue(str(row[55]))

            self.nsrif.SetValue(str(row[5]))            
        else: 
            ##self.__MDI__.CnvVM(str(row[32]))                                    
            ##self.sc1.SetValue(self.__MDI__.val)
            self.codage.SetValue(str(row[31]))
            ##self.__MDI__.CnvVM(str(row[30]))
            ##self.sc2.SetValue(self.__MDI__.val)
        if (self.codage.GetValue().strip()!=""):self.FndAge(self)
        self.SelCOMBO(self)
        self.OffTxt(self)
        self.modi.Enable(True)
        self.modi.SetFocus()
        self.canc.Show(False)
        self.inte.Show(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(False)
        self.dele.Show(False)
        self.stampa.Enable(True)


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
        self.dele.Show(True)
        self.dele.Enable(True)
        
        
    def SaveTxt(self, evt):
        self.OffTxt(self)
        self.inte.SetFocus()
        self.ok.Show(False)
        self.new.Show(True)
        self.dele.Show(False)
        self.dele.Enable(False)

    def EvtChar(self, evt):
        evt_char = evt.GetKeyCode()
        #print "EvtChar %s" % evt_char
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()

    def EvtCharS(self, evt):
        evt_char = evt.GetKeyCode()
        #print "EvtCharS %s" % evt_char
        if evt_char==49: self.ntbk.SetSelection(0)
        if evt_char==50: self.ntbk.SetSelection(1)
        if evt_char==51: self.ntbk.SetSelection(2)
        if evt_char==52: self.ntbk.SetSelection(3)
        evt.Skip() 
       
    def OffTxt(self, evt):
        self.codcf.Enable(False)
        self.ccodcf.Enable(False)
        self.codcf1.Enable(False)
        self.ccoddest.Enable(False)
        self.modidest.Enable(False)
        self.cancdest.Enable(False)
        self.codage.Enable(False)
        self.ccodage.Enable(False)
        self.ragsoc3.Enable(False)
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
        ##self.sc1.Enable(False)
        ##self.sc2.Enable(False)
        self.web.Enable(False)
        self.PAGAM.Enable(False)
        self.note.Enable(False)
        self.note.SetBackgroundColour(self.color)
        self.nsrif.Enable(False)   
	#modifica banca
	self.paese.Enable(False)
        self.cod_c.Enable(False)
        self.cin.Enable(False)
	# modifica listino
	self.lst.Enable(False)
        self.clst.Enable(False)
        # modifica email fax doc
        self.faxd.Enable(False)
	self.emaild.Enable(False)
        self.abi.Enable(False)
        self.cab.Enable(False)
        self.ncc.Enable(False)
        self.banca.Enable(False)
        self.rbCONFER.Enable(False)
        self.rbPREVIS.Enable(False)
        self.cntr = ""
        if self.codcf1.GetValue()!="": self.modidest.SetLabel('Mo&difica')
        if self.codcf1.GetValue()=="": self.modidest.SetLabel('&Nuovo')


    def OnTxt(self ,evt):
        self.ragsoc3.Enable(True)
        self.modidest.Enable(True)
        self.cancdest.Enable(True)
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
        self.codage.Enable(True)
        self.ccodage.Enable(True)
        self.piva.Enable(True)
        self.codfisc.Enable(True)
        self.email.Enable(True)
        ##self.sc1.Enable(True)
        ##self.sc2.Enable(True)
	# modifica fax email doc
	self.faxd.Enable(True)
	self.emaild.Enable(True)
        self.web.Enable(True)
        self.localit.Enable(True)
        self.stato.Enable(True)
        self.PAGAM.Enable(True)
        self.note.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.note.Enable(True)
        self.nsrif.Enable(True)
        self.abi.Enable(True)
        self.cab.Enable(True)
        self.ncc.Enable(True)
        self.banca.Enable(True)
        self.paese.Enable(True)
        self.cod_c.Enable(True)
        self.cin.Enable(True)
        self.rbCONFER.Enable(True)
        self.rbPREVIS.Enable(True)
        
    def DelTxt(self, evt):
        self.codcf.SetValue('')
        self.codcf1.SetValue('')
        self.codage.SetValue('')
        self.ragsoc1age.SetValue('')
        self.ragsoc3.SetValue('')
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
        ##self.sc1.SetValue('')
        ##self.sc2.SetValue('')
        self.email.SetValue('')
        self.web.SetValue('')
        self.abi.SetValue('')
        self.cab.SetValue('')
        self.ncc.SetValue('')        
	self.paese.SetValue('')
        self.cod_c.SetValue('')
        self.cin.SetValue('')
        self.faxd.SetValue('')
        self.emaild.SetValue('')

        self.banca.SetValue('')
        if self.vPAGAM.GetValue()=="":
            self.vPAGAM.SetValue("PAG23")
            self.sPAGAM = ""
        
        self.SelCOMBO(self)
        self.note.SetValue('')
        self.nsrif.SetValue('')
        self.t_cpart.SetValue(self.tcpart)
        #print self.tblanag, self.t_cpart.GetValue()
        #self.reg_def.SetValue('N')
        self.precon.SetValue("C")
        self.rbCONFER.SetValue(True)
        self.rbPREVIS.SetValue(False)   
 
    def SelCOMBO(self, evt):
        # Funzione Cerca TabGen
        vPAGAM = self.vPAGAM.GetValue()
        self.PAGAM.Clear()
        sql = """ select cod, valore, descriz from tabgen """
        try:
            #cr = slef.prnt.GetConnAZ().cursor ()
            cr = self.CnAz.cursor ()
            cr.execute(sql)                 
            while (1):
                row = cr.fetchone () 
                if row==None: 
                    break
                if (row[0]=="PAGAM"):
                    if (row[1]==vPAGAM):self.sPAGAM = row[2]
                    self.PAGAM.Append(row[2],row[1])    
        except StandardError, msg:
            self.__MDI__.MsgErr("Anag"," tabgen Error %s"  % (msg))
        self.CnAz.commit()
        cntPAGAM = 0
        cntPAGAM = self.PAGAM.FindString(self.sPAGAM)
        self.PAGAM.Select(cntPAGAM)

    def SelPAGAM(self, evt):
        self.Sel(evt)
        self.vPAGAM.SetValue(self.cb_val)

    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str =  evt.GetString()
        evt.Skip()
        
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        dlg.ShowModal()
        dlg.Destroy()

          
    def SetFcs(self, evt):
        #print "SetFocus"
        evt.Skip()

    def CallAfter(self, func, *args, **kargs):
        def function(args = args, kargs = kargs):
            return func(*args, **kargs)
        wx.CallAfter(function)
        
    def CallLocked(self, evt):
        if self:
            if self._locked:
                self.CallAfter(self.CallLocked, evt)
            else:
                self._locked = True
                wx.BeginBusyCursor()
                try:
                    evt()
                finally:
                    self._locked = False
                    wx.EndBusyCursor()

    def KillFcs_cap(self,evt):
        self.CallAfter(self.CallLocked, self.GetV_cap)
        evt.Skip()
                   
    def GetV_cap(self):            
        vcap = self.cap.GetValue()
        if (vcap!=""):
            if (vcap.isdigit()!= True):
                self.Message("CAP "  +  cfg.msgdatono,self.ttl)
                self.cap.SetFocus()

    def KillFcs_tabi(self,evt):
        #self.CallAfter(self.CallLocked, self.GetV_tabi)
        evt.Skip()

    def GetV_tabi(self):
        vtabi = self.tabi.GetValue()
        if (vtabi!=""):
            if (vtabi.isdigit()!= True ):
                self.Message("Telefono "  +  cfg.msgdatono,self.ttl)
                self.tabi.SetFocus()

    def KillFcs_codcf(self,evt):
        #self.CallAfter(self.CallLocked, self.GetV_codcf)
        evt.Skip()
                
    def GetV_codcf(self):
        vcodcf = self.codcf.GetValue()
        if (vcodcf==""):
            self.Message("Cod. "  +  cfg.msgdatono,self.ttl)
            self.codcf.SetFocus()

    def KillFcs_mob(self, evt):
        #self.CallAfter(self.CallLocked, self.GetV_mob)
        evt.Skip()
            
    def GetV_mob(self):
        vmob = self.mob.GetValue()
        if (vmob!=""):
            if (vmob.isdigit()!= True ):
                self.Message("Mobile "  +  cfg.msgdatono,self.ttl)
                self.mob.SetFocus()

    def KillFcs_pr(self, evt):
        #self.CallAfter(self.CallLocked, self.GetV_pr)
        evt.Skip()

    def GetV_pr(self):
        vpr = self.pr.GetValue()
        if (vpr!=""): 
            if (vpr.isalpha()!= True):
                self.Message("PR "  +  cfg.msgdatono,self.ttl)
                self.pr.SetFocus()
            
    def KillFcs_codfisc(self,evt):
        #self.CallAfter(self.CallLocked, self.GetV_codfisc)
        evt.Skip()

    def GetV_codfisc(self):
        vcodfisc = self.codfisc.GetValue()
        if (vcodfisc!=""):
            if (vcodfisc.isalnum()!= True):
                self.Message("Cod. Fisc. "  +  cfg.msgdatono,self.ttl)
                self.codfisc.SetFocus()

    def KillFcs_piva(self,evt):
        #self.CallAfter(self.CallLocked, self.GetV_piva)
        evt.Skip()

    def GetV_piva(self):
        vpiva = self.piva.GetValue()
        if (vpiva!=""):
            if (vpiva.isdigit()!= True):
                self.Message(" IVA "  +  cfg.msgdatono,self.ttl)
                self.piva.SetFocus()

    def KillFcs_fax(self, evt):
        #self.CallAfter(self.CallLocked, self.GetV_fax)
        evt.Skip()
            
    def GetV_fax(self):
        vfax = self.fax.GetValue()
        if (vfax!=""):
            if (vfax.isdigit()!= True ):
                self.Message("Fax "  +  cfg.msgdatono,self.ttl)
                self.fax.SetFocus()

    def KillFcs_tuff(self, evt):
        #self.CallAfter(self.CallLocked, self.GetV_tuff)
        evt.Skip()
            
    def GetV_tuff(self):
        vtuff = self.tuff.GetValue()
        if (vtuff!=""):
            if (vtuff.isdigit()!= True ):
                self.Message("Telefono Uff "  +  cfg.msgdatono,self.ttl)
                self.tuff.SetFocus()
            
    def Close(self, evt):
        #if (self.ragsoc2.GetValue()!="" or self.ragsoc1.GetValue()!=""):
        if (self.ragsoc1.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgesci, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal()==wx.ID_YES:
                dlg.Destroy()
                self.AggMenu(True,self.IDMENU )
                wx.GetApp().GetPhasisMdi().CloseTabObj(self)
            else:
                dlg.Destroy() 
        else:
            self.AggMenu(True,self.IDMENU )
            wx.GetApp().GetPhasisMdi().CloseTabObj(self)
                 
    def Modi(self, evt):
        dlg = wx.MessageDialog(self, msgmodi_anag, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.ModiTxt(self)
            self.cntr = "modi"
            self.ntbk.SetFocus()
            dlg.Destroy()
        else:
            self.cntr = ""
            dlg.Destroy()
 
    def New(self, evt):
        # Funzione Nuovo
        self.DelTxt(self)
        #self.ntbk.SetFocus()
        self.cntr = "new"
        self.NewTxt(self)
        tcpart = self.t_cpart.GetValue().upper()
        sql = """ select max(cod) from anag where t_cpart = "%s" """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % tcpart)
            while (1):
                row = cr.fetchone()
                if row==None:
                    break
                if (row[0]==None) : self.codcf.SetValue('1')
                if (row[0] != None) : self.codcf.SetValue(str(int(row[0]) + 1))
        except StandardError, msg:
            self.__MDI__.MsgErr("Anag"," New Error %s"  % (msg))
        self.CnAz.commit()
     
    def Save(self, evt):
        vcntr = self.cntr
        vtabi = self.tabi.GetValue()
        vmob = self.mob.GetValue()
        vfax = self.fax.GetValue()
        vtuff = self.tuff.GetValue()
        vpr = self.pr.GetValue()
        vpr1 = self.pr1.GetValue()
        if vpr=="":vpr = "--"
        if vpr1=="":vpr1 = "--"
        ##self.__MDI__.CnvPM(self.sc1.GetValue())
        vsc1 = 0 #self.__MDI__.val
        ##self.__MDI__.CnvPM(self.sc2.GetValue())
        vsc2 = 0 #self.__MDI__.val
        vcodfisc = self.codfisc.GetValue()
        vpiva = self.piva.GetValue()
        vcodcf = self.codcf.GetValue()
        vcodcf1 = self.codcf1.GetValue()
        vragsoc1 = self.ragsoc1.GetValue().strip().title() 
        if (vcodcf.isdigit()!= True ):
            self.Message(cfg.msgdatono,self.ttl)
        if (vragsoc1==""):
            self.Message(cfg.msgcmp_null,self.ttl)
            self.ragsoc1.SetFocus()
        else:
            self.SaveTxt(self)
            #print "else"
            #print self.position
            #raise RuntimeError, 'write failed'
            vtcpart = self.t_cpart.GetValue().strip().upper()        
            vcodcf = self.codcf.GetValue().strip()
            vcodcf1 = self.codcf1.GetValue().strip()
            vragsoc2 = self.ragsoc2.GetValue().strip().title() 
            vragsoc1 = self.ragsoc1.GetValue().strip().title()  
            vindiriz = self.indiriz.GetValue().strip().title()
            vzona = self.zona.GetValue().strip().title()
            vlocalit = self.localit.GetValue().strip().title()
            vcap = self.cap.GetValue().strip()
            #if vcap=="" : vcap = 0                   
            vpr = self.pr.GetValue().strip().upper()
            if vpr=="":vpr = "--"
            vstato = self.stato.GetValue().title()
            vtabi = self.tabi.GetValue().strip()        
            vfax = self.fax.GetValue().strip() 	    
            vmob = self.mob.GetValue().strip()
            vtuff = self.tuff.GetValue().strip()       
            vemail = self.email.GetValue().strip()
            vweb = self.web.GetValue().strip()
            vpiva = self.piva.GetValue().strip()
            vcodfisc = self.codfisc.GetValue().strip().upper()
            vindiriz1 = self.indiriz1.GetValue().strip().title()
            vzona1 = self.zona1.GetValue().strip().title()
            vlocalit1 = self.localit1.GetValue().strip().title()
            vcap1 = self.cap1.GetValue().strip()
            #if vcap1=="" : vcap1 = 0                   
            vpr1 = self.pr1.GetValue().strip().upper()
            if vpr1=="":vpr1 = "--"
            vstato1 = self.stato1.GetValue().strip().title()
            vbanca = self.banca.GetValue().strip().title()
            vabi = self.abi.GetValue().strip()
            if vabi=="" : vabi = 0                       
            vcab = self.cab.GetValue().strip()
            if vcab=="" : vcab = 0   
            vncc = self.ncc.GetValue().strip()
            vcodage = self.codage.GetValue().strip()
            vcod_ma = self.codage.GetValue().strip()
            vnote = self.note.GetValue().strip().upper()
            vPAGAM = self.vPAGAM.GetValue()
            vprecon = self.precon.GetValue().strip().upper()  
            #vreg_def = self.reg_def.GetValue()
            vcodbar = "" 
            vnsrif = self.nsrif.GetValue().strip().title()
            vfaxd = self.faxd.GetValue().strip() 
            vemaild = self.emaild.GetValue().strip().lower()   	    
            valiva = ""
            #vsc = ""
            #vsc1 = ""
            #vcod_ma = ""
            vprovv_ma = vsc1
            vprovv = vsc2
            vlst = ""
            vlst = ""
            if vlst=="" : vlst = 0                 
            #vsc2 = ""
            #if vsc2=="" : vsc2 = 0
            vsc3 = ""
            if vsc3=="" : vsc3 = 0               
            vfido = ""
            if vfido=="" : vfido = 0   
            vcod_div = ""
            vscad_da = ""
            vscad_a = ""
            vconseg = ""
            vtrasp = ""
            vcodvet = ""
            vcod_pdc = ""
            vmastro = ""
            if vmastro=="" : vmastro = 0          
            vrag_part = ""
            vcampo1 = ""
            vcampo2 = ""
	    # modifica banca
            vpaese = self.paese.GetValue().strip().upper()
            vcod_c = self.cod_c.GetValue().strip()
            vcin = self.cin.GetValue().strip().upper()

            vfrm1modi = vcodbar,vragsoc1,vragsoc2,vnsrif
            vfrm1 = vtcpart,int(vcodcf),vcodbar,vragsoc1,vragsoc2,vnsrif #6
            vfrm2 = vindiriz,vcap,vzona,vlocalit,vpr,vstato #6
            vfrm3 = vindiriz1,vcap1,vzona1,vlocalit1,vpr1,vstato1 #6
            vfrm4 = vtabi,vtuff,vmob,vfax,vweb,vemail #6
            vfrm5 = vcodfisc,vpiva,vbanca,vncc,int(vabi),int(vcab) #6
            vfrm6_cf = float(vsc1),float(vsc2),float(vsc3),int(vlst),\
                       vscad_da,vscad_a,vconseg,vtrasp #8
            vfrm6_age = float(vprovv),vcod_ma,float(vprovv_ma),vscad_da,vscad_a #5
            vfrm7_cf = vcodage,vcodcf1,vcodvet,vcod_pdc,vPAGAM,vmastro,vcod_div,\
                       float(vfido),vrag_part #8
            vfrm7_age = vcod_pdc,vPAGAM,int(vmastro),vcod_div,vrag_part #5
            vfrm8 = vprecon,vnote,vcampo1,vcampo2,vpaese,vcod_c,vcin,vfaxd,vemaild #4
            vfrm8modi = vprecon,vnote,vcampo1,vcampo2,vpaese,vcod_c,vcin,vfaxd,vemaild,int(vcodcf),vtcpart #6
            valueSql_cf =  vfrm1 + vfrm2 + vfrm3 + vfrm4 + vfrm5 +\
                           vfrm6_cf + vfrm7_cf + vfrm8
            valueSql_age =  vfrm1 + vfrm2 + vfrm3 + vfrm4 + vfrm5 +\
                            vfrm6_age + vfrm7_age + vfrm8
            valueSql_modi_cf = vfrm1modi + vfrm2 + vfrm3 + vfrm4 + vfrm5 +\
                               vfrm6_cf + vfrm7_cf + vfrm8modi
            valueSql_modi_age = vfrm1modi + vfrm2 + vfrm3 + vfrm4 + vfrm5 +\
                                vfrm6_age + vfrm7_age + vfrm8modi

            if(vcntr=="new"):
                # Funzione Salva 
                try:
                    cr = self.CnAz.cursor()
                    if self.tblanag=='agenti' :
                        sql = """ insert into agenti 
                                  values("%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s")  """                    
                        cr.execute(sql % valueSql_age)
                    else :
                        sql = """ insert into anag
                                  values("%s","%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s","%s") """
                        cr.execute(sql % valueSql_cf)
                except StandardError, msg:
                    self.__MDI__.MsgErr("Anag"," Ins Anag Error %s"  % (msg))
                self.CnAz.commit()
            if(vcntr=="modi"):
                try:
                    cr = self.CnAz.cursor()
                    if self.tblanag=='agenti' :
                        sql = """ update agenti set
                                  codbar = "%s", rag_soc1 = "%s", 
				  rag_soc2 = "%s", nsrif = "%s", 
				  indiriz = "%s", cap = "%s", zona = "%s", 
                                  localit = "%s", pr = "%s", stato = "%s",
				  indiriz1 = "%s", cap1 = "%s", zona1 = "%s", 
				  localit1 = "%s", pr1 = "%s", stato1 = "%s",
				  tel_abit = "%s", tel_uff = "%s", 
				  mobile = "%s", fax= "%s", web = "%s", 
				  e_mail = "%s", codfisc = "%s", piva = "%s", 
				  banca = "%s", num_cc = "%s", abi = "%s", 
				  cab = "%s", provv = "%s", cod_ma = "%s", 
                                  provv_ma = "%s", scad_da = "%s", 
				  scad_a = "%s", cod_pdc = "%s", cod_pag= "%s", 
				  mastro = "%s", vdiv = "%s", rag_part = "%s", 
                                  precon = "%s", note = "%s", campo1 = "%s", 
				  campo2 = "%s"
                                  where cod = "%s" and t_cpart = "%s" """                  
                        cr.execute(sql % valueSql_modi_age)
                    else :
                        sql = """ update anag set
                                  codbar = "%s", rag_soc1 = "%s", 
				  rag_soc2 = "%s", nsrif = "%s", 
				  indiriz = "%s", cap = "%s", zona = "%s", 
                                  localit = "%s", pr = "%s", stato = "%s",
				  indiriz1 = "%s", cap1 = "%s", zona1 = "%s", 
				  localit1 = "%s", pr1 = "%s", stato1 = "%s",
				  tel_abit = "%s", tel_uff = "%s", 
				  mobile = "%s", fax= "%s", web = "%s", 
				  e_mail = "%s", codfisc = "%s", piva = "%s", 
				  banca = "%s", num_cc = "%s", abi = "%s", 
				  cab = "%s", sc1 = "%s", sc2 = "%s", 
				  sc3 = "%s", lst = "%s", scad_da = "%s",
				  scad_a = "%s", conseg = "%s", trasp = "%s",
				  cod_age = "%s", cod_dest = "%s", 
				  cod_vet = "%s",  cod_pdc = "%s", 
				  cod_pag= "%s", mastro = "%s", vdiv = "%s", 
                                  fido = "%s", rag_part = "%s", precon = "%s", 
				  note = "%s", campo1 = "%s", campo2 = "%s",
				  paese = "%s", cod_c = "%s", cin = "%s",
				  faxd = "%s", emaild = "%s"
                                  where cod = "%s" and t_cpart = "%s" """
                        cr.execute(sql % valueSql_modi_cf)
                except StandardError, msg:
                    self.__MDI__.MsgErr("Anag","Update Error %s"  % (msg))
                self.CnAz.commit()

    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgnodele_anag, self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal()==wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr = ""
            dlg.Destroy()
            
    def Dele(self, evt):
        # Funzione Elimina
        dlg = wx.MessageDialog(self, cfg.msgdele_anag,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.cntr = "dele"
            cod = self.codcf.GetValue()
            if self.tblanag=='agenti' :
                sql = """ delete from agenti where cod = "%s" and t_cpart = "%s" """
            else:
                sql = """ delete from anag where cod = "%s" and t_cpart = "%s" """
            valueSql = int(cod),self.tcpart
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
            except StandardError, msg:
                self.__MDI__.MsgErr("Anag"," Dele Error %s"  % (msg))
            self.CnAz.commit()
            self.IntAnag(self)
            dlg.Destroy()
        else:
            self.cntr = ""
            dlg.Destroy()
       
    def FndAge(self, evt):
        # Funzione cerca
        cnt_rec = 0
        tcpart_age = "A"
        self.ragsoc1age.SetValue("")
        cod = self.codage.GetValue()
        if cod=="" :cod = 0
        elif (cod.isdigit()!= True): cod = 0
        val = self.codage.GetValue()       
        sql = """ select cod, rag_soc1 , provv 
                  from agenti where cod = "%s" or rag_soc1 like "%s" """
        valueSql = int(cod),'%' + val.title() + '%'
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec += 1
        except StandardError, msg:
            self.__MDI__.MsgErr("Anag"," FndAge Error %s"  % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAge(row)
        elif (cnt_rec>1):
            import srcanag
            control = [tcpart_age,self.codage,self.ragsoc1age,self.FndAge]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        

    def FndAnagIs(self, evt):
        cnt_rec = 0
        val1 = self.ragsoc1.GetValue().strip()
        val2 = self.ragsoc2.GetValue().strip()
        if (val1!="" and self.cntr=="new"):
            sql = """ select * from anag 
                          where rag_soc1 = "%s" and t_cpart = "%s" """
            valueSql = val1.title(), self.tcpart
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec += 1
            except StandardError, msg:
                self.__MDI__.MsgErr("Anag"," FndAnagIs Error %s"  % (msg))
            self.CnAz.commit()
            if (cnt_rec==1 and cnt_rec<2):
                self.Message(cfg.msgdatosi,self.ttl)
                self.cntr = ""
                self.FndSel(row)
            elif (cnt_rec>1):
                import srcanag
                control = [self.tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
                win = srcanag.create(self,control) 
                win.Centre(wx.BOTH)
                win.Show(True)
                
    def FndAnag(self, evt): 
        # Funzione cerca  		
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec = 0
            val = self.ragsoc1.GetValue()
            cod = self.codcf.GetValue()
            sql = """ select * from anag 
                          where t_cpart = "%s" and rag_soc1 like "%s" 
                          order by rag_soc1 desc """
            valueSql = self.tcpart, '%' + val.title() + '%'
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)           
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec += 1
            except StandardError, msg:
                self.__MDI__.MsgErr("Anag"," FndAnag Error %s"  % (msg))
            self.CnAz.commit()
            if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
            elif (cnt_rec==1 and cnt_rec<2): self.FndSel(row)
            elif (cnt_rec>1):
                import srcanag
                control = [self.tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
                win = srcanag.create(self,control) 
                win.Centre(wx.BOTH)
                win.Show(True)
            else:
                self.indiriz.SetFocus()
  
    def FndCodCF(self, evt):
        # Funzione cerca cod
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec = 0
            cod = self.codcf.GetValue()
            if cod=="" :cod = 0
            elif (cod.isdigit()!= True): cod = 0
            sql = """ select * from anag 
                          where cod = "%s" and t_cpart = "%s" """
            valueSql = int(cod), self.tcpart
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec += 1
            except StandardError, msg:
                self.__MDI__.MsgErr("Anag"," FndCodCF Error %s"  % (msg))
            self.CnAz.commit()
            if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
            elif (cnt_rec==1 and cnt_rec<2): self.FndSel(row)


    def FndCodCFDest(self, evt):
        # Funzione Cerca Codice   
        cnt_rec = 0
        val = self.ragsoc3.GetValue().upper()
        cod = self.codcf1.GetValue()
        sql = """ select * from tblcf where cod = "%s" and t_cpart = "%s" """
        valueSql = int(cod), self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec += 1
        except StandardError, msg:
            self.__MDI__.MsgErr("Anag"," FndCodCFDest Error %s"  % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttldest)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnagDest(row)
        
    def FndAnagDest(self, evt):
        # Funzione Cerca CF
        cnt_rec = 0
        val = self.ragsoc3.GetValue()
        cod = self.codcf1.GetValue()
        sql = """ select * from tblcf where rag_soc1 like "%s" 
                  and t_cpart = "%s" """
        valueSql = '%' + val.title() + '%', self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec += 1
        except StandardError, msg:
            self.__MDI__.MsgErr("Anag"," FndAnagDest Error %s"  % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttldest)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnagDest(row)
        elif (cnt_rec>1):
            import base.srctblcf
            control = [self.tcpart,self.codcf1,self.ragsoc3,self.FndCodCFDest]               
            win = base.srctblcf.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else:
            self.nsrif.SetFocus()
            
    def FndSelAnagDest(self, evt):
        row = evt
        self.codcf1.SetValue(str(row[1]))
        self.ragsoc3.SetValue(str(row[3]).title())          
        self.nsrif.SetFocus()

    def ModiDest(self, evt):
        ttl = "Anagrafica Spedizioni"
        codcf = self.codcf.GetValue()
        import base.tblcf
        control = [ttl,self.tcpart,self.codcf1,self.ragsoc3,codcf]               
        win = base.tblcf.create(self,control) 
        win.Centre(wx.BOTH)
        win.Show(True)

    def CancDest(self, evt):
        self.codcf1.SetValue('')
        self.ragsoc3.SetValue('')

    def is_look(self):
        if (self.cntr!="new" and self.cntr!="modi"): return False
        else : return True
        
    def data_reload(self,rec,cntrp):
        self.rec=rec
        tcpart=cntrp.upper()
        if (tcpart=="C" or tcpart=="F" or tcpart=="V" or tcpart=="T"):
            self.tblanag = "anag"
        if (tcpart=="A"):self.tblanag = "agenti"
        self.tcpart=tcpart
        self.Start(self)


