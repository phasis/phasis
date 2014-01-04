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
import  wx.lib.masked as masked


def create(parent,cnt):
    return MovCon(parent,cnt)
  
class MovCon(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######

        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        #wx.Frame.__init__(self, id=wx.NewId(), name='',
        #      parent=prnt, pos=wx.Point(0, 0), 
        #      style=wx.DEFAULT_FRAME_STYLE  , title=cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt_save=0
        self.ttl=cnt[0]
        self.tbl=cnt[4]
        self.tcpart="C"        
        self.rec = cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        #self.SetClientSize(wx.Size(680, 425))
        #self.font=self.GetFont()
        self.color=self.GetBackgroundColour()
        Nid = wx.NewId()
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz=self.__MDI__.GetConnAZ()
        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon= self.__MDI__.GetDataC()
        self.dzDatiAzienda= self.__MDI__.dzDatiAzienda
        self.lc_Slct=""
        self.Da_Av=""
        self.stt_doc="E"

        
        self.pnl = wx.Panel(id=wx.NewId(), name='',
              parent=self, pos=wx.Point(0, 0), size = wx.DLG_SZE(self,680/2,420/2), #size=wx.Size(680, 420),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        self.sbox_cf = wx.StaticBox(self.pnl, Nid, " Registrazione ",
              wx.DLG_PNT(self.pnl, 5,7), wx.DLG_SZE(self.pnl, 265,30))
        self.lmov = wx.StaticText(self.pnl, -1, "Numero :", 
              wx.DLG_PNT(self.pnl, 10,22))
        self.anno = wx.ComboBox(self.pnl, Nid, self.annoc,
              wx.DLG_PNT(self.pnl, 45,20), wx.DLG_SZE(self.pnl, 35,-1), [],
              wx.CB_DROPDOWN | wx.CB_SORT )  
        wx.StaticText(self.pnl, -1, "/", wx.DLG_PNT(self.pnl, 85,22))
        self.num_mov = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 90,20), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT) 
        self.cnum_mov = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 135,20),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl, -1, "Data :", wx.DLG_PNT(self.pnl, 160,22))
        #self.datamov = wx.TextCtrl(self.pnl, Nid, "",
        #      wx.DLG_PNT(self.pnl, 185,20), 
        #      wx.DLG_SZE(self.pnl, 50,cfg.DIMFONTDEFAULT),
        #      wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)

        self.datamov = masked.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 180,20), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT,autoformat='EUDATEDDMMYYYY/')


        self.cdatamov = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 240,20),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.vdatamov = wx.TextCtrl(self.pnl, Nid, "", wx.DLG_PNT(self.pnl, 280, 135))

        # causale 
        self.lCAUSA = wx.StaticText(self.pnl, -1, "Causale :", 
              wx.DLG_PNT(self.pnl, 7,42))
        self.vCAUSA = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 32,40), 
              wx.DLG_SZE(self.pnl, 35,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)            
        self.cCAUSA = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 68,40),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV),wx.TE_PROCESS_ENTER)
        wx.StaticText(self.pnl, -1, "Descrizione :", 
              wx.DLG_PNT(self.pnl, 82,42))
        self.dCAUSA = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 120, 40), 
              wx.DLG_SZE(self.pnl, 150,cfg.DIMFONTDEFAULT))
        # fine causale       

        self.pnl1 = wx.Panel(id = wx.NewId(), name = 'panel1',
              parent = self.pnl, pos = wx.Point(0,130), size = wx.DLG_SZE(self,680/2,190/2))
        self.pnl1.SetFont(self.font)
        
        self.pnl2 = wx.Panel(id = wx.NewId(), name = 'panel2',
              parent = self.pnl, pos = wx.Point(0,130), size = wx.DLG_SZE(self,680/2,190/2))
        self.pnl2.SetFont(self.font)

        wx.StaticText(self.pnl1, -1, "Controp.:", 
              wx.DLG_PNT(self.pnl1, 7,7)) #10,62
        self.CF = wx.ComboBox(self.pnl1, Nid,"",
              wx.DLG_PNT(self.pnl1, 35,5), wx.DLG_SZE(self.pnl1, 55,-1), [],
              wx.CB_DROPDOWN | wx.CB_SORT ) #65,60
        self.vCF = wx.TextCtrl(self.pnl1, -1, "", wx.DLG_PNT(self.pnl1, 275,35))
        self.lc1odcf = wx.StaticText(self.pnl1, -1, "Cod.", 
              wx.DLG_PNT(self.pnl1, 95,7)) #135,62
        self.codcf= wx.TextCtrl(self.pnl1, -1, "",
              wx.DLG_PNT(self.pnl1, 112, 5), 
              wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT))#185,60
        self.ccodcf = wx.BitmapButton(self.pnl1, -1, png,
              wx.DLG_PNT(self.pnl1, 152,5),
              wx.DLG_SZE(self.pnl1,cfg.btnSzeSH,cfg.btnSzeV))#250,60
        self.lragsoc1 = wx.StaticText(self.pnl1,-1,"Rag.Soc.1 ( Cognome ) :", 
              wx.DLG_PNT(self.pnl1, 157,7))#12,75
        self.ragsoc1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 245,5), 
              wx.DLG_SZE(self.pnl1, 75,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.cragsoc1 = wx.BitmapButton(self.pnl1, -1, png,
              wx.DLG_PNT(self.pnl1, 322,5),
              wx.DLG_SZE(self.pnl1,cfg.btnSzeSH,cfg.btnSzeV)) #135,85     
        self.lragsoc2 = wx.StaticText(self.pnl1, -1, "Rag. Soc.2 ( Nome ) :", 
              wx.DLG_PNT(self.pnl1, 7,23)) #55,75
        self.ragsoc2 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 75, 21), 
              wx.DLG_SZE(self.pnl1, 60,cfg.DIMFONTDEFAULT)) #153, 85         
        self.ldoc = wx.StaticText(self.pnl1, -1, "N.Doc.:", 
              wx.DLG_PNT(self.pnl1, 137,23)) #10,102)
        self.num_doc = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 161,21), 
              wx.DLG_SZE(self.pnl1, 30,cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) #60,100      
        wx.StaticText(self.pnl1, -1, "Data :", 
              wx.DLG_PNT(self.pnl1, 192,23)) #105,102
        #self.datadoc = wx.TextCtrl(self.pnl1, Nid, "",
        #      wx.DLG_PNT(self.pnl1, 115,25), 
        #      wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT), 
        #      wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)#130,100
        self.datadoc = masked.TextCtrl(self.pnl1, -1, "",
              wx.DLG_PNT(self.pnl1, 212,21), 
              wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT,autoformat='EUDATEDDMMYYYY/')#130,100
        self.cdatadoc = wx.BitmapButton(self.pnl1, -1, png,
              wx.DLG_PNT(self.pnl1, 258,21),
              wx.DLG_SZE(self.pnl1,cfg.btnSzeSH,cfg.btnSzeV)) #183,100
        self.ltotale_doc = wx.StaticText(self.pnl1, Nid, "Tot.Doc.:", 
              wx.DLG_PNT(self.pnl1, 272,23)) #205,102
        self.totale_doc = wx.TextCtrl(self.pnl1, Nid, "0,00",
              wx.DLG_PNT(self.pnl1, 300,21), 
              wx.DLG_SZE(self.pnl1, 34, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) #240,100     
        self.lc1 = wx.ListCtrl(self.pnl1, Nid,
              wx.DLG_PNT(self.pnl1, 5,35), wx.DLG_SZE(self.pnl1, 325,57),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)  #5,120
        #wx.StaticLine(self.pnl, -1, wx.DLG_PNT(self.pnl, 5,155), 
        #      wx.DLG_SZE(self.pnl, 283,-1)) 

        self.lc2 = wx.ListCtrl(self.pnl2, Nid,
              wx.DLG_PNT(self.pnl2, 5,2), wx.DLG_SZE(self.pnl2, 325,80),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)   
      
        wx.StaticText(self.pnl, -1, "Note :", wx.DLG_PNT(self.pnl, 5,152))
        self.note = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 32, 150), 
              wx.DLG_SZE(self.pnl, 228,cfg.DIMFONTDEFAULT), 
              wx.TE_PROCESS_ENTER)
        self.limportoval = wx.StaticText(self.pnl, Nid, "Importi  D/A :", 
              wx.DLG_PNT(self.pnl, 280,152)) #235,152
        self.importoval = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 275,140), 
              wx.DLG_SZE(self.pnl, 55, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )      
        self.ldifferenza = wx.StaticText(self.pnl, -1, "Sbilancio :", 
              wx.DLG_PNT(self.pnl, 235,197))
        self.differenza = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 275,195), 
              wx.DLG_SZE(self.pnl, 55, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )

        # conto dare 
        wx.StaticText(self.pnl, -1, "C/Dare:", 
              wx.DLG_PNT(self.pnl, 5,167))
        self.vCONTOD = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 32,165), 
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT), 
              wx.TE_PROCESS_ENTER)            
        self.cCONTOD = wx.BitmapButton(self.pnl, -1, png,
              wx.DLG_PNT(self.pnl, 65,165),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV),
              wx.TE_PROCESS_ENTER)
        self.ldCONTOD = wx.StaticText(self.pnl, -1, "Descrizione :", 
              wx.DLG_PNT(self.pnl, 82,167))
        self.dCONTOD = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 120, 165), 
              wx.DLG_SZE(self.pnl, 140,cfg.DIMFONTDEFAULT))
        self.importoD = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 275,165), 
              wx.DLG_SZE(self.pnl, 55, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER ) 
        # fine conto dare

        # conto avere 
        wx.StaticText(self.pnl, -1, "C/Avere:", 
              wx.DLG_PNT(self.pnl, 5,182))
        self.vCONTOA = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 32,180), 
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)            
        self.cCONTOA = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 65,180),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV),wx.TE_PROCESS_ENTER)
        self.ldCONTOA = wx.StaticText(self.pnl, -1, "Descrizione :", 
              wx.DLG_PNT(self.pnl, 82,182))
        self.dCONTOA = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 120, 180), 
              wx.DLG_SZE(self.pnl, 140,cfg.DIMFONTDEFAULT))
        self.importoA = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 275,180), 
              wx.DLG_SZE(self.pnl, 55, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER ) 
        # fine conto avere

        #self.differenza.SetFont(self.font)
        self.nriga = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 275,87)) 
        self.stt_mov = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 275,87))                           
        self.anno_iva = self.annoc
        self.vDIV = wx.TextCtrl(self.pnl, -1, "EU", 
              wx.DLG_PNT(self.pnl, 275,87)) 
        self.imponibval = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.anno_doc = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.vTIPO_DOC = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.num_doc1 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.conto = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.segno = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))
        self.PDC = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.t_cpart = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.CAMBIO = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.vTIPO_IVA1 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.vTIPO_IVA = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.vALIVA = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.registro = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.imponib = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.rigagior = wx.TextCtrl(self.pnl, -1, "0", 
              wx.DLG_PNT(self.pnl, 275,87))  
        self.paggior = wx.TextCtrl(self.pnl, -1, "0", 
              wx.DLG_PNT(self.pnl, 275,87))    
        self.ok = wx.Button(self.pnl, Nid, cfg.vcok, 
             wx.DLG_PNT(self.pnl, 275,10), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )      
        self.new = wx.Button(self.pnl, Nid, cfg.vcnew, 
             wx.DLG_PNT(self.pnl, 275,10), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )      
        self.oktestata = wx.Button(self.pnl, Nid, cfg.vcconf, 
             wx.DLG_PNT(self.pnl, 275,10), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )              
        self.inte = wx.Button(self.pnl, Nid, cfg.vcint, 
             wx.DLG_PNT(self.pnl, 275,25),
             wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.canc = wx.Button(self.pnl, Nid, cfg.vccanc, 
             wx.DLG_PNT(self.pnl, 275,25), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.modi = wx.Button(self.pnl, Nid, cfg.vcmodi, 
             wx.DLG_PNT(self.pnl, 275,40), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.dele = wx.Button(self.pnl, Nid, cfg.vcdele, 
             wx.DLG_PNT(self.pnl, 275,40), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
             wx.DLG_PNT(self.pnl, 275,55), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.newr = wx.Button(self.pnl, Nid, cfg.vcnewr, 
             wx.DLG_PNT(self.pnl, 5,195), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))      
        self.okr = wx.Button(self.pnl, Nid, cfg.vcokr, 
             wx.DLG_PNT(self.pnl, 70,195), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))
        self.modir = wx.Button(self.pnl, Nid, cfg.vcmodir, 
             wx.DLG_PNT(self.pnl, 70,195), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))
        self.intr = wx.Button(self.pnl, Nid, cfg.vcintr, 
             wx.DLG_PNT(self.pnl, 135,195), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
        self.delr = wx.Button(self.pnl, Nid, cfg.vcdeler, 
             wx.DLG_PNT(self.pnl, 185,195), 
             wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
        #self.SetFont(self.font)
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)

        self.delr.Bind(wx.EVT_BUTTON, self.DelRow)
        self.dele.Bind(wx.EVT_BUTTON, self.CntrDele)        
        self.oktestata.Bind(wx.EVT_BUTTON, self.OkTestata)
        self.canc.Bind(wx.EVT_BUTTON, self.Close)  
        self.okr.Bind(wx.EVT_BUTTON, self.OkRow)
        self.modi.Bind(wx.EVT_BUTTON, self.Modi)
        self.modir.Bind(wx.EVT_BUTTON, self.ModiRow)
        self.inte.Bind(wx.EVT_BUTTON, self.IntTestata)
        self.intr.Bind(wx.EVT_BUTTON, self.IntRow)
        self.newr.Bind(wx.EVT_BUTTON, self.NewRow)
        self.new.Bind(wx.EVT_BUTTON, self.New)
        self.ok.Bind(wx.EVT_BUTTON, self.Save)
        # < diegom
        self.cdatadoc.Bind(wx.EVT_BUTTON, self.FndVend)
        # > diegom
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.lc1.Bind(wx.EVT_LEFT_DCLICK, self.ModiRow)      
        self.lc1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlctlc1) 
        self.lc1.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlctlc1) 
        self.lc1.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) 
        # < diegom disab
        self.lc2.Bind(wx.EVT_LEFT_DCLICK, self.ModiRow)      
        self.lc2.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlctlc2) 
        self.lc2.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlctlc2) 
        self.lc2.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) 
        #self.pnl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct) # occhio forse self.lc
        #self.pnl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlct) # occhio forse self.lc
        #self.pnl.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) # occhio forse self.lc
        # < diegom disab
        self.importoA.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_importo)
        self.importoD.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_importo)

        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)   
        self.cCAUSA.Bind(wx.EVT_BUTTON, self.FndTABGEN)
        self.vCAUSA.Bind(wx.EVT_TEXT_ENTER, self.FndTABGEN)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.ragsoc1.Bind(wx.EVT_CHAR, self.EvtChar)        
        self.cnum_mov.Bind(wx.EVT_BUTTON, self.FndMov)
        self.num_mov.Bind(wx.EVT_TEXT_ENTER, self.FndMov)
        self.cdatamov.Bind(wx.EVT_BUTTON, self.CntData)
        self.datadoc.Bind(wx.EVT_TEXT_ENTER, self.CntDataDoc)

        self.cCONTOA.Bind(wx.EVT_BUTTON, self.FndPIACONA)
        self.vCONTOA.Bind(wx.EVT_TEXT_ENTER, self.FndPIACONA)
        self.cCONTOD.Bind(wx.EVT_BUTTON, self.FndPIACOND)
        self.vCONTOD.Bind(wx.EVT_TEXT_ENTER, self.FndPIACOND)
        self.note.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_note)
        self.num_mov.Bind(wx.EVT_CHAR, self.EvtChar)
        self.CF.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_CF) 
        self.num_doc.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_num_doc)        
        self.totale_doc.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_tot_doc)       
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.CF.Bind(wx.EVT_COMBOBOX, self.SelCF)
        # agg_movcon su at_all2       
        self.Start(self)
 

    def SelCAUSA(self,valueSql ):
        sql = """ select val1, val2 from tabgen where valore = "%s" """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql) 
            #print valueSql
            rows = cr.fetchall()
            for row in rows:
                #print row[0]
                if (row[0]=="LG"):
                    self.lc_Slct="lc2"
                    if (valueSql=="141" or valueSql=="140" or valueSql=="145" or valueSql=="240" or valueSql=="241" or valueSql=="245"):
                        self.stt_doc="R" 
                        self.lc_Slct="lc1"
                if (row[0]=="RI"):
                    self.lc_Slct="lc1"
        except StandardError, msg:
                self.__MDI__.MsgErr("movcon","SelCAUSA Error %s " % (msg))
        self.oktestata.Enable(True)
        self.OnAnagTxt(self)
	self.CnAz.commit()


    def Start(self, evt):
        self.pnl1.Show(False)
        self.pnl2.Show(True)
        #self.lragsoc2.Show(False)
        #self.ragsoc2.Show(False)
        self.cnt_save=0
        self.anno.Enable(False)
        self.vdatamov.Show(False)         
        self.importoval.Show(False) 
        #self.vCAUSA.Enable(False)
        self.dCAUSA.Enable(False)
        #self.cCAUSA.Enable(False)
        self.note.Enable(False)
        self.num_doc.Enable(False)
        self.datadoc.Enable(False)
        self.cdatadoc.Enable(False)
        self.vCF.Show(False)
        self.CF.Enable(False)
        self.codcf.Enable(False)
        self.ccodcf.Enable(False)        
        self.ccodcf.Show(False)         
        self.ragsoc1.Enable(False)
        self.cragsoc1.Enable(False)
        self.ragsoc2.Enable(False)
        self.vDIV.Show(False)  
        self.nriga.Show(False)  
        self.stt_mov.Show(False) 
        self.imponibval.Show(False)    
        self.anno_doc.Show(False)    
        self.vTIPO_DOC.Show(False)    
        self.num_doc1.Show(False)
        self.PDC.Show(False) 
        self.conto.Show(False)    
        self.segno.Show(False)    
        self.t_cpart.Show(False)    
        self.CAMBIO.Show(False)    
        self.vTIPO_IVA1.Show(False)    
        self.vTIPO_IVA.Show(False)    
        self.vALIVA.Show(False)    
        self.registro.Show(False)    
        self.imponib.Show(False)    
        self.rigagior.Show(False)    
        self.paggior.Show(False)  
        self.vDIV.Enable(False)
        self.PDC.Enable(False) 
        self.nriga.Enable(False)    
        self.imponibval.Enable(False)    
        self.anno_doc.Enable(False)    
        self.vTIPO_DOC.Enable(False)    
        self.num_doc1.Enable(False)    
        self.conto.Enable(False)    
        self.segno.Enable(False)    
        self.t_cpart.Enable(False)    
        self.CAMBIO.Enable(False)    
        self.vTIPO_IVA1.Enable(False)    
        self.vTIPO_IVA.Enable(False)    
        self.vALIVA.Enable(False)    
        self.registro.Enable(False)    
        self.imponib.Enable(False)    
        self.rigagior.Enable(False)    
        self.paggior.Enable(False)  
        self.importoA.Enable(False)        
        self.importoD.Enable(False)
        self.totale_doc.Enable(False)
        self.DelAnagTxt(self)
        self.DelDescTxt(self)
        self.OffAnagTxt(self)
        self.OffDescTxt(self)
        self.data = self.datacon         
        self.datamov.SetValue(self.data)
        self.datamov.Enable(True)
        self.num_mov.Enable(True)
        self.num_mov.SetFocus()
        self.cnum_mov.Enable(True)   
        self.lc1.ClearAll()
        self.lc1.InsertColumn(0, "Anno",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(1, "Num. Mov.",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(2, "Data Mov.",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(3, "Num. Riga",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(4, "Anno IVA",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(5, "Div",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(6, "PDC",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(7, "Descrizione Operazione",width=wx.DLG_SZE(self.pnl, 100,-1).width)
        self.lc1.InsertColumn(8, "Importo",width=wx.DLG_SZE(self.pnl, 40,-1).width)      
        self.lc1.InsertColumn(9, "Imponibile",width=cfg._COLSZ0_)     
        self.lc1.InsertColumn(10, "Anno Doc.",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(11, "Tipo Doc.",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(12, "Data Doc.",width=wx.DLG_SZE(self.pnl, 40,-1).width)#
        self.lc1.InsertColumn(13, "Num Doc.",width=wx.DLG_SZE(self.pnl, 40,-1).width)#
        self.lc1.InsertColumn(14, "Num Doc1.",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(15, "Conto",width=wx.DLG_SZE(self.pnl, 25,-1).width)
        self.lc1.InsertColumn(16, "Totale Doc.",width=cfg._COLSZ0_)#
        self.lc1.InsertColumn(17, "segno",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(18, "Tipo CPart",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(19, "Cod CF",width=cfg._COLSZ0_)        
        self.lc1.InsertColumn(20, "Cambio",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(21, "Tipo IVA",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(22, "Tipo IVA1",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(23, "Aliq. IVA",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(24, "Registro",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(25, "Imponib",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(26, "Rigagior",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(27, "Paggior",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(28, "Note",width=cfg._COLSZ0_)
        self.lc1.InsertColumn(29, "Conto D/A",width=cfg._COLSZ0_) #   
        self.lc1.InsertColumn(30, "Importo D.",width=wx.DLG_SZE(self.pnl, 40,-1).width) #
        self.lc1.InsertColumn(31, "Importo A.",width=wx.DLG_SZE(self.pnl, 40,-1).width) #
        self.lc1.InsertColumn(32, "Descrizione conto",width=wx.DLG_SZE(self.pnl, 150,-1).width) #


        self.lc1.SetBackgroundColour(self.color)
        self.lc1.Enable(False)
        
        self.lc2.ClearAll()

        self.lc2.InsertColumn(0, "Anno",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(1, "Numero.",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(2, "Data Reg.",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(3, "Num. Riga",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(4, "Anno IVA",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(5, "Cod. Div",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(6, "Causale",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(7, "Descrizione Operazione",width=wx.DLG_SZE(self.pnl, 100,-1).width) #
        self.lc2.InsertColumn(8, "Importo",width=wx.DLG_SZE(self.pnl, 40,-1).width) 
        self.lc2.InsertColumn(9, "Imponibile",width=cfg._COLSZ0_)     
        self.lc2.InsertColumn(10, "Anno Doc.",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(11, "Tipo Doc.",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(12, "Data Doc.",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(13, "Num Doc.",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(14, "Num Doc1.",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(15, "Conto",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(16, "Importo",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(17, "Segno",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(18, "CPartita",width=cfg._COLSZ0_)   
        self.lc2.InsertColumn(19, "Cambio",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(20, "Tipo IVA",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(21, "Tipo IVA1",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(22, "Aliq. IVA",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(23, "Registro",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(24, "Imponibile",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(25, "Rigagior",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(26, "Paggior",width=cfg._COLSZ0_)
        self.lc2.InsertColumn(27, "Note",width=cfg._COLSZ0_)        
        self.lc2.InsertColumn(28, "STT_MOV",width=cfg._COLSZ0_)    
        self.lc2.InsertColumn(29, "Conto D/A",width=cfg._COLSZ0_) #   
        self.lc2.InsertColumn(30, "Importo D.",width=wx.DLG_SZE(self.pnl, 40,-1).width) #
        self.lc2.InsertColumn(31, "Importo A.",width=wx.DLG_SZE(self.pnl, 40,-1).width) #
        self.lc2.InsertColumn(32, "Descrizione conto",width=wx.DLG_SZE(self.pnl, 150,-1).width) #

        self.lc2.SetBackgroundColour(self.color)
        self.lc2.Enable(False)
        
        self.stampa.Enable(False)        
        self.stampa.Show(False)

        self.ok.Show(False)
        self.oktestata.Show(False)
        self.oktestata.Enable(False)
     
        # < diegom
        #self.cdatadoc.Show(False)
        # > diegom
        self.canc.Show(True)
        self.new.Enable(True)
        self.new.Show(True)
        self.modi.Enable(False)
        self.inte.Show(False)
        self.modi.Show(True)
        self.dele.Show(False)
        self.dele.Enable(False)
        self.newr.Enable(False)
        self.okr.Enable(False)
        self.modir.Enable(False)
        self.intr.Enable(False)
        self.delr.Enable(False)
        #self.cCAUSA.Enable(False)          
        #self.lc1odcf.SetLabel(" Cod. Cliente :")
        #self.sCAUSA='C'
        #if (self.tcpart=="C"):self.lc1odcf.SetLabel(" Cod. Cliente :")
        self.vCF.SetValue("C")
        self.sCF=""
        self.SelCOMBO(self)
        self.cntr=""
        self.cntr_row=""
        self.row=0
        if (self.rec!=""):
            self.num_mov.SetValue(self.rec)
            self.FndMov(self)

    def KillFcs_des(self, evt):
        if self.vCAUSA.GetValue()=='':
            self.dCAUSA.SetValue(self.dCAUSA.GetValue().upper())

    def KillFcs_tot_doc(self, evt):
        self.oktestata.SetFocus()

    def KillFcs_note(self, evt):
        #self.importoval.SetFocus()
        self.vCONTOD.SetFocus()

    def KillFcs_importo(self, evt):
        self.okr.SetFocus()

        
    def KillFcs_num_doc(self, evt):  
        self.datadoc.SetFocus()
        
    def KillFcs_CF(self, evt):  
        if self.vCF.GetValue()=="M" :self.num_doc.SetFocus()
        else: self.ragsoc1.SetFocus()
       
    def CntData(self, evt):
        if (self.cntr=="new" or self.cntr=="modi"):    
            datamov=self.datamov.GetValue().strip()
            #print datamov
            cnt_gma=0
            gma = datamov.split('/')         
            if len(gma) == 3:
                gg = int(gma[0])
                mm = int(gma[1])
                aa = int(gma[2])
                if gg > 0 and gg <= 31:
                    cnt_gma+=1
                    if mm >= 0 and mm <= 12:
                        cnt_gma+=1
                        if aa == int(self.annoc):
                            cnt_gma+=1
                            if self.vdatamov.GetValue()=="": 
                                self.vdatamov.SetValue(self.datamov.GetValue())
                            vdatamov = self.vdatamov.GetValue()
                            vgma =vdatamov.split('/')
                            vgg = int(vgma[0])
                            vmm = int(vgma[1])
                            vaa = int(vgma[2])
                            vdata =int(vgma[2]+vgma[1]+vgma[0])
                            data=int(gma[2]+gma[1]+gma[0])
                            self.CF.SetFocus()
                            if data < vdata :
                                dlg = wx.MessageDialog(self,cfg.msgdatault ,self.ttl, 
                                      wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                                if dlg.ShowModal() == wx.ID_YES:
                                    self.vdatamov.SetValue(self.datamov.GetValue())
                                    self.datamov.Enable(False)
                                    self.vCAUSA.SetFocus()
                                    dlg.Destroy()
                                else:
                                    self.datamov.SetFocus()
                                    dlg.Destroy()
                            else:
                                self.vdatamov.SetValue(self.datamov.GetValue())
                                self.datamov.Enable(False)
                                self.vCAUSA.SetFocus()
                                
                if cnt_gma==2 and aa <> int(self.annoc):
                    self.Message(cfg.msgdataes + self.annoc,self.ttl)            
                elif cnt_gma!=3 : self.Message(cfg.msgdatano ,self.ttl)

    def CntDataDoc(self, evt):
        datadoc=self.datadoc.GetValue().strip()
        if datadoc =='': self.totale_doc.SetFocus()
        else:
            cnt_gma=0
            gma = datadoc.split('/')
            try:
                if (gma[0].isdigit()!= True):
                    self.Message(cfg.msgdatano ,self.ttl)
                elif (gma[1].isdigit()!= True):
                    self.Message(cfg.msgdatano ,self.ttl)
                elif (gma[2].isdigit()!= True):
                    elf.Message(cfg.msgdatano ,self.ttl)
            except:
                self.Message(cfg.msgdatano ,self.ttl)

            if len(gma) == 3:
                gg = int(gma[0])
                mm = int(gma[1])
                aa = int(gma[2])
                if gg > 0 and gg <= 31:
                    cnt_gma+=1
                    if mm >= 0 and mm <= 12:
                        cnt_gma+=1
                        if aa == int(self.annoc):
                            cnt_gma+=1
                if cnt_gma==2 and aa <> int(self.annoc):
                    self.Message(cfg.msgdataes + self.annoc,self.ttl)            
                elif cnt_gma!=3 : self.Message(cfg.msgdatano ,self.ttl)
                elif cnt_gma==3 : self.totale_doc.SetFocus()
        
    def IntTestata(self, evt):
        if(self.lc1.GetItemCount()!=0 or self.codcf.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgint, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.rec=""
                self.Start(self)
            else:
                dlg.Destroy()
        else:
            self.rec=""
            self.Start(self)

    def NewTxt(self, evt):
        self.lc_Slct=""
        self.OnAnagTxt(self)
        self.cdatadoc.Enable(False)
        self.num_mov.Enable(False)
        self.cnum_mov.Enable(False)
        self.datamov.Enable(True)
        self.datamov.SetFocus()
        self.new.Show(False)
        self.ok.Show(False)
        self.oktestata.Show(True)

        self.canc.Show(False)
        self.inte.Show(True)
        self.modi.Enable(False)


    def ModiTxt(self, evt):
        # <> diegom
        #self.OnAnagTxt(self)
        self.cntr="modi"       
        self.num_mov.Enable(False)
        self.cnum_mov.Enable(False)
        self.datamov.Enable(True)
        self.datamov.SetFocus()
        self.modi.Enable(False)
        self.modi.Show(False)
        self.dele.Show(True)
	self.ok.Enable(True)
        self.oktestata.Show(True)
        self.oktestata.Enable(True)
        self.vCAUSA.Enable(True)
        self.cCAUSA.Enable(True)
        self.dCAUSA.Enable(True)
        self.CF.Enable(True)
        self.codcf.Enable(True)
        self.ccodcf.Enable(True)
        self.ragsoc1.Enable(True)
        self.cragsoc1.Enable(True)
        self.ragsoc2.Enable(True)
        self.num_doc.Enable(True)
        self.datadoc.Enable(True)
        vCAUSA=self.vCAUSA.GetValue()
        if (vCAUSA=="120" or vCAUSA=="240" or vCAUSA=="241"  or vCAUSA=="245"): 
            self.cdatadoc.Enable(False)
        else:
            self.cdatadoc.Enable(True)
        self.totale_doc.Enable(True)

    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()

    def EvtCharqt(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr_row==""):self.IntRow(self)
        evt.Skip()
        
    def OffAnagTxt(self, evt):
        if (self.lc_Slct=="lc1"):

            self.CF.Enable(False)
            self.cdatadoc.Enable(False)
            self.vCAUSA.Enable(False)
            self.cCAUSA.Enable(False)
            self.note.Enable(False)
            self.num_mov.Enable(False)
            self.cnum_mov.Enable(False)
            self.datamov.Enable(False)
            self.ragsoc1.Enable(False)
            self.cragsoc1.Enable(False)
            self.num_doc.Enable(False)
            self.datadoc.Enable(False)
            self.totale_doc.Enable(False)
            #self.lragsoc2.Show(False)
            #self.ragsoc2.Show(False)
            self.ragsoc2.Enable(False)

        self.ragsoc1.Enable(False)
        self.cragsoc1.Enable(False)
        self.vCAUSA.Enable(False)
        self.cCAUSA.Enable(False)


    
    # <> diegom             
    def OnAnagTxt(self ,evt):
        if (self.lc_Slct=="lc1"):
            vCAUSA=self.vCAUSA.GetValue()
            self.pnl1.Show(True)
            self.pnl2.Show(False)
            self.lragsoc2.Show(True)
            self.ragsoc2.Show(True)
            self.ragsoc2.Enable(True)
            self.num_doc.Enable(True)
            #print "ok" 
            #print self.vCF.GetValue()
            #print "ok" 
            if (vCAUSA=="120" or vCAUSA=="240" or vCAUSA=="241"  or vCAUSA=="245"): 
                 #self.cdatadoc.Show(False)
                 self.cdatadoc.Enable(False)
            else: self.cdatadoc.Enable(True)#; self.cdatadoc.Show(True)
            self.cdatadoc.Enable(True)
            self.datadoc.Enable(True)
            self.totale_doc.Enable(True)
            if self.stt_doc=="R": self.dCAUSA.Enable(True)

            if (vCAUSA=="110" or vCAUSA=="120" or self.stt_doc=="R"): self.CF.Enable(False)
            else: self.CF.Enable(True)

        elif (self.lc_Slct=="lc2"):
            self.pnl2.Show(True)
            self.pnl1.Show(False)
            self.dCAUSA.Enable(True)

        self.ragsoc1.Enable(True)
        self.cragsoc1.Enable(True)
        self.vCAUSA.Enable(True)
        self.cCAUSA.Enable(True)


    def DelAnagTxt(self, evt):
        self.num_mov.SetValue('')
        self.vdatamov.SetValue('')
        self.datamov.SetValue('')
        self.codcf.SetValue('')
        self.vTIPO_DOC.SetValue('')
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.vCAUSA.SetValue('')
        self.dCAUSA.SetValue('')
        self.num_doc.SetValue('')
        self.datadoc.SetValue('')
        self.totale_doc.SetValue('')
        self.vCF.SetValue('')
        self.stt_doc="E"
        self.lc_Slct=""
        self.Da_Av=""
        self.differenza.SetValue('0,00')

    def SelCOMBO(self, evt):
        vCF=self.vCF.GetValue()
        self.CF.Clear()
        for item in cfg.vcCF:
            if (item[:1]==vCF):self.sCF=item  
            self.CF.Append(item, item[:1])      
        cntCF=0
        cntCF=self.CF.FindString(self.sCF)
        self.CF.Select(cntCF)

    # <> diegom
    def SelCF(self, evt):
        self.Sel(evt)
        self.vCF.SetValue(self.cb_val)
        #vvv=self.vCF.GetValue()
        #print "SelCF " + vvv 
        #if self.vCF.GetValue()=="F": self.lc1odcf.SetLabel(" Cod. Fornit. :")
        #if self.vCF.GetValue()=="C": self.lc1odcf.SetLabel(" Cod. Cliente :")
        #self.lragsoc2.Show(True)
        #self.ragsoc2.Show(True)
        self.cragsoc1.Show(True)
        self.lragsoc1.SetLabel("Rag.Soc.1 ( Cognome ) :")
        self.ragsoc1.SetValue('')
        self.codcf.SetValue('')
        self.ragsoc1.Enable(True)

    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str= evt.GetString()
        evt.Skip()
        
    def SetFcs(self, evt):
        evt.Skip()
      
        
    ## Funzioni Lista ------------------------------------        

    # < diego
    def getColTxtlc2(self, index, col):
        item = self.lc2.GetItem(index, col)
        return item.GetText()

    def getColTxtlc1(self, index, col):
        item = self.lc1.GetItem(index, col)
        return item.GetText()
          
    def LstSlctlc1(self, evt):      
        self.currentItem = evt.m_itemIndex
        self.anno.SetValue(self.lc1.GetItemText(self.currentItem))
        self.num_mov.SetValue(self.getColTxtlc1(self.currentItem, 1))
        self.datamov.SetValue(self.getColTxtlc1(self.currentItem, 2))
        self.nriga.SetValue(self.getColTxtlc1(self.currentItem, 3))
        self.vDIV.SetValue(self.getColTxtlc1(self.currentItem, 5))
        self.vCAUSA.SetValue(self.getColTxtlc1(self.currentItem, 6))        
        self.dCAUSA.SetValue(self.getColTxtlc1(self.currentItem, 7))
        self.segno.SetValue(self.getColTxtlc1(self.currentItem, 17))
        cont_segno = self.segno.GetValue()
        if cont_segno=="A":
            self.vCONTOD.SetValue('')
            self.dCONTOD.SetValue('')
            self.importoD.SetValue('')
            self.vCONTOA.SetValue(self.getColTxtlc1(self.currentItem, 15))
            self.dCONTOA.SetValue(self.getColTxtlc1(self.currentItem, 32))
            self.importoA.SetValue(self.getColTxtlc1(self.currentItem, 8))
        if cont_segno=="D":
            self.vCONTOA.SetValue('')
            self.dCONTOA.SetValue('')
            self.importoA.SetValue('')
            self.vCONTOD.SetValue(self.getColTxtlc1(self.currentItem, 15))
            self.dCONTOD.SetValue(self.getColTxtlc1(self.currentItem, 32))
            self.importoD.SetValue(self.getColTxtlc1(self.currentItem, 8))
        self.importoval.SetValue(self.getColTxtlc1(self.currentItem, 8))
        self.imponibval.SetValue(self.getColTxtlc1(self.currentItem, 9))
        self.anno_doc.SetValue(self.getColTxtlc1(self.currentItem, 10))
        self.vTIPO_DOC.SetValue(self.getColTxtlc1(self.currentItem, 11))
        self.datadoc.SetValue(self.getColTxtlc1(self.currentItem, 12))
        self.num_doc.SetValue(self.getColTxtlc1(self.currentItem, 13))
        self.num_doc1.SetValue(self.getColTxtlc1(self.currentItem, 14))
        self.conto.SetValue(self.getColTxtlc1(self.currentItem, 15))
        #self.t_cpart.SetValue(self.getColTxtlc1(self.currentItem, 18))
        #self.codcf.SetValue(self.getColTxtlc1(self.currentItem, 18))
        self.CAMBIO.SetValue(self.getColTxtlc1(self.currentItem, 19))
        self.vTIPO_IVA.SetValue(self.getColTxtlc1(self.currentItem, 20))
        self.vTIPO_IVA1.SetValue(self.getColTxtlc1(self.currentItem, 21))
        self.vALIVA.SetValue(self.getColTxtlc1(self.currentItem, 22))
        self.registro.SetValue(self.getColTxtlc1(self.currentItem, 23))
        self.imponib.SetValue(self.getColTxtlc1(self.currentItem, 24))
        self.rigagior.SetValue(self.getColTxtlc1(self.currentItem, 25))
        self.paggior.SetValue(self.getColTxtlc1(self.currentItem, 26))
        self.note.SetValue(self.getColTxtlc1(self.currentItem, 27))
        self.stt_mov.SetValue(self.getColTxtlc1(self.currentItem, 28))
        self.row = self.currentItem
        self.SelRow(self)
        # > diego

    def LstSlctlc2(self, evt):      
        self.currentItem = evt.m_itemIndex
        self.anno.SetValue(self.lc2.GetItemText(self.currentItem))
        self.num_mov.SetValue(self.getColTxtlc2(self.currentItem, 1))
        self.datamov.SetValue(self.getColTxtlc2(self.currentItem, 2))
        self.nriga.SetValue(self.getColTxtlc2(self.currentItem, 3))
        self.vDIV.SetValue(self.getColTxtlc2(self.currentItem, 5))
        self.vCAUSA.SetValue(self.getColTxtlc2(self.currentItem, 6))        
        self.dCAUSA.SetValue(self.getColTxtlc2(self.currentItem, 7))
        self.segno.SetValue(self.getColTxtlc2(self.currentItem, 17))
        cont_segno = self.segno.GetValue()
        if cont_segno=="A": 
            self.vCONTOD.SetValue('')
            self.dCONTOD.SetValue('')
            self.importoD.SetValue('')
            self.vCONTOA.SetValue(self.getColTxtlc2(self.currentItem, 15))
            self.dCONTOA.SetValue(self.getColTxtlc2(self.currentItem, 32))
            self.importoA.SetValue(self.getColTxtlc2(self.currentItem, 8))
        if cont_segno=="D":
            self.vCONTOA.SetValue('')
            self.dCONTOA.SetValue('')
            self.importoA.SetValue('')
            self.vCONTOD.SetValue(self.getColTxtlc2(self.currentItem, 15))
            self.dCONTOD.SetValue(self.getColTxtlc2(self.currentItem, 32))
            self.importoD.SetValue(self.getColTxtlc2(self.currentItem, 8))
        self.importoval.SetValue(self.getColTxtlc2(self.currentItem, 8))
        self.imponibval.SetValue(self.getColTxtlc2(self.currentItem, 9))
        self.anno_doc.SetValue(self.getColTxtlc2(self.currentItem, 10))
        self.vTIPO_DOC.SetValue(self.getColTxtlc2(self.currentItem, 11))
        self.datadoc.SetValue(self.getColTxtlc2(self.currentItem, 12))
        self.num_doc.SetValue(self.getColTxtlc2(self.currentItem, 13))
        self.num_doc1.SetValue(self.getColTxtlc2(self.currentItem, 14))
        self.conto.SetValue(self.getColTxtlc2(self.currentItem, 15))
        #self.t_cpart.SetValue(self.getColTxtlc2(self.currentItem, 18)) # vuoto
        #self.codcf.SetValue(self.getColTxtlc2(self.currentItem, 18)) # vuoto
        self.CAMBIO.SetValue(self.getColTxtlc2(self.currentItem, 19))
        self.vTIPO_IVA.SetValue(self.getColTxtlc2(self.currentItem, 20))
        self.vTIPO_IVA1.SetValue(self.getColTxtlc2(self.currentItem, 21))
        self.vALIVA.SetValue(self.getColTxtlc2(self.currentItem, 22))
        self.registro.SetValue(self.getColTxtlc2(self.currentItem, 23))
        self.imponib.SetValue(self.getColTxtlc2(self.currentItem, 24))
        self.rigagior.SetValue(self.getColTxtlc2(self.currentItem, 25))
        self.paggior.SetValue(self.getColTxtlc2(self.currentItem, 26))
        self.note.SetValue(self.getColTxtlc2(self.currentItem, 27))
        self.stt_mov.SetValue(self.getColTxtlc2(self.currentItem, 28))
        self.row = self.currentItem
        self.SelRow(self)
        # > diego

        
    def LstAct(self, evt):
        self.SelRow(self)
        self.currentItem = evt.m_itemIndex


    def FndSelAnag(self, evt):
        row=evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.vCF.SetValue(str(row[0]))
        print "ok"
        print self.vCF.GetValue()
        print "ok"
        self.oktestata.Enable(True)
        self.num_doc.SetFocus()
        # < diegom
        #tcpart = self.vCF.GetValue()
        #print "ultimo"
        #print tcpart
        if  self.vCF.GetValue()=="C":
            self.vCF.SetValue('C')
            self.CF.Enable(False)
            self.CF.SetValue('Cliente') 
        elif self.vCF.GetValue()=="F":
            self.vCF.SetValue('F')
            self.CF.Enable(False)
            self.CF.SetValue('Fornitore') 
        #print tcpart
        # > diegom
        #if (self.lc_Slct=="lc1"):
            #self.cdatadoc.Enable(True)

        
           
    def FndSelMov(self, evt):
        #print "fndselmov"  
        row=evt
        self.anno.SetValue(str(row[0]))
        self.num_mov.SetValue(str(row[1]))
        self.vdatamov.SetValue(str(row[2]))
        self.datamov.SetValue(str(row[2]))
        # < diegom
        self.dCAUSA.SetValue(str(row[7]))
        self.vCAUSA.SetValue(str(row[6]))
        self.vCF.SetValue(str(row[31]))
        self.codcf.SetValue(str(row[18]))
        self.vTIPO_DOC.SetValue(row[11])
        # > diegom
        self.datadoc.SetValue(str(row[12]))
        self.num_doc.SetValue(str(row[13]))
        self.__MDI__.CnvVM(row[16])
        totaledoc=self.__MDI__.val
        self.totale_doc.SetValue(totaledoc)
        # < diegom
        vCAUSA = self.vCAUSA.GetValue()

        sql = """ select val1, val2 from tabgen where valore = "%s" """
        try:
            #print int(vCAUSA) 
            cr = self.CnAz.cursor ()
            cr.execute(sql % int(vCAUSA)) 
            rows = cr.fetchall()
            for row in rows:
                #print row[0]
                if (row[0]=="LG"):
                    if (vCAUSA=="141" or vCAUSA=="140" or vCAUSA=="145" or vCAUSA=="240" or vCAUSA=="241" or vCAUSA=="245"):
                        self.lc_Slct="lc1"
                        self.FndMovCorpolc1(self) 
                        self.FndCodCF(self)
                        self.SelCOMBO(self)
                    else:
                        self.lc_Slct="lc2"
                        self.FndMovCorpolc2(self)
                if (row[0]=="RI"):
                    self.lc_Slct="lc1"
                    self.FndMovCorpolc1(self) 
                    self.FndCodCF(self)
                    self.SelCOMBO(self)
        except StandardError, msg:
                self.__MDI__.MsgErr("movcon","SelCAUSA Error %s " % (msg))
	self.CnAz.commit()
        # > diegom
        self.num_mov.Enable(False)
        self.datamov.Enable(False)
        self.new.Enable(False)
        self.canc.Show(False)
        self.inte.Show(True)        
        self.modi.Enable(True)
        self.modi.SetFocus()
        

    def FndMov(self, evt):

        num_mov = self.num_mov.GetValue()
        if num_mov == "" :
            self.Message(cfg.msgass +" --> "+ str(self.tbl),self.ttl)
        else:
            cnt_rec=0       
            anno = self.anno.GetValue()
            valueSql = int(num_mov),anno
            try:
                sql = """ select * from movcon where num_mov = "%s" and anno = "%s" and conto==10 """
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
                #print "prima "
                #print cnt_rec
                if cnt_rec==0:
              	    self.CnAz.commit()
                    sql = """ select * from movcon where num_mov = "%s" and anno = "%s" and conto==30 """
                    cr = self.CnAz.cursor ()
                    cr.execute(sql % valueSql)
                    rows = cr.fetchall()
                    for row in rows:
                        cnt_rec+=1
                    #print "seconda "
                    #print cnt_rec
                if cnt_rec==0:
              	    self.CnAz.commit()
                    sql = """ select * from movcon where num_mov = "%s" and anno = "%s" """
                    cr = self.CnAz.cursor ()
                    cr.execute(sql % valueSql)
                    rows = cr.fetchall()
                    for row in rows:
                        cnt_rec+=1
                    #print "terza " 
                    #print cnt_rec
            except StandardError, msg:
                self.__MDI__.MsgErr("movcon","FndMov Error %s " % (msg))
	    self.CnAz.commit()
            if (cnt_rec==0):self.Message(cfg.msgass+" --> "+ str(self.tbl),self.ttl)
            else : self.FndSelMov(row)  
                   

    def FndMovCorpolc1(self, evt):
        #print "fndmovcorpolc1"
        #print self.lc_Slct
        rowlc=0
        cnt_rec=0
        num_mov = self.num_mov.GetValue()
        anno = self.anno.GetValue()
        sql = """ select * from movcon where num_mov = "%s" 
                  and anno = "%s" order by num_rig desc """
        valueSql = int(num_mov), anno
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                for rowlc in range(1):
                    row_lc = self.lc1.GetItemCount() 
                    self.lc1.InsertStringItem(rowlc, str(row[0]))
                    self.lc1.SetStringItem(rowlc, 1, str(row[1]))
                    self.lc1.SetStringItem(rowlc, 2, str(row[2]))
                    self.lc1.SetStringItem(rowlc, 3, str(row[3]))
                    self.lc1.SetStringItem(rowlc, 4, str(row[4]))
                    self.lc1.SetStringItem(rowlc, 5, str(row[5]))
                    self.lc1.SetStringItem(rowlc, 6, str(row[6]))
                    self.lc1.SetStringItem(rowlc, 7, str(row[7]))
                    self.__MDI__.CnvVM(row[8])
                    imporval=self.__MDI__.val
                    self.__MDI__.CnvVM(row[9])
                    imponval=self.__MDI__.val
                    self.lc1.SetStringItem(rowlc, 8, imporval)
                    self.lc1.SetStringItem(rowlc, 9, imponval)
                    self.lc1.SetStringItem(rowlc, 10, str(row[10]))
                    self.lc1.SetStringItem(rowlc, 11, str(row[11]))
                    self.lc1.SetStringItem(rowlc, 12, str(row[12]))
                    self.lc1.SetStringItem(rowlc, 13, str(row[13]))
                    self.lc1.SetStringItem(rowlc, 14, str(row[14]))                    
                    self.lc1.SetStringItem(rowlc, 15, str(row[15]))
                    #self.__MDI__.CnvVM(row[16])
                    #totdoc=self.__MDI__.val
                    #self.lc1.SetStringItem(rowlc, 16, totdoc)
                    self.lc1.SetStringItem(rowlc, 16, str(row[16])) 
                    self.lc1.SetStringItem(rowlc, 17, str(row[17]))
                    self.lc1.SetStringItem(rowlc, 18, str(row[18]))
                    self.lc1.SetStringItem(rowlc, 19, str(row[19]))
                    self.lc1.SetStringItem(rowlc, 20, str(row[20]))
                    self.lc1.SetStringItem(rowlc, 24, str(row[24]))
                    self.lc1.SetStringItem(rowlc, 25, str(row[25]))
                    self.lc1.SetStringItem(rowlc, 26, str(row[26]))  
                    self.lc1.SetStringItem(rowlc, 27, str(row[27]))
                    self.lc1.SetStringItem(rowlc, 28, str(row[28]))
                    if str(row[17])=="D":
                        self.__MDI__.CnvVM(row[8])
                        importoD=self.__MDI__.val
                        self.lc1.SetStringItem(rowlc, 30, importoD)
                    elif str(row[17])=="A":
                        self.__MDI__.CnvVM(row[8])
                        importoA=self.__MDI__.val
                        self.lc1.SetStringItem(rowlc, 31, importoA)
                    self.lc1.SetStringItem(rowlc, 32, str(row[29]))
  
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","FndMovCorpo Error %s " % (msg))
        self.CnAz.commit()
        self.CalcDifferenzalc1(self)
        # <> diegom
        self.pnl1.Show(True)
        self.pnl2.Show(False)

	#self.OkTestata(self)

    # < diego da aggiustare campi       
    def FndMovCorpolc2(self, evt):
        rowlc=0
        cnt_rec=0
        num_mov = self.num_mov.GetValue()
        anno = self.anno.GetValue()
        sql = """ select * from movcon where num_mov = "%s" 
                  and anno = "%s" order by num_rig desc """
        valueSql = int(num_mov), anno
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                for rowlc in range(1):
                    row_lc = self.lc2.GetItemCount() 
                    self.lc2.InsertStringItem(rowlc, str(row[0]))
                    self.lc2.SetStringItem(rowlc, 1, str(row[1]))
                    self.lc2.SetStringItem(rowlc, 2, str(row[2]))
                    self.lc2.SetStringItem(rowlc, 3, str(row[3]))
                    self.lc2.SetStringItem(rowlc, 4, str(row[4]))
                    self.lc2.SetStringItem(rowlc, 5, str(row[5]))
                    self.lc2.SetStringItem(rowlc, 6, str(row[6]))
                    self.lc2.SetStringItem(rowlc, 7, str(row[7]))
                    self.__MDI__.CnvVM(row[8])
                    imporval=self.__MDI__.val
                    self.__MDI__.CnvVM(row[9])
                    imponval=self.__MDI__.val
                    self.lc2.SetStringItem(rowlc, 8, imporval)
                    self.lc2.SetStringItem(rowlc, 9, imponval)
                    self.lc2.SetStringItem(rowlc, 10, str(row[10]))
                    self.lc2.SetStringItem(rowlc, 11, str(row[11]))
                    self.lc2.SetStringItem(rowlc, 12, str(row[12]))
                    self.lc2.SetStringItem(rowlc, 13, str(row[13]))
                    self.lc2.SetStringItem(rowlc, 14, str(row[14]))                    
                    self.lc2.SetStringItem(rowlc, 15, str(row[15]))
                    self.lc2.SetStringItem(rowlc, 16, str(row[16]))        
                    self.lc2.SetStringItem(rowlc, 17, str(row[17]))
                    self.lc2.SetStringItem(rowlc, 18, str(row[18]))
                    self.lc2.SetStringItem(rowlc, 19, str(row[19]))
                    self.lc2.SetStringItem(rowlc, 20, str(row[20]))
                    self.lc2.SetStringItem(rowlc, 24, str(row[24]))
                    self.lc2.SetStringItem(rowlc, 25, str(row[25]))
                    self.lc2.SetStringItem(rowlc, 26, str(row[26]))  
                    self.lc2.SetStringItem(rowlc, 27, str(row[27]))
                    self.lc2.SetStringItem(rowlc, 28, str(row[28]))
                    self.lc2.SetStringItem(rowlc, 29, str(row[15]))
                    if str(row[17])=="D":
                        self.__MDI__.CnvVM(row[8])
                        importoD=self.__MDI__.val
                        self.lc2.SetStringItem(rowlc, 30, importoD)
                    elif str(row[17])=="A":
                        self.__MDI__.CnvVM(row[8])
                        importoA=self.__MDI__.val
                        self.lc2.SetStringItem(rowlc, 31, importoA)
                    self.lc2.SetStringItem(rowlc, 32, str(row[29]))
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","FndMovCorpo Error %s " % (msg))
        self.CnAz.commit()
        self.CalcDifferenzalc2(self)
        self.pnl2.Show(True)
        self.pnl1.Show(False)

    # < diego

    def Modi(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgmodi_doc, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.ModiTxt(self)
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()

    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgnodele_doc, self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr=""
            dlg.Destroy()
            
    def Dele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdele_doc,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.cntr=""
            vCAUSA = self.vCAUSA.GetValue()
            vanno = self.anno.GetValue()
            vnum_mov = self.num_mov.GetValue()
            valueSql = vCAUSA, vanno, int(vnum_mov)
            try:
                cr = self.CnAz.cursor()
                sql = """ delete from movcon where causa = "%s" 
                          and anno = "%s" and num_mov = "%s" """                
                cr.execute(sql % valueSql)
            except StandardError, msg:
                self.__MDI__.MsgErr("movcon"," Error %s " % (msg)) 
            self.CnAz.commit()
            self.Start(self)
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()
    
 
    def OkTestata(self, evt):
    # < diegom
        #print "oktestata"
        #print self.lc_Slct
        #valTIPO_DOC=self.vTIPO_DOC.GetValue()
        #print valTIPO_DOC
        
        if  self.lc_Slct=="lc1":
            valragsoc1 = self.ragsoc1.GetValue()
            valnum_doc = self.num_doc.GetValue()
            valdatadoc = self.datadoc.GetValue()
            valtotale_doc = self.totale_doc.GetValue()
            valTIPO_DOC=self.vTIPO_DOC.GetValue()
            if valdatadoc=="  /  /    ": valdatadoc=""

            if (valnum_doc!="" and valragsoc1!="" and valdatadoc!="" and valtotale_doc!="" and valTIPO_DOC!="" or 
                valnum_doc!="" and valragsoc1!="" and valdatadoc!="" and valtotale_doc!="" and self.vCF.GetValue()=="F"):
                self.vCAUSA.Enable(False)
                self.cCAUSA.Enable(False)
                self.dCAUSA.Enable(False)
                self.codcf.Enable(False)
                self.ragsoc1.Enable(False)
                self.cragsoc1.Enable(False)
                self.ragsoc2.Enable(False)
                self.num_doc.Enable(False)
                self.datadoc.Enable(False)
                self.cdatadoc.Enable(False)
                self.totale_doc.Enable(False)
                self.pnl1.Show(True)
                self.pnl2.Show(False)
                self.CF.SetFocus()
                self.lragsoc1.SetLabel("Rag.Soc.1 ( Cognome ) :")
                self.lragsoc2.SetLabel("Rag.Soc.2 ( Nome ) :")
                self.lragsoc2.Show(True)
                self.ragsoc2.Show(True)
                self.lc1.SetBackgroundColour(wx.Colour(255, 255, 255))
                self.lc1.Enable(True)
                if (self.cntr=="new" or self.cntr=="modi"):
                    self.OffAnagTxt(self)
                    self.oktestata.Show(False)
                    self.new.Show(False)
                    self.ok.Show(True)
                    self.ok.Enable(True)
                    self.newr.Enable(True)
                    self.newr.SetFocus()
            elif (valnum_doc=="" or valragsoc1=="" or valdatadoc=="" or valtotale_doc=="" or valTIPO_DOC==""): 
                if valragsoc1=="": 
                    self.Message("Attenzione inserire ragione sociale",self.ttl)
                    self.cragsoc1.SetFocus()
                elif valnum_doc=="": 
                    self.Message("Attenzione inserire numero documento",self.ttl)
                    self.num_doc.SetFocus()
                elif valdatadoc=="": 
                    self.Message("Attenzione inserire data del documento",self.ttl)
                    self.cdatadoc.SetFocus()
                elif valtotale_doc=="": 
                    self.Message("Attenzione inserire totale documento",self.ttl)
                    self.totale_doc.SetFocus()
                elif valTIPO_DOC=="" and self.vCF.GetValue()!="F": 
                    self.Message("Attenzione confermare esistenza del documento",self.ttl)
                    self.cdatadoc.SetFocus()



        else:
            self.lc2.SetBackgroundColour(wx.Colour(255, 255, 255))
            self.lc2.Enable(True)
            self.pnl2.Show(True)
            self.pnl1.Show(False)
            self.lc2.SetBackgroundColour(wx.Colour(255, 255, 255))
            self.lc2.Enable(True)

            if (self.cntr=="new" or self.cntr=="modi"):
                self.OffAnagTxt(self)
                self.oktestata.Show(False)
                self.new.Show(False)
                self.ok.Show(True)
                self.ok.Enable(True)
                self.newr.Enable(True)
                self.newr.SetFocus()



    def OffDescTxt(self, evt):        
        self.vCAUSA.Enable(False)
        self.cCAUSA.Enable(False)
        self.dCAUSA.Enable(False)
        self.note.Enable(False)
        self.importoA.Enable(False)
        self.importoD.Enable(False)
        self.differenza.Enable(False)
        self.modir.Enable(False)
        self.okr.Enable(False)
        self.modir.Show(True)
        self.okr.Show(False)
        self.intr.Enable(False)
        self.delr.Enable(False)
        self.newr.Enable(True)
        self.newr.SetFocus()
        self.vCONTOA.Enable(False)
        self.dCONTOA.Enable(False)
        self.cCONTOA.Enable(False)
        self.vCONTOD.Enable(False)
        self.dCONTOD.Enable(False)
        self.cCONTOD.Enable(False)

    def OffDescTxtAll(self, evt):
        self.lc1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.lc1.Enable(True)           
        self.lc2.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.lc2.Enable(True)      
        self.note.Enable(False)
        self.nriga.Enable(False)
        self.vCONTOA.Enable(False)
        self.dCONTOA.Enable(False)
        self.cCONTOA.Enable(False)
        self.vCONTOD.Enable(False)
        self.dCONTOD.Enable(False)
        self.cCONTOD.Enable(False)
        self.importoD.Enable(False)
        self.importoA.Enable(False)

    def OnDescTxt(self, evt):
        self.lc1.SetBackgroundColour(self.color)
        self.lc1.Enable(False)
        self.lc2.SetBackgroundColour(self.color)
        self.lc2.Enable(False)
        self.note.Enable(True)
        self.importoA.Enable(True)
        self.importoD.Enable(True)
        self.vCONTOA.Enable(True)
        self.dCONTOA.Enable(True)
        self.cCONTOA.Enable(True)
        self.vCONTOD.Enable(True)
        self.dCONTOD.Enable(True)
        self.cCONTOD.Enable(True)
        self.importoD.Enable(True)
        self.importoA.Enable(True)

        
    def NewRow(self, evt):
        self.OnDescTxt(self)
        self.DelDescTxt(self)
        self.cntr_row="new"
        self.note.SetFocus()
        self.newr.Enable(False)
        self.intr.Enable(True)
        self.modir.Enable(False)
        self.okr.Enable(True)
        self.modir.Show(False)
        self.okr.Show(True)
        self.cnt_save=0
        
    def ModiRow(self, evt):
        print "1"
        print self.vCF.GetValue()
        self.OnDescTxt(self)   
        self.cntr_row="modi"
        #self.importoval.SetFocus()
        self.delr.Enable(True)
        self.cntr_row=""
        self.modir.Show(False)
        self.modir.Enable(False)
        self.okr.Show(True)
        self.okr.Enable(True)
        
    def DelDescTxt(self, evt):
        #self.vCAUSA.SetValue('')
        #self.dCAUSA.SetValue('')
        #self.note.SetValue('')
        self.importoA.SetValue('')
        self.importoD.SetValue('')
        self.vCONTOA.SetValue('')
        self.dCONTOA.SetValue('')
        self.vCONTOD.SetValue('')
        self.dCONTOD.SetValue('')
        
       
    def CalcDifferenzalc1(self,evt):
        importo = 0
        vimporto = 0
        importoD = 0
        importoA = 0
        vimportoD = 0
        vimportoA = 0
        totale = self.totale_doc.GetValue()
        if totale=='':totale ='0'
        self.__MDI__.CnvPM(totale)
        totale = self.__MDI__.val
        for x in range(self.lc1.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxtlc1(x, 30))
            #print "30-" + str(self.getColTxt(x, 30))+"-"
            importoD_row=self.__MDI__.val
            #print "30_" + str(importoD_row) + "_"
            if importoD_row=="0": importoD_row=0
            #print type(importoD_row)
            #if importoD_row=="": importoD_row=0 
            importoD+=importoD_row
            vimportoD=totale+importoD
       
        for x in range(self.lc1.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxtlc1(x, 31))
            #print "31-" + str(self.getColTxt(x, 31)) +"-"
            importoA_row=self.__MDI__.val 
            #print "31_" + str(importoA_row) + "_"
            if importoA_row=="0": importoA_row=0
            #print type(importoA_row)
            #if importoA_row=="": importoA_row=0
            importoA+=importoA_row
            vimportoA=totale+importoA
        vimporto = vimportoD - vimportoA
        self.__MDI__.CnvVM(vimporto)
        if self.__MDI__.val=='':self.__MDI__.val='0,00'
        self.differenza.SetValue(self.__MDI__.val)



    def CalcDifferenzalc2(self,evt):
        importo = 0
        vimporto = 0
        importoD = 0
        importoA = 0
        vimportoD = 0
        vimportoA = 0
        totale = self.totale_doc.GetValue()
        if totale=='':totale ='0'
        self.__MDI__.CnvPM(totale)
        totale = self.__MDI__.val
        for x in range(self.lc2.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxtlc2(x, 30))
            importoD_row=self.__MDI__.val
            if importoD_row=="0": importoD_row=0
            #print type(importoD_row)
            importoD+=importoD_row
            vimportoD=totale+importoD
       
        for x in range(self.lc2.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxtlc2(x, 31))
            importoA_row=self.__MDI__.val 
            if importoA_row=="0": importoA_row=0
            #print type(importoA_row)
            importoA+=importoA_row
            vimportoA=totale+importoA
        vimporto = vimportoD - vimportoA
        self.__MDI__.CnvVM(vimporto)
        if self.__MDI__.val=='':self.__MDI__.val='0,00'
        self.differenza.SetValue(self.__MDI__.val)



    def SelRow(self,evt):
        self.intr.Enable(True)
        self.modir.Enable(True)
        self.newr.Enable(False)      

    def IntRow(self,evt):
        self.OffDescTxt(self)
        self.DelDescTxt(self)
        self.lc1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.lc1.Enable(True) 
        self.lc2.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.lc2.Enable(True) 
        
    def DelRow(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdelrow, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            if (self.lc_Slct=="lc1"): self.lc1.DeleteItem(self.row)            
            if (self.lc_Slct=="lc2"): self.lc2.DeleteItem(self.row)
            self.IntRow(self)
            if (self.lc_Slct=="lc1"): self.CalcDifferenzalc1(self)
            if (self.lc_Slct=="lc2"): self.CalcDifferenzalc2(self)       
            self.newr.SetFocus()
            dlg.Destroy()
        else:
            dlg.Destroy()
        
    def RmpRowlc1(self, evt):
        self.lc1.InsertStringItem(self.row, self.anno.GetValue())
        self.lc1.SetStringItem(self.row, 1, self.num_mov.GetValue())
        self.lc1.SetStringItem(self.row, 2, self.datamov.GetValue())
        self.lc1.SetStringItem(self.row, 3, self.nriga.GetValue())
        #self.lc1.SetStringItem(self.row, 4, self.anno_iva.GetValue())
        self.lc1.SetStringItem(self.row, 4, self.anno_iva)
        self.lc1.SetStringItem(self.row, 5, self.vDIV.GetValue())
        self.lc1.SetStringItem(self.row, 6, self.vCAUSA.GetValue())
        self.lc1.SetStringItem(self.row, 7, self.dCAUSA.GetValue())
        #self.lc1.SetStringItem(self.row, 8, self.importoval.GetValue())
        self.lc1.SetStringItem(self.row, 9, self.imponibval.GetValue())
        self.lc1.SetStringItem(self.row, 10, self.anno_doc.GetValue())
        self.lc1.SetStringItem(self.row, 11, self.vTIPO_DOC.GetValue())
        self.lc1.SetStringItem(self.row, 12, self.datadoc.GetValue())
        self.lc1.SetStringItem(self.row, 13, self.num_doc.GetValue())
        self.lc1.SetStringItem(self.row, 14, self.num_doc1.GetValue())
        if self.vCONTOA.GetValue()!="":
            self.lc1.SetStringItem(self.row, 15, self.vCONTOA.GetValue())
            self.lc1.SetStringItem(self.row, 8, self.importoA.GetValue())
            self.lc1.SetStringItem(self.row, 32, self.dCONTOA.GetValue())
            self.lc1.SetStringItem(self.row, 30, "", wx.LIST_FORMAT_RIGHT) #impdare    
            #self.lc1.SetStringItem(self.row, 31, self.importoA.GetValue(), wx.LIST_FORMAT_RIGHT)#impavere
            self.lc1.SetStringItem(self.row, 31, self.importoA.GetValue())#impavere
        else :
            self.lc1.SetStringItem(self.row, 15, self.vCONTOD.GetValue())
            self.lc1.SetStringItem(self.row, 8, self.importoD.GetValue())
            self.lc1.SetStringItem(self.row, 32, self.dCONTOD.GetValue())
            #self.lc1.SetStringItem(self.row, 30, self.importoD.GetValue(), wx.LIST_FORMAT_RIGHT) #impdare    
            self.lc1.SetStringItem(self.row, 30, self.importoD.GetValue()) #impdare     
            self.lc1.SetStringItem(self.row, 31, "", wx.LIST_FORMAT_RIGHT)#impavere
        self.lc1.SetStringItem(self.row, 16, self.totale_doc.GetValue())
        self.lc1.SetStringItem(self.row, 17, self.segno.GetValue())
        self.lc1.SetStringItem(self.row, 18, self.codcf.GetValue()) #cpart
        self.lc1.SetStringItem(self.row, 19, self.CAMBIO.GetValue())
        self.lc1.SetStringItem(self.row, 20, self.vTIPO_IVA.GetValue())
        self.lc1.SetStringItem(self.row, 21, self.vTIPO_IVA1.GetValue())
        self.lc1.SetStringItem(self.row, 22, self.vALIVA.GetValue())
        self.lc1.SetStringItem(self.row, 23, self.registro.GetValue())
        self.lc1.SetStringItem(self.row, 24, self.imponib.GetValue())
        self.lc1.SetStringItem(self.row, 25, self.rigagior.GetValue())
        self.lc1.SetStringItem(self.row, 26, self.paggior.GetValue())
        self.lc1.SetStringItem(self.row, 27, self.note.GetValue())                                    
        self.lc1.SetStringItem(self.row, 28, self.stt_mov.GetValue())



    def RmpRowlc2(self, evt):
        self.lc2.InsertStringItem(self.row, self.anno.GetValue())
        self.lc2.SetStringItem(self.row, 1, self.num_mov.GetValue())
        self.lc2.SetStringItem(self.row, 2, self.datamov.GetValue())
        self.lc2.SetStringItem(self.row, 3, self.nriga.GetValue())
        self.lc2.SetStringItem(self.row, 4, self.anno_iva)
        self.lc2.SetStringItem(self.row, 5, self.vDIV.GetValue())
        self.lc2.SetStringItem(self.row, 6, self.vCAUSA.GetValue())
        self.lc2.SetStringItem(self.row, 7, self.dCAUSA.GetValue())
        #self.lc2.SetStringItem(self.row, 8, self.importoval.GetValue())
        self.lc2.SetStringItem(self.row, 9, self.imponibval.GetValue())
        self.lc2.SetStringItem(self.row, 10, self.anno_doc.GetValue())
        self.lc2.SetStringItem(self.row, 11, self.vTIPO_DOC.GetValue())
        self.lc2.SetStringItem(self.row, 12, self.datadoc.GetValue())
        self.lc2.SetStringItem(self.row, 13, self.num_doc.GetValue())
        self.lc2.SetStringItem(self.row, 14, self.num_doc1.GetValue())
        if self.vCONTOA.GetValue()!="":
            self.lc2.SetStringItem(self.row, 15, self.vCONTOA.GetValue())
            self.lc2.SetStringItem(self.row, 8, self.importoA.GetValue())
            self.lc2.SetStringItem(self.row, 32, self.dCONTOA.GetValue())
            self.lc2.SetStringItem(self.row, 30, "", wx.LIST_FORMAT_RIGHT) #impdare    
            self.lc2.SetStringItem(self.row, 31, self.importoA.GetValue(), wx.LIST_FORMAT_RIGHT)#impavere

        else :
            self.lc2.SetStringItem(self.row, 15, self.vCONTOD.GetValue())
            self.lc2.SetStringItem(self.row, 8, self.importoD.GetValue())
            self.lc2.SetStringItem(self.row, 32, self.dCONTOD.GetValue())
            self.lc2.SetStringItem(self.row, 30, self.importoD.GetValue(), wx.LIST_FORMAT_RIGHT) #impdare    
            self.lc2.SetStringItem(self.row, 31, "", wx.LIST_FORMAT_RIGHT)#impavere
        self.lc2.SetStringItem(self.row, 16, self.totale_doc.GetValue())
        self.lc2.SetStringItem(self.row, 17, self.segno.GetValue())
        #self.lc2.SetStringItem(self.row, 18, self.codcf.GetValue()) #cpart
        self.lc2.SetStringItem(self.row, 19, self.CAMBIO.GetValue())
        self.lc2.SetStringItem(self.row, 20, self.vTIPO_IVA.GetValue())
        self.lc2.SetStringItem(self.row, 21, self.vTIPO_IVA1.GetValue())
        self.lc2.SetStringItem(self.row, 22, self.vALIVA.GetValue())
        self.lc2.SetStringItem(self.row, 23, self.registro.GetValue())
        self.lc2.SetStringItem(self.row, 24, self.imponib.GetValue())
        self.lc2.SetStringItem(self.row, 25, self.rigagior.GetValue())
        self.lc2.SetStringItem(self.row, 26, self.paggior.GetValue())
        self.lc2.SetStringItem(self.row, 27, self.note.GetValue())                                    
        self.lc2.SetStringItem(self.row, 28, self.stt_mov.GetValue())

     
    def OkRow(self, evt):
        #print "okrow"
        cnt_val=0
        if self.vCONTOA.GetValue()!="" :
            valimportoA = self.importoA.GetValue().replace(",","")
            if (self.vCONTOA.GetValue()!="" and valimportoA!="" and valimportoA.isdigit()== True):
                self.__MDI__.CnvPM5(self.importoA.GetValue())
                vimportoA = self.__MDI__.val
                cnt_val+=1
                #print "ok_1"
            else:
                self.Message(cfg.msgimportono,self.ttl)
                self.importoA.SetFocus()

        if self.vCONTOD.GetValue()!="" :
            valimportoD = self.importoD.GetValue().replace(",","")
            if (self.vCONTOD.GetValue()!="" and valimportoD!="" and valimportoD.isdigit()== True):
                self.__MDI__.CnvPM5(self.importoD.GetValue())
                vimportoD = self.__MDI__.val
                cnt_val+=1
            else:
                self.Message(cfg.msgimportono,self.ttl)
                self.importoD.SetFocus()

        if (cnt_val==1):
            if self.vCONTOD.GetValue()!="" :
                self.__MDI__.CnvVM(vimportoD)
                self.importoD.SetValue(self.__MDI__.val)
            elif self.vCONTOA.GetValue()!="" :
                self.__MDI__.CnvVM(vimportoA)
                self.importoA.SetValue(self.__MDI__.val)

            self.OffDescTxt(self)
            # <> diegom chiama funzioni RmpRowlc1 inserire lc2  
            if ( self.cntr_row=="new"):
                #print "chiama RmpRowlc1"
                if (self.lc_Slct=="lc1"): self.row = self.lc1.GetItemCount()
                if (self.lc_Slct=="lc2"): self.row = self.lc2.GetItemCount()
                nriga =self.row+1
                self.nriga.SetValue(str(nriga*10))
                if (self.lc_Slct=="lc1"): self.RmpRowlc1(self)
                if (self.lc_Slct=="lc2"): self.RmpRowlc2(self)
            if ( self.cntr_row==""):
                if (self.lc_Slct=="lc1"): self.RmpRowlc1(self)
                if (self.lc_Slct=="lc2"): self.RmpRowlc2(self)
                if (self.lc_Slct=="lc1"): self.lc1.DeleteItem(self.row+1)
                if (self.lc_Slct=="lc2"): self.lc2.DeleteItem(self.row+1)
                if (self.lc_Slct=="lc1"): 
                    self.lc1.SetItemState(self.row-1, 
                           wx.LIST_STATE_SELECTED,
                           wx.LIST_STATE_SELECTED)
                if (self.lc_Slct=="lc2"): 
                    self.lc2.SetItemState(self.row-1, 
                           wx.LIST_STATE_SELECTED,
                           wx.LIST_STATE_SELECTED)

            if (self.lc_Slct=="lc1"): self.CalcDifferenzalc1(self)
            if (self.lc_Slct=="lc2"): self.CalcDifferenzalc2(self)
            self.newr.Enable(True)
            self.newr.SetFocus()
            self.modi.Enable(False)
            self.modir.Enable(False)
            self.okr.Enable(False)
            self.cntr_row=""

    #---------- funzioni ricerca
    def FndCodCF(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        cod = self.codcf.GetValue()
        
        # < diegom
        tcpart = self.vCF.GetValue()
        #print "oooooooo"
        #print tcpart
        sql = """ select * from anag where cod = "%s" and t_cpart = "%s" """
        #print tcpart
        # <> diegom sostituito cod con tcpart
        valueSql = int(cod),tcpart
        #valueSql = int(cod),cod
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1 
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","FndCodCF Error %s " % (msg)) 
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)
        if  tcpart=="F": self.lc1odcf.SetLabel(" Cod. Fornit. :")
        if  tcpart=="C": self.lc1odcf.SetLabel(" Cod. Cliente :")

    def FndAnag(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue()
        cod = self.codcf.GetValue()
        tcpart = self.vCF.GetValue()
        valueSql = tcpart, '%' + val.title() + '%'
        sql = """ select * from anag 
                  where t_cpart = "%s" and rag_soc1 like "%s" 
                  order by rag_soc1 desc """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","FndAnag Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)
        elif (cnt_rec>1):
            try:
	        import srcanag
            except :
	        pass
            try:
                base.srcanag
            except :
                pass

            control = [tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else:
            self.oktestata.Enable(True)
            self.num_doc.SetFocus()            


    def FndPIACONA(self, evt):
        self.vCONTOA.Enable(True)
        self.dCONTOA.Enable(True)
        self.cCONTOA.Enable(True)
        self.importoA.Enable(True)
        self.Da_Av="A"
        self.segno.SetValue('A')
        cod = self.vCONTOA.GetValue()    
        descriz = self.dCONTOA.GetValue()
        cnt_rec = 0
        if cod=="":
            sql = """ select * from piacon where descriz like "%s" order by descriz desc """
            valueSql = '%' + descriz + '%' 
        else:
            sql = """ select * from piacon where cod = "%s" order by descriz desc """
            valueSql = int(cod)   
        #print sql % valueSql     
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","FndPIACON Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.dCONTOA.SetValue(row[1])
            self.vCONTOA.SetValue(row[0])
            valoreCONTOA = self.vCONTOA.GetValue()
        elif (cnt_rec>1):
            try:
	        import srcpiac
            except :
	        pass
            try:
                import base.srcpiac
            except :
                pass
            control = ['Ricerca Causali Contabili',self.vCONTOA,self.dCONTOA,self.FndPIACONA, cod, descriz]     
            win = srcpiac.create(self,control)
            win.Centre(wx.BOTH)
            win.Show(True) 
            self.importoA.SetFocus()   
        self.vCONTOD.Enable(False)
        self.dCONTOD.Enable(False)
        self.cCONTOD.Enable(False)
        self.importoD.Enable(False)

    def FndPIACOND(self, evt):
        self.vCONTOD.Enable(True)
        self.dCONTOD.Enable(True)
        self.cCONTOD.Enable(True)
        self.importoD.Enable(True)
        self.Da_Av="D"
        self.segno.SetValue('D')
        cod = self.vCONTOD.GetValue()    
        descriz = self.dCONTOD.GetValue()
        cnt_rec = 0
        if cod=="":
            sql = """ select * from piacon where descriz like "%s" order by descriz desc """
            valueSql = '%' + descriz + '%' 
        else :
            sql = """ select * from piacon where cod = "%s" order by descriz desc """
            valueSql = int(cod)  
            #valueSql = '%' + cod + '%'  
        #print sql % valueSql     
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","FndPIACON Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.dCONTOD.SetValue(row[1])
            self.vCONTOD.SetValue(row[0])
            valoreCONTOD = self.vCONTOD.GetValue()
            # <> diegom
            #print valoreCONTOD
 
        elif (cnt_rec>1):
            try:
	        import srcpiac
            except :
	        pass
            try:
                import base.srcpiac
            except :
                pass
            control = ['Ricerca Causali Contabili',self.vCONTOD,self.dCONTOD,self.FndPIACOND, cod, descriz]     
            win = srcpiac.create(self,control)
            win.Centre(wx.BOTH)
            win.Show(True) 
            self.importoD.SetFocus()   
        self.vCONTOA.Enable(False)
        self.dCONTOA.Enable(False)
        self.cCONTOA.Enable(False)
        self.importoA.Enable(False)

    def FndTABGEN(self, evt):
        valoreCAUSA = self.vCAUSA.GetValue()
        if (valoreCAUSA=='110' or valoreCAUSA=='140' or valoreCAUSA=='141' or valoreCAUSA=='145'):
            self.vCF.SetValue('C')
            self.CF.Enable(False)
            self.CF.SetValue('Cliente') 
        if (valoreCAUSA=='120' or valoreCAUSA=='240' or valoreCAUSA=='241' or valoreCAUSA=='245'):   
            self.vCF.SetValue('F')
            self.CF.Enable(False)
            self.CF.SetValue('Fornitore')     
        print "okkkkkk" 
        val = self.vCAUSA.GetValue()
        self.SelCAUSA(val)
        #print "val"
        #print val
        cod = "CAUSA"
        cnt_rec = 0
        sql = """ select * from tabgen where cod = "%s" and valore like "%s" """
        valueSql = cod,'%'+val+'%'
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","FndTABGEN Error %s " % (msg))
        self.CnAz.commit()

        if (cnt_rec==1 and cnt_rec<2):
            self.dCAUSA.SetValue(row[2])
            # < diegom
            #self.note.SetValue(row[2])
            valoreCAUSA = self.vCAUSA.GetValue()
            vCAUSA = self.vCAUSA.GetValue()
            if (row[0]=="LG"):
                self.lc_Slct="lc2"
                self.pnl2.Show(True)
                self.pnl1.Show(False)
                #self.OkTestata(self)
            if (row[0]=="RI"):
                self.lc_Slct="lc1"
                self.pnl1.Show(True)
                self.pnl2.Show(False)
                #self.OkTestata(self)
          
            if (valoreCAUSA=='110' or valoreCAUSA=='140' or valoreCAUSA=='141' or valoreCAUSA=='145'):
                self.vCF.SetValue('C')
                self.CF.Enable(False)
                self.CF.SetValue('Cliente') 
            if (valoreCAUSA=='120' or valoreCAUSA=='240' or valoreCAUSA=='241' or valoreCAUSA=='245'):   
                self.vCF.SetValue('F')
                self.CF.Enable(False)
                self.CF.SetValue('Fornitore')
 
            # > diegom 
            #if (valoreCAUSA=='140' or valoreCAUSA=='145' or valoreCAUSA=='170'):
                #self.segno.SetValue('D') # da controllare
            #self.note.SetFocus()
        elif (cnt_rec>1):
            try:
	        import srctabg
            except :
	        pass
            try:
                import base.srctabg
            except :
                pass
            control = ['Ricerca Causale',self.vCAUSA,self.dCAUSA,self.FndTABGEN,'CAUSA']     
            win = srctabg.create(self,control)
            win.Centre(wx.BOTH)
            win.Show(True) 
            self.note.SetFocus()


    # < diegom da vedere in seguito
    def FndVend(self, evt):
        #print "fndvend" 
        cnt_rec = 0
        vnumdoc = self.num_doc.GetValue()
        vanno_doc = self.anno.GetValue()
        vragsoc1 = self.ragsoc1.GetValue()
        vcodcf = self.codcf.GetValue()
        valTIPO_DOC = self.vTIPO_DOC.GetValue()
        vdata_doc = self.datadoc.GetValue()
        vstt_doc = self.stt_doc

        if vdata_doc=="  /  /    " : vdata_doc=""
        if vnumdoc=='' : vnumdoc = 0

        if   (int(vnumdoc)==0 and vragsoc1=="" and vdata_doc==""):
             sql = """ select * from docu1 where anno = "%s" """ # and stt_doc="%s" """ 
             valueSql = vanno_doc #, vstt_doc

        if   (int(vnumdoc)==0 and vragsoc1!="" and vdata_doc==""):
             #print "1........"
             sql = """ select * from docu1 
                       where cod_cf = "%s" 
                       and anno = "%s" 
		       and rag_soc1 like "%s" """ # and stt_doc="%s" """
             valueSql = vcodcf, vanno_doc, vragsoc1 #, vstt_doc

        elif (int(vnumdoc)==0 and vragsoc1=="" and vdata_doc!=""):
             #print "2........"
             sql = """ select * from docu1 
                       where data_doc = "%s" 
                       and anno = "%s" """ # and stt_doc="%s" """
             valueSql = vdata_doc, vanno_doc #, vstt_doc

        elif (int(vnumdoc)==0 and vragsoc1!="" and vdata_doc!="" and vcodcf!=""):
             #print "3........"
             sql = """ select * from docu1 
                       where data_doc = "%s" 
                       and rag_soc1 like "%s" 
                       and cod_cf = "%s" """ # and stt_doc="%s" """
             valueSql = vdata_doc, vragsoc1, vcodcf #, vstt_doc

        elif (int(vnumdoc)!=0 and vragsoc1!="" and vdata_doc=="" and vcodcf!=""):
             #print "4........"
             sql = """ select * from docu1 
                       where num_doc = "%s" 
                       and rag_soc1 like "%s"
                       and cod_cf = "%s" """ # and stt_doc="%s" """
             valueSql = int(vnumdoc), vragsoc1, vcodcf #, vstt_doc

        elif (int(vnumdoc)!=0 and vragsoc1=="" and vdata_doc!="" and vcodcf!=""):
             #print "5........"
             sql = """ select * from docu1 
                       where num_doc = "%s" 
                       and data_doc = "%s" """ # and stt_doc="%s" """
             valueSql =  int(vnumdoc), vdata_doc #, vstt_doc

        elif (int(vnumdoc)!=0 and vragsoc1=="" and vdata_doc=="" and vcodcf!=""):
             #print "6........"
             sql = """ select * from docu1 
                       where num_doc = "%s" """ # and stt_doc="%s" """
             valueSql = int(vnumdoc) #, vstt_doc

        elif (valTIPO_DOC!="" and int(vnumdoc)!=0):
             #print "7........."
             sql = """ select * from docu1 
                       where num_doc = "%s"
                       and tipo_doc = "%s"
                       and data_doc = "%s" 
                       and rag_soc1 like "%s" 
                       and cod_cf = "%s" """ # and stt_doc="%s" """
             valueSql = int(vnumdoc), valTIPO_DOC, vdata_doc, vragsoc1, vcodcf #, vstt_doc


        try:
             cr = self.CnAz.cursor ()
             cr.execute(sql % valueSql)
             rows = cr.fetchall()
             cnt_rec=len(rows)
        except StandardError, msg:
             #self.__MDI__.MsgErr("MovCon"," FndVend Mov Error %s" % (msg))
             print msg
        self.CnAz.commit()
        #print sql % valueSql
        #print cnt_rec
        if (cnt_rec>1 or cnt_rec==0):
            import srcdocmov 
            control = [self.anno, self.num_doc, self.ragsoc1, 
                       self.datadoc, self.vTIPO_DOC, self.codcf, 
                       self.FndVend, self.stt_doc]  
            win = srcdocmov.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)  
        elif (cnt_rec==1): self.FndSelVend(rows[0])
  
    # > diegom

    def FndSelVend(self, evt):
        row = evt
        self.anno_doc.SetValue(str(row[1]))
        self.vTIPO_DOC.SetValue(str(row[0]))
        self.num_doc.SetValue(str(row[2])) 
        self.datadoc.SetValue(row[3])
        self.codcf.SetValue(row[4])
        self.ragsoc1.SetValue(row[5])
        #print "riempi campi"
           

    def Stampa(self, evt):   
     	anno = self.anno.GetValue()
	num_mov = self.num_doc.GetValue()
	tipo_mov = 'movcon' 
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,   
              tipo = tipo_mov, 
              parametriSql = (anno,num_mov),
              #datiazienda = self.dzDatiAzienda,
              anteprima = True )
        
    def New(self, evt):
        self.NewTxt(self)
        self.cntr = "new"
        registro = "R1" 
        anno = self.anno.GetValue()
        chiave = "RMOV"   
        sql = """ select * from libriaz 
                  where chiave = "%s" and anno = "%s" and registro = "%s" """
        valueSql = chiave, anno, registro
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            while (1):
                row=cr.fetchone()
                if row == None:
                    break
                if (row[3] == None) : self.num_mov.SetValue('1')
                if (row[3] != None) : self.num_mov.SetValue(str(int(row[3])+1))
                if (row[16] == None) : self.vdatamov.SetValue(self.data)
                if (row[16] != None) : self.vdatamov.SetValue(row[16])
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","New Error %s " % (msg))
        self.CnAz.commit()
        num_mov = int(self.num_mov.GetValue())
        #self.datamov.SetValue(self.vdatamov.GetValue())
             
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
                        
    def Close(self, evt):
        if (self.ragsoc2.GetValue()!="" or self.ragsoc1.GetValue()!=""):
            dlg = wx.MessageDialog(self,cfg.msgesci, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
                self.AggMenu(True,self.IDMENU)
                wx.GetApp().GetPhasisMdi().CloseTabObj(self)
                #self.Destroy()
            else:
                dlg.Destroy()
        else:
            self.AggMenu(True,self.IDMENU)
            wx.GetApp().GetPhasisMdi().CloseTabObj(self)
            #self.Destroy()
            
    def CntSave(self, evt):
        if self.differenza.GetValue()!='0,00' and self.PDC.GetValue()!='0,00':
            dlg = wx.MessageDialog(self,cfg.msgdiffno, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                self.cnt_save=0
                self.ok.SetFocus()
            else:
                self.cnt_save=1
                
        
    def Save(self, evt):
        #print self.cnt_save 
        #print self.codcf.GetValue()
      
        if (self.cnt_save==0):
            vCAUSA=self.vCAUSA.GetValue()
            #print "inizio if save"
            vcntr=self.cntr
            #self.cntr=""
            self.cnt_save=0
            vanno=self.anno.GetValue()
            vnum_mov=int(self.num_mov.GetValue())
            valCF = self.vCF.GetValue()
            # libriaz
            chiave="RMOV"
            registro="R1"


            vdatadoc=self.datadoc.GetValue()
            vdatamov=self.datamov.GetValue()


            if (self.lc_Slct=="lc1"):
                data_int=self.datadoc.GetValue()
            elif (self.lc_Slct=="lc2"):
                data_int=self.datamov.GetValue()

            data_lst = data_int.split("/")
            data_int = str(data_lst[2]) + str(data_lst[1]) + str(data_lst[0])

            vcodcf=self.codcf.GetValue()

            mess_err = 0
 
            if (vCAUSA=="120" or vCAUSA=="110"):
                mess_err=3 
                nrow=self.lc1.GetItemCount() 
                if (nrow==0): mess_err=1
                else:
                    for row in range(nrow):
                        valconto=self.getColTxtlc1(row,15)
                        if (self.lc_Slct=="lc1"):
                            if (valconto=="10" and valCF=="C" or valconto=="30" and valCF=="F"): mess_err=0; 
                        #if (self.lc_Slct=="lc2"):
                            #if (valconto=="30"): mess_err=0;                   
                  
            elif (self.lc_Slct=="lc2"): 
                nrow=self.lc2.GetItemCount()
                if nrow==0: mess_err=1
                else: mess_err=0 

            if (mess_err==1): self.Message("Inserire almeno una operazione ",self.ttl)
            elif (mess_err==3): 
                  if valCF=="C": self.Message("Inserire operazione Cliente ",self.ttl)
                  elif valCF=="F": self.Message("Inserire operazione Fornitore ",self.ttl)


            #valconto=self.getColTxtlc1(1,15)
            #print "nrow"
            #print nrow
            #for row in range(nrow)

            if mess_err==0 :
                if (vcntr=="new"): vcntr_reg="new"; vcntr="new"
                elif (vcntr=="modi"): vcntr_reg=""; vcntr="modi"
            else:
                vcntr=""
                vcntr_reg=""

            vnum_doc=self.num_doc.GetValue()  
            vtipodoc=""
            vrigadoc=""
            vanno_doc=""
            #valDIV=self.vDIV.GetValue()
            #vt_cpart=self.vCF.GetValue()              
            valueSql = vnum_mov,vanno
            # > diegom
        
            if(vcntr=="modi"):
                try:
                    cr = self.CnAz.cursor()
                    sql = """ delete from movcon where num_mov = "%s" and anno = "%s" """
                    cr.execute(sql % valueSql)   
        	except StandardError, msg:
            	    self.__MDI__.MsgErr("movcon","Delete Error %s " % (msg))
        	self.CnAz.commit()
                vcntr="new" 
                vcntr_reg=""    
            if(vcntr=="new"):
                #print "if new"
                if (self.lc_Slct=="lc1"): nrow=self.lc1.GetItemCount() 
                if (self.lc_Slct=="lc2"): nrow=self.lc2.GetItemCount()
                vnriga=0
                for row in range(nrow):
                    ## Valori CORPO
                    # < diegom lc1
                    if (self.lc_Slct=="lc1"):
                        print "lc1"
                        vnriga += 10 #vnriga=self.getColTxtlc1(row, 3)
                        vanno_iva=self.getColTxtlc1(row, 4)
                        valDIV="EU" #self.getColTxtlc1(row, 5)
                        vPDC=self.getColTxtlc1(row, 6)
                        if (vcntr_reg==""):
                            vdCAUSA=self.getColTxtlc1(row, 7)
                        if (vcntr_reg=="new"):
                            vdCAUSA=self.getColTxtlc1(row, 7)
                            vdCAUSA=vdCAUSA + " N. " + str(self.getColTxtlc1(row, 13)) 
                            vdCAUSA=vdCAUSA + " - " + str(self.datadoc.GetValue())
                        vimporval=self.getColTxtlc1(row, 8)
                        self.__MDI__.CnvPM(vimporval)
                        vimporval=self.__MDI__.val
                        vimponval=self.getColTxtlc1(row, 9)
                        self.__MDI__.CnvPM(vimponval)
                        vimponval=self.__MDI__.val
                        vanno_doc=self.getColTxtlc1(row, 10)
                        valTIPO_DOC=self.vTIPO_DOC.GetValue()
                        vdatadoc=self.datadoc.GetValue() #self.getColTxtlc1(row, 12)
                        vnum_doc=self.getColTxtlc1(row, 13)
                        vnum_doc1=self.getColTxtlc1(row, 14)
                        valCONTO=self.getColTxtlc1(row, 15)
                        vimporto=self.totale_doc.GetValue() #self.getColTxtlc1(row, 16)
                        self.__MDI__.CnvPM(vimporto)
                        vimporto=self.__MDI__.val
                        vsegno=self.getColTxtlc1(row, 17)
                        #vcodcf=self.getColTxtlc1(row, 18) #cpart
                        vCAMBIO=0 #self.getColTxtlc1(row, 19)
                        valTIPO_IVA=self.getColTxtlc1(row, 20)
                        valTIPO_IVA1=self.getColTxtlc1(row, 21)
                        valALIVA=self.getColTxtlc1(row, 22)
                        vregistro=0 #self.getColTxtlc1(row, 23)
                        vimponib=self.getColTxtlc1(row, 24)
                        self.__MDI__.CnvPM(vimponib)
                        vimponib=self.__MDI__.val
                        vrigagior=self.getColTxtlc1(row, 25)
                        if vrigagior==None or vrigagior=="" :vrigagior=0
                        vpaggior=self.getColTxtlc1(row, 26)
                        if vpaggior==None or vpaggior=='':vrigagior=0
                        vnote=self.getColTxtlc1(row, 27)                                    
                        vstt_mov="C"#self.getColTxtlc1(row, 28)
                        vdCONTO=self.getColTxtlc1(row, 32)
                        #print vcodcf
                        vm0=vanno,vnum_mov #2
                        vm1=vdatamov,vnriga,vanno_iva,valDIV,vPDC,vdCAUSA,vimporval,vimponval #8
                        vm2=vanno_doc,valTIPO_DOC,vdatadoc,vnum_doc,vnum_doc1,valCONTO,vimporto #7
                        vm3=vsegno,vcodcf,vCAMBIO,valTIPO_IVA,valTIPO_IVA1,valALIVA #6
                        vm4=vregistro,vimponib,int(vrigagior),int(vpaggior),vnote,vstt_mov,vdCONTO #7
                        vm5=int(data_int),valCF #2
                        #print vdCONTO
                        valueSql = vm0 + vm1 + vm2 + vm3 + vm4 + vm5
                    # > diegom lc1
                    # < diegom lc2
                    if (self.lc_Slct=="lc2"):
                        valCF=""
                        print "lc2"
                        vnriga += 10 #vnriga=self.getColTxtlc2(row, 3)
                        vanno_iva=self.getColTxtlc2(row, 4)
                        valDIV="EU" #self.getColTxtlc2(row, 5)
                        vPDC=self.getColTxtlc2(row, 6)
                        vdCAUSA=self.getColTxtlc2(row, 7)
                        vimporval=self.getColTxtlc2(row, 8)
                        self.__MDI__.CnvPM(vimporval)
                        vimporval=self.__MDI__.val
                        vimponval=self.getColTxtlc2(row, 9)
                        self.__MDI__.CnvPM(vimponval)
                        vimponval=self.__MDI__.val
                        vanno_doc=self.getColTxtlc2(row, 10)
                        valTIPO_DOC="" #self.getColTxtlc2(row, 11)
                        vdatadoc="" #self.datadoc.GetValue() #self.getColTxtlc2(row, 12)
                        vnum_doc="" #self.getColTxtlc2(row, 13)
                        vnum_doc1="" #self.getColTxtlc2(row, 14)
                        valCONTO=self.getColTxtlc2(row, 15)
                        vimporto=self.totale_doc.GetValue() #self.getColTxtlc2(row, 16)
                        self.__MDI__.CnvPM(vimporto)
                        vimporto=self.__MDI__.val
                        vsegno=self.getColTxtlc2(row, 17)
                        vcodcf="" #self.getColTxtlc2(row, 18) #cpart
                        vCAMBIO=0 #self.getColTxtlc2(row, 19)
                        valTIPO_IVA=self.getColTxtlc2(row, 20)
                        valTIPO_IVA1=self.getColTxtlc2(row, 21)
                        valALIVA=self.getColTxtlc2(row, 22)
                        vregistro=0 #self.getColTxtlc2(row, 23)
                        vimponib=self.getColTxtlc2(row, 24)
                        self.__MDI__.CnvPM(vimponib)
                        vimponib=self.__MDI__.val
                        vrigagior=self.getColTxtlc2(row, 25)
                        if vrigagior==None or vrigagior=="" :vrigagior=0
                        vpaggior=self.getColTxtlc2(row, 26)
                        if vpaggior==None or vpaggior=='':vrigagior=0
                        vnote=self.getColTxtlc2(row, 27)                                    
                        vstt_mov=self.getColTxtlc2(row, 28)
                        vdCONTO=self.getColTxtlc2(row, 32)
                        #print vcodcf
                        vm0=vanno,vnum_mov #2
                        vm1=vdatamov,vnriga,vanno_iva,valDIV,vPDC,vdCAUSA,vimporval,vimponval #8
                        vm2=vanno_doc,valTIPO_DOC,vdatadoc,vnum_doc,vnum_doc1,valCONTO,vimporto #7
                        vm3=vsegno,vcodcf,vCAMBIO,valTIPO_IVA,valTIPO_IVA1,valALIVA #6
                        vm4=vregistro,vimponib,int(vrigagior),int(vpaggior),vnote,vstt_mov,vdCONTO #7
                        vm5=int(data_int),valCF #2
                        #print vdCONTO
                        valueSql = vm0 + vm1 + vm2 + vm3 + vm4 + vm5
                    # > diegom lc2

                    ## Funzione Salva movcon
                    try:
                        cr = self.CnAz.cursor()
                        sql = """ insert into movcon
                                  values("%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s") """
                        cr.execute(sql % valueSql) 
        	    except StandardError, msg:
                        self.__MDI__.MsgErr("movcon","Save Error %s " % (msg))
        	    self.CnAz.commit()
                valueSql = vnum_mov,vdatamov,chiave,vanno,registro
                if(vcntr_reg=="new"):
                    try:
                       cr = self.CnAz.cursor()
                       sql = """ update libriaz set ultnum = "%s",
                                 udatreg = "%s"
                                 where chiave = "%s" 
                                 and anno = "%s" and registro = "%s" """
                       cr.execute(sql % valueSql) 
        	    except StandardError, msg:
                        self.__MDI__.MsgErr("movcon","Update Libriaz Error %s " % (msg))
        	    self.CnAz.commit()
                # < diegom
                # AGGIORNARE STT_DOC SU DOCU1 E DOCU2
                    valueSql = vanno, vnum_doc, valTIPO_DOC
                    try:
                        cr = self.CnAz.cursor()
                        sql = """ update docu1 set stt_doc = "R" 
                              where anno = "%s" 
                              and num_doc = "%s" and tipo_doc = "%s" """  
                        cr.execute(sql % valueSql) 
                    except StandardError, msg:
                        print "Update docu1 Error %s" % (msg)
                    self.CnAz.commit()
                    try:
                        cr = self.CnAz.cursor()
                        sql = """ update docu2 set stt_doc = "R" 
                              where anno = "%s" 
                              and num_doc = "%s" and tipo_doc = "%s" """  
                        cr.execute(sql % valueSql) 
                    except StandardError, msg:
                        print "Update docu2 Error %s" % (msg)
                    self.CnAz.commit()






                if (mess_err==0): self.Start(self)
                #self.stampa.SetFocus()     
        else:
            if self.cnt_save==1: pass 
            else: self.Message(cfg.msgass,self.ttl)

 
    def is_look(self):
        if (self.cntr!="new" and self.cntr!="modi"): return False
        else : return True
        
    def data_reload(self,rec,cntrp):
        self.rec=rec
        #self.tcpart=cntrp.upper()
        self.Start(self)
