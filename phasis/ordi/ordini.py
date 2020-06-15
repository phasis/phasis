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
import wx.lib.buttons as buttons #import *
import string 
from cfg import *
import cfg

def create(parent,cnt):
    return Ordini(parent,cnt)
  
class Ordini(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.ttl = cnt[0]
        self.val_numord = 0
        self.tipoord  = cnt[1]
        self.tcpart = "C"
        if self.tipoord=='OF': self.tcpart = "F"
        self.tblart = "articoli"
        self.ttlanag = _('Anagrafica Clienti')
        self.ttlart = _('Anagrafica Articoli')
        self.ttldest = _('Anagrafica Spedizione')        
        self.rec = cnt[2]
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        self.voktestata = 0
        #self.font = self.GetFont()        
        self.color = self.GetBackgroundColour()
        Nid = wx.NewId()
        self.__MDI__ =  wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz = self.__MDI__.GetConnAZ()
        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon =  self.__MDI__.GetDataC()
        self.dzDatiAzienda =  self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id = wx.NewId(), name = '',
              parent = self, pos = wx.Point(0, 0), size = wx.DLG_SZE(self,680/2,420/2), #size = wx.Size(680, 420),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        self.ntbk = wx.Notebook(id = wx.NewId(), name = 'notebook',
              parent = self.pnl, pos = wx.DLG_PNT(self.pnl, 5/2,5/2), #pos = wx.Point(5, 5), 
              size = wx.DLG_SZE(self.pnl,cfg.NTBKHTUTTI/2,cfg.NTBKVTUTTI/2),style = 0)
              #size = wx.Size(cfg.NTBKH,cfg.NTBKV), style = 0)
        self.ntbk.SetFont(self.font)
        
        self.pnl1 = wx.Panel(id = wx.NewId(), name = 'panel1',
              parent = self.ntbk, pos = wx.Point(0, 0))
        self.pnl1.SetFont(self.font)
        self.pnl2 = wx.Panel(id = wx.NewId(), name = 'panel2',
              parent = self.ntbk, pos = wx.Point(0, 0))
        self.pnl2.SetFont(self.font)
        self.pnl3 = wx.Panel(id = wx.NewId(), name = 'panel3',
              parent = self.ntbk, pos = wx.Point(0, 0))
        self.pnl3.SetFont(self.font)
        
        self.ntbk.AddPage(imageId = -1, page = self.pnl1, 
            select = True, text = _(' Testata')+' (1) ')
        self.ntbk.AddPage(imageId = -1, page = self.pnl2, 
            select = False, text = _(' Corpo')+' (2) ')
        self.ntbk.AddPage(imageId = -1, page = self.pnl3, 
            select = False, text = _(' Calce')+' (3) ')
        
        #self.pnl.SetFont(self.font)
        #self.pnl1.SetFont(self.font)
        #self.pnl2.SetFont(self.font)
        #self.pnl3.SetFont(self.font)
        #self.ntbk.SetFont(self.font)
        
        wx.StaticText(self.pnl1, -1, _("Doc. :"), wx.DLG_PNT(self.pnl1, 5,7))
        self.TIPO_ORD = wx.ComboBox(self.pnl1, Nid,"",
              wx.DLG_PNT(self.pnl1, 27,5), 
              wx.DLG_SZE(self.pnl1, 90,-1),[],wx.CB_DROPDOWN | wx.CB_SORT )
        self.vTIPO_ORD =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 275,90))
        self.lord = wx.StaticText(self.pnl1, -1, _("Num. :"), 
              wx.DLG_PNT(self.pnl1, 120,7))
        self.anno = wx.ComboBox(self.pnl1, Nid, self.annoc,
              wx.DLG_PNT(self.pnl1, 145,5), 
              wx.DLG_SZE(self.pnl1, 35,-1),[self.annoc], wx.CB_DROPDOWN | wx.CB_SORT )  
        wx.StaticText(self.pnl1, -1, "/", wx.DLG_PNT(self.pnl1, 182,7))
        self.num_ord = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 185,5), 
              wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER ) 
        self.cnum_ord = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 226,5),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl1, -1, _("Data :"), 
              wx.DLG_PNT(self.pnl1, 243,7))
        self.data_ord = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 264,5), 
              wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)
        self.cdataord = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 315,5),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.vdata_ord = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 280, 125), 
              wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl1, -1,_(" Vs. Ordine :"), wx.DLG_PNT(self.pnl1, 5,20))
        self.vs_ord = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 5,30),
              wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) 
        wx.StaticText(self.pnl1, -1, _("Data :"), 
              wx.DLG_PNT(self.pnl1, 60,20))
        self.vs_data = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 60, 30), 
              wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.cvsdata = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 115,30),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.sbox_cf = wx.StaticBox(self.pnl1, Nid, _(' Cliente '),
              wx.DLG_PNT(self.pnl1, 5,45), wx.DLG_SZE(self.pnl1, 265,65))
        self.lcodcf =  wx.StaticText(self.pnl1, -1, _("Codice"),  
              wx.DLG_PNT(self.pnl1, 10,55))
        self.codcf =  wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 10, 65),  
              wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT) ,wx.TE_PROCESS_ENTER)
        self.codcf1 =  wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 10, 65), 
              wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT))
        self.ccodcf = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 55,65), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lragsoc = wx.StaticText(self.pnl1, -1, _("Cessionario :"), 
              wx.DLG_PNT(self.pnl1, 75,55))
        self.ragsoc1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 75,65), 
              wx.DLG_SZE(self.pnl1, 120,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)    
        self.cragsoc1 = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 200,65),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc3 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 75,65), 
              wx.DLG_SZE(self.pnl1, 120,cfg.DIMFONTDEFAULT))    
        self.cragsoc3 = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 200,65),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc2 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 148, 65), 
              wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)          
        self.ragsoc4 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 148, 65), 
              wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))          
        self.lindiriz = wx.StaticText(self.pnl1, -1, _("Indirizzo :"), 
              wx.DLG_PNT(self.pnl1, 10,82))
        self.indiriz = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,80), 
              wx.DLG_SZE(self.pnl1, 170,cfg.DIMFONTDEFAULT))
        self.cdest = wx.Button(self.pnl1, Nid,  _(' Cliente '), 
              wx.DLG_PNT(self.pnl1, 218,80),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.rdest1 = wx.Button(self.pnl1, Nid, _("Annulla"),
              wx.DLG_PNT(self.pnl1, 218,65),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        wx.StaticText(self.pnl1, -1, _("Citta` :"), 
              wx.DLG_PNT(self.pnl1, 10,97))
        self.zona = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,95), 
              wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl1, -1, _("CAP :"), wx.DLG_PNT(self.pnl1, 150,97))
        self.cap = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 180, 95), 
              wx.DLG_SZE(self.pnl1, 35,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl1, -1, _("PR :"), wx.DLG_PNT(self.pnl1, 225,97))
        self.pr = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 243, 95),
              wx.DLG_SZE(self.pnl1, 20,cfg.DIMFONTDEFAULT))
        self.indiriz1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,80), 
              wx.DLG_SZE(self.pnl1, 170,cfg.DIMFONTDEFAULT))
        self.zona1 = wx.TextCtrl(self.pnl1, Nid, "",
            wx.DLG_PNT(self.pnl1, 45,95), 
              wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))
        self.cap1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 180, 95), 
              wx.DLG_SZE(self.pnl1, 35,cfg.DIMFONTDEFAULT))
        self.pr1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 243, 95), 
              wx.DLG_SZE(self.pnl1, 20,cfg.DIMFONTDEFAULT))
        self.vDIVvend =  wx.TextCtrl(self.pnl1, -1, "", 
            wx.DLG_PNT(self.pnl1, 280,130))
        wx.StaticText(self.pnl1, -1, _("Vs Rifer. :"), 
              wx.DLG_PNT(self.pnl1, 10,114))
        self.vsrif = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45, 112), 
              wx.DLG_SZE(self.pnl1, 85,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)
        wx.StaticText(self.pnl1, -1, _("Ns Rifer. :"), 
              wx.DLG_PNT(self.pnl1, 143,114))
        self.nsrif = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 180, 112), 
            wx.DLG_SZE(self.pnl1, 85,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)          
        self.lnote = wx.StaticText(self.pnl1, -1, _("Note :"), 
              wx.DLG_PNT(self.pnl1, 10,129))
        self.note = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,127), 
              wx.DLG_SZE(self.pnl1, 220,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)
        self.stt_ord1 = wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 285,137))  
        self.lcodage = wx.StaticText(self.pnl1, -1, _("Agente :"), 
              wx.DLG_PNT(self.pnl1, 10,144))
        self.codage = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,142), 
              wx.DLG_SZE(self.pnl1, 45,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.ccodage = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 93,142),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc1age = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 108,142), 
              wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        wx.StaticText(self.pnl1, -1, _("Priorita`:"), 
              wx.DLG_PNT(self.pnl1, 213,144))
        self.PRIO = wx.ComboBox(self.pnl1, Nid,"5",
              wx.DLG_PNT(self.pnl1, 245,142), 
              wx.DLG_SZE(self.pnl1, 20,-1),[],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vPRIO = wx.TextCtrl(self.pnl1, -1, "", 
            wx.DLG_PNT(self.pnl1, 275,90))
        wx.StaticText(self.pnl1, -1, _("Pagamento :"), 
              wx.DLG_PNT(self.pnl1, 10,160))
        self.PAGAM = wx.ComboBox(self.pnl1, Nid,"",
              wx.DLG_PNT(self.pnl1, 60,158), 
              wx.DLG_SZE(self.pnl1, 120,-1),[],
            wx.CB_DROPDOWN | wx.CB_SORT | wx.TE_PROCESS_ENTER)
        self.vPAGAM = wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 275,90))
        self.cmpiliberi = wx.Button(self.pnl1, Nid, _("Campi Liberi"),
              wx.DLG_PNT(self.pnl1,205,158),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.localit =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 280,37))
        self.stato =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 280,37))
        self.localit1 =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 280,37)) 
        self.stato1 =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 280,37))       
        self.conse =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))
        self.trasp =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))
        self.cod_vet =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))
        self.rag_ord =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))
        self.campo1 =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))        
        self.campo2 =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))
        self.lc = wx.ListCtrl(self.pnl2, Nid,
              wx.DLG_PNT(self.pnl2, 5,10), 
              wx.DLG_SZE(self.pnl2, 323,95),
              wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)   
        #wx.StaticLine(self.pnl, -1, wx.DLG_PNT(self.pnl, 5,155), 
        #      wx.DLG_SZE(self.pnl, 283,-1)) 
        self.lcod = wx.StaticText(self.pnl2, -1, _("Codice :"), 
              wx.DLG_PNT(self.pnl2, 5,112))
        self.codart = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 30,110), 
              wx.DLG_SZE(self.pnl2, 55,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)            
        self.ccodart = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 86,110),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH, cfg.btnSzeV), 
            wx.TE_PROCESS_ENTER)
        #self.ccodart.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL))
        self.codbar = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 35,110), 
              wx.DLG_SZE(self.pnl2, 60,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)            
        self.ccodbar = buttons.GenToggleButton(self.pnl2, Nid, "|''|'|", 
              wx.DLG_PNT(self.pnl2, 99,110),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        #self.ccodbar.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL))
        # inizio personalizzazione testo
        self.ctesto = buttons.GenButton(self.pnl2, Nid, "T", 
              wx.DLG_PNT(self.pnl2, 112,110),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dtesto = wx.TextCtrl(self.pnl2, -1, "", wx.DLG_PNT(self.pnl2,5,5))
        # fine personalizzazione testo
        self.ccodinfo = buttons.GenButton(self.pnl2, Nid, " ? ", 
              wx.DLG_PNT(self.pnl2, 125,110), 
            wx.DLG_SZE(self.pnl2,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl2, -1, _("Descrizione :"), 
              wx.DLG_PNT(self.pnl2, 140,112))
        self.descriz = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 180, 110), 
              wx.DLG_SZE(self.pnl2, 130,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)                     
        self.cdescriz = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 315,110),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))       
        wx.StaticText(self.pnl2, -1, _("UM :"), 
              wx.DLG_PNT(self.pnl2, 5,127))
        self.UM = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 23,125), 
              wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.lmis = wx.StaticText(self.pnl2, -1, _("Mis :"), 
              wx.DLG_PNT(self.pnl2, 50,127))
        self.mis = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 70,125), 
              wx.DLG_SZE(self.pnl2, 20,cfg.DIMFONTDEFAULT))                    
        wx.StaticText(self.pnl2, -1, _("Sc % :"), 
              wx.DLG_PNT(self.pnl2, 95,127))
        self.sc1 = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 120,125), 
              wx.DLG_SZE(self.pnl2, 25, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.lvALIVA = wx.StaticText(self.pnl2, -1, _("Cod. Iva :"), 
              wx.DLG_PNT(self.pnl2, 155,127))
        self.vALIVA = wx.TextCtrl(self.pnl2, Nid, "20",
              wx.DLG_PNT(self.pnl2, 190,125), 
              wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )
        self.cALIVA = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 215,125),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dALIVA = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 230,125), 
              wx.DLG_SZE(self.pnl2, 95, cfg.DIMFONTDEFAULT))   
        self.lvPDC = wx.StaticText(self.pnl2, -1, _("Cod. p.d.c. :"), 
              wx.DLG_PNT(self.pnl2, 235,127))
        self.vPDC = wx.TextCtrl(self.pnl2, Nid, "7501",
              wx.DLG_PNT(self.pnl2, 280,125), 
              wx.DLG_SZE(self.pnl2, 30, cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )
        self.cvPDC = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 315,125),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        #self.lpeso = wx.StaticText(self.pnl2, -1, "Peso :", 
        #      wx.DLG_PNT(self.pnl2, 230,127))
        #self.peso = wx.TextCtrl(self.pnl2, Nid, "",
        #      wx.DLG_PNT(self.pnl2, 255,125), 
        #      wx.DLG_SZE(self.pnl2, 20,-1), wx.ALIGN_RIGHT)                    
        #self.lvolume = wx.StaticText(self.pnl2, -1, "volume :", 
        #       wx.DLG_PNT(self.pnl2, 280,127))
        #self.volume = wx.TextCtrl(self.pnl2, Nid, "",
        #       wx.DLG_PNT(self.pnl2, 300,125), 
        #       wx.DLG_SZE(self.pnl2, 20,-1), wx.ALIGN_RIGHT)
        self.llst = wx.StaticText(self.pnl2, -1, _("Listino :"), 
              wx.DLG_PNT(self.pnl2, 5,142))
        self.lst = wx.TextCtrl(self.pnl2, Nid, "",
             wx.DLG_PNT(self.pnl2, 33,140), 
             wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT),
             wx.ALIGN_RIGHT )   
        self.clst = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 57,140),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        # ult modifica      
        wx.StaticText(self.pnl2, -1, _("Colli :"), wx.DLG_PNT(self.pnl2, 82,142))
        self.colli = wx.TextCtrl(self.pnl2, -1, "",
              wx.DLG_PNT(self.pnl2, 100,140), 
              wx.DLG_SZE(self.pnl2, 25, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )
        
        self.lprovv = wx.StaticText(self.pnl2, -1, _("Provv. :"), 
              wx.DLG_PNT(self.pnl2, 73,142))
        self.provv = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 100,140), 
              wx.DLG_SZE(self.pnl2, 25, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.lcosto = wx.StaticText(self.pnl2, -1, _("Costo :"), 
              wx.DLG_PNT(self.pnl2, 132,142))
        self.costo = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 157,140), 
              wx.DLG_SZE(self.pnl2, 40, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )        
        self.lprezzo = wx.StaticText(self.pnl2, Nid, _("Prezzo :"), 
              wx.DLG_PNT(self.pnl2, 202,142))
        self.prezzo = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 232,140), 
              wx.DLG_SZE(self.pnl2, 45, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )      
        wx.StaticText(self.pnl2, -1, _("Qt :"), 
              wx.DLG_PNT(self.pnl2, 283,142))
        self.qt = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 297,140), 
              wx.DLG_SZE(self.pnl2, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )
        #self.qt = wx.SpinCtrl(self.pnl2, -1, "0.00",
        #      wx.DLG_PNT(self.pnl2, 295,140),
        #      wx.DLG_SZE(self.pnl2, 30,-1))
        #self.qt.SetRange(0.00,9999.99)
        self.importo = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))     
        self.ltotale = wx.StaticText(self.pnl2, -1, _("Totale :"), 
              wx.DLG_PNT(self.pnl2, 235,162))
        #self.ltotale.SetFont(self.font)
        #self.ltotale.SetForegroundColour(wx.Colour(128, 128, 128))
        self.totale = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 262,160), 
              wx.DLG_SZE(self.pnl2, 65, cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT )
        #self.totale.SetFont(self.font)
        self.sc2 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.sc3 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))        
        self.prezzo2 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.prezzo1 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.nriga = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.vinprod = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 5,37))
        self.vUM = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 5,37))                    
        self.vMERCE = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 5,52))                                                        
        self.vIMBAL = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,127))                          
        self.vCONFE = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))                    
        self.codmerc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.qt_ord = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.qt_con = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.qt_eva = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.prezzo_ag = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.datacons = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  

        self.peso = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.stt_ord2 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.annodoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))          
        self.tipodoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.datadoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.numdoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.campo2_art = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.campo1_art = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.sbox_calce = wx.StaticBox(self.pnl3, Nid, " ",
              wx.DLG_PNT(self.pnl3, 5,10), 
              wx.DLG_SZE(self.pnl3, 320,160))
        self.lnote_calce = wx.StaticText(self.pnl3, -1, _("Note :"), 
              wx.DLG_PNT(self.pnl3, 10,27))
        self.note_calce = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 45,25), 
              wx.DLG_SZE(self.pnl3, 260,55), style = wx.TE_MULTILINE)        
        self.lASPET = wx.StaticText(self.pnl3, Nid, _("Aspetto :"), 
              wx.DLG_PNT(self.pnl3, 15,87))
        self.vASPET =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 55,85), 
              wx.DLG_SZE(self.pnl3, 20, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cASPET = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 80,85),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dASPET =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 95,85), 
              wx.DLG_SZE(self.pnl3, 80, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.ltot_colli = wx.StaticText(self.pnl3, Nid, _("Num. totale colli :"), 
              wx.DLG_PNT(self.pnl3, 15,102))
        self.tot_colli =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 75,100), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.ltot_peso = wx.StaticText(self.pnl3, Nid, _("Peso colli :"), 
              wx.DLG_PNT(self.pnl3, 125,102))
        self.tot_peso =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 165,100), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.lscf = wx.StaticText(self.pnl3, Nid, _("Sconti finali :"), 
              wx.DLG_PNT(self.pnl3, 15,117))
        self.scf1 = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 75,115), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.scf2 = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 110,115), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.scf3 = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 145,115), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.lvPDC_SC = wx.StaticText(self.pnl3, -1, _("Cod. p.d.c. :"), 
              wx.DLG_PNT(self.pnl3, 205,117))
        self.vPDC_SC = wx.TextCtrl(self.pnl3, Nid, "6105",
              wx.DLG_PNT(self.pnl3, 250,115), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cvPDC_SC = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 285,115),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))       
        self.lprezzo_ac = wx.StaticText(self.pnl3, Nid, _("Acconto :"), 
              wx.DLG_PNT(self.pnl3, 15,132))
        self.prezzo_ac =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 55,130), 
              wx.DLG_SZE(self.pnl3, 50, cfg.DIMFONTDEFAULT),  wx.ALIGN_RIGHT )        
        self.lprezzo_ac1 = wx.StaticText(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 120,132))
        self.prezzo_ac1 =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 210, 130), 
              wx.DLG_SZE(self.pnl3, 50, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.csaldo = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 265,130),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))   
        self.ltotaledoc = wx.StaticText(self.pnl3, Nid, _("Totale Ordine :"),
              wx.DLG_PNT(self.pnl3, 180,152))
        self.totaledoc =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 240, 150), 
              wx.DLG_SZE(self.pnl3, 60, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )  
        self.vCONSEG = wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,117))  
        self.campo1_calce = wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,117))  
        self.campo2_calce = wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,117))  
        self.fndvTIPO_ORD = wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,117))  
        self.ok = wx.Button(self.pnl1, Nid, cfg.vcok, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )      
        self.new = wx.Button(self.pnl1, Nid, cfg.vcnew, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )      
        self.oktestata = wx.Button(self.pnl1, Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )              
        self.inte = wx.Button(self.pnl1, Nid, cfg.vcint,
              wx.DLG_PNT(self.pnl, 275,45), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.canc = wx.Button(self.pnl1, Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 275,45), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.modi = wx.Button(self.pnl1, Nid, cfg.vcmodi, 
              wx.DLG_PNT(self.pnl, 275,60), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.dele = wx.Button(self.pnl1, Nid, cfg.vcdele, 
              wx.DLG_PNT(self.pnl, 275,60),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.stampa = wx.Button(self.pnl1, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 275,75), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.skanag = wx.Button(self.pnl1, Nid, cfg.vcanag, 
              wx.DLG_PNT(self.pnl, 275,90), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV) )
        self.newr = wx.Button(self.pnl2, Nid, cfg.vcnewr, 
              wx.DLG_PNT(self.pnl2, 5,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))      
        self.okart = wx.Button(self.pnl2, Nid, cfg.vcokr, 
              wx.DLG_PNT(self.pnl2, 67,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))
        self.modir = wx.Button(self.pnl2, Nid, cfg.vcmodir,
              wx.DLG_PNT(self.pnl2, 67,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))
        self.intr = wx.Button(self.pnl2, Nid, cfg.vcintr, 
              wx.DLG_PNT(self.pnl2, 130,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.delr = wx.Button(self.pnl2, Nid, cfg.vcdeler, 
              wx.DLG_PNT(self.pnl2, 182,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.rbCONFER = wx.RadioButton(self.pnl1, Nid, cfg.vcCONF,
              wx.DLG_PNT(self.pnl1, 275,110), 
              wx.DLG_SZE(self.pnl1, 55,10))  
        self.rbEVASO = wx.RadioButton(self.pnl1, Nid, _(" Evaso "),
              wx.DLG_PNT(self.pnl1, 275,120), 
              wx.DLG_SZE(self.pnl1, 55,10))
        self.rbPREVIS = wx.RadioButton(self.pnl1, Nid, cfg.vcPREV,
              wx.DLG_PNT(self.pnl1, 275,130), 
              wx.DLG_SZE(self.pnl1, 55,10))

        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        for x in self.pnl1.GetChildren(): x.SetFont(self.font)
        for x in self.pnl2.GetChildren(): x.SetFont(self.font)
        for x in self.pnl3.GetChildren(): x.SetFont(self.font)
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)

        self.ccodinfo.Bind(wx.EVT_BUTTON, self.FndCodInfo)
        self.skanag.Bind(wx.EVT_BUTTON, self.StpSkAnag)
        #self.pnl.Bind(wx.EVT_BUTTON, self.Addi)      
        self.delr.Bind(wx.EVT_BUTTON, self.DelRow)
        self.dele.Bind(wx.EVT_BUTTON, self.CntrDele)        
        self.oktestata.Bind(wx.EVT_BUTTON, self.OkTestata)
        self.canc.Bind(wx.EVT_BUTTON, self.Close)  
        self.okart.Bind(wx.EVT_BUTTON, self.OkRow)
        self.modi.Bind(wx.EVT_BUTTON, self.Modi)
        self.modir.Bind(wx.EVT_BUTTON, self.ModiRow)
        self.inte.Bind(wx.EVT_BUTTON, self.IntTestata)
        self.intr.Bind(wx.EVT_BUTTON, self.IntRow)
        self.newr.Bind(wx.EVT_BUTTON, self.NewRow)
        self.new.Bind(wx.EVT_BUTTON, self.New)
        self.ok.Bind(wx.EVT_BUTTON, self.Save)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.csaldo.Bind(wx.EVT_BUTTON, self.CalcSaldo)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.ModiRow)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct) # occhio dovrebbe essere self.lc
        self.lc.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlct) # occhio dovrebbe essere self.lc
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) # occhio dovrebbe essere self.lc      
        #self.pnl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct) # occhio dovrebbe essere self.lc
        #self.pnl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlct) # occhio dovrebbe essere self.lc
        #self.pnl.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) # occhio dovrebbe essere self.lc
        #self.pnl.Bind(wx.EVT_LIST_KEY_DOWN, self.DblClick)
        self.qt.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        self.sc1.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        self.prezzo.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        self.ccodage.Bind(wx.EVT_BUTTON, self.FndAge)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.cragsoc3.Bind(wx.EVT_BUTTON, self.FndAnagDest)        
        self.ccodart.Bind(wx.EVT_BUTTON, self.FndCodArt)
        self.ctesto.Bind(wx.EVT_BUTTON, self.OpenTesto) #personaliz testo		
        self.codart.Bind(wx.EVT_TEXT_ENTER, self.FndCodArt)
        self.descriz.Bind(wx.EVT_TEXT_ENTER, self.FndDesArt)  	
        self.codage.Bind(wx.EVT_TEXT_ENTER, self.FndAge)
        #self.codcf.Bind(wx.EVT_TEXT_ENTER, self.FndCodCF)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.ragsoc3.Bind(wx.EVT_TEXT_ENTER, self.FndAnagDest)        
        self.ragsoc1.Bind(wx.EVT_CHAR, self.EvtChar)
        #self.note.Bind(wx.EVT_CHAR, self.EvtChar)
        self.cnum_ord.Bind(wx.EVT_BUTTON, self.FndOrd)
        self.num_ord.Bind(wx.EVT_TEXT_ENTER, self.FndOrd)
        self.data_ord.Bind(wx.EVT_TEXT_ENTER, self.CntData)
        self.vs_data.Bind(wx.EVT_TEXT_ENTER, self.CntvsData)
        self.descriz.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_des)
        #self.dataord.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_dataord)
        #self.vsdata.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_vsdata)        
        self.cvsdata.Bind(wx.EVT_BUTTON, self.CntvsData)
        self.cdataord.Bind(wx.EVT_BUTTON, self.CntData)
        self.vs_ord.Bind(wx.EVT_CHAR, self.EvtChar)
        self.num_ord.Bind(wx.EVT_CHAR, self.EvtChar)
        self.newr.Bind(wx.EVT_CHAR, self.EvtCharS)
        self.cALIVA.Bind(wx.EVT_BUTTON, self.FndSelALIVA)
        self.vALIVA.Bind(wx.EVT_TEXT_ENTER, self.FndSelALIVA)
        self.codbar.Bind(wx.EVT_TEXT_ENTER, self.FndCodBar)
        self.ccodbar.Bind(wx.EVT_BUTTON, self.SelCodBar)
        self.codbar.Bind(wx.EVT_TEXT_ENTER, self.FndCodBar)
        self.vs_ord.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_vs_ord)
        #self.vsdata.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_vsdata)
        self.vsrif.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_vsrif)
        self.nsrif.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_nsrif)
        self.PAGAM.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_PAGAM)        
        self.note.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_note)
        self.rbCONFER.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.rbPREVIS.Bind(wx.EVT_RADIOBUTTON, self.RadioB)        
        #self.rbPREVIS.Bind(wx.EVT_RADIOBUTTON, self.RadioB)          
        #self.prezzo.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_prezzo)
        #self.sc1.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_sc1)
        #self.qt.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_qt)
        self.PAGAM.Bind(wx.EVT_COMBOBOX, self.SelPAGAM)
        self.TIPO_ORD.Bind(wx.EVT_COMBOBOX, self.SelTIPO_ORD)
        #cdataord.Bind(wx.EVT_CALENDAR_DAY,self.CalSel)
        self.cdest.Bind(wx.EVT_BUTTON, self.CDest)
        self.rdest1.Bind(wx.EVT_BUTTON, self.RDest)     
        self.Bind(wx.EVT_CLOSE, self.Close) 
        self.Bind(wx.EVT_CHAR, self.EvtCharS)
        self.InsLibriaz()
        self.InsTabGen()
        self.Start(self)

    def InsLibriaz(self):
        sql = """ select registro from libriaz where registro="PC" """	
        try:
            cr =  self.CnAz.cursor ()
            cr.execute(sql)
   	    row = cr.fetchone()
            if row==None:  
                print "qua"
    	        import ins_libriaz
                self.AggMenu(True,self.IDMENU )
                wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        except StandardError, msg:   
            print "qui"
   	self.CnAz.commit()

    def InsTabGen(self):
        sql = """ select valore from tabgen where valore="PC" """	
        try:
            cr =  self.CnAz.cursor ()
            cr.execute(sql)
   	    row = cr.fetchone()
            if row==None:  
                print "qua"
    	        import ins_tabgen
                self.AggMenu(True,self.IDMENU )
                wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        except StandardError, msg:   
            print "qui"
   	self.CnAz.commit()

    def Start(self, evt):
        self.stampa.Enable(False)
        self.dtesto.Show(False) # personalizza testo
        self.fndvTIPO_ORD.SetValue('')
        self.ccodinfo.Enable(False) 
        self.vTIPO_ORD.SetValue(self.tipoord)
        self.cdest.SetLabel(_('Destinatario')) ######
        self.lst.SetValue("1")
        self.vDIVvend.SetValue("EU")
        self.vPRIO.SetValue("5")
        self.trasp.SetValue("TRA1")
        self.rag_ord.SetValue("A")
        self.campo1.SetValue("")
        self.campo2.SetValue("")
        self.note.SetBackgroundColour(self.color)
        self.note_calce.SetBackgroundColour(self.color)  
        self.DelAnagTxt(self)
        self.DelArtTxt(self)
        self.OffAnagTxt(self)
        self.OffArtTxt(self)
        self.data = self.datacon #strftime("%d/%m/%Y")        
        self.data_ord.SetValue(self.data)
        self.vdata_ord.SetValue(self.data)
        self.data_ord.Enable(True)
        self.TIPO_ORD.Enable(False)        
        self.num_ord.Enable(True)
        self.num_ord.SetFocus()
        #self.stt_ord1.SetValue("C")
        #self.stt_ord2.SetValue("C")
        ##self.stt_ord1.SetValue("P")
        ##self.stt_ord2.SetValue("P")
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Descrizione"))
        self.lc.InsertColumn(2, _("Q.ta`"))
        self.lc.InsertColumn(3, _("Prezzo"))
        self.lc.InsertColumn(4, _("Sc%"))
        self.lc.InsertColumn(5, _("Importo"))
        self.lc.InsertColumn(6, _("Iva"))
        self.lc.InsertColumn(7, _("UM"))
        self.lc.InsertColumn(8, _("Mis"))
        self.lc.InsertColumn(9, _("n riga"))
        self.lc.InsertColumn(10, "")
        self.lc.InsertColumn(11, "")
        self.lc.InsertColumn(12, "")
        self.lc.InsertColumn(13, "")
        self.lc.InsertColumn(14, "")
        self.lc.InsertColumn(15, "")
        self.lc.InsertColumn(16, "")
        self.lc.InsertColumn(17, "")
        self.lc.InsertColumn(18, "")
        self.lc.InsertColumn(19, "")
        self.lc.InsertColumn(20, "")
        self.lc.InsertColumn(21, "")
        self.lc.InsertColumn(22, "")
        self.lc.InsertColumn(23, "")
        self.lc.InsertColumn(24, "")
        self.lc.InsertColumn(25, "")
        self.lc.InsertColumn(26, "")
        self.lc.InsertColumn(27, "")
        self.lc.InsertColumn(28, "")
        self.lc.InsertColumn(29, "")
        self.lc.InsertColumn(30, "")
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self.pnl,  60,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self.pnl, 100,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self.pnl, 27,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self.pnl, 50,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self.pnl,  25,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self.pnl,  50,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self.pnl,  25,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self.pnl, 20,-1).width)
        self.lc.SetColumnWidth(8, wx.DLG_SZE(self.pnl, 20,-1).width)
        self.lc.SetColumnWidth(9, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(10, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(11, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(12, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(13, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(14, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(15, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(16, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(17, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(18, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(19, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(20, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(21, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(22, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(23, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(24, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(25, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(26, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(27, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(28, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(29, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(30, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetFont(self.font)
        self.lc.SetBackgroundColour(self.color)
        self.lc.Enable(False)
        self.sbox_cf.SetLabel(_(' Cliente '))
        self.tbl = "ord1"
        #self.t_cpart.SetValue("C") # valore tipo contro partita
        self.vPDC.SetValue("7501")
        self.vPDC_SC.SetValue("6105")
        self.UM.SetValue("PZ")
        self.vALIVA.SetValue("20")
        self.vIMBAL.SetValue("IMBVS")
        self.vCONFE.SetValue("CFSF")
        if (self.tcpart=="C"): self.sbox_cf.SetLabel(_(' Cliente '))
        if (self.tcpart=="F"): self.sbox_cf.SetLabel(_(' Fornitore '))
        if self.vPAGAM.GetValue()=="" :
            self.vPAGAM.SetValue(cfg.tipopagam)
            self.sPAGAM = ""
        if self.vPAGAM.GetValue()=='PAG23':
            self.lprezzo_ac1.SetLabel(_('Importo Finanziamento :'))
        else:self.lprezzo_ac1.SetLabel(_(' Saldo alla consegna :'))
        self.SelCOMBO(self)
        self.cntr = ""
        self.cntr_row = ""
        self.row = 0
        self.ShowFalse(self)
        self.EnableFalse(self)
        self.new.Enable(True)
        self.indiriz.Show(True)
        self.cap.Show(True)
        self.zona.Show(True)      
        self.pr.Show(True)
        self.codcf.Show(True)
        self.ragsoc1.Show(True)
        #self.ragsoc2.Show(True)
        self.cragsoc1.Show(True) 
        self.indiriz1.Show(True)       
        if self.ccodbar.GetValue()==0:
            self.codart.Show(True)
            self.codbar.Show(False)            
        else:
            self.codart.Show(False) 
            self.codbar.Show(True)
        if (self.rec!=""):
            self.num_ord.SetValue(self.rec)
            self.FndOrd(self)
        if self.tcpart=='F':
            self.lcosto.Show(False)
            self.costo.Show(False)
            #self.lprovv.Show(False)
            #self.provv.Show(False)                 
        self.ntbk.SetFocus() 
        self.ntbk.SetSelection(0)	
        #self.rbEVASO.SetValue(False)	
        #self.rbEVASO.Enable(False)
        #self.rbCONFER.SetValue(False)
        #self.rbPREVIS.SetValue(True)
        self.oldnum_ord = ""
        self.oldvTIPO_ORD = ""
        self.provv.Show(False)
        self.lprovv.Show(False)
        if self.tipoord=="OC": 
            self.sTIPO_ORD = 'OC'
            self.stt_ord1.SetValue("C")
            self.stt_ord2.SetValue("C")
        if self.tipoord=="OF": 
            self.sTIPO_ORD = 'OF'
            self.stt_ord1.SetValue("C")
            self.stt_ord2.SetValue("C")
        if self.tipoord=="PF": 
            self.sTIPO_ORD = 'PF'
            self.stt_ord1.SetValue("P")
            self.stt_ord2.SetValue("P")
        if self.tipoord=="PC": 
            self.sTIPO_ORD = 'PC'
            self.stt_ord1.SetValue("P")
            self.stt_ord2.SetValue("P")
        self.SelRadioB(self)


    def EnableFalse(self, evt):
        self.ccodinfo.Enable(False)    
        self.skanag.Enable(False)
        self.csaldo.Enable(False)
        self.cdest.Enable(False)
        self.rdest1.Enable(False)          
        self.indiriz1.Enable(False)
        self.zona1.Enable(False)
        self.pr1.Enable(False)
        self.cap1.Enable(False)
        self.localit1.Enable(False)
        self.stato1.Enable(False)     
        self.indiriz.Enable(False)
        self.zona.Enable(False)
        self.pr.Enable(False)
        self.cap.Enable(False)
        self.localit.Enable(False)
        self.stato.Enable(False)
        self.ragsoc3.Enable(False)
        self.ragsoc4.Enable(False)
        self.codcf1.Enable(False)
        self.anno.Enable(False)
        self.conse.Enable(False)
        self.clst.Enable(False)
        self.vDIVvend.Enable(False)
        self.lst.Enable(False)
        self.PRIO.Enable(False)
        self.vPRIO.Enable(False)        
        self.trasp.Enable(False)
        self.rag_ord.Enable(False)        
        self.codcf.Enable(False)       
        self.ccodcf.Enable(False)        
        self.ragsoc1.Enable(False)
        self.cragsoc1.Enable(False)
        self.ragsoc2.Enable(False)     
        self.vTIPO_ORD.Enable(False)       
        #self.note.Enable(False)
        self.cmpiliberi.Enable(False)        
        self.campo1.Enable(False)
        self.campo2.Enable(False)     
        self.ragsoc1age.Enable(False)
        self.vsrif.Enable(False)
        self.nsrif.Enable(False)    
        self.vs_ord.Enable(False)
        self.vs_data.Enable(False) 
        self.importo.Enable(False)        
        self.rbCONFER.Enable(False)
        self.rbPREVIS.Enable(False)          
        self.rbEVASO.Enable(False)
        self.vdata_ord.Enable(False)     
        self.cnum_ord.Enable(True)
        self.codmerc.Enable(False)
        self.qt_ord.Enable(False)
        self.qt_con.Enable(False)
        self.qt_eva.Enable(False)
        self.prezzo_ag.Enable(False)
        self.datacons.Enable(False)
        self.colli.Enable(False)
        self.peso.Enable(False)        
        self.stt_ord1.Enable(False)
        self.stt_ord2.Enable(False)
        self.annodoc.Enable(False)        
        self.tipodoc.Enable(False)
        self.datadoc.Enable(False)
        self.numdoc.Enable(False)
        self.campo2_art.Enable(False)
        self.campo1_art.Enable(False)
        self.totaledoc.Enable(False)        
        self.stampa.Enable(False)
        #self.stampac.Enable(False)
        self.modi.Enable(False)
        self.dele.Enable(False)        
        self.newr.Enable(False)
        self.okart.Enable(False)
        self.modir.Enable(False)
        self.intr.Enable(False)
        self.delr.Enable(False)
        self.ccodart.Enable(False)   
        self.ctesto.Enable(False) # personalizza testo
        self.PAGAM.Enable(False)
        self.vPAGAM.Enable(False)
        self.codage.Enable(False)
        self.ccodage.Enable(False)
        #self.note.SetBackgroundColour(self.color)
        self.note.Enable(False)
        #self.note_calce.SetBackgroundColour(self.color)
        self.note_calce.Enable(False)
        self.scf1.Enable(False)
        self.scf2.Enable(False)
        self.scf3.Enable(False)
        self.tot_colli.Enable(False)
        self.tot_peso.Enable(False)
        self.vASPET.Enable(False)
        self.cASPET.Enable(False)
        self.dASPET.Enable(False)
        self.vCONSEG.Enable(False)
        self.vPDC.Enable(False)
        self.vPDC_SC.Enable(False)
        self.cvPDC.Enable(False)
        self.cvPDC_SC.Enable(False)           
        self.prezzo_ac.Enable(False)
        self.prezzo_ac1.Enable(False)
        self.campo2_calce.Enable(False)
        self.campo1_calce.Enable(False)

    def ShowFalse(self, evt):
        self.ragsoc3.Show(False)
        self.ragsoc4.Show(False)
        self.cragsoc3.Show(False)           
        self.localit1.Show(False)
        self.stato1.Show(False)
        self.localit.Show(False)
        self.stato.Show(False)
        self.indiriz1.Show(False)
        self.cap1.Show(False)
        self.zona1.Show(False)      
        self.pr1.Show(False)
        self.codcf1.Show(False)
        self.ragsoc2.Show(False)
        self.ragsoc4.Show(False)  
        #self.note.Show(False)        
        #self.ragsoc1age.Show(False)         
        #self.vdata_ord.Show(False)        
        self.vTIPO_ORD.Show(False)
        self.fndvTIPO_ORD.Show(False)	
        self.vDIVvend.Show(False)
        self.vPRIO.Show(False)
        self.conse.Show(False)
        self.trasp.Show(False)
        self.cod_vet.Show(False)
        self.rag_ord.Show(False)
        self.campo1.Show(False)
        self.campo2.Show(False)
        self.vdata_ord.Show(False)
        #self.sc1.Show(False)   
        self.sc2.Show(False)
        self.sc3.Show(False)
        self.nriga.Show(False)
        #self.lvolume.Show(False)
        #self.lpeso.Show(False)        
        #self.volume.Show(False)
        #self.peso.Show(False)
        #self.vPDC.Show(False)
        self.dALIVA.Show(False)
        self.vUM.Show(False)
        self.vMERCE.Show(False)
        self.vinprod.Show(False)
        #self.vALIVA.Show(False)
        self.vIMBAL.Show(False)
        self.vCONFE.Show(False) 
        self.prezzo1.Show(False)
        self.prezzo2.Show(False)
        self.importo.Show(False)   
        self.stt_ord1.Show(False)
        self.stt_ord2.Show(False)
        self.codmerc.Show(False)
        self.qt_ord.Show(False)
        self.qt_con.Show(False)
        self.qt_eva.Show(False)
        self.prezzo_ag.Show(False)
        self.datacons.Show(False)
        #self.colli.Show(False)
        self.peso.Show(False)
        self.annodoc.Show(False)        
        self.tipodoc.Show(False)
        self.datadoc.Show(False)
        self.numdoc.Show(False)
        self.campo2_art.Show(False)
        self.campo1_art.Show(False)
        self.ok.Show(False)
        self.canc.Show(True)
        self.oktestata.Show(False)
        self.new.Show(True)
        self.modi.Show(True)        
        self.dele.Show(False)
        self.vPAGAM.Show(False)
        self.vCONSEG.Show(False)
        self.campo2_calce.Show(False)
        self.campo1_calce.Show(False)
        self.inte.Show(False)
        
    def CDest(self, evt):
        if self.cdest.GetLabel()== _('Destinatario'):  ########
            self.cdest.SetLabel(_(' Cliente '))
            self.sbox_cf.SetLabel(_(' Destinatario '))
            self.lragsoc.SetLabel(_("Destinazione merce :"))
            self.codcf.Show(False)
            self.codcf1.Show(True)    
            self.ragsoc1.Show(False)
            self.cragsoc1.Show(False) 
            self.indiriz1.Show(True)
            self.ragsoc3.Show(True)
            self.ragsoc3.Enable(True)          
            self.cragsoc3.Show(True)
            self.cap1.Show(True)
            self.zona1.Show(True) 
            self.pr1.Show(True)     
            self.indiriz.Show(False)
            self.cap.Show(False)
            self.zona.Show(False)       
            self.pr.Show(False)
            self.rdest1.Enable(True)
            self.ragsoc3.SetFocus()
        else:
            self.cdest.SetLabel(_('Destinatario'))
            self.sbox_cf.SetLabel(_(' Cliente '))
            self.lragsoc.SetLabel(_("Cessionario :"))
            self.codcf.Show(True)
            self.codcf1.Show(False)            
            self.ragsoc1.Show(True)
            self.cragsoc1.Show(True) 
            self.indiriz1.Show(True)
            self.ragsoc3.Show(False)
            self.ragsoc3.Enable(False)          
            self.cragsoc3.Show(False) 
            self.indiriz.Show(True)
            self.cap.Show(True)
            self.zona.Show(True)     
            self.pr.Show(True)
            self.indiriz1.Show(False)
            self.cap1.Show(False)
            self.zona1.Show(False)       
            self.pr1.Show(False)
            #self.localit1.Show(False)         
            #self.stato1.Show(False)      
            self.rdest1.Enable(False)
            self.ragsoc1.SetFocus()
         
    def RDest(self, evt):
        self.ragsoc3.SetValue('')
        self.ragsoc4.SetValue('')
        self.indiriz1.SetValue('')
        self.zona1.SetValue('')
        self.localit1.SetValue('')
        self.cap1.SetValue('')
        self.pr1.SetValue('')
        self.stato1.SetValue('')
        self.codcf1.SetValue('')        
        self.ragsoc3.SetFocus()
     
    def SelCodBar(self, evt):
        if self.ccodbar.GetValue()==0 :
            self.ccodbar.SetToggle(False)
            self.codart.Show(True)
            self.codbar.Show(False)
            self.lcod.SetLabel(_("Codice :"))
            self.codart.SetFocus()
            self.codbar.SetValue('')
        else:
            self.ccodbar.SetToggle(True)
            self.codart.Show(False)
            self.codbar.Show(True)
            self.lcod.SetLabel(_("BarCod:"))
            self.codbar.SetFocus()
            self.codart.SetValue('')
   
    def SelRadioB(self, evt):
        if (self.stt_ord1.GetValue()=="P"):
            self.stt_ord1.SetValue("P")
            self.stt_ord2.SetValue("P")
            self.rbPREVIS.SetValue(True)
            self.rbCONFER.SetValue(False)
            self.rbEVASO.SetValue(False) 
        elif (self.stt_ord1.GetValue()=="C"):
            self.stt_ord2.SetValue("C")
            self.rbPREVIS.SetValue(False)
            self.rbCONFER.SetValue(True)
            self.rbEVASO.SetValue(False) 
        elif (self.stt_ord1.GetValue()=="E"):
            self.stt_ord2.SetValue("E")
            self.rbPREVIS.SetValue(False)
            self.rbCONFER.SetValue(False)
            self.rbEVASO.SetValue(True) 
        #elif (self.stt_ord1.GetValue()=="G"):
        #    self.stt_ord2.SetValue("G")
        #    self.rbPREVIS.SetValue(False)
        #    self.rbCONFER.SetValue(False)
        #    self.rbEVASO.SetValue(True) 	

    def RadioB(self, evt):
        if self.rbPREVIS.GetValue()==True:
            self.stt_ord1.SetValue("P")
            self.stt_ord2.SetValue("P")
        if self.rbEVASO.GetValue()==True:
            self.stt_ord1.SetValue("E")
            self.stt_ord2.SetValue("E")
        elif self.rbCONFER.GetValue()==True:
            self.stt_ord1.SetValue("C")
            self.stt_ord2.SetValue("C")
            self.New(self)#modifica
            
    def IntTestata(self, evt):
        if(self.voktestata==1):
            dlg = wx.MessageDialog(self, cfg.msgint, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
            if dlg.ShowModal()==wx.ID_YES:
                self.rec = ""
                self.Start(self)
                self.cdest.SetLabel(_(' Cliente '))
                self.CDest(self)
            else:
                dlg.Destroy()
        else:
            self.rec = ""
            self.stt_ord1.SetValue("")
            self.stt_ord2.SetValue("")
            self.Start(self)
            self.cdest.SetLabel(_(' Cliente '))
            self.CDest(self)

    def NewTxt(self, evt):
        self.OnAnagTxt(self)
        self.TIPO_ORD.Enable(False)
        self.num_ord.Enable(False)
        self.cnum_ord.Enable(False)
        self.data_ord.Enable(True)
        self.data_ord.SetFocus()
        self.new.Show(False)
        self.ok.Show(False)
        self.oktestata.Show(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.modi.Enable(False)

    def ModiTxt(self, evt):
        self.OnAnagTxt(self)
        self.cntr = "modi"
        self.TIPO_ORD.Enable(False)        
        self.num_ord.Enable(False)
        self.cnum_ord.Enable(False)
        self.data_ord.Enable(True)
        self.data_ord.SetFocus()
        self.new.Show(False)
        self.ok.Show(False)
        self.oktestata.Show(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.modi.Enable(False)
        self.modi.Show(False)
        self.dele.Show(True)
        self.dele.Enable(True)
        
    def KillFcs_colli(self, evt):
        self.qt.SetFocus()	   
    
    def KillFcs_vs_ord(self, evt):
        self.vs_data.SetFocus()
        
    #def KillFcs_vsdata(self, evt):
    #    self.ragsoc1.SetFocus()

    def KillFcs_note(self, evt):
        self.codage.SetFocus()
        
    def KillFcs_vsrif(self, evt):
        self.nsrif.SetFocus()

    def KillFcs_nsrif(self, evt):
        self.note.SetFocus()

    def KillFcs_PAGAM(self, evt):
        self.oktestata.SetFocus()

    def CntvsData(self, evt):
        if (self.cntr=="new" or self.cntr=="modi"):
            cnt_gma = 0
            vsdata = self.vs_data.GetValue().strip()
            if vsdata !="":
                gma = vsdata.split('/')
                try:
                    if (gma[0].isdigit()!=True):
                        self.Message(cfg.msgdatano ,self.ttl)
                    elif (gma[1].isdigit()!=True):
                        self.Message(cfg.msgdatano ,self.ttl)
                    elif (gma[2].isdigit()!=True):
                        self.Message(cfg.msgdatano ,self.ttl)
                except:
                    self.Message(cfg.msgdatano ,self.ttl)
                
                if len(gma)==3:
                    gg = int(gma[0])
                    mm = int(gma[1])
                    aa = int(gma[2])
                    if gg > 0 and gg < 31:
                        cnt_gma+=1
                        if mm>=0 and mm<=12:
                            cnt_gma+=1
                            if aa<=int(self.annoc) :
                                cnt_gma+=1
                    if cnt_gma!=3: self.Message(cfg.msgdatano ,self.ttl)
                    if cnt_gma==3: self.ragsoc1.SetFocus()
            else:self.ragsoc1.SetFocus()

    def CntData(self, evt):
        if (self.cntr=="new" or self.cntr=="modi"):    
            data_ord = self.data_ord.GetValue().strip()
            cnt_gma = 0
            gma = data_ord.split('/')
            try:
                if (gma[0].isdigit()!=True):
                    self.Message(cfg.msgdatano ,self.ttl)
                elif (gma[1].isdigit()!=True):
                    self.Message(cfg.msgdatano ,self.ttl)
                elif (gma[2].isdigit()!=True):
                    self.Message(cfg.msgdatano ,self.ttl)
            except:
                self.Message(cfg.msgdatano ,self.ttl)
            if len(gma)==3:
                gg = int(gma[0])
                mm = int(gma[1])
                aa = int(gma[2])
                if gg > 0 and gg<=31:
                    cnt_gma+=1
                    if mm>=0 and mm<=12:
                        cnt_gma+=1
                        if aa==int(self.annoc):
                            cnt_gma+=1
                            vdata_ord = self.vdata_ord.GetValue()
                            vgma  = vdata_ord.split('/')
                            vgg = int(vgma[0])
                            vmm = int(vgma[1])
                            vaa = int(vgma[2])
                            vdata  = int(vgma[2] + vgma[1] + vgma[0])
                            data = int(gma[2] + gma[1] + gma[0])
                            self.vs_ord.SetFocus()
                            if data < vdata :
                                dlg = wx.MessageDialog(self,cfg.msgdatault ,
                                    self.ttl, wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                                if dlg.ShowModal()==wx.ID_YES:
                                    self.vdata_ord.SetValue(self.data_ord.GetValue())
                                    self.data_ord.Enable(False)
                                    self.num_ord.Enable(False)
                                    dlg.Destroy()
                                else:
                                    self.data_ord.SetFocus()
                                    dlg.Destroy()
                            else:
                                self.vdata_ord.SetValue(self.data_ord.GetValue())
                                self.data_ord.Enable(False)
                                self.num_ord.Enable(False)
                if cnt_gma==2 and aa <> int(self.annoc):
                    self.Message(cfg.msgdataes  +  self.annoc,self.ttl)            
                elif cnt_gma!=3 : self.Message(cfg.msgdatano ,self.ttl)
           
    def EvtChar(self, evt):
        evt_char = evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()

    def EvtCharS(self, evt):
        evt_char = evt.GetKeyCode()
        if evt_char==49: 
            self.ntbk.SetSelection(0)
            if (self.cntr=="new" or self.cntr=="modi") : self.ok.SetFocus()
        if evt_char==50: 
            self.ntbk.SetSelection(1)
            self.ntbk.SetFocus()
        if evt_char==51: self.ntbk.SetSelection(2)
        evt.Skip() 

    def OffAnagTxt(self, evt):
        self.num_ord.Enable(False)
        self.cnum_ord.Enable(False)
        self.data_ord.Enable(False)
        self.vs_ord.Enable(False)
        self.vs_data.Enable(False)  
        self.rbCONFER.Enable(False)
        self.rbPREVIS.Enable(False)


    def OnAnagTxt(self ,evt):
        self.codage.Enable(True)
        self.ccodage.Enable(True)
        self.nsrif.Enable(True)
        self.vsrif.Enable(True)
        self.vs_ord.Enable(True)
        self.vs_data.Enable(True)
        self.ragsoc1.Enable(True)      
        self.cragsoc1.Enable(True)
        self.note.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.note.Enable(True)
        self.PAGAM.Enable(True)
        self.rbCONFER.Enable(True)
        self.rbPREVIS.Enable(True)
        self.cdest.Enable(True)
        
    def DelAnagTxt(self, evt):
        self.num_ord.SetValue('')
        self.vdata_ord.SetValue('')
        self.data_ord.SetValue('')
        self.vs_ord.SetValue('')
        self.vs_data.SetValue('')
        self.codcf.SetValue('')
        self.codcf1.SetValue('')
        self.codage.SetValue('')
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.indiriz.SetValue('')
        self.zona.SetValue('')
        self.localit.SetValue('')
        self.cap.SetValue('')
        self.pr.SetValue('')
        self.stato.SetValue('')
        self.ragsoc3.SetValue('')
        self.ragsoc4.SetValue('')
        self.indiriz1.SetValue('')
        self.zona1.SetValue('')
        self.localit1.SetValue('')
        self.cap1.SetValue('')
        self.pr1.SetValue('')
        self.stato1.SetValue('')      
        self.note.SetValue('')
        self.note_calce.SetValue('')        
        self.sc2.SetValue('0,00')
        self.scf1.SetValue('0,00')
        self.scf2.SetValue('0,00')
        self.scf3.SetValue('0,00')        
        vPAGAM = self.vPAGAM.GetValue()
        if vPAGAM=="" :
            self.vPAGAM.SetValue(cfg.tipopagam)
            self.sPAGAM = ""      
        self.vPDC.SetValue('7501')
        self.vPDC_SC.SetValue('6105')
        self.vALIVA.SetValue("20")
        self.dALIVA.SetValue(_("Aliquota 20%"))
        #self.reg_def.SetValue('N')
        self.vsrif.SetValue('')
        self.nsrif.SetValue('')
        self.ragsoc1age.SetValue('')
        self.prezzo_ac.SetValue('0,00')
        self.prezzo_ac1.SetValue('0,00')
        self.prezzo_ag.SetValue('0,00')
        self.totale.SetValue('0,00')
        self.provv.SetValue('0,00')
        self.colli.SetValue('0,00')
        self.peso.SetValue('0,00')        
        self.tot_colli.SetValue('0,00')
        self.tot_peso.SetValue('0,00')
        self.totaledoc.SetValue('0,00')

        
    def SelCOMBO(self, evt):      
        vPAGAM = self.vPAGAM.GetValue()
        self.PAGAM.Clear()
        vTIPO_ORD = self.vTIPO_ORD.GetValue()
        self.TIPO_ORD.Clear()
        sql = """ select * from tabgen """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)                 
            while (1):
                row = cr.fetchone () 
                if row==None: 
                    break          
                if (row[0]=="PAGAM"):
                    if (row[1]==vPAGAM):self.sPAGAM = row[2]
                    self.PAGAM.Append(row[2],row[1])
                if (row[0]=="TIPOORD"):
                    if (row[1]==vTIPO_ORD):self.sTIPO_ORD = row[2]
                    self.TIPO_ORD.Append(row[2],row[1])
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," SelCOMBO tabgen Error %s" % (msg))
        self.CnAz.commit()
                               
        cntPAGAM = 0
        cntPAGAM = self.PAGAM.FindString(self.sPAGAM)
        self.PAGAM.Select(cntPAGAM)
        cntTIPO_ORD = 0
        cntTIPO_ORD = self.TIPO_ORD.FindString(self.sTIPO_ORD)
        self.TIPO_ORD.Select(cntTIPO_ORD)

    def SelPAGAM(self, evt):
        self.Sel(evt)
        self.vPAGAM.SetValue(self.cb_val)
        if self.vPAGAM.GetValue()=='PAG23':
            self.lprezzo_ac1.SetLabel(_('Importo Finanziamento :'))
        else:self.lprezzo_ac1.SetLabel(_(' Saldo alla consegna :'))
        
    def SelTIPO_ORD(self, evt):
        self.Sel(evt)
        self.vTIPO_ORD.SetValue(self.cb_val)

    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str =  evt.GetString()
        evt.Skip()
        #self.SetClientSize(wx.Size(680, 425))

    def SetFcs(self, evt):
        evt.Skip()
        
    #def KillFcs_qt(self, evt):
    #    vqt = self.qt.GetValue().replace(",","")
    #    if (vqt.isdigit()!=True):
    #        self.Message(cfg.msgqtno,self.ttl)
    #        self.qt.SetFocus()
    #    #evt.Skip()

    def KillFcs_des(self, evt):
        if self.codart.GetValue()=='':
            self.descriz.SetValue(self.descriz.GetValue().upper())  
        
    #def KillFcs_prezzo(self, evt):
    #    vprezzo = self.prezzo.GetValue().replace(",","")  
    #    if (vprezzo.isdigit()!=True):
    #        self.Message(cfg.msgprezno,self.ttl)
    #        self.prezzo.SetFocus()
      
    #def KillFcs_sc1(self, evt):
    #    vsc1 = self.sc1.GetValue().replace(",","")
    #    if (vsc1.isdigit()!=True):
    #        self.Message(cfg.msgscno,self.ttl)
    #        self.sc1.SetFocus()
        
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()
            
    def LstSlct(self, evt):      
        self.currentItem = evt.m_itemIndex
        self.codart.SetValue(self.lc.GetItemText(self.currentItem))
        self.descriz.SetValue(self.getColTxt(self.currentItem, 1))
        self.qt.SetValue(self.getColTxt(self.currentItem, 2))
        self.prezzo.SetValue(self.getColTxt(self.currentItem, 3))
        self.sc1.SetValue(self.getColTxt(self.currentItem, 4))
        self.importo.SetValue(self.getColTxt(self.currentItem, 5))
        self.vALIVA.SetValue(self.getColTxt(self.currentItem, 6))
        self.UM.SetValue(self.getColTxt(self.currentItem, 7))
        self.mis.SetValue(self.getColTxt(self.currentItem, 8))
        self.nriga.SetValue(self.getColTxt(self.currentItem, 9))
        self.codbar.SetValue(self.getColTxt(self.currentItem, 10))
        self.codmerc.SetValue(self.getColTxt(self.currentItem, 11))
        self.qt_ord.SetValue(self.getColTxt(self.currentItem, 12))
        self.qt_con.SetValue(self.getColTxt(self.currentItem, 13))
        self.qt_eva.SetValue(self.getColTxt(self.currentItem, 14))
        self.prezzo_ag.SetValue(self.getColTxt(self.currentItem, 15))
        self.sc2.SetValue(self.getColTxt(self.currentItem, 16))
        self.sc3.SetValue(self.getColTxt(self.currentItem, 17))
        self.provv.SetValue(self.getColTxt(self.currentItem, 18))
        self.datacons.SetValue(self.getColTxt(self.currentItem, 19))
        self.colli.SetValue(self.getColTxt(self.currentItem, 20))
        self.peso.SetValue(self.getColTxt(self.currentItem, 21))
        self.lst.SetValue(self.getColTxt(self.currentItem, 22))
        self.vPDC.SetValue(self.getColTxt(self.currentItem, 23))
        self.stt_ord2.SetValue(self.getColTxt(self.currentItem, 24))
        self.annodoc.SetValue(self.getColTxt(self.currentItem, 25))        
        self.tipodoc.SetValue(self.getColTxt(self.currentItem, 26))
        self.datadoc.SetValue(self.getColTxt(self.currentItem, 27))
        self.numdoc.SetValue(self.getColTxt(self.currentItem, 28))
        self.campo1_art.SetValue(self.getColTxt(self.currentItem, 29))
        self.campo2_art.SetValue(self.getColTxt(self.currentItem, 30))
        self.row = self.currentItem
        self.SelRow(self)
        
    def LstAct(self, evt):
        self.SelRow(self)
        self.currentItem = evt.m_itemIndex

    def FndSelAnag(self, evt):
        row = evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.__MDI__.CnvVM(row[30])
        if(self.__MDI__.val==""):self.__MDI__.val = "0"
        self.sc1.SetValue(self.__MDI__.val)             
        self.__MDI__.CnvVM(row[31])
        self.sc2.SetValue(self.__MDI__.val)
        self.indiriz.SetValue(str(row[6]).title())
        cap = string.zfill(str(row[7]).strip(),5)
        self.cap.SetValue(cap)        
        self.zona.SetValue(str(row[8]).title())
        self.localit.SetValue(str(row[9]))
        self.pr.SetValue(str(row[10]).strip().upper())
        self.stato.SetValue(str(row[11]).strip().upper())
        if (self.cntr!="new"):
            self.indiriz1.SetValue(str(row[12]).title())
            cap1 = string.zfill(str(row[7]).strip(),5)
            self.cap1.SetValue(cap1)        
            self.zona1.SetValue(str(row[14]).title())
            self.localit1.SetValue(str(row[15]))
            self.pr1.SetValue(str(row[16]).strip().upper())
            self.stato1.SetValue(str(row[17]).strip().upper())                      
        self.sTIPO_ORD = self.tipoord
        self.vPAGAM.SetValue(str(row[41]))
        if self.vPAGAM.GetValue()=="":
            self.vPAGAM.SetValue(cfg.tipopagam)
            self.sPAGAM = ""
        #self.note.SetValue(row[29])
        #self.reg.SetValue(row[30])
        self.SelCOMBO(self)
        self.OffAnagTxt(self)
        self.rbCONFER.Enable(False)
        self.rbPREVIS.Enable(False)
        if (self.cntr=="modi"):
            self.skanag.Enable(True)
            self.inte.Show(True)
            self.dele.Show(False)
            self.dele.Enable(False)            
            self.modi.Show(True)
            self.modi.Enable(True)
            self.modi.SetFocus()
            
        if (self.cntr=="new"):
            self.codage.SetValue(str(row[38]))            
            if self.codage.GetValue()!="": self.FndAge(self)
            self.canc.Show(False)
            self.inte.Show(True)
            self.new.Show(False)
            self.oktestata.SetFocus()
            self.dele.Show(False)
            self.dele.Enable(False)            
            self.modi.Show(True)
            self.modi.Enable(False)  
        self.vsrif.SetFocus()
        
    def FndALIVA(self, evt):
        val = self.vALIVA.GetValue()
        cod =  "ALIVA"
        cnt_rec = 0
        sql = """ select * from tabgen where cod = "%s" and valore like "%s" """
        valueSql = cod, '%' + val + '%'
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndALIVA Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.dALIVA.SetValue(row[2])
            self.qt.SetFocus()
        elif (cnt_rec>1):
            try:
                import srctabg
            except :
                pass
            try:
                import base.srctabg
            except :
                pass
            control = ['Ricerca Cod. IVA',self.vALIVA,self.dALIVA,self.FndSelALIVA,'ALIVA']     
            win = srctabg.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

    def FndSelALIVA(self, evt):
        val = self.vALIVA.GetValue()
        cod =  "ALIVA"
        cnt_rec = 0
        sql = """ select * from tabgen where cod = "%s" and valore = "%s" """
        valueSql = cod, val
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndSelALIVA Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.dALIVA.SetValue(row[2])
            self.qt.SetFocus()
        else:self.FndALIVA(self)

    def FndSelOrd(self, evt):
        if self.cntr=="new" :
            self.EnableFalse(self)
            self.oktestata.Show(False)
            self.new.Show(True)
        self.stampa.Enable(True)
        row = evt
        self.vTIPO_ORD.SetValue(str(row[0]))
        self.anno.SetValue(str(row[1]))
        self.num_ord.SetValue(str(row[2]))
        self.vdata_ord.SetValue(str(row[3]))
        self.data_ord.SetValue(str(row[3]))
        self.codcf.SetValue(str(row[4]))
        self.ragsoc1.SetValue(str(row[5]))
        self.ragsoc2.SetValue(str(row[6]))
        self.indiriz.SetValue(str(row[7]))
        cap = string.zfill(str(row[8]).strip(),5)
        self.cap.SetValue(cap)
        self.zona.SetValue(str(row[9]))
        self.localit.SetValue(str(row[10]))
        self.pr.SetValue(str(row[11]))
        self.stato.SetValue(str(row[12]))
        self.__MDI__.CnvNone(row[13])
        self.codcf1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[14]) 
        self.ragsoc3.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[15]) 
        self.ragsoc4.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[16])        
        self.indiriz1.SetValue(self.__MDI__.val)
        if row[17]=='' or row[17]==None:
            self.cap1.SetValue('')
        else:
            cap1 = string.zfill(str(row[17]).strip(),5)
            self.cap1.SetValue(cap1)
        self.__MDI__.CnvNone(row[18])
        self.zona1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[19])
        self.localit1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[20])
        self.pr1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[21])
        self.stato1.SetValue(self.__MDI__.val)
        self.stt_ord1.SetValue(str(row[22])) 
        self.lst.SetValue(str(row[23]))
        self.vs_ord.SetValue(str(row[24]))
        self.vs_data.SetValue(str(row[25]))     
        self.vDIVvend.SetValue(str(row[26]))
        codage = str(row[27])
        self.codage.SetValue(codage)
        if (codage!=""): self.FndAge(self)
        self.vPRIO.SetValue(str(row[28]))        
        self.vPAGAM.SetValue(str(row[29]))
        self.vCONSEG.SetValue(str(row[30]))
        self.trasp.SetValue(str(row[31]))
        self.cod_vet.SetValue(str(row[32]))
        self.vsrif.SetValue(str(row[33]))
        self.nsrif.SetValue(str(row[34]))
        self.rag_ord.SetValue(str(row[35]))        
        self.campo1.SetValue(str(row[36]))
        self.campo2.SetValue(str(row[37]))
        self.note.SetValue(str(row[38]))
        self.vASPET.SetValue(str(row[39]))
        #self.tot_colli.SetValue(str(row[40]))
        #self.tot_peso.SetValue(str(row[41]))        
        #self.scf1.SetValue(str(row[42]))        
        #self.scf2.SetValue(str(row[43]))  
        #self.scf3.SetValue(str(row[44]))
        self.tot_colli.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(row[41])
        self.tot_peso.SetValue(self.__MDI__.val) 
        self.__MDI__.CnvVM(row[42])
        self.scf1.SetValue(self.__MDI__.val)  
        self.__MDI__.CnvVM(row[43])
        self.scf2.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(row[44])
        self.scf3.SetValue(self.__MDI__.val)
        self.vPDC_SC.SetValue(str(row[45]))
        self.prezzo_ac.SetValue(str(row[46]))    
        self.prezzo_ac1.SetValue(str(row[47]))
        self.campo1_calce.SetValue(str(row[48]))  
        self.campo2_calce.SetValue(str(row[49]))  
        self.note_calce.SetValue(str(row[50]))
        self.SelCOMBO(self)
        self.FndOrdCorpo(self)
        self.TIPO_ORD.Enable(False)
        self.num_ord.Enable(False)
        self.data_ord.Enable(False)
        self.new.Enable(False)
        self.canc.Show(False)
        self.inte.Show(True)	
        self.SelRadioB(self)
        if self.stt_ord1.GetValue()=="P" or self.stt_ord1.GetValue()=="C":
            self.skanag.Enable(True)
            self.modi.Enable(True)
            self.modi.SetFocus()
        else:
            self.Message(cfg.msgordicons,self.ttl)
            self.inte.SetFocus()
        
    def FndOrd(self, evt):
        fndvTIPO_ORD = self.fndvTIPO_ORD.GetValue()   
        vnumord = self.num_ord.GetValue()
        #if num_ord=="" :
            #self.Message(cfg.msgass  + " --> " +  self.tbl,self.ttl)
        if vnumord=='' : vnumord = 0	    
        #else:
        cnt_rec = 0       
        anno = self.anno.GetValue()
        vTIPO_ORD = self.vTIPO_ORD.GetValue()
        if fndvTIPO_ORD!="" and self.rec=="":
            sql = """ select * from ordi1
                    where num_ord = "%s" and tipo_ord = "%s" 
                    and anno = "%s" """
            valueSql = int(vnumord), fndvTIPO_ORD, anno
        elif self.rec!="":
            sql = """ select * from ordi1
                    where num_ord = "%s" and tipo_ord = "%s" 
                    and anno = "%s" """
            valueSql = int(vnumord), vTIPO_ORD, anno
        elif int(vnumord) != 0 :
            sql = """ select * from ordi1
                    where tipo_ord = "%s" and num_ord = "%s" and anno = "%s" """
            valueSql = vTIPO_ORD, int(vnumord), anno
        else :
            sql = """ select * from ordi1
                    where tipo_ord = "%s" and anno = "%s" """
            valueSql = vTIPO_ORD, anno
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            ####if rows==[] and vnumord!=0:
            ####    self.Message(cfg.msgass + self.tbl,self.ttl)
            cnt_rec=len(rows)
            ####for row in rows:
            ####    cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndOrd Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0): self.Message(cfg.msgass +" --> ",self.ttl)
        elif (cnt_rec==1): self.FndSelOrd(rows[0])                                        
        #elif (cnt_rec>1):
        else :
            import srcord  
            stt_ord = ''
            self.fndvTIPO_ORD.SetValue('')
            control = [self.vTIPO_ORD, self.anno, self.num_ord,
                self.vdata_ord, self.FndOrd, stt_ord, self.fndvTIPO_ORD]   
            win = srcord.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)	   
        ####elif(self.cntr=="new"): self.data_ord.SetFocus() 
        #elif (cnt_rec==0 ):
            #self.Message(cfg.msgass  + " --> " +  self.tbl,self.ttl)
	

    def FndOrdCorpo(self, evt):
        rowlc = 0
        cnt_rec = 0
        num_ord = self.num_ord.GetValue()
        anno = self.anno.GetValue()
        vTIPO_ORD = self.vTIPO_ORD.GetValue()
        sql = """ select * from ordi2 where num_ord = "%s"
                and tipo_ord = "%s" and anno = "%s" 
                order by num_rig desc    """
        valueSql = int(num_ord), vTIPO_ORD, anno
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows: 
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()     
                    self.__MDI__.CnvVM(row[11])
                    qt_ord = self.__MDI__.val
                    self.__MDI__.CnvVM(row[12])
                    qt_con = self.__MDI__.val
                    self.__MDI__.CnvVM(row[13])
                    qt_eva = self.__MDI__.val
                    self.__MDI__.CnvVM5(row[14])
                    prezzo = self.__MDI__.val
                    self.__MDI__.CnvVM(row[18])
                    sc1 = self.__MDI__.val
                    if (sc1==""):sc1 = "0,0"
                    self.__MDI__.CnvVM(row[19])
                    sc2 = self.__MDI__.val
                    self.__MDI__.CnvVM(row[20])
                    sc3 = self.__MDI__.val
                    self.__MDI__.CnvVM(row[16])
                    tot_riga = self.__MDI__.val
                    self.lc.InsertStringItem(rowlc, row[5])
                    self.lc.SetStringItem(rowlc, 1, row[8])
                    self.lc.SetStringItem(rowlc, 2, qt_ord)
                    self.lc.SetStringItem(rowlc, 3, prezzo)
                    self.lc.SetStringItem(rowlc, 4, sc1)
                    self.lc.SetStringItem(rowlc, 5, tot_riga)
                    self.lc.SetStringItem(rowlc, 6, row[17])
                    self.lc.SetStringItem(rowlc, 7, row[9])        
                    self.lc.SetStringItem(rowlc, 8, row[10])
                    self.lc.SetStringItem(rowlc, 9, str(row[4]))
                    self.lc.SetStringItem(rowlc, 10, str(row[6]))
                    self.lc.SetStringItem(rowlc, 11, row[7])
                    self.lc.SetStringItem(rowlc, 12, qt_ord)
                    self.lc.SetStringItem(rowlc, 13, qt_con)
                    self.lc.SetStringItem(rowlc, 14, qt_eva)
                    self.lc.SetStringItem(rowlc, 15, str(row[15]))
                    self.lc.SetStringItem(rowlc, 16, sc2)        
                    self.lc.SetStringItem(rowlc, 17, sc3)
                    self.lc.SetStringItem(rowlc, 18, str(row[21]))
                    self.lc.SetStringItem(rowlc, 19, str(row[22]))
                    self.lc.SetStringItem(rowlc, 20, str(row[23]))
                    self.lc.SetStringItem(rowlc, 21, str(row[24]))
                    self.lc.SetStringItem(rowlc, 22, str(row[25]))
                    self.lc.SetStringItem(rowlc, 23, str(row[26]))
                    self.lc.SetStringItem(rowlc, 24, str(row[27]))
                    self.lc.SetStringItem(rowlc, 25, str(row[28]))
                    self.lc.SetStringItem(rowlc, 26, str(row[29]))  
                    self.lc.SetStringItem(rowlc, 27, str(row[30]))
                    self.lc.SetStringItem(rowlc, 28, str(row[31]))
                    self.lc.SetStringItem(rowlc, 29, str(row[32]))
                    self.lc.SetStringItem(rowlc, 30, str(row[33]))
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndOrdCorpo Error %s" % (msg))
        self.CnAz.commit()
            
        self.CalcTotale(self)
        
    def Modi(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgmodi_doc, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.ModiTxt(self)
            #self.ntbk.SetFocus()
            dlg.Destroy()
        else:
            self.cntr = ""
            dlg.Destroy()

    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgnodele_doc, self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal()==wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr = ""
            dlg.Destroy()
            
    def Dele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdele_doc,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.cntr = ""
            vTIPO_ORD = self.vTIPO_ORD.GetValue()
            vanno = self.anno.GetValue()
            vnum_ord = self.num_ord.GetValue()
            valueSql = vTIPO_ORD, vanno, int(vnum_ord)
            try:
                cr = self.CnAz.cursor()
                sql = """ delete * from  ordi1 
                        where tipo_ord = "%s" and  anno = "%s" 
                        and  num_ord = "%s" """
                cr.execute(sql % valueSql)
            except StandardError, msg:
                self.__MDI__.MsgErr("ordini"," Dele ordi1 Error %s" % (msg))
            self.CnAz.commit()
            try:
                cr = self.CnAz.cursor()
                sql = """ delete * from  ordi2
                        where tipo_ord = "%s" and  anno = "%s" 
                        and  num_ord = "%s" """
                cr.execute(sql % valueSql)		
            except StandardError, msg:
                self.__MDI__.MsgErr("ordini"," Dele ordi2 Error %s" % (msg))
            self.CnAz.commit()
            self.Start(self)
            dlg.Destroy()
        else:
            self.cntr = ""
            dlg.Destroy()
     
    def OkTestata(self, evt):
        if (self.codcf.GetValue()==""):
            self.Message(cfg.msgnocod,self.ttl)
            self.cdest.SetLabel(_(' Cliente '))
            self.CDest(self)
            self.ragsoc1.SetFocus()
        else:
            self.voktestata = 1
            self.codage.Enable(False)
            self.ccodage.Enable(False)
            self.ragsoc1.Enable(False)
            self.cragsoc1.Enable(False)
            self.ragsoc3.Enable(False)
            self.cragsoc3.Enable(False)
            self.cdest.Enable(False)  
            self.nsrif.Enable(False)
            self.vsrif.Enable(False)
            #self.abi.Enable(False)
            #self.cab.Enable(False)
            #self.banca.Enable(False)
            #self.note.SetBackgroundColour(self.color)
            self.note.Enable(False)
            #self.note_calce.SetBackgroundColour(self.color)
            self.note_calce.Enable(False)
            self.PAGAM.Enable(False)
            self.lc.SetBackgroundColour(wx.Colour(255, 255, 255))
            self.lc.Enable(True)
            self.prezzo_ac.Enable(True)
            self.prezzo_ac1.Enable(True)
            self.csaldo.Enable(True)
            #self.note_calce.Enable(True)
            #if (self.cntr=="modi"):
                #self.LoadOrd(self)
            print self.cntr 
            if (self.cntr=="new" or self.cntr=="modi"):

                self.OffAnagTxt(self)
                self.oktestata.Show(False)
                self.ok.Show(True)
                self.ok.Enable(True)
                self.new.Show(False)
                self.ntbk.SetSelection(1)
                self.newr.Enable(True)
                self.newr.SetFocus()
       
    def FndAge(self, evt):
        cnt = 0
        sql = """ select max(cod) from agenti """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            cnt = cr.fetchone()
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndAge max Error %s" % (msg))
        self.CnAz.commit()
        cnt_rec = 0
        tcpart_age = "A"
        self.ragsoc1age.SetValue("")
        cod = self.codage.GetValue()
        val = self.codage.GetValue()
        #val = self.ragsoc1age.GetValue()
        if cod=="" : cod = 0
        elif (cod.isdigit()!=True): cod = 0
        sql = """ select cod, rag_soc1, provv from agenti 
                where cod = "%s" or rag_soc1 like "%s" """
        valueSql = int(cod), '%' + val.title() + '%'  
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndAge Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0 and cnt[0]>1): cnt_rec=cnt[0]
        if (cnt_rec==0 ): 
            self.PAGAM.SetFocus()
            self.codage.SetValue("")
            self.ragsoc1age.SetValue("")
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAge(row)
        elif (cnt_rec>1):
            try:
                import srcanag
            except :
                pass
            try:
                import base.srcanag
            except :
                pass
            control = ['A',self.codage,self.ragsoc1age,self.FndAge]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
 
    def FndSelAge(self, evt):
        row = evt
        self.codage.SetValue(str(row[0]))
        self.ragsoc1age.SetValue(str(row[1]).title())
        self.__MDI__.CnvVM(row[2])
        self.provv.SetValue(self.__MDI__.val)
        self.PAGAM.SetFocus()

    def FndCodCF(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        cod = self.codcf.GetValue()
        sql = """ select * from anag where cod = "%s" and t_cpart = "%s" """
        valueSql = int(cod), self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1  
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndCodCF Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttlanag)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)

    def FndAnag(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().title()
        cod = self.codcf.GetValue()
        sql = """ select * from anag where rag_soc1 like "%s"
                and t_cpart = "%s" """
        valueSql = '%' + val + '%', self.tcpart	  
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndAnag Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttlanag)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)
        elif (cnt_rec>1):
            try:
                import srcanag
            except :
                pass
            try:
                import base.srcanag
            except :
                pass
            control = [self.tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else:
            self.nsrif.SetFocus()

    def FndSelAnag(self, evt):
        row = evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.__MDI__.CnvVM(row[30])
        if(self.__MDI__.val==""):self.__MDI__.val = "0"
        self.sc1.SetValue(self.__MDI__.val)             
        self.__MDI__.CnvVM(row[31])
        self.sc2.SetValue(self.__MDI__.val)
        if row[12]=='':
            cap = string.zfill(str(row[7]).strip(),5)#'%05s' % row[7]
            if cap=="00000" : cap  = ""
            self.indiriz.SetValue(str(row[6]).title())
            self.zona.SetValue(str(row[8]).title())
            self.localit.SetValue(str(row[9]))
            self.cap.SetValue(cap)
            self.pr.SetValue(str(row[10]).strip().upper())
        else:
            cap = string.zfill(str(row[13]).strip(),5)#'%05s' % row[13]
            if cap=="00000" : cap  = ""
            self.indiriz.SetValue(str(row[12]).title())
            self.zona.SetValue(str(row[14]).title())
            self.localit.SetValue(str(row[15]))
            self.cap.SetValue(cap)
            self.pr.SetValue(str(row[16]).strip().upper())                      
        self.sTIPO_ORD = self.tipoord
        self.vPAGAM.SetValue(str(row[42]))
        if self.vPAGAM.GetValue()=="":
            self.vPAGAM.SetValue(cfg.tipopagam)
            self.sPAGAM = ""
        #self.note.SetValue(row[29])
        #self.reg.SetValue(row[30])
        self.SelCOMBO(self)
        self.OffAnagTxt(self)
        self.rbCONFER.Enable(False)
        self.rbPREVIS.Enable(False)
        if (self.cntr=="modi"):
            self.skanag.Enable(True)
            self.inte.Show(True)
            self.dele.Show(False)
            self.dele.Enable(False)            
            self.modi.Show(True)
            self.modi.Enable(True)
            self.modi.SetFocus()
        if (self.cntr=="new"):
            self.codage.SetValue(str(row[38]))            
            if self.codage.GetValue()!="": self.FndAge(self)
            self.canc.Show(False)
            self.inte.Show(True)
            self.new.Show(False)
            self.oktestata.SetFocus()
            self.dele.Show(False)
            self.dele.Enable(False)            
            self.modi.Show(True)
            self.modi.Enable(False)  
            #self.ntbk.SetSelection(1)
        self.vsrif.SetFocus()

    def FndCodCFDest(self, evt):
        cnt_rec = 0
        val = self.ragsoc3.GetValue().upper()
        cod = self.codcf1.GetValue()
        sql = """ select * from tblcf where cod = "%s"
                and t_cpart = "%s" """
        valueSql = int(cod), self.tcpart	  	
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1  
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndCodCFDest Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttldest)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnagDest(row)
        
    def FndAnagDest(self, evt):
        cnt_rec = 0
        val = self.ragsoc3.GetValue().title()
        cod = self.codcf1.GetValue()
        sql = """ select * from tblcf where tag_soc1 like "%s"
                and t_cpart = "%s" """
        valueSql = '%' + val + '%', self.tcpart	
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndAnagDest Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttldest)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnagDest(row)
        elif (cnt_rec>1):
            try:
                import srctblcf
            except :
                pass
            try:
                import base.srctblcf
            except :
                pass
            control = [self.tcpart,self.codcf1,self.ragsoc3,self.FndCodCFDest,self.codcf]               
            win = srctblcf.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else:
            self.nsrif.SetFocus()
            
    def FndSelAnagDest(self, evt):
        row = evt
        self.codcf1.SetValue(str(row[1]))
        self.ragsoc3.SetValue(str(row[3]).title())
        self.ragsoc4.SetValue(str(row[4]).title())
        self.indiriz1.SetValue(str(row[6]).title())
        cap1 = string.zfill(str(row[7]).strip(),5)
        self.cap1.SetValue(cap1)
        self.__MDI__.CnvNone(row[8])
        self.zona1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[9])
        self.localit1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[10])
        self.pr1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvNone(row[11])
        self.stato1.SetValue(self.__MDI__.val)
        self.vsrif.SetFocus()


    def OffArtTxt(self, evt):        
        self.codart.Enable(False)
        self.codbar.Enable(False)
        self.ccodart.Enable(False)
        self.ccodbar.Enable(False)
        self.ctesto.Enable(False) # personalizza testo 
        self.ccodinfo.Enable(False)	
        self.descriz.Enable(False)
        self.cdescriz.Enable(False)
        self.UM.Enable(False)
        self.mis.Enable(False)
        self.provv.Enable(False)
        self.costo.Enable(False)
        self.colli.Enable(False)
        self.qt.Enable(False)
        self.prezzo.Enable(False)
        self.sc1.Enable(False)
        self.vALIVA.Enable(False)
        self.cALIVA.Enable(False)
        #self.nriga.Enable(False)
        self.peso.Enable(False)
        self.totale.Enable(False)
        self.vinprod.Enable(False)
        self.UM.Enable(False)
        self.vMERCE.Enable(False)
        self.vIMBAL.Enable(False)
        self.vCONFE.Enable(False)
        self.modir.Enable(False)
        self.okart.Enable(False)
        self.modir.Show(True)
        self.okart.Show(False)
        self.intr.Enable(False)
        self.delr.Enable(False)
        self.newr.Enable(True)
        self.newr.SetFocus()

    def OffArtTxtAll(self, evt):
        self.lc.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.lc.Enable(True)        
        self.codart.Enable(False)
        self.ccodart.Enable(False)
        self.codbar.Enable(False)
        self.ccodbar.Enable(False)
        self.ctesto.Enable(False) # personalizza testo
        self.descriz.Enable(False)
        self.cdescriz.Enable(False)
        self.UM.Enable(False)
        #self.mis.Enable(False)
        #self.lcosto.Show(False)
        #self.costo.Show(False)
        self.costo.Enable(False)
        #self.prezzo.Enable(False)
        #self.sc1.Enable(False)
        self.nriga.Enable(False)
        #self.qt.Enable(False)
        self.peso.Enable(False)
        self.totale.Enable(False)
        self.vinprod.Enable(False)
        self.vMERCE.Enable(False)
        self.vIMBAL.Enable(False)
        self.vCONFE.Enable(False)
        #self.lc.Enable(False)
        
    def OnArtTxt(self, evt):
        self.lc.SetBackgroundColour(self.color)
        self.lc.Enable(False)
        self.codart.Enable(True)
        self.ccodart.Enable(True)
        self.codbar.Enable(True)
        #self.codbar.Show(True)
        self.ccodbar.Enable(True)
        self.ctesto.Enable(True) # personalizza testo
        self.ccodinfo.Enable(True)
        self.descriz.Enable(True)
        self.cdescriz.Enable(True)
        self.UM.Enable(True)
        self.mis.Enable(True)
        self.provv.Enable(True)
        self.prezzo.Enable(True)
        self.sc1.Enable(True)
        self.colli.Enable(True)
        self.qt.Enable(True)
        self.vALIVA.Enable(True)
        self.cALIVA.Enable(True)
              
    def NewRow(self, evt):
        self.OnArtTxt(self)
        self.DelArtTxt(self)
        self.cntr_row = "new"
        if self.ccodbar.GetValue()==False :
            self.codart.Show(True)
            self.codbar.Show(False)
            #self.codart.SetFocus()
            self.descriz.SetFocus()
        else:
            self.codart.Show(False)
            self.codbar.Show(True)
            self.codbar.SetFocus()
        self.newr.Enable(False)
        self.intr.Enable(True)
        self.modir.Enable(False)
        self.okart.Enable(True)
        self.modir.Show(False)
        self.okart.Show(True)
        
    def ModiRow(self, evt):
        self.OnArtTxt(self)   
        self.cntr_row = "modi"
        self.qt.SetFocus()
        self.delr.Enable(True)
        self.cntr_row = ""
        self.modir.Show(False)
        self.modir.Enable(False)
        self.okart.Show(True)
        self.okart.Enable(True)
        
    def DelArtTxt(self, evt):
        self.codart.SetValue('')
        self.codbar.SetValue('')
        self.descriz.SetValue('')
        self.UM.SetValue('')
        self.prezzo.SetValue('')
        self.costo.SetValue('')
        self.importo.SetValue('')
        self.qt.SetValue('')
        #self.volume.SetValue('')
        self.peso.SetValue('0,00')
        self.colli.SetValue('0,00')
        self.prezzo_ag.SetValue('0,00')
        #self.vALIVA.SetValue('20')
        #self.dALIVA.SetValue("Aliquota 20%")

    def CalcSaldo(self,evt):
        if self.prezzo_ac.GetValue()=='':self.prezzo_ac.SetValue('0')
        if self.totaledoc.GetValue()=='':self.totaledoc.SetValue('0')
        totordi = self.totaledoc.GetValue()
        accordi = self.prezzo_ac.GetValue()
        self.__MDI__.CnvPM(totordi)
        totordi = self.__MDI__.val
        self.__MDI__.CnvPM(accordi)
        accordi = self.__MDI__.val
        saldo = totordi-accordi
        self.__MDI__.CnvVM(saldo)
        self.prezzo_ac1.SetValue(self.__MDI__.val)
        
    def CalcTotale(self,evt):
        tot_colli = 0
        importo = 0
        imponibile = 0
        iva = 0
        for x in range(self.lc.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxt(x, 20))
            colli_row = float(self.__MDI__.val)
            tot_colli = colli_row
            self.__MDI__.CnvPM(self.getColTxt(x, 5))
            imponibile_row = float(self.__MDI__.val)
            self.__MDI__.CnvPM(self.getColTxt(x, 6))
            iva_row = float(self.__MDI__.val)  
            if (type(iva_row)==float) :
                iva+=imponibile_row*iva_row/100
            imponibile+=imponibile_row
        importo=imponibile+iva    
        self.__MDI__.CnvVM(imponibile)
        self.totale.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(importo)
        self.totaledoc.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(tot_colli)
        self.tot_colli.SetValue(self.__MDI__.val)
    
    def SelRow(self,evt):
        self.intr.Enable(True)
        self.modir.Enable(True)
        self.newr.Enable(False)      

    def IntRow(self,evt):
        self.OffArtTxt(self)
        self.DelArtTxt(self)
        self.lc.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.lc.Enable(True) 
        
    def DelRow(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdelrow, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.lc.DeleteItem(self.row)
            self.IntRow(self)
            self.CalcTotale(self)       
            self.newr.SetFocus()
            dlg.Destroy()
            #self.Close(true)
        else:
            dlg.Destroy()
        
    def RmpRow(self, evt):
        self.lc.InsertStringItem(self.row, self.codart.GetValue())
        self.lc.SetStringItem(self.row, 1, self.descriz.GetValue())
        self.lc.SetStringItem(self.row, 2, self.qt.GetValue())
        self.lc.SetStringItem(self.row, 3, self.prezzo.GetValue())
        self.lc.SetStringItem(self.row, 4, self.sc1.GetValue())
        self.lc.SetStringItem(self.row, 5, self.importo.GetValue())
        self.lc.SetStringItem(self.row, 6, self.vALIVA.GetValue())
        self.lc.SetStringItem(self.row, 7, self.UM.GetValue())        
        self.lc.SetStringItem(self.row, 8, self.mis.GetValue())
        self.lc.SetStringItem(self.row, 9, self.nriga.GetValue())
        self.lc.SetStringItem(self.row, 10, self.codbar.GetValue())
        self.lc.SetStringItem(self.row, 11, self.codmerc.GetValue())
        self.lc.SetStringItem(self.row, 12, self.qt_ord.GetValue())
        self.lc.SetStringItem(self.row, 13, self.qt_con.GetValue())
        self.lc.SetStringItem(self.row, 14, self.qt_eva.GetValue())
        self.lc.SetStringItem(self.row, 15, self.prezzo_ag.GetValue())
        self.lc.SetStringItem(self.row, 16, self.sc2.GetValue())        
        self.lc.SetStringItem(self.row, 17, self.sc3.GetValue())
        self.lc.SetStringItem(self.row, 18, self.provv.GetValue())
        self.lc.SetStringItem(self.row, 19, self.datacons.GetValue())
        self.lc.SetStringItem(self.row, 20, self.colli.GetValue())
        self.lc.SetStringItem(self.row, 21, self.peso.GetValue())
        self.lc.SetStringItem(self.row, 22, self.lst.GetValue())
        self.lc.SetStringItem(self.row, 23, self.vPDC.GetValue())
        self.lc.SetStringItem(self.row, 24, self.stt_ord2.GetValue())
        self.lc.SetStringItem(self.row, 25, self.annodoc.GetValue())        
        self.lc.SetStringItem(self.row, 26, self.tipodoc.GetValue())
        self.lc.SetStringItem(self.row, 27, self.datadoc.GetValue())  
        self.lc.SetStringItem(self.row, 28, self.numdoc.GetValue())
        self.lc.SetStringItem(self.row, 29, self.campo1_art.GetValue())
        self.lc.SetStringItem(self.row, 30, self.campo2_art.GetValue())

    def OkRow(self, evt):
        cnt_val = 0
        valprezzo = self.prezzo.GetValue().replace(",","")
        valprezzo = valprezzo.replace("-","") 
        if (valprezzo!="" and valprezzo.isdigit()==True):
            self.__MDI__.CnvPM5(self.prezzo.GetValue())
            vprezzo = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgprezno,self.ttl)
            self.prezzo.SetFocus()
                
        sc1 = self.sc1.GetValue().replace(",","")  
        if (sc1!="" and sc1.isdigit()==True):
            self.__MDI__.CnvPM(self.sc1.GetValue())
            vsc1 = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgscno,self.ttl)
            self.sc1.SetFocus()
            
        qt = self.qt.GetValue().replace(",","") 
        if (qt!="" and qt.isdigit()==True):
            self.__MDI__.CnvPM(self.qt.GetValue())
            vqt = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgqtno,self.ttl)
            self.qt.SetFocus()
        if (cnt_val==3):
            importo = (vprezzo*vqt)-(vprezzo*vqt*vsc1/100)
            self.__MDI__.CnvVM(importo)
            self.importo.SetValue(self.__MDI__.val)
            self.OffArtTxt(self)
        
            if ( self.cntr_row=="new"):
                self.row = self.lc.GetItemCount()
                nriga  = self.row + 1
                self.nriga.SetValue(str(nriga*10))
                self.RmpRow(self)
                
            if ( self.cntr_row==""):
                self.RmpRow(self)
                self.lc.DeleteItem(self.row + 1)
                self.lc.SetItemState(self.row-1, 
                    wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
                
            self.CalcTotale(self)
            self.newr.Enable(True)
            self.newr.SetFocus()
            self.modir.Enable(False)
            self.okart.Enable(False)
            self.cntr_row = ""

    def FndSelArt(self, evt):
        row = evt
        self.codart.SetValue(str(row[0]))
        self.descriz.SetValue(str(row[2]))
        self.UM.SetValue(str(row[3]))
        self.mis.SetValue(str(row[4]))         
        self.__MDI__.CnvVM5(row[7])
        self.costo.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM5(row[5])
        self.prezzo1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM5(row[6])
        self.prezzo2.SetValue(self.__MDI__.val)
        self.prezzo.SetValue(self.prezzo1.GetValue())
        if self.tcpart=='F':
            self.prezzo.SetValue(self.costo.GetValue())
            self.lcosto.Show(False)
            self.costo.Show(False)
            #self.lprovv.Show(False)
            #self.provv.Show(False)
        self.codbar.SetValue(str(row[1]))          
        self.vALIVA.SetValue(str(row[11]))
        self.vMERCE.SetValue(str(row[8]))
        self.vIMBAL.SetValue(str(row[23]))
        self.vCONFE.SetValue(str(row[24]))
        self.peso.SetValue(str(row[25]))
        #self.volume.SetValue(str(row[26]))
        self.vinprod.SetValue(str(row[29]))
        self.OffArtTxtAll(self)
        self.vALIVA.SetFocus()

    def FndCodInfo(self, evt):
        cod = self.codart.GetValue().upper()     
        des = self.descriz.GetValue().upper()
        try:
            import infoart
        except :
            pass
        try:
            import base.infoart
        except :
            pass
        #control = [cod,des]
        #win = infoart.create(self,control) 
        if cod!="" and des!="" : 
            control = [cod,des]
            win = infoart.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else: self.Message(_("ATTENZIONE!!! campo di ricerca vuoto") ,self.ttl)

    def FndCodArt(self, evt):
        cnt_rec = 0
        cod = self.codart.GetValue().upper()
        sql = """ select * from articoli where cod like "%s" """
        valueSql = '%' + cod + '%'
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndCodArt Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec>=1000): self.Message(cfg.msgfnd  +  str(cnt_rec) ,self.ttl)
        elif (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2):self.FndSelArt(row)     
        elif (cnt_rec>1):
            try:
                import srcart
            except :
                pass
            try:
                import base.srcart
            except :
                pass
            control = [self.tblart,self.codart,self.descriz,self.FndArt]
            win = srcart.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

        
    def FndCodBar(self, evt): 
        cnt_rec = 0
        cod = self.codbar.GetValue()
        sql = """ select * from articoli where codbar = "%s" """
        valueSql = cod
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1 
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndCodBar Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelArt(row)

    def FndDesArt(self, evt):
        cnt_rec = 0
        val = self.descriz.GetValue().upper()
        sql = """ select * from articoli 
                where descriz like "%s" order by descriz """
        valueSql = '%' + val + '%'	
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndDesArt Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelArt(row)
        elif (cnt_rec>1):
            import base.srcart
            control = [self.tblart,self.codart,self.descriz,self.FndArt]
            win = base.srcart.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)


    def FndArt(self, evt):
        cnt_rec = 0
        val = self.descriz.GetValue().upper()
        cod = self.codart.GetValue().upper()
        sql = """ select * from articoli where cod = "%s" """
        valueSql = cod 
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," FndArt Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelArt(row)
        
      
    def FndArtSel(self, evt):
        self.okart.Enable(True)
        self.okart.SetFocus()
                        
        
    def New(self, evt):
        if self.cntr!="modi" :#modifica 	    
            self.IntTestata(self)
            self.NewTxt(self)
            self.cntr = "new"
        else: 
            self.cntr = "new" 
            self.oldnum_ord = int(self.num_ord.GetValue())
            self.oldvTIPO_ORD = self.vTIPO_ORD.GetValue()
            if self.rbCONFER.GetValue()==True: self.vTIPO_ORD.SetValue("OC")
            self.SelCOMBO(self) 
        registro = self.vTIPO_ORD.GetValue()
        anno = self.anno.GetValue()
        chiave = "RORD"  
        sql = """ select * from libriaz 
                where chiave = "%s" and  anno = "%s" and  registro = "%s" """
        valueSql = chiave, anno, registro
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            while (1):
                row = cr.fetchone()
                if row==None:
                    break

                if (row[3]==None or row[3]=="") : 
                    self.num_ord.SetValue('1')
                else : 
                    self.num_ord.SetValue(str(int(row[3]) + 1))
                    self.val_numord = int(self.num_ord.GetValue())
                if (row[16]==None or row[16]=="") : 
                    self.vdata_ord.SetValue(self.data)
                else:
                    self.vdata_ord.SetValue(row[16])
                    self.data_ord.SetValue(self.data)
        except StandardError, msg:
            self.__MDI__.MsgErr("ordini"," New num_ord Error %s" % (msg))
        self.CnAz.commit()
        num_ord = int(self.num_ord.GetValue())
            
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal()==wx.ID_OK:
            dlg.Destroy()
                        
    def Close(self, evt):
        if (self.ragsoc2.GetValue()!="" or self.ragsoc1.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgesci, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
            if dlg.ShowModal()==wx.ID_YES:
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

            
    def Save(self, evt):
        if(self.lc.GetItemCount()!=0 and self.codcf.GetValue()!=""):
            vcntr = self.cntr
            self.cntr = ""
            vTIPO_ORD = self.vTIPO_ORD.GetValue()
            vanno = self.anno.GetValue()
            vnum_ord = int(self.num_ord.GetValue())            
            vdata_ord = self.data_ord.GetValue()
            chiave = "RORD"
            registro = vTIPO_ORD
            vcod_cf = self.codcf.GetValue()
            vragsoc2 = self.ragsoc2.GetValue()
            vragsoc1 = self.ragsoc1.GetValue()
            vindiriz = self.indiriz.GetValue()
            vcap = self.cap.GetValue()
            vzona = self.zona.GetValue()
            vlocalit = self.localit.GetValue()
            vpr = self.pr.GetValue()
            vstato = self.stato.GetValue()
            vcodcf1 = self.codcf1.GetValue()
            vindiriz1 = self.indiriz1.GetValue()
            vragsoc3 = self.ragsoc3.GetValue()
            vragsoc4 = self.ragsoc4.GetValue()
            vcap1 = self.cap1.GetValue()
            vzona1 = self.zona1.GetValue()
            vlocalit1 = self.localit1.GetValue()
            vpr1 = self.pr1.GetValue()
            if (vpr1=='' or vpr1=='None')and (vcodcf1!=''): vpr1 = '--'
            vstato1 = self.stato1.GetValue()
            vstt_ord1 = self.stt_ord1.GetValue()
            vstt_ord2 = self.stt_ord2.GetValue()
            vlst = int(self.lst.GetValue())
            vvsord = self.vs_ord.GetValue()  
            vvsdata = self.vs_data.GetValue()
            vdiv = self.vDIVvend.GetValue()
            vcodage = self.codage.GetValue()
            vPRIO = int(self.vPRIO.GetValue())
            vPAGAM = self.vPAGAM.GetValue()              
            vconseg = self.vCONSEG.GetValue()
            vtrasp = self.trasp.GetValue()
            vcod_vet = self.cod_vet.GetValue()
            vvsrif = self.vsrif.GetValue()
            vnsrif = self.nsrif.GetValue()
            vrag_ord = self.rag_ord.GetValue()
            vcampo1 = self.campo1.GetValue()
            vcampo2 = self.campo2.GetValue()
            vnote = self.note.GetValue()
            vo1_1 = vTIPO_ORD,vanno,vnum_ord,vdata_ord,vcod_cf,vragsoc1,vragsoc2
            vo1_1_modi = vdata_ord,vcod_cf,vragsoc1,vragsoc2
            vo1_2 = vindiriz,vcap,vzona,vlocalit,vpr,vstato,vcodcf1
            vo1_3 = vragsoc3,vragsoc4,vindiriz1,vcap1,vzona1,vlocalit1,vpr1,vstato1
            vo1_4 = vstt_ord1,vlst,vvsord,vvsdata
            vo1_5 = vdiv,vcodage,vPRIO,vPAGAM,vconseg,vtrasp,vcod_vet
            vo1_6 = vvsrif,vnsrif,vrag_ord,vcampo1,vcampo2,vnote
            vo1_6_modi = vTIPO_ORD,vanno,vnum_ord
            vordi1 = vo1_1  +  vo1_2  +  vo1_3  +  vo1_4  +  vo1_5  +  vo1_6
            vordi1_modi = vo1_1_modi  +  vo1_2  +  vo1_3  +  vo1_4  + \
                         vo1_5  +  vo1_6
            vvaspet = self.vASPET.GetValue()
            vtot_colli = self.tot_colli.GetValue()
            self.__MDI__.CnvPM(vtot_colli)
            vtot_colli = float(self.__MDI__.val)
            vtot_peso = self.tot_peso.GetValue()
            self.__MDI__.CnvPM(vtot_peso)
            vtot_peso = float(self.__MDI__.val)
            vsc1 = 0
            vsc2 = 0
            vsc3 = 0
            vprez_ac = self.prezzo_ac.GetValue()
            self.__MDI__.CnvPM(vprez_ac)
            vprez_ac = float(self.__MDI__.val)
            vprez_ac1 = self.prezzo_ac1.GetValue()
            self.__MDI__.CnvPM(vprez_ac1)
            vprez_ac1 = float(self.__MDI__.val)
            vvPDC_SC = self.vPDC_SC.GetValue()                
            vcampo1_calce = 0#self.campo1_calce.GetValue()
            vcampo2_calce = 0#self.campo2_calce.GetValue()
            vnote_calce = self.note_calce.GetValue()
            vo3_1 = vvaspet,vtot_colli,vtot_peso
            vo3_2 = vsc1,vsc2,vsc3,vvPDC_SC,vprez_ac,vprez_ac1
            vo3_3 = vcampo1_calce,vcampo2_calce,vnote_calce
            vordi3 = vo3_1  +  vo3_2  +  vo3_3
            valueSql = vordi1 + vordi3
            valueSql_modi = vordi1_modi + vordi3 +  vo1_6_modi
            if(vcntr=="new"):
                try:
                    cr = self.CnAz.cursor()
                    sql =  """ insert into ordi1
                               values("%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s") """
                    cr.execute(sql % valueSql)  
                except StandardError, msg:
                        self.__MDI__.MsgErr("ordini"," Save insert ordi1 Error %s" % (msg))
                self.CnAz.commit()
                # modifica
                if self.oldnum_ord!="":
                    valueSql = "E", self.oldvTIPO_ORD, self.anno.GetValue(), self.oldnum_ord
                    try:
                        cr = self.CnAz.cursor()
                        sql1old = """ update ordi1 set stt_ord = "%s" 
                                    where tipo_ord = "%s" and anno = "%s" 
                                    and num_ord = "%s" """

                        cr.execute(sql1old % valueSql)  
                    except StandardError, msg:
                            self.__MDI__.MsgErr("ordini"," Save update old ordi1 Error %s" % (msg))
                    self.CnAz.commit()
                    try:
                        cr = self.CnAz.cursor()
                        sql1old = """ update ordi2 set stt_ord = "%s" 
                                    where tipo_ord = "%s" and anno = "%s" 
                                    and num_ord = "%s" """

                        cr.execute(sql1old % valueSql)  
                    except StandardError, msg:
                            self.__MDI__.MsgErr("ordini"," Save update old ordi2 Error %s" % (msg))
                    self.CnAz.commit()
		
            if(vcntr=="modi"):
                try:
                    cr = self.CnAz.cursor()
                    sql = """ update ordi1 set data_ord = "%s", cod_cf = "%s" , 
                              rag_soc1 = "%s", rag_soc2 = "%s", indiriz = "%s",
                            cap = "%s", zona = "%s", localit = "%s", pr = "%s",
                            stato = "%s", cod_dest = "%s", rag_soc3 = "%s",
                            rag_soc4 = "%s", indiriz1 = "%s", cap1 = "%s",
                            zona1 = "%s", localit1 = "%s", pr1 = "%s",
                            stato1 = "%s", stt_ord = "%s", lst = "%s",
                            vsord = "%s",vsdata = "%s", vdiv = "%s", 
                            cod_age = "%s", prio = "%s", pagam = "%s",
                            conse = "%s", trasp = "%s", cod_vet = "%s", 
                            vsrif = "%s", nsrif = "%s", rag_ord = "%s",
                            campo1 = "%s", campo2 = "%s", note = "%s", 
                            aspet = "%s", colli = "%s", peso = "%s", 
                            sc1 = "%s", sc2 = "%s", sc3 = "%s", pdc_sc = "%s",
                            prez_ac = "%s", prez_ac1 = "%s", campo3 = "%s", 
                            campo4 = "%s", note1 = "%s" 
                            where tipo_ord = "%s" and anno = "%s" 
                            and num_ord = "%s" """
                    cr.execute(sql % valueSql_modi) 
                except StandardError, msg:
                        self.__MDI__.MsgErr("ordini"," Save update ordi1 Error %s" % (msg))
                self.CnAz.commit()
                valueSql = vTIPO_ORD, vanno, int(vnum_ord)
                try:
                    cr = self.CnAz.cursor()
                    sql = """ delete from ordi2 
                            where tipo_ord = "%s" and  anno = "%s" 
                            and  num_ord = "%s" """                     
                    cr.execute(sql % valueSql)  
                except StandardError, msg:
                        self.__MDI__.MsgErr("ordini"," Dele modi ordi2 Error %s" % (msg))
                self.CnAz.commit()
            nrow = self.lc.GetItemCount() 
            for row in range(nrow):
                vcod_mag = 1
                vnriga = int(self.getColTxt(row, 9))    
                vcodart = self.getColTxt(row, 0)
                vcodbar = self.getColTxt(row, 10)
                vMERCE = self.getColTxt(row, 11)
                vdescriz = self.getColTxt(row, 1)        
                vUM = self.getColTxt(row, 7)
                if vUM=='':vUM = '--'
                vmis = self.getColTxt(row, 8)
                vqt_ord = self.getColTxt(row, 2)
                self.__MDI__.CnvPM(vqt_ord)
                vqt_ord = float(self.__MDI__.val)                  
                vqt_con = 0
                vqt_eva = 0
                vprez_un = self.getColTxt(row, 3)
                self.__MDI__.CnvPM5(vprez_un)
                vprez_un = float(self.__MDI__.val)
                vprez_ag = self.getColTxt(row, 15)
                self.__MDI__.CnvPM5(vprez_ag)
                vprez_ag = float(self.__MDI__.val)
                vtot_riga = self.getColTxt(row, 5)
                self.__MDI__.CnvPM(vtot_riga)
                vtot_riga = float(self.__MDI__.val)
                vALIVA = self.getColTxt(row, 6)
                vsc1 = self.getColTxt(row, 4)
                self.__MDI__.CnvPM(vsc1)
                vsc1 = float(self.__MDI__.val) 
                vsc2 = 0
                vsc3 = 0
                vprovv = self.getColTxt(row, 18)
                self.__MDI__.CnvPM(vprovv)
                vprovv = float(self.__MDI__.val)
                vdatacons = self.getColTxt(row, 19)
                vcolli = self.getColTxt(row, 20)
                self.__MDI__.CnvPM(vcolli)
                vcolli = float(self.__MDI__.val)
                vpeso = self.getColTxt(row, 21)
                self.__MDI__.CnvPM(vpeso)
                vpeso = float(self.__MDI__.val) 
                vlst = int(self.getColTxt(row, 22))
                vpdc = self.getColTxt(row, 23)
                vstt_ord2 = self.getColTxt(row, 24)
                vannodoc = self.getColTxt(row, 25)                
                vtipodoc = self.getColTxt(row, 26)
                vdatadoc = self.getColTxt(row, 27)
                vnumdoc = self.getColTxt(row, 28)
                vcampo1_corpo = self.getColTxt(row, 29)
                vcampo2_corpo = self.getColTxt(row, 30)
                if self.oldnum_ord!="": vstt_ord2 ="C"
                vo2_1 = vTIPO_ORD,vanno,vnum_ord,vcod_mag,vnriga,vcodart,vcodbar,vMERCE
                vo2_2 = vdescriz,vUM,vmis,vqt_ord,vqt_con,vqt_eva,vprez_un,vprez_ag
                vo2_3 = vtot_riga,vALIVA,vsc1,vsc2,vsc3,vprovv,vdatacons
                vo2_4 = vcolli,vpeso,vlst,vpdc,vstt_ord2,vannodoc,vtipodoc,vdatadoc,vnumdoc
                vo2_5 = vcampo1_corpo,vcampo2_corpo
                valueSql = vo2_1  +  vo2_2  +  vo2_3  +  vo2_4  +  vo2_5
                try:
                    cr = self.CnAz.cursor()
                    sql = """ insert into ordi2
                              values("%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s") """
                    cr.execute(sql % valueSql)  
                except StandardError, msg:
                        self.__MDI__.MsgErr("ordini"," Save insert ordi2 Error %s" % (msg))
                self.CnAz.commit()
                if vcntr!="modi" : 
                    valueSql = vnum_ord, vdata_ord, chiave, vanno, registro
                    try:
                        cr = self.CnAz.cursor()
                        sql = """ update libriaz set ultnum = "%s", udatreg = "%s" 
                                where chiave = "%s" and  anno = "%s" 
                                and  registro = "%s" """                    
                        cr.execute(sql % valueSql)  
                    except StandardError, msg:
                            self.__MDI__.MsgErr("ordini"," Save update libriaz Error %s" % (msg))
                    self.CnAz.commit()
            self.OffAnagTxt(self)
            self.OffArtTxt(self)
            self.voktestata = 0
            self.ok.Show(False)
            self.oktestata.Show(False)
            self.inte.Show(True)
            self.inte.Enable(True)
            self.new.Enable(True)
            self.new.Show(True)
            self.dele.Enable(False)
            self.stampa.Enable(True)
            self.stampa.SetFocus()
            self.cntr = ""
            self.oldnum_ord = ""
            self.oldvTIPO_ORD = ""

        else:
            self.Message(cfg.msgass,self.ttl)

    def StpSkAnag(self, evt):
        #<daniele> 
        codcf = self.codcf.GetValue()
        import skprint
        skprint.stampaDoc(
            conn = self.CnAz ,   #connessione
              tipo = 'sanag' + self.tcpart.lower(), #tipo documento e parametro
              parametriSql = (self.tcpart, codcf),
              #datiazienda = self.dzDatiAzienda,
              anteprima = True )
        #</daniele>                               

    #<daniele> 
    def Stampa(self, evt):   
        anno = self.anno.GetValue()
        num_ord = self.num_ord.GetValue()
        tipo_ord = self.vTIPO_ORD.GetValue()
        tipo = self.vTIPO_ORD.GetValue()
        if tipo_ord=="PC": tipo = "OC"
        if tipo_ord=="PF": tipo = "OF"

        import skprint
        skprint.stampaDoc(
            conn = self.CnAz ,   #connessione
              tipo = tipo, #tipo documento e parametro
              parametriSql = (anno,tipo_ord,num_ord),
              datiazienda = self.dzDatiAzienda,
              anteprima = True )
    #</daniele>     

    # personalizza testo
    def OpenTesto(self, evt):       
        #print "OpenTesto"
        try:
            import testo
        except :
            pass
        try:
            import base.testo
        except :
            pass
        #import testo    
        control = [self.dtesto,self.InsTesto]               
        win = testo.create(self,control) 
        win.Centre(wx.BOTH)
        win.Show(True)

    # personalizza testo
    def InsTesto(self, evt): 
        val = self.dtesto.GetValue()
        nriga = 0
        ldescriz = [ x for x in val.split('\n') if x != '']
        #ldescriz = ldescriz.reverse()
        #print ldescriz
        for descriz in ldescriz:
            nriga+=10
            self.RmpTesto(descriz.upper())
        self.IntRow(self)

    # personalizza testo
    def RmpTesto(self, evt): 
        #print evt
        row=0
        self.row = self.lc.GetItemCount()
        nriga =str((self.row+1)*10)
        descriz = evt
        self.lc.InsertStringItem(self.row, '')
        self.lc.SetStringItem(self.row, 1, descriz)
        self.lc.SetStringItem(self.row, 2, '0')
        self.lc.SetStringItem(self.row, 3, '0')
        self.lc.SetStringItem(self.row, 4, '0')
        self.lc.SetStringItem(self.row, 5, '0')
        self.lc.SetStringItem(self.row, 6, '')
        self.lc.SetStringItem(self.row, 7, '')        
        self.lc.SetStringItem(self.row, 8, '')
        self.lc.SetStringItem(self.row, 9, nriga)
        self.lc.SetStringItem(self.row, 10, '')
        self.lc.SetStringItem(self.row, 11, '')
        self.lc.SetStringItem(self.row, 12, '0')
        self.lc.SetStringItem(self.row, 13, '0')
        self.lc.SetStringItem(self.row, 14, '0')
        self.lc.SetStringItem(self.row, 15, '0')
        self.lc.SetStringItem(self.row, 16, '0')        
        self.lc.SetStringItem(self.row, 17, '0')
        self.lc.SetStringItem(self.row, 18, '')
        self.lc.SetStringItem(self.row, 19, '')
        self.lc.SetStringItem(self.row, 20, '0')
        self.lc.SetStringItem(self.row, 21, '0')
        self.lc.SetStringItem(self.row, 22, '1')
        self.lc.SetStringItem(self.row, 23, '')
        self.lc.SetStringItem(self.row, 24, '')
        self.lc.SetStringItem(self.row, 25, '')       
        self.lc.SetStringItem(self.row, 26, '')
        self.lc.SetStringItem(self.row, 27, '')  
        self.lc.SetStringItem(self.row, 28, '')
        self.lc.SetStringItem(self.row, 29, '')
        self.lc.SetStringItem(self.row, 30, '')

    def is_look(self):
        if (self.cntr!="new" and self.cntr!="modi"): return False
        else : return True
        
    def data_reload(self,rec,cntrp):
        self.rec=rec
        self.tipoord=cntrp
        self.tcpart = "C"
        if self.tipoord=='OF': self.tcpart = "F"
        self.Start(self)
            
