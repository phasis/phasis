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
from cfg import *
import cfg

def create(parent,cnt):
    return Vendite(parent,cnt)
  
class Vendite(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        #wx.Frame.__init__(self, id = wx.NewId(), name = '',
        #      parent = prnt, pos = wx.Point(0, 0), 
        #      style = wx.DEFAULT_FRAME_STYLE  , title = cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.SetClientSize(wx.Size(600, 425))
        self.ttl = cnt[0]
        self.rec = cnt[2]
        self.voktestata = 0
        if cnt[1]=='':self.tipo_doc = cfg.tipodoc 
        else :self.tipo_doc = cnt[1]
        self.tcpart = "C"
        if self.tipo_doc =='B3': self.tcpart = "F"
        self.ttlanag = _('Anagrafica Clienti')
        self.ttlart = _('Anagrafica Articoli')
        self.ttldest = _('Anagrafica Spedizione')
        self.tblart = "articoli"
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]   
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
              #size = wx.Size(cfg.NTBKH,cfg.NTBKV),style = 0)
        self.ntbk.SetFont(self.font)
        
        self.pnl1 = wx.Panel(id = wx.NewId(), name = 'panel1',
              parent = self.ntbk, pos = wx.Point(0, 0))#, size = wx.Size(680, 420))
        self.pnl1.SetFont(self.font)
        
        self.pnl2 = wx.Panel(id = wx.NewId(), name = 'panel2',
              parent = self.ntbk, pos = wx.Point(0, 0))#, size = wx.Size(680, 420))
        self.pnl2.SetFont(self.font)
        
        self.pnl3 = wx.Panel(id = wx.NewId(), name = 'panel3',
              parent = self.ntbk, pos = wx.Point(0, 0))#, size = wx.Size(680, 420))
        self.pnl3.SetFont(self.font)
        
        self.ntbk.AddPage(imageId = -1, page = self.pnl1, 
              select = True, text = _(' Testata')+' (1) ')
        self.ntbk.AddPage(imageId = -1, 
              page = self.pnl2, select = False, text = _(' Corpo')+' (2) ')
        self.ntbk.AddPage(imageId = -1, 
              page = self.pnl3, select = False, text = _(' Calce')+' (3) ')
        
        #self.pnl.SetFont(self.font)
        #self.pnl1.SetFont(self.font)
        #self.pnl2.SetFont(self.font)
        #self.pnl3.SetFont(self.font)
        #self.ntbk.SetFont(self.font)
        
        #wx.StaticText(self.pnl1, -1, "Doc. :", wx.DLG_PNT(self.pnl1, 5,7))
        self.TIPO_DOC = wx.ComboBox(self.pnl1, Nid,"",
              wx.DLG_PNT(self.pnl1, 5,5), wx.DLG_SZE(self.pnl1, 110,-1),[],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vTIPO_DOC =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 275,90))
        self.ldoc = wx.StaticText(self.pnl1, -1, _("Num. :"), 
              wx.DLG_PNT(self.pnl1, 120,7))
        self.anno = wx.ComboBox(self.pnl1, Nid, self.annoc,
              wx.DLG_PNT(self.pnl1, 145,5),
              wx.DLG_SZE(self.pnl1, 35,-1), [self.annoc],
              wx.CB_DROPDOWN | wx.CB_SORT )  
        wx.StaticText(self.pnl1, -1, "/", wx.DLG_PNT(self.pnl1, 182,7))
        self.num_doc = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 185,5), wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) 
        self.cnum_doc = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 226,5),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV), wx.TE_PROCESS_ENTER)
        wx.StaticText(self.pnl1, -1, _("Data :"), wx.DLG_PNT(self.pnl1, 243,7))
        self.data_doc = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 264,5), wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)
        # self.datadoc = wx.IntCtrl(self.pnl1, Nid, "",
        #wx.DLG_PNT(self.pnl1, 264,5), wx.DLG_SZE(self.pnl1, 50,-1))
        self.cdatadoc = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 315,5),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.vdata_doc = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 264, 5), wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl1, -1, _(" Vs. Ordine :"), 
              wx.DLG_PNT(self.pnl1, 5,20))
        self.vs_ord = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 5,30), wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) 
        wx.StaticText(self.pnl1, -1, _("Data :"), wx.DLG_PNT(self.pnl1, 60,20))
        self.vs_data = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 60, 30), wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT),
              wx.TE_PROCESS_ENTER)
        self.cvsdata = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 115,30),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))                                   
        self.sbox_cf = wx.StaticBox(self.pnl1, Nid, _(' Cliente '),
              wx.DLG_PNT(self.pnl1, 5,45), wx.DLG_SZE(self.pnl1, 265,65))
        #self.sbox1 = wx.StaticBox(self.pnl1, Nid, "",
        #wx.DLG_PNT(self.pnl1, 5,90), wx.DLG_SZE(self.pnl1, 265,65))
        self.lcodcf =  wx.StaticText(self.pnl1, -1, _("Codice"), 
              wx.DLG_PNT(self.pnl1, 10,55))
        self.codcf =  wx.TextCtrl(self.pnl1, Nid, "",
                      wx.DLG_PNT(self.pnl1, 10, 65), 
              wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT))
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
              wx.DLG_SZE(self.pnl1, 120,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)    
        self.cragsoc1 = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 200,65),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc3 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 75,65), 
              wx.DLG_SZE(self.pnl1, 120,cfg.DIMFONTDEFAULT))    
        self.cragsoc3 = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 200,65),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        #wx.StaticText(self.pnl1, -1, "Rag. Sociale2 ( Nome ) :", 
        #      wx.DLG_PNT(self.pnl1, 153,55))
        self.ragsoc2 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 148, 65), wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))          
        self.ragsoc4 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 148, 65), wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))          
        self.lindiriz = wx.StaticText(self.pnl1, -1, _("Indirizzo :"), 
              wx.DLG_PNT(self.pnl1, 10,82))
        self.indiriz = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,80), wx.DLG_SZE(self.pnl1, 170,cfg.DIMFONTDEFAULT))
        self.cdest = wx.Button(self.pnl1, Nid,  _(' Cliente '), 
              wx.DLG_PNT(self.pnl1, 218,80), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.rdest1 = wx.Button(self.pnl1, Nid, _("Annulla"), 
              wx.DLG_PNT(self.pnl1, 218,65),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        wx.StaticText(self.pnl1, -1, _("Citta' :"), wx.DLG_PNT(self.pnl1, 10,97))
        self.zona = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,95), wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl1, -1, _("CAP :"), wx.DLG_PNT(self.pnl1, 150,97))
        self.cap = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 180, 95), wx.DLG_SZE(self.pnl1, 35,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl1, -1, _("PR :"), wx.DLG_PNT(self.pnl1, 225,97))
        self.pr = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 243, 95), wx.DLG_SZE(self.pnl1, 20,cfg.DIMFONTDEFAULT))
        #self.lindiriz = wx.StaticText(self.pnl1, -1, "Destinaz:", 
        #      wx.DLG_PNT(self.pnl1, 10,79))
        self.indiriz1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,80), wx.DLG_SZE(self.pnl1, 170,cfg.DIMFONTDEFAULT))
        #self.cindiriz = wx.Button(self.pnl1, Nid, "...", 
        #     wx.DLG_PNT(self.pnl1, 220,77),
        #     wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.zona1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,95), wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))
        self.cap1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 180, 95), wx.DLG_SZE(self.pnl1, 35,cfg.DIMFONTDEFAULT))
        self.pr1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 243, 95), wx.DLG_SZE(self.pnl1, 20,cfg.DIMFONTDEFAULT))
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
        self.stt_doc1 = wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 280,122))  
        self.lcodage = wx.StaticText(self.pnl1, -1, _("Agente :"), 
              wx.DLG_PNT(self.pnl1, 10,144))
        self.codage = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,142), 
              wx.DLG_SZE(self.pnl1, 45,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)
        self.ccodage = wx.BitmapButton(self.pnl1, -1, png,#wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 93,142),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc1age = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 108,142), wx.DLG_SZE(self.pnl1, 100,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl1, -1, _("Pagamento :"), 
              wx.DLG_PNT(self.pnl1, 10,160))
        self.PAGAM = wx.ComboBox(self.pnl1, Nid,"",
              wx.DLG_PNT(self.pnl1, 60,158), wx.DLG_SZE(self.pnl1, 120,-1),
              [],wx.CB_DROPDOWN | wx.CB_SORT )
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
        self.rag_doc =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))
        self.campo1 =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))        
        self.campo2 =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl3, 280,37))
        self.lc = wx.ListCtrl(self.pnl2, Nid,
              wx.DLG_PNT(self.pnl2, 5,10), wx.DLG_SZE(self.pnl2, 323,95),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)   
        #wx.StaticLine(self.pnl, -1, wx.DLG_PNT(self.pnl, 5,155), 
        #      wx.DLG_SZE(self.pnl, 283,-1)) 
        self.lcod = wx.StaticText(self.pnl2, -1, _("Codice :"), 
              wx.DLG_PNT(self.pnl2, 5,112))
        self.codart = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 30,110), 
              wx.DLG_SZE(self.pnl2, 55,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)            
        self.ccodart = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 86,110),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH, cfg.btnSzeV))
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
              wx.DLG_SZE(self.pnl2, 130,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)                     
        self.cdescriz = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 315,110),
              wx.DLG_SZE(self.pnl2,cfg.btnSzeSH,cfg.btnSzeV))       
        wx.StaticText(self.pnl2, -1, _("UM :"), wx.DLG_PNT(self.pnl2, 5,127))
        self.UM = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 23,125), wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT))
        self.lmis = wx.StaticText(self.pnl2, -1, _("Mis :"), 
              wx.DLG_PNT(self.pnl2, 50,127))
        self.mis = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 70,125), wx.DLG_SZE(self.pnl2, 20,cfg.DIMFONTDEFAULT))                    
        wx.StaticText(self.pnl2, -1, _("Sc % :"), wx.DLG_PNT(self.pnl2, 95,127))
        self.sc1 = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 120,125), 
              wx.DLG_SZE(self.pnl2, 25, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        #self.sc1 = wx.SpinCtrl(self.pnl2, -1, "0.00",
        #      wx.DLG_PNT(self.pnl2, 120,125),
        #      wx.DLG_SZE(self.pnl2, 30,-1))
        self.lvALIVA = wx.StaticText(self.pnl2, -1, _("Cod. Iva :"), 
              wx.DLG_PNT(self.pnl2, 155,127))
        self.vALIVA = wx.TextCtrl(self.pnl2, Nid, "20",
              wx.DLG_PNT(self.pnl2, 190,125), 
              wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER  )
        self.cALIVA = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 215,125), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dALIVA = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 230,125), wx.DLG_SZE(self.pnl2, 95, cfg.DIMFONTDEFAULT))
        self.lvPDC = wx.StaticText(self.pnl2, -1, _("Cod. p.d.c. :"), 
              wx.DLG_PNT(self.pnl2, 235,127))
        self.vPDC = wx.TextCtrl(self.pnl2, Nid, "7501",
              wx.DLG_PNT(self.pnl2, 280,125), 
              wx.DLG_SZE(self.pnl2, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cvPDC = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 315,125),
              wx.DLG_SZE(self.pnl2,cfg.btnSzeSH,cfg.btnSzeV))            
        #self.lpeso = wx.StaticText(self.pnl2, -1, "Peso :", 
        #      wx.DLG_PNT(self.pnl2, 230,127))
        #self.peso = wx.TextCtrl(self.pnl2, Nid, "",
        #     wx.DLG_PNT(self.pnl2, 255,125), 
        #     wx.DLG_SZE(self.pnl2, 20,-1), wx.ALIGN_RIGHT)                    
        #self.lvolume = wx.StaticText(self.pnl2, -1, "volume :", 
        #     wx.DLG_PNT(self.pnl2, 280,127))
        #self.volume = wx.TextCtrl(self.pnl2, Nid, "",
        #     wx.DLG_PNT(self.pnl2, 300,125), 
        #     wx.DLG_SZE(self.pnl2, 20,-1), wx.ALIGN_RIGHT)
        self.llst = wx.StaticText(self.pnl2, -1, _("Listino :"), 
              wx.DLG_PNT(self.pnl2, 5,142))
        self.lst = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 33,140), 
              wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )   
        self.clst = wx.BitmapButton(self.pnl2, -1, png,#wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 57,140), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl2, -1, _("Colli :"), wx.DLG_PNT(self.pnl2, 73,142))
        self.colli = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 100,140), 
              wx.DLG_SZE(self.pnl2, 25, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )
        #self.lprovv = wx.StaticText(self.pnl2, -1, "Provv. :", 
        #      wx.DLG_PNT(self.pnl2, 73,142))
        #      wx.DLG_SZE(self.pnl2, 25, -1), wx.ALIGN_RIGHT )
        self.lcosto = wx.StaticText(self.pnl2, -1, _("Costo :"), 
              wx.DLG_PNT(self.pnl2, 132,142))
        self.costo = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 157,140), 
              wx.DLG_SZE(self.pnl2, 40, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )        
        self.lprezzo = wx.StaticText(self.pnl2, Nid, _("Prezzo :"), 
              wx.DLG_PNT(self.pnl2, 202,142))
        self.prezzo = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 232,140), 
              wx.DLG_SZE(self.pnl2, 45, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )      
        wx.StaticText(self.pnl2, -1, _("Q.ta`:"), wx.DLG_PNT(self.pnl2, 283,142))
        self.qt_1 = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 297,140), 
              wx.DLG_SZE(self.pnl2, 30, cfg.DIMFONTDEFAULT),
                         wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )
         #self.qt_1  = wx.SpinCtrl(self.pnl2, -1, "0.00",
         #     wx.DLG_PNT(self.pnl2, 295,140),
         #     wx.DLG_SZE(self.pnl2, 30,-1))
         #self.qt_1.SetRange(0.00,9999.99)
        self.importo = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))     
        self.ltotale = wx.StaticText(self.pnl2, -1, _("Totale :"), 
              wx.DLG_PNT(self.pnl2, 235,162))
        #self.ltotale.SetFont(self.font)
        #self.ltotale.SetForegroundColour(wx.Colour(128, 128, 128))
        self.totale = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 262,160), wx.DLG_SZE(self.pnl2, 65, cfg.DIMFONTDEFAULT),
                         wx.ALIGN_RIGHT )
        #self.totale.SetFont(self.font)
        #self.t_cpart = wx.TextCtrl(self.pnl2, -1, "", 
        #     wx.DLG_PNT(self.pnl2, 275,37))
        #self.sc1 = wx.TextCtrl(self.pnl2, -1, "", 
        #     wx.DLG_PNT(self.pnl2, 275,37))
        #self.ragsoc1age = wx.TextCtrl(self.pnl2, -1, "", 
        #     wx.DLG_PNT(self.pnl2, 275,37))
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
        self.vCONFEart = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.vIMBALart = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))                 
        self.codmerc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.qt_2 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.qt_3 = wx.TextCtrl(self.pnl2, -1, "",
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.prez_ag = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        #self.colli = wx.TextCtrl(self.pnl2, -1, "", 
        #     wx.DLG_PNT(self.pnl2, 285,137))  
        self.provv = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.peso = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.stt_doc2 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.annodoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))          
        self.tipodoc = wx.TextCtrl(self.pnl2, -1, "",    
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.datadoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.numdoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.vnum_mov = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.vdatamov = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.rigamag = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.rigaord = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.cod_mag = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.cambio = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.campo2_art = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.campo1_art = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.sbox_calce = wx.StaticBox(self.pnl3, Nid, " ",
              wx.DLG_PNT(self.pnl3, 5,10), wx.DLG_SZE(self.pnl3, 320,160))
        self.lASPET = wx.StaticText(self.pnl3, Nid, _("Aspetto :"), 
              wx.DLG_PNT(self.pnl3, 15,27))
        self.vASPET = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 55,25), 
              wx.DLG_SZE(self.pnl3, 35, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cASPET = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 95,25),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dASPET = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 110,25), wx.DLG_SZE(self.pnl3, 100, cfg.DIMFONTDEFAULT))
        self.lTRASP = wx.StaticText(self.pnl3, Nid, _("Trasporto :"), 
              wx.DLG_PNT(self.pnl3, 15,42))
        self.vTRASP = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 55,40), 
              wx.DLG_SZE(self.pnl3, 35, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cTRASP  = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 95,40),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dTRASP = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 110,40), wx.DLG_SZE(self.pnl3, 100, cfg.DIMFONTDEFAULT))

        self.ltot_colli = wx.StaticText(self.pnl3, Nid, _("Num. totale colli :"), 
              wx.DLG_PNT(self.pnl3, 215,27))
        self.tot_colli = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 275,25), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )

        self.ltot_peso = wx.StaticText(self.pnl3, Nid, _("Peso colli :"), 
              wx.DLG_PNT(self.pnl3, 215,42))
        self.tot_peso = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 275,40), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )

        self.lIMBAL = wx.StaticText(self.pnl3, Nid, _("Imballo :"), 
              wx.DLG_PNT(self.pnl3, 15,57))
        self.vIMBAL = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 55,55), 
              wx.DLG_SZE(self.pnl3, 35, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cIMBAL  = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 95,55),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dIMBAL = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 110,55), wx.DLG_SZE(self.pnl3, 100, cfg.DIMFONTDEFAULT))

        self.lCONSEG = wx.StaticText(self.pnl3, Nid, _("Consegna :"), 
              wx.DLG_PNT(self.pnl3, 15,72))
        self.vCONSEG = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 55,70), 
              wx.DLG_SZE(self.pnl3, 35, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cCONSEG  = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 95,70),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dCONSEG = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 110,70), wx.DLG_SZE(self.pnl3, 100, cfg.DIMFONTDEFAULT))
     
        self.lVETT = wx.StaticText(self.pnl3, Nid, _("Vettore :"), 
              wx.DLG_PNT(self.pnl3, 15,87))
        self.vVETT = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 55,85), 
              wx.DLG_SZE(self.pnl3, 35, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cVETT  = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 95,85),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dVETT = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 110,85), 
              wx.DLG_SZE(self.pnl3, 100, cfg.DIMFONTDEFAULT))

        self.ddata_tra = wx.StaticText(self.pnl3, -1, _("Data Trasporto:"), 
              wx.DLG_PNT(self.pnl3, 15,102))
        self.data_tra = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 75,100), 
              wx.DLG_SZE(self.pnl3, 50,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)

        self.dora_tra = wx.StaticText(self.pnl3, -1, _("Ora Trasporto:"),
              wx.DLG_PNT(self.pnl3, 135,102))
        self.ora_tra = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 190,100), wx.DLG_SZE(self.pnl3, 40,cfg.DIMFONTDEFAULT))

        #self.spinless_ctrl = wx.TimeCtrl( self.pnl3, 80, name = "spinless control" )
        #self.time24 = wx.TimeCtrl( self.pnl3, 50, fmt24hr = True, name = "24 hour control" )        
        #spin2 = wx.SpinButton( self.pnl3, 60, wx.DefaultPosition, wx.Size(-1,20), 0 )
        #self.time24.BindSpinButton( spin2 )        

        self.lnote_calce = wx.StaticText(self.pnl3, -1, _("Note :"), 
              wx.DLG_PNT(self.pnl3, 15,122))
        self.note_calce = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 45,120), wx.DLG_SZE(self.pnl3, 255,cfg.DIMFONTDEFAULT))        

        self.lscf = wx.StaticText(self.pnl3, Nid, _("Sconti finali :"), 
              wx.DLG_PNT(self.pnl3, 15,137))
        self.scf1 = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 60,135), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.scf2 = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 95,135), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.scf3 = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 130,135), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )        
	
        #inizio personalizza
        self.lvPDC_SC = wx.StaticText(self.pnl3, -1, _("Cod. p.d.c. :"),
              wx.DLG_PNT(self.pnl3, 165,137))
        self.vPDC_SC = wx.TextCtrl(self.pnl3, Nid, "6105",
              wx.DLG_PNT(self.pnl3, 205,135), 
              wx.DLG_SZE(self.pnl3, 30, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cvPDC_SC = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 240,135),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))  
        self.lvRACC = wx.StaticText(self.pnl3, -1, _("Ritenuta d'acconto :"), 
              wx.DLG_PNT(self.pnl3, 15,152))
        self.vRACC = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 80,150), 
              wx.DLG_SZE(self.pnl3, 20, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER  )
        self.cRACC = wx.BitmapButton(self.pnl3, -1, png,#wx.Button(self.pnl3, Nid, "...", 
              wx.DLG_PNT(self.pnl3, 102,150), 
              wx.DLG_SZE(self.pnl3,cfg.btnSzeSH,cfg.btnSzeV))
        self.dRACC = wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 115,150), wx.DLG_SZE(self.pnl3, 60, cfg.DIMFONTDEFAULT))
        
        self.ltotaledoc = wx.StaticText(self.pnl3, Nid, _("TotaleDocumento:"),
             wx.DLG_PNT(self.pnl3, 182,137))
        self.totaledoc =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 245, 135), 
              wx.DLG_SZE(self.pnl3, 70, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )

        self.ltotalepag = wx.StaticText(self.pnl3, Nid, _("Totale a pagare:"),
              wx.DLG_PNT(self.pnl3, 182,152))
        self.totalepag =  wx.TextCtrl(self.pnl3, Nid, "",
              wx.DLG_PNT(self.pnl3, 245, 150), 
              wx.DLG_SZE(self.pnl3, 70, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )  
        #fine personalizza

        self.cod_imb =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.iva_imb =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.prez_imb =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.cod_spe =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.iva_spe =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.prez_spe =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.cod_riv =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.iva_riv =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.prez_riv =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.cod_bol =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.iva_bol =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.prez_bol =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.cod_tra =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.iva_tra =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.prez_tra =  wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))
        self.campo1_calce = wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.campo2_calce = wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.fndvTIPO_DOC = wx.TextCtrl(self.pnl3, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.ok = wx.Button(self.pnl1, Nid, cfg.vcok, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))      
        self.new = wx.Button(self.pnl1, Nid, cfg.vcnew, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))      
        self.oktestata = wx.Button(self.pnl1, Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))              
        self.inte = wx.Button(self.pnl1, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 275,45), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self.pnl1, Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 275,45), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.modi = wx.Button(self.pnl1, Nid, cfg.vcmodi, 
              wx.DLG_PNT(self.pnl, 275,60), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.dele = wx.Button(self.pnl1, Nid, cfg.vcdele, 
              wx.DLG_PNT(self.pnl, 275,60), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa = wx.Button(self.pnl1, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 275,75), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.skanag = wx.Button(self.pnl1, Nid, cfg.vcanag, 
              wx.DLG_PNT(self.pnl, 275,90), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        ##self.selonnote = wx.Button(self.pnl1, Nid, "Visual. No&te", 
              ##wx.DLG_PNT(self.pnl, 275,80), 
              ##wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        ##self.seloffnote = wx.Button(self.pnl1, Nid, "Annulla No&te", 
              ##wx.DLG_PNT(self.pnl, 275,80), 
              ##wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
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

        #self.SetFont(self.font)
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        for x in self.pnl1.GetChildren(): x.SetFont(self.font)
        for x in self.pnl2.GetChildren(): x.SetFont(self.font)
        for x in self.pnl3.GetChildren(): x.SetFont(self.font)
        
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)

        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)


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
        #self.selonnote.Bind(wx.EVT_BUTTON, self.SelOnNote)
        #self.seloffnote.Bind(wx.EVT_BUTTON, self.SelOffNote)
        #self.bprezzo.Bind(wx.EVT_BUTTON, self.SelBprezzo)
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.ModiRow)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct) # occhio, dovrebbe essere self.lc
        self.lc.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlct) # occhio, dovrebbe essere self.lc
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) # occhio, dovrebbe essere self.lc       
        #self.pnl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct) # occhio, dovrebbe essere self.lc
        #self.pnl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlct) # occhio, dovrebbe essere self.lc
        #self.pnl.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) # occhio, dovrebbe essere self.lc
        #self.pnl.Bind(wx.EVT_LIST_KEY_DOWN, self.DblClick)
        self.qt_1.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        self.sc1.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        self.prezzo.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        #self.ccodcf.Bind(wx.EVT_BUTTON, self.FndCodCF)
        self.ccodage.Bind(wx.EVT_BUTTON, self.FndAge)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.cragsoc3.Bind(wx.EVT_BUTTON, self.FndAnagDest)             
        self.ccodart.Bind(wx.EVT_BUTTON, self.FndCodArt)
        self.ctesto.Bind(wx.EVT_BUTTON, self.OpenTesto) #personaliz testo			
        self.ccodinfo.Bind(wx.EVT_BUTTON, self.FndCodInfo)
        #self.cdescriz.Bind(wx.EVT_BUTTON, self.FndDescArt)    
        self.codart.Bind(wx.EVT_TEXT_ENTER, self.FndCodArt)
        self.descriz.Bind(wx.EVT_TEXT_ENTER, self.FndDesArt)  
        self.codage.Bind(wx.EVT_TEXT_ENTER, self.FndAge)
        #self.codcf.Bind(wx.EVT_TEXT_ENTER, self.FndCodCF)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.ragsoc3.Bind(wx.EVT_TEXT_ENTER, self.FndAnagDest)      
        self.ragsoc1.Bind(wx.EVT_CHAR, self.EvtChar)
        #self.note.Bind(wx.EVT_CHAR, self.EvtChar)
        self.cnum_doc.Bind(wx.EVT_BUTTON, self.FndVend)
        self.num_doc.Bind(wx.EVT_TEXT_ENTER, self.FndVend)
        self.data_doc.Bind(wx.EVT_TEXT_ENTER, self.CntData)
        self.data_tra.Bind(wx.EVT_TEXT_ENTER, self.CntData_Tra)
        self.vs_data.Bind(wx.EVT_TEXT_ENTER, self.CntvsData)
        #self.descriz.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_des)
        #self.datadoc.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_datadoc)
        #self.vsdata.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_vsdata)        
        self.cvsdata.Bind(wx.EVT_BUTTON, self.CntvsData)
        self.cdatadoc.Bind(wx.EVT_BUTTON, self.CntData)
        self.vs_ord.Bind(wx.EVT_CHAR, self.EvtChar)
        self.num_doc.Bind(wx.EVT_CHAR, self.EvtChar)
        self.codbar.Bind(wx.EVT_TEXT_ENTER, self.FndCodBar)
        self.ccodbar.Bind(wx.EVT_BUTTON, self.SelCodBar)
        self.codbar.Bind(wx.EVT_TEXT_ENTER, self.FndCodBar)
        self.cALIVA.Bind(wx.EVT_BUTTON, self.FndSelALIVA)
        self.vALIVA.Bind(wx.EVT_TEXT_ENTER, self.FndSelALIVA)
        self.cRACC.Bind(wx.EVT_BUTTON, self.FndSelRACC) #personaliz
        self.vRACC.Bind(wx.EVT_TEXT_ENTER, self.FndSelRACC) #personaliz
        self.colli.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_colli)
        self.vs_ord.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_vs_ord)
        #self.vsdata.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_vsdata)
        self.vsrif.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_vsrif)
        self.nsrif.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_nsrif)
        self.PAGAM.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_PAGAM)        
        self.note.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_note)
        self.vASPET.Bind(wx.EVT_TEXT_ENTER, self.FndASPET)
        self.cASPET.Bind(wx.EVT_BUTTON, self.FndASPET)
        self.vTRASP.Bind(wx.EVT_TEXT_ENTER, self.FndTRASP)
        self.cTRASP.Bind(wx.EVT_BUTTON, self.FndTRASP)
        self.vCONSEG.Bind(wx.EVT_TEXT_ENTER, self.FndCONSEG)
        self.cCONSEG.Bind(wx.EVT_BUTTON, self.FndCONSEG)
        self.vIMBAL.Bind(wx.EVT_TEXT_ENTER, self.FndIMBAL)
        self.cIMBAL.Bind(wx.EVT_BUTTON, self.FndIMBAL)
        self.vVETT.Bind(wx.EVT_TEXT_ENTER, self.FndCodVett)
        self.cVETT.Bind(wx.EVT_BUTTON, self.FndCodVett)
        self.tot_colli.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_tot_colli)
        self.tot_peso.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_tot_peso)        
        ##self.prezzo.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_prezzo)
        ##self.sc1.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_sc1)
        ##self.qt_1.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_qt_1)
        self.PAGAM.Bind(wx.EVT_COMBOBOX, self.SelPAGAM)
        self.TIPO_DOC.Bind(wx.EVT_COMBOBOX, self.SelTIPO_DOC)        
        self.cdest.Bind(wx.EVT_BUTTON, self.CDest)
        self.rdest1.Bind(wx.EVT_BUTTON, self.RDest)     
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.Bind(wx.EVT_CHAR, self.EvtCharS)       
        #self.ntbk.Bind(wx.EVT_CHAR, self.EvtCharS)
        
        self.Start(self)

    def Start(self, evt):
        self.dtesto.Show(False) # personalizza testo
        self.fndvTIPO_DOC.SetValue('')
        self.ccodinfo.Enable(False) 
        if self.vTIPO_DOC.GetValue()=='':self.vTIPO_DOC.SetValue(self.tipo_doc)
        self.cdest.SetLabel(_('Destinatario'))  ###############
        self.lst.Enable(False)
        self.lst.SetValue("1")
        self.vDIVvend.SetValue("EU")
        self.rag_doc.SetValue("A")
        #self.note.Enable(False)
        #self.note.Show(False)
        #self.note = ""
        self.campo1.SetValue("")
        self.campo2.SetValue("")     
        self.DelAnagTxt(self)
        self.DelArtTxt(self)
        self.OffAnagTxt(self)
        self.OffArtTxt(self)
        self.data = self.datacon #strftime("%d/%m/%Y")   
        self.data_doc.SetValue(self.data)
        self.data_tra.SetValue(self.data)
        self.vdata_doc.SetValue(self.data)
        self.data_doc.Enable(True)
        self.TIPO_DOC.Enable(True)        
        self.num_doc.Enable(True)
        self.cnum_doc.Enable(True)
        self.stt_doc1.SetValue("E")
        self.stt_doc2.SetValue("E")
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice")) # COD
        self.lc.InsertColumn(1, _("Descrizione")) # DESCRIZ
        self.lc.InsertColumn(2, _("Q.ta`")) # QT_1
        self.lc.InsertColumn(3, _("Prezzo")) # PREZ_UN
        self.lc.InsertColumn(4, _("Sc%")) # SC1
        self.lc.InsertColumn(5, _("Importo")) # TOT_RIGA
        self.lc.InsertColumn(6, _("Iva")) # ALIVA
        self.lc.InsertColumn(7, _("UM")) # UM
        self.lc.InsertColumn(8, _("Mis")) # MIS
        self.lc.InsertColumn(9, _("n riga")) # NUM_RIGA
        self.lc.InsertColumn(10, "") # CODBAR
        self.lc.InsertColumn(11, "") # CODMERC
        self.lc.InsertColumn(12, "") # QT_2
        self.lc.InsertColumn(13, "") # QT_3
        self.lc.InsertColumn(14, "") # PREZ_AG
        self.lc.InsertColumn(15, "") # SC2
        self.lc.InsertColumn(16, "") # SC3
        self.lc.InsertColumn(17, "") # PROVV
        self.lc.InsertColumn(18, "") # CAMBIO
        self.lc.InsertColumn(19, "") # COLLI
        self.lc.InsertColumn(20, "") # PESO
        self.lc.InsertColumn(21, "") # LST
        self.lc.InsertColumn(22, "") # PDC
        self.lc.InsertColumn(23, "") # ANNODOC
        self.lc.InsertColumn(24, "") # TIPODOC
        self.lc.InsertColumn(25, "") # DATADOC
        self.lc.InsertColumn(26, "") # NUMDOC
        self.lc.InsertColumn(27, "") # RIGAORD
        self.lc.InsertColumn(28, "") # RIGAMAG
        self.lc.InsertColumn(29, "") # RAG_DOC
        self.lc.InsertColumn(30, "") # CAMPO1
        self.lc.InsertColumn(31, "") # CAMPO2
        self.lc.InsertColumn(32, "") # STT_DOC
        self.lc.InsertColumn(33, "") # COD_MAG
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
        self.lc.SetColumnWidth(31, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(32, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(33, wx.DLG_SZE(self.pnl, 0,-1).width)
##        self.bprezzo.Enable(False)
##        self.bprezzo.SetLabel(" Prezzo &1 ")            
        self.sbox_cf.SetLabel(_(' Cliente '))
        self.tbl = "docu1"
##        self.t_cpart.SetValue("C") # valore tipo contro partita
        self.vPDC.SetValue("7501")
        self.vPDC_SC.SetValue("6105")
        self.UM.SetValue("PZ")
        self.vALIVA.SetValue("20")
        self.dALIVA.SetValue(_("Aliquota 20%"))
        self.vRACC.SetValue("")#personaliz
        self.dRACC.SetValue("")#personaliz
        self.lvPDC_SC.Show(False)#personaliz
        self.vPDC_SC.Show(False)#personaliz
        self.cvPDC_SC.Show(False)#personaliz
        self.vCONFEart.SetValue("CFCR")
        self.vIMBALart.SetValue("IMBCR")
        self.sTIPO_DOC = 'F1'
        if (self.tcpart=="C"): self.sbox_cf.SetLabel(_(' Cliente '))
        if (self.tcpart=="F"): self.sbox_cf.SetLabel(_(' Fornitore '))
        if self.vPAGAM.GetValue()=="" :
            self.vPAGAM.SetValue(cfg.tipopagam)
            self.sPAGAM = ""        
        if self.vIMBAL.GetValue()=='' or self.vIMBAL.GetValue()== 'None':
            self.vIMBAL.SetValue("IMBCR")           
        if self.vASPET.GetValue()=='' or self.vASPET.GetValue()== 'None':
            self.vASPET.SetValue("CFCR")           
        if self.vCONSEG.GetValue()=='' or self.vCONSEG.GetValue()== 'None':
            self.vCONSEG.SetValue("POR1")                           
        if self.vTRASP.GetValue()=='' or  self.vTRASP.GetValue()== 'None':
            self.vTRASP.SetValue("TRA1")
        self.SelTABGEN(self)
        if self.vVETT.GetValue()=='' or self.vVETT.GetValue()== 'None':
            self.vVETT.SetValue("1")
        self.FndCodVett(self)    
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
        self.cragsoc1.Show(True) 
        self.indiriz1.Show(True)
        if self.ccodbar.GetValue()==0:
            self.codart.Show(True)
            self.codbar.Show(False)            
        else:
            self.codart.Show(False) 
            self.codbar.Show(True)
        if (self.rec!=""):
            self.num_doc.SetValue(self.rec)
            self.FndVend(self)
        self.OffAll(self)
        self.ntbk.SetFocus() 
        self.ntbk.SetSelection(0)
        self.codbar.Show(False)
        self.num_doc.SetFocus()

    def EnableFalse(self, evt):
        self.skanag.Enable(False)
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
        self.clst.Enable(False)
        self.vDIVvend.Enable(False)
        self.lst.Enable(False)   
        self.rag_doc.Enable(False)        
        self.codcf.Enable(False)       
        self.ccodcf.Enable(False)        
        self.ragsoc1.Enable(False)
        self.cragsoc1.Enable(False)
        self.ragsoc2.Enable(False)       
        self.vTIPO_DOC.Enable(False)       
        self.cmpiliberi.Enable(False)        
        self.campo1.Enable(False)
        self.campo2.Enable(False)     
        self.ragsoc1age.Enable(False)
        self.vsrif.Enable(False)
        self.nsrif.Enable(False)    
        self.vs_ord.Enable(False)
        self.vs_data.Enable(False) 
        self.importo.Enable(False)        
        self.vdata_doc.Enable(False)
        self.data_tra.Enable(False)
        self.ora_tra.Enable(False) 
        self.cnum_doc.Enable(True)
        self.codmerc.Enable(False)
        self.qt_1.Enable(False)
        self.qt_2.Enable(False)
        self.qt_3.Enable(False)
        self.prez_ag.Enable(False)
        self.colli.Enable(False)
        self.peso.Enable(False)        
        self.stt_doc1.Enable(False)
        self.stt_doc2.Enable(False)
        self.annodoc.Enable(False)        
        self.tipodoc.Enable(False)
        self.datadoc.Enable(False)
        self.numdoc.Enable(False)
        self.campo2_art.Enable(False)
        self.campo1_art.Enable(False)
        self.totaledoc.Enable(False)        
        self.stampa.Enable(False)      
        self.modi.Enable(False)
        self.dele.Enable(False)        
        self.newr.Enable(False)
        self.okart.Enable(False)
        self.modir.Enable(False)
        self.intr.Enable(False)
        self.delr.Enable(False)
        self.ccodinfo.Enable(False)       
        self.ccodart.Enable(False)  
        self.ctesto.Enable(False) # personalizza testo
        self.PAGAM.Enable(False)
        self.vPAGAM.Enable(False)
        self.codage.Enable(False)
        self.ccodage.Enable(False)
        self.note.SetBackgroundColour(self.color)
        self.note.Enable(False)
        self.note_calce.SetBackgroundColour(self.color)
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
##        self.prezzo_ac.Enable(False)
##        self.prezzo_ac1.Enable(False)
        self.campo2_calce.Enable(False)
        self.campo1_calce.Enable(False)
        self.cRACC.Enable(False) #personaliz
        self.dRACC.Enable(False) #personaliz
        self.vRACC.Enable(False) #personaliz
        self.totalepag.Enable(False) #personaliz
        
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
        self.codmerc.Show(False)
        #self.qt_1.Show(False)
        self.qt_2.Show(False)
        self.qt_3.Show(False)
        self.prez_ag.Show(False)
        self.provv.Show(False)
        ##self.colli.Show(False)
        self.peso.Show(False)
        self.annodoc.Show(False)        
        self.tipodoc.Show(False)
        self.datadoc.Show(False)
        self.numdoc.Show(False)
        self.cod_imb.Show(False)  
        self.iva_imb.Show(False)
        self.prez_imb.Show(False)
        self.cod_spe.Show(False)
        self.iva_spe.Show(False)
        self.prez_spe.Show(False)
        self.cod_riv.Show(False)
        self.iva_riv.Show(False)
        self.prez_riv.Show(False)
        self.cod_bol.Show(False)
        self.iva_bol.Show(False)
        self.prez_bol.Show(False)
        self.cod_tra.Show(False)
        self.iva_tra.Show(False)
        self.prez_tra.Show(False)       
        self.rigaord.Show(False)
        self.rigamag.Show(False)
        self.campo2_art.Show(False)
        self.campo1_art.Show(False)
        self.cod_mag.Show(False)
        self.cambio.Show(False)
        self.sc2.Show(False)
        self.sc3.Show(False)
        self.nriga.Show(False)
        self.vUM.Show(False)
        self.vMERCE.Show(False)
        self.vinprod.Show(False)
        self.vDIVvend.Show(False)
        self.vTIPO_DOC.Show(False)
        self.fndvTIPO_DOC.Show(False)	
        self.rag_doc.Show(False)
        self.campo2.Show(False)
        self.campo1.Show(False)
        self.vCONFEart.Show(False)
        self.vIMBALart.Show(False)
        self.oktestata.Show(False)
        self.new.Enable(True)
        self.new.Show(True)
        self.ok.Show(False)
        self.canc.Show(True)
        self.modi.Show(True)
        self.dele.Show(False)
        self.stt_doc1.Show(False)
        self.stt_doc2.Show(False)
        self.inte.Show(False)
        self.campo2_calce.Show(False)
        self.campo1_calce.Show(False)
        self.dALIVA.Show(False)


    def StpSkAnag(self, evt):
    #<daniele> 
        codcf = self.codcf.GetValue()
        tcpart = self.tcpart
        tblanag = 'anag'
        import skprint
        valueSql = tcpart, codcf
        skprint.stampaDoc(
              conn = self.CnAz ,   #connessione
              tipo = 'sanag'+tcpart.lower(), #tipo documento e parametro
              parametriSql = valueSql,
              #datiazienda = self.dzDatiAzienda,
              anteprima = True )
    #</daniele>                            

    def CDest(self, evt):
        if self.cdest.GetLabel()== _('Destinatario'):  ############
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
##          self.stato1.Show(True)
##          self.localit1.Show(True)          
            self.indiriz.Show(False)
            self.cap.Show(False)
            self.zona.Show(False)       
            self.pr.Show(False)
##          self.localit1.Show(False)         
##          self.stato1.Show(False)
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
##          self.localit.Show(True)           
##          self.stato.Show(True)
            self.indiriz1.Show(False)
            self.cap1.Show(False)
            self.zona1.Show(False)       
            self.pr1.Show(False)
##          self.localit1.Show(False)         
##          self.stato1.Show(False)      
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

        
    def OffAll(self, evt):
        self.codcf.Enable(False)
        self.ccodcf.Enable(False)        
        self.ragsoc1.Enable(False)
        self.cragsoc1.Enable(False)
        self.ragsoc2.Enable(False)
        self.indiriz.Enable(False)
        self.zona.Enable(False)
        self.pr.Enable(False)
        self.cap.Enable(False)
        self.localit.Enable(False)
        self.stato.Enable(False)
        self.anno.Enable(False)
        self.vTIPO_DOC.Enable(False)
        self.clst.Enable(False)
        self.vDIVvend.Enable(False)
        self.rag_doc.Enable(False)
        self.vnum_mov.Show(False)
        self.vdatamov.Show(False)
        self.cmpiliberi.Enable(False)        
        self.campo1.Enable(False)
        self.campo2.Enable(False) 
        self.ragsoc1age.Enable(False)
        self.vsrif.Enable(False)
        self.nsrif.Enable(False)    
        self.vs_ord.Enable(False)
        self.vs_data.Enable(False)
        self.vdata_doc.Show(False)
        self.note.SetBackgroundColour(self.color)
        self.note_calce.SetBackgroundColour(self.color)
        self.prezzo1.Show(False)
        self.prezzo2.Show(False)
        self.importo.Enable(False)
        self.importo.Show(False)      
        self.vdata_doc.Enable(False)
        self.codmerc.Enable(False)
        self.qt_1.Enable(False)
        self.qt_2.Enable(False)
        self.qt_3.Enable(False)
        self.prez_ag.Enable(False)
        self.colli.Enable(False)
        self.peso.Enable(False)        
        self.stt_doc1.Enable(False)
        self.stt_doc2.Enable(False)
        self.annodoc.Enable(False)        
        self.tipodoc.Enable(False)
        self.datadoc.Enable(False)
        self.numdoc.Enable(False)
        self.campo2_art.Enable(False)
        self.campo1_art.Enable(False)
        self.cod_imb.Enable(False)
        self.iva_imb.Enable(False)
        self.prez_imb.Enable(False)
        self.cod_spe.Enable(False)
        self.iva_spe.Enable(False)
        self.prez_spe.Enable(False)
        self.cod_riv.Enable(False)
        self.iva_riv.Enable(False)
        self.prez_riv.Enable(False)
        self.cod_bol.Enable(False)
        self.iva_bol.Enable(False)
        self.prez_bol.Enable(False)
        self.cod_tra.Enable(False)
        self.iva_tra.Enable(False)
        self.prez_tra.Enable(False)
        #self.lc.SetFont(self.font)
        self.lc.SetBackgroundColour(self.color)
        self.lc.Enable(False)        
        self.ccodart.Enable(False)
        self.ccodinfo.Enable(False)
        self.PAGAM.Enable(False)
        self.vPAGAM.Enable(False)
        self.vPAGAM.Show(False)        
        self.codage.Enable(False)
        self.ccodage.Enable(False)
        self.note.SetBackgroundColour(self.color)
        self.note.Enable(False)
        self.note_calce.SetBackgroundColour(self.color)
        self.note_calce.Enable(False)
        self.scf1.Enable(False)
        self.scf2.Enable(False)
        self.scf3.Enable(False)
        self.tot_colli.Enable(False)
        self.tot_peso.Enable(False)        
        self.vIMBAL.Enable(False)
        self.cIMBAL.Enable(False)
        self.dIMBAL.Enable(False)
        self.vASPET.Enable(False)
        self.cASPET.Enable(False)
        self.dASPET.Enable(False)
        self.vCONSEG.Enable(False)
        self.cCONSEG.Enable(False)
        self.dCONSEG.Enable(False)
        self.vTRASP.Enable(False)
        self.dTRASP.Enable(False)
        self.cTRASP.Enable(False)
        self.campo2_calce.Enable(False)
        self.campo1_calce.Enable(False)
        self.vALIVA.Enable(False)
        self.cALIVA.Enable(False)
        self.dALIVA.Enable(False)
        self.vRACC.Enable(False) #personaliz
        self.cRACC.Enable(False) #personaliz
        self.dRACC.Enable(False) #personaliz        
        self.totalepag.Enable(False) #personaliz
        self.vVETT.Enable(False)
        self.dVETT.Enable(False)
        self.cVETT.Enable(False)
        self.vPDC.Enable(False)
        self.vPDC_SC.Enable(False)
        self.cvPDC.Enable(False)
        self.cvPDC_SC.Enable(False)
        self.totaledoc.Enable(False)
        self.data_tra.Enable(False)
        self.ora_tra.Enable(False)  
        
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

    def FndASPET(self, evt):        
        val = self.vASPET.GetValue().upper()
        cod = "CONFE"
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
            self.__MDI__.MsgErr("Vendite"," FndTABGENc Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.vASPET.SetValue(row[1].upper())
            self.dASPET.SetValue(row[2])
            self.vTRASP.SetFocus()
        elif (cnt_rec>1):
            try:
                import srctabg
            except :
                pass
            try:
                import base.srctabg
            except :
                pass

            control = ['Ricerca Tipo Imballo',self.vASPET,self.dASPET,self.FndASPET,'CONFE']     
            win = srctabg.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

       
    def FndTRASP(self, evt):        
        val = self.vTRASP.GetValue().upper()
        cod = "TRASP"
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
            self.__MDI__.MsgErr("Vendite"," FndTRASP Error %s" % (msg))
        self.CnAz.commit()
                
                        
        if (cnt_rec==1 and cnt_rec<2):
            self.vTRASP.SetValue(row[1].upper())
            self.dTRASP.SetValue(row[2])
            self.vIMBAL.SetFocus()
        elif (cnt_rec>1):
            try:
                import srctabg
            except :
                pass
            try:
                import base.srctabg
            except :
                pass
            control = ['Ricerca Causale Trasporto',self.vTRASP,self.dTRASP,self.FndTRASP,'TRASP']     
            win = srctabg.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

    def FndCONSEG(self, evt):        
        val = self.vCONSEG.GetValue().upper()
        cod = "PORTO"
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
            self.__MDI__.MsgErr("Vendite"," FndCONSEG Error %s" % (msg))
        self.CnAz.commit()
                
                        
        if (cnt_rec==1 and cnt_rec<2):
            self.vCONSEG.SetValue(row[1].upper())
            self.dCONSEG.SetValue(row[2])
            self.vVETT.SetFocus()
        elif (cnt_rec>1):
            try:
                import srctabg
            except :
                pass
            try:
                import base.srctabg
            except :
                pass
            control = ['Ricerca Consegna',self.vCONSEG,self.dCONSEG,self.FndCONSEG,'PORTO']     
            win = srctabg.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

    def FndIMBAL(self, evt):        
        val = self.vIMBAL.GetValue().upper()
        cod = "IMBAL"
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
            self.__MDI__.MsgErr("Vendite"," FndIMBA Error %s" % (msg))
        self.CnAz.commit()
                
                        
        if (cnt_rec==1 and cnt_rec<2):
            self.vIMBAL.SetValue(row[1].upper())
            self.dIMBAL.SetValue(row[2])
            self.vCONSEG.SetFocus()
        elif (cnt_rec>1):
            try:
                import srctabg
            except :
                pass
            try:
                import base.srctabg
            except :
                pass
            control = ['Ricerca Imballo',self.vIMBAL,self.dIMBAL,self.FndIMBAL,'IMBAL']     
            win = srctabg.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

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
            self.Start(self)
            self.cdest.SetLabel(_(' Cliente '))
            self.CDest(self)            

    def NewTxt(self, evt):
        self.OnAnagTxt(self)
        self.TIPO_DOC.Enable(False)
        self.num_doc.Enable(False)
        self.cnum_doc.Enable(False)
        self.data_doc.Enable(True)
        self.data_doc.SetFocus()
        self.new.Show(False)
        self.ok.Show(False)
        self.oktestata.Show(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.modi.Enable(False)

    def ModiTxt(self, evt):
        self.OnAnagTxt(self)
        self.cntr = "modi"
        self.TIPO_DOC.Enable(False)        
        self.num_doc.Enable(False)
        self.cnum_doc.Enable(False)
        self.data_doc.Enable(True)
        self.data_doc.SetFocus()
        self.new.Show(False)
        self.ok.Show(False)
        self.oktestata.Show(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.modi.Enable(False)
        self.modi.Show(False)
        self.dele.Show(True)
        self.dele.Enable(True)
        
    def KillFcs_vs_ord(self, evt):
        self.vs_data.SetFocus()
        
    ##def KillFcs_vsdata(self, evt):
    ##        self.ragsoc1.SetFocus()

    def KillFcs_tot_colli(self, evt):
        self.tot_peso.SetFocus()
        
    def KillFcs_tot_peso(self, evt):
        self.data_tra.SetFocus()
        
    def KillFcs_note(self, evt):
        self.codage.SetFocus()
        
    def KillFcs_vsrif(self, evt):
        self.nsrif.SetFocus()

    def KillFcs_nsrif(self, evt):
        self.note.SetFocus()

    def KillFcs_PAGAM(self, evt):
        self.oktestata.SetFocus()

    def KillFcs_colli(self, evt):
        self.qt_1.SetFocus()
    
    def CntvsData(self, evt):
        if (self.cntr=="new" or self.cntr=="modi"):
            cnt_gma = 0
            vsdata = self.vs_data.GetValue().strip()
            if vsdata!="":
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
                    if gg>0 and gg < 31:
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
            data_doc = self.data_doc.GetValue().strip()
            cnt_gma = 0
            gma = data_doc.split('/')
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
##                self.Message(cfg.msgdatano ,self.ttl)
##            else:
                gg = int(gma[0])
                mm = int(gma[1])
                aa = int(gma[2])
                if gg>0 and gg<=31:
                    cnt_gma+=1
                    if mm>=0 and mm<=12:
                        cnt_gma+=1
                        if aa==int(self.annoc):
                            cnt_gma+=1
                            if (self.vdata_doc.GetValue()=='') : self.vdata_doc.SetValue(data_doc)
                            vdata_doc = self.vdata_doc.GetValue()
                            vgma  = vdata_doc.split('/')
                            vgg = int(vgma[0])
                            vmm = int(vgma[1])
                            vaa = int(vgma[2])
                            vdata  = int(vgma[2]+vgma[1]+vgma[0])
                            data = int(gma[2]+gma[1]+gma[0])
                            self.vs_ord.SetFocus()
                            #print data,vdata
                            if data < vdata :
                                dlg = wx.MessageDialog(self,  _("Data ultima : ") + vdata_doc + "\r "+cfg.msgdatault  ,self.ttl, wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                                if dlg.ShowModal()==wx.ID_YES:
                                    self.vdata_doc.SetValue(self.data_doc.GetValue())
                                    self.data_doc.Enable(False)
                                    #self.vs_ord.SetFocus()
                                    dlg.Destroy()
                                else:
                                    self.data_doc.SetFocus()
                                    dlg.Destroy()
                            else:
                                self.vdata_doc.SetValue(self.data_doc.GetValue())
                                self.data_doc.Enable(False)
                if cnt_gma==2 and aa <> int(self.annoc):
                    self.Message(cfg.msgdataes + self.annoc,self.ttl)            
                elif cnt_gma!=3 : self.Message(cfg.msgdatano ,self.ttl)

    def CntData_Tra(self, evt):
        if (self.cntr=="new" or self.cntr=="modi"):    
            data_tra = self.data_tra.GetValue().strip()
            cnt_gma = 0
            gma = data_tra.split('/')
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
                if gg>0 and gg<=31:
                    cnt_gma+=1
                    if mm>=0 and mm<=12:
                        cnt_gma+=1
                        if aa==int(self.annoc):
                            cnt_gma+=1
                            vdata_doc = self.vdata_doc.GetValue()
                            vgma  = vdata_doc.split('/')
                            vgg = int(vgma[0])
                            vmm = int(vgma[1])
                            vaa = int(vgma[2])
                            vdata  = int(vgma[2]+vgma[1]+vgma[0])
                            data = int(gma[2]+gma[1]+gma[0])
                            self.ora_tra.SetFocus()
                            if data < vdata :
                                dlg = wx.MessageDialog(self,cfg.msgdatra ,self.ttl, wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                                if dlg.ShowModal()==wx.ID_YES:
                                    self.ora_tra.SetFocus()
                                    dlg.Destroy()
                                else:
                                    self.data_tra.SetFocus()
                                    dlg.Destroy()

                if cnt_gma==2 and aa <> int(self.annoc):
                    self.Message(cfg.msgdataes + self.annoc,self.ttl)            
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
            if (self.cntr=="new" or self.cntr=="modi"): self.ok.SetFocus()
        if evt_char==50: 
            self.ntbk.SetSelection(1)
            self.ntbk.SetFocus()
        if evt_char==51: self.ntbk.SetSelection(2)
        evt.Skip()  

       
    def OffAnagTxt(self, evt):
        self.num_doc.Enable(False)
        self.cnum_doc.Enable(False)
        self.data_doc.Enable(False)
        self.vs_ord.Enable(False)
        self.vs_data.Enable(False)        

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
        self.vASPET.Enable(True)
        self.cASPET.Enable(True)  
        self.vTRASP.Enable(True)
        self.cTRASP.Enable(True)        
        self.vCONSEG.Enable(True)
        self.cCONSEG.Enable(True)
        self.vIMBAL.Enable(True)
        self.cIMBAL.Enable(True)
        self.vVETT.Enable(True)
        self.cVETT.Enable(True)
        #self.vRACC.Enable(True)
        self.tot_colli.Enable(True)
        self.tot_peso.Enable(True)
        self.cdest.Enable(True)
        self.data_tra.Enable(True)
        self.ora_tra.Enable(True)
        self.cRACC.Enable(True) #personaliz
        self.dRACC.Enable(True) #personaliz
        self.vRACC.Enable(True) #personaliz
	
        
    def DelAnagTxt(self, evt):
        self.vASPET.SetValue("CFCR") 
        self.vTRASP.SetValue("TRA1")
        self.vIMBAL.SetValue("IMBCR")
        self.vCONSEG.SetValue("POR1")
        self.SelTABGEN(self)
        self.vVETT.SetValue("1")
        self.num_doc.SetValue('')
        self.vdata_doc.SetValue('')
        self.data_doc.SetValue('')
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
        #self.sc1.SetValue('')
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
##        self.reg_def.SetValue('N')
        self.vsrif.SetValue('')
        self.nsrif.SetValue('')
        self.ragsoc1age.SetValue('')
        self.totaledoc.SetValue('0,00')        
        self.prez_ag.SetValue('0,00')
        self.totale.SetValue('0,00')
        self.provv.SetValue('0,00')
        self.colli.SetValue('')
        self.peso.SetValue('')        
        self.tot_colli.SetValue('')
        self.tot_peso.SetValue('')
        self.data_tra.SetValue('')
        #self.ora_tra.SetValue('')
        self.dRACC.SetValue('') #personaliz
        self.vRACC.SetValue('') #personaliz
        self.totalepag.SetValue('0,00') #personaliz

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
            self.__MDI__.MsgErr("Vendite"," FndALIVA Error %s" % (msg))
        self.CnAz.commit()
                
        if (cnt_rec==1 and cnt_rec<2):
            self.dALIVA.SetValue(row[2])
            self.qt_1.SetFocus()
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
            self.__MDI__.MsgErr("Vendite"," FndSelALIVA Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.dALIVA.SetValue(row[2])
            ##self.costo_un.SetFocus()
            ##self.qt_1.SetFocus()
            self.colli.SetFocus()
        else:self.FndALIVA(self)

    def SelTABGEN(self, evt):     
        sql = " select * from tabgen "
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)                 
            while (1):
                row = cr.fetchone () 
                if row==None: 
                    break         
                if (row[0]=="PORTO"):
                    if (row[1]==self.vCONSEG.GetValue()):
                        self.dCONSEG.SetValue(str(row[2]))
                if (row[0]=="IMBAL"):
                    if (row[1]==self.vIMBAL.GetValue()):
                        self.dIMBAL.SetValue(str(row[2]))
                if (row[0]=="CONFE"):
                    if (row[1]==self.vASPET.GetValue()):
                        self.dASPET.SetValue(str(row[2]))
                if (row[0]=="TRASP"):
                    if (row[1]==self.vTRASP.GetValue()):
                        self.dTRASP.SetValue(str(row[2]))  
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," SelTABGEN Error %s" % (msg))
        self.CnAz.commit()
                
                                      
    def SelCOMBO(self, evt):      
        vPAGAM = self.vPAGAM.GetValue()
        self.PAGAM.Clear()
        vTIPO_DOC = self.vTIPO_DOC.GetValue()
        self.TIPO_DOC.Clear()
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
                if (row[0]=="TIPODOC"):
                    if (row[1]==vTIPO_DOC):self.sTIPO_DOC = row[2]
                    self.TIPO_DOC.Append(row[2],row[1])
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," Cerca PAGAM Error %s" % (msg))
        self.CnAz.commit()
        cntPAGAM = 0
        cntPAGAM = self.PAGAM.FindString(self.sPAGAM)
        self.PAGAM.Select(cntPAGAM)
        cntTIPO_DOC = 0
        cntTIPO_DOC = self.TIPO_DOC.FindString(self.sTIPO_DOC)
        self.TIPO_DOC.Select(cntTIPO_DOC)

    def SelPAGAM(self, evt):
        self.Sel(evt)
        self.vPAGAM.SetValue(self.cb_val)
        
    def SelTIPO_DOC(self, evt):
        self.Sel(evt)
        self.vTIPO_DOC.SetValue(self.cb_val)
        vTIPODOC = self.vTIPO_DOC.GetValue()
        self.stt_doc1.SetValue("E")
        self.stt_doc2.SetValue("E")
        if vTIPODOC=="B1" or vTIPODOC=="B2":
            self.stt_doc1.SetValue("C")
            self.stt_doc2.SetValue("C")
            self.tcpart = "C"
        if vTIPODOC=="B3" :
            self.stt_doc1.SetValue("F")
            self.stt_doc2.SetValue("F")
            self.tcpart = "F"
        if vTIPODOC=='R1' or vTIPODOC=='C1' or vTIPODOC=='F1' or vTIPODOC=='F1':
            self.data_tra.Show(False)
            self.ora_tra.Show(False)
            self.ddata_tra.Show(False)
            self.dora_tra.Show(False)
        else:
            self.data_tra.Show(True)
            self.ora_tra.Show(True)
            self.ddata_tra.Show(True)
            self.dora_tra.Show(True)              

    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str =  evt.GetString()     
        evt.Skip()
        
    def SetFcs(self, evt):
        #self.__MDI__.MsgErr("Vendite"," SetFocus"
        evt.Skip()
        

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
    ## Funzioni Lista ------------------------------------
        
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()
            
    def LstSlct(self, evt):      
        self.currentItem = evt.m_itemIndex
        self.codart.SetValue(self.lc.GetItemText(self.currentItem))
        self.descriz.SetValue(self.getColTxt(self.currentItem, 1))
        self.qt_1.SetValue(self.getColTxt(self.currentItem, 2))
        self.prezzo.SetValue(self.getColTxt(self.currentItem, 3))
        self.sc1.SetValue(self.getColTxt(self.currentItem, 4))
        self.importo.SetValue(self.getColTxt(self.currentItem, 5))
        self.vALIVA.SetValue(self.getColTxt(self.currentItem, 6))
        self.UM.SetValue(self.getColTxt(self.currentItem, 7))
        self.mis.SetValue(self.getColTxt(self.currentItem, 8))
        self.nriga.SetValue(self.getColTxt(self.currentItem, 9))
        self.codbar.SetValue(self.getColTxt(self.currentItem, 10))
        self.codmerc.SetValue(self.getColTxt(self.currentItem, 11))
        self.qt_2.SetValue(self.getColTxt(self.currentItem, 12))
        self.qt_3.SetValue(self.getColTxt(self.currentItem, 13))
        self.prez_ag.SetValue(self.getColTxt(self.currentItem, 14))
        self.sc2.SetValue(self.getColTxt(self.currentItem, 15))
        self.sc3.SetValue(self.getColTxt(self.currentItem, 16))
        self.provv.SetValue(self.getColTxt(self.currentItem, 17))
        self.cambio.SetValue(self.getColTxt(self.currentItem, 18))
        self.colli.SetValue(self.getColTxt(self.currentItem, 19))
        self.peso.SetValue(self.getColTxt(self.currentItem, 20))
        self.lst.SetValue(self.getColTxt(self.currentItem, 21))
        self.vPDC.SetValue(self.getColTxt(self.currentItem, 22))
        self.annodoc.SetValue(self.getColTxt(self.currentItem, 23))
        self.tipodoc.SetValue(self.getColTxt(self.currentItem, 24))
        self.datadoc.SetValue(self.getColTxt(self.currentItem, 25))        
        self.numdoc.SetValue(self.getColTxt(self.currentItem, 26))
        self.rigaord.SetValue(self.getColTxt(self.currentItem, 27))
        self.rigamag.SetValue(self.getColTxt(self.currentItem, 28))
        self.rag_doc.SetValue(self.getColTxt(self.currentItem, 29))
        self.campo1_art.SetValue(self.getColTxt(self.currentItem, 30))
        self.campo2_art.SetValue(self.getColTxt(self.currentItem, 31))
        self.stt_doc2.SetValue(self.getColTxt(self.currentItem, 32))
        self.cod_mag.SetValue(self.getColTxt(self.currentItem, 33))
        self.row = self.currentItem
        #print self.nriga.GetValue()
        self.SelRow(self)
        
    def LstAct(self, evt):
        self.SelRow(self)
        self.currentItem = evt.m_itemIndex

    def FndCodVett(self, evt):
        ## Funzione Cerca Codice
        self.dVETT.SetValue('')
        cnt_rec = 0
        cod = self.vVETT.GetValue()
        tcpart = 'V'
        sql = """ select * from anag
                where cod like "%s" and t_cpart = "%s" """
        valueSql = '%'+cod+'%',tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1    
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndCodVett Error %s" % (msg))
        self.CnAz.commit()
        #if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttl)
        if (cnt_rec==1 and cnt_rec<2): self.FndSelVett(row)
        elif (cnt_rec>1):
            try:
                import srcanag
            except :
                pass
            try:
                import base.srcanag
            except :
                pass
            control = [tcpart,self.vVETT,self.dVETT,self.FndCodVett]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else:
            self.tot_colli.SetFocus()


    def FndSelVett(self, evt):
        row = evt
        self.dVETT.SetValue(str(row[3]).title())
        self.tot_colli.SetFocus()


    def FndCodCFDest(self, evt):
        cnt_rec = 0
        val = self.ragsoc3.GetValue().upper()
        cod = self.codcf1.GetValue()
        sql = """ select * from tblcf
                where cod = "%s" and t_cpart = "%s" """
        valueSql = int(cod), self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1   
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndCodCFDest Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttldest)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnagDest(row)
        
    def FndAnagDest(self, evt):
        cnt_rec = 0
        val = self.ragsoc3.GetValue()
        cod = self.codcf1.GetValue()
        sql = """ select * from tblcf
                where rag_soc1 like "%s" and t_cpart = "%s" """
        valueSql = '%' + val.title() + '%', self.tcpart	
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndAnagDest Error %s" % (msg))
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
        cap1 = string.zfill(str(row[7]).strip(),5)#'%05s' % row[7]
        if cap1=="00000" : cap1  = ""
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
        
    def FndSelAnag(self, evt):
        row = evt
        ###print row
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
        self.sTIPO_DOC = self.tipo_doc
        self.vPAGAM.SetValue(str(row[42]))
        if self.vPAGAM.GetValue()== "":
            self.vPAGAM.SetValue(cfg.tipopagam)
            self.sPAGAM = ""
        self.SelCOMBO(self)
        self.OffAnagTxt(self)
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
           
    def FndSelVend(self, evt):
        if self.cntr=="new" :
            self.EnableFalse(self)
            self.oktestata.Show(False)
            self.new.Show(True)
        self.stampa.Enable(True) 
        self.skanag.Enable(True)   
        row = evt
        #print row
        self.vTIPO_DOC.SetValue(str(row[0]))
        self.anno.SetValue(str(row[1]))
        self.num_doc.SetValue(str(row[2]))
        self.vdata_doc.SetValue(str(row[3]))
        self.data_doc.SetValue(str(row[3]))
        self.codcf.SetValue(str(row[4]))
        self.ragsoc1.SetValue(str(row[5]))
        self.ragsoc2.SetValue(str(row[6]))
        self.indiriz.SetValue(str(row[7]))
        cap = string.zfill(str(row[8]).strip(),5)#'%05s' % row[8]
        if cap=="00000" : cap  = ""
        self.cap.SetValue(cap)
        self.zona.SetValue(str(row[9]))
        self.localit.SetValue(str(row[10]))
        self.pr.SetValue(str(row[11]))
        self.stato.SetValue(str(row[12]))        

        self.codcf1.SetValue(str(row[13]))
        self.ragsoc3.SetValue(str(row[14]))
        self.ragsoc4.SetValue(str(row[15]))
        self.indiriz1.SetValue(str(row[16]))
        cap1 = string.zfill(str(row[17]).strip(),5)#'%05s' % row[17]
        if cap1=="00000" : cap1  = ""
        self.cap1.SetValue(cap1)
        self.zona1.SetValue(str(row[18]))
        self.localit1.SetValue(str(row[19]))
        self.pr1.SetValue(str(row[20]))
        self.stato1.SetValue(str(row[21]))         
        self.lst.SetValue(str(row[23]))
        self.vs_ord.SetValue(str(row[24]))
        self.vs_data.SetValue(str(row[25]))     
        self.vDIVvend.SetValue(str(row[26]))
        codage = str(row[27])
        self.codage.SetValue(codage)
        if (codage!=""):self.FndAge(self)     
        self.vPAGAM.SetValue(str(row[28]))
        self.vCONSEG.SetValue(str(row[29]))
        self.vTRASP.SetValue(str(row[30]))
        self.vVETT.SetValue(str(row[31]))
        self.vsrif.SetValue(str(row[32]))
        self.nsrif.SetValue(str(row[33]))
        self.rag_doc.SetValue(str(row[34]))        
        #self.campo1.SetValue(str(row[35]))        
        self.campo2.SetValue(str(row[36]))
        self.note.SetValue(str(row[37]))
        #    DATI CALCE ------
        self.vRACC.SetValue(str(row[35])) #personaliz
        if self.vRACC.GetValue()!='': self.FndSelRACC(self) #personaliz
        
        self.vIMBAL.SetValue(str(row[38]))
        self.vASPET.SetValue(str(row[39]))
        self.__MDI__.CnvVM5(row[40])
        tot_colli = self.__MDI__.val
        self.tot_colli.SetValue(tot_colli)
        self.__MDI__.CnvVM5(row[41])
        tot_peso = self.__MDI__.val
        self.tot_peso.SetValue(tot_peso)        
        self.scf1.SetValue(str(row[42]))        
        self.scf2.SetValue(str(row[43]))  
        self.scf3.SetValue(str(row[44]))
        self.vPDC_SC.SetValue(str(row[45]))
        self.cod_imb.SetValue(str(row[46]))
        self.iva_imb.SetValue(str(row[47]))
        self.prez_imb.SetValue(str(row[48]))
        self.cod_spe.SetValue(str(row[49]))
        self.iva_spe.SetValue(str(row[50]))
        self.prez_spe.SetValue(str(row[51]))
        self.cod_riv.SetValue(str(row[52]))
        self.iva_riv.SetValue(str(row[53]))
        self.prez_riv.SetValue(str(row[54]))
        self.cod_bol.SetValue(str(row[55]))
        self.iva_bol.SetValue(str(row[56]))
        self.prez_bol.SetValue(str(row[57]))
        self.cod_tra.SetValue(str(row[58]))
        self.iva_tra.SetValue(str(row[59]))
        self.prez_tra.SetValue(str(row[60]))
        if row[61]==None:self.data_tra.SetValue('')
        else:self.data_tra.SetValue(str(row[61]))
        if row[62]==None:self.ora_tra.SetValue('00:00:00')
        else: self.ora_tra.SetValue(str(row[62]))          
        self.campo1_calce.SetValue(str(row[63]))  
        self.campo2_calce.SetValue(str(row[64]))  
        self.note_calce.SetValue(str(row[65]))
        self.stt_doc1.SetValue(str(row[66]))
        self.stt_doc2.SetValue(str(row[66]))
        self.SelCOMBO(self)
        self.FndVendCorpo(self)
        self.TIPO_DOC.Enable(False)
        self.num_doc.Enable(False)
        self.data_doc.Enable(False)
        self.SelTABGEN(self)
        self.FndCodVett(self)
        self.new.Enable(False)
        self.canc.Show(False)
        self.inte.Show(True)
        if self.stt_doc1.GetValue()=="E" and self.vTIPO_DOC.GetValue()=='B1':       
            self.Message(cfg.msgordicons,self.ttl)
            self.inte.SetFocus()
        else:
            self.modi.Enable(True)
            self.modi.SetFocus()
        
    def FndVend(self, evt):
        fndvTIPO_DOC = self.fndvTIPO_DOC.GetValue()
        vnumdoc = self.num_doc.GetValue()
        #if num_doc=="" :
        #    self.Message(cfg.msgass +" --> "+ self.ttl,self.ttl)
        if vnumdoc=='' : vnumdoc = 0		    
        #else:
        cnt_rec = 0   
        anno = self.anno.GetValue()
        vTIPO_DOC = self.vTIPO_DOC.GetValue()        
        if fndvTIPO_DOC !="" and self.rec=="":
            sql = """ select * from docu1 
                    where num_doc = "%s" and tipo_doc = "%s"  
                    and anno = "%s" """
            valueSql = int(vnumdoc), fndvTIPO_DOC, anno
        elif self.rec !="":
            sql = """ select * from docu1 
                    where num_doc = "%s" and tipo_doc = "%s"  
                    and anno = "%s" """
            valueSql = int(vnumdoc), vTIPO_DOC, anno		   
        elif int(vnumdoc) != 0 :
            sql = """ select * from docu1 
                    where num_doc = "%s" and anno = "%s" """
            valueSql = int(vnumdoc), anno
        else :
            sql = """ select * from docu1 
                    where tipo_doc = "%s" and anno = "%s" """
            valueSql = vTIPO_DOC, anno
        try:
             cr = self.CnAz.cursor ()
             cr.execute(sql % valueSql)
             rows = cr.fetchall()
             
             cnt_rec=len(rows)
             ####for row in rows:
             ####    cnt_rec+=1
        
        except StandardError, msg:
             self.__MDI__.MsgErr("Vendite"," FndVend Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgass +" --> "+ self.tbl,self.ttl)
        elif (cnt_rec==1): self.FndSelVend(rows[0])
        ####if (cnt_rec==1 and cnt_rec<2): self.FndSelVend(row)                                        
        ####elif (cnt_rec>1):
        else :
            import srcdoc 
            stt_doc = ''
            self.fndvTIPO_DOC.SetValue('')
            control = [self.vTIPO_DOC, self.anno, self.num_doc,
                self.vdata_doc, self.FndVend, stt_doc, self.fndvTIPO_DOC]   
            win = srcdoc.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)                        

    def FndVendCorpo(self, evt):
        rowlc = 0
        cnt_rec = 0
        num_doc = self.num_doc.GetValue()
        anno = self.anno.GetValue()
        vTIPO_DOC = self.vTIPO_DOC.GetValue()
        sql = """ select * from docu2 
                where num_doc = "%s" and tipo_doc = "%s" and anno = "%s"
                order by num_rig desc """
        valueSql = int(num_doc), vTIPO_DOC, anno
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows: 
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount() 
                    self.__MDI__.CnvVMQT(row[11])
                    qt_1 = self.__MDI__.val
                    self.__MDI__.CnvVMQT(row[12])
                    qt_2 = self.__MDI__.val
                    self.__MDI__.CnvVMQT(row[13])
                    qt_3 = self.__MDI__.val
                    self.__MDI__.CnvVMPZ(row[14])
                    prezzo = self.__MDI__.val
                    self.__MDI__.CnvVM(row[23])
                    colli = self.__MDI__.val
                    self.__MDI__.CnvVM(row[18])
                    sc1 = self.__MDI__.val
                    if (sc1==""):sc1 = "0,0"
                    self.__MDI__.CnvVM(row[19])
                    sc2 = self.__MDI__.val
                    self.__MDI__.CnvVM(row[20])
                    sc3 = self.__MDI__.val
                    self.__MDI__.CnvVM(row[16])
                    tot_riga = self.__MDI__.val
                    self.lc.InsertStringItem(rowlc, row[5]) # COD
                    self.lc.SetStringItem(rowlc, 1, row[8]) # DESCRIZ
                    self.lc.SetStringItem(rowlc, 2, qt_1) # QT_1
                    self.lc.SetStringItem(rowlc, 3, prezzo) # PREZ_UN
                    self.lc.SetStringItem(rowlc, 4, sc1) # SC1
                    self.lc.SetStringItem(rowlc, 5, tot_riga) # TOT_RIGA
                    self.lc.SetStringItem(rowlc, 6, row[17]) # ALIVA
                    self.lc.SetStringItem(rowlc, 7, row[9]) # UM       
                    self.lc.SetStringItem(rowlc, 8, row[10]) # MIS
                    self.lc.SetStringItem(rowlc, 9, str(row[4])) # NUM_RIGA
                    self.lc.SetStringItem(rowlc, 10, str(row[6])) # CODBAR
                    self.lc.SetStringItem(rowlc, 11, row[7]) # CODMERC
                    self.lc.SetStringItem(rowlc, 12, qt_2) # QT_2
                    self.lc.SetStringItem(rowlc, 13, qt_3) # QT_3
                    self.lc.SetStringItem(rowlc, 14, str(row[15])) # PREZ_AG
                    self.lc.SetStringItem(rowlc, 15, sc2) # SC2       
                    self.lc.SetStringItem(rowlc, 16, sc3) # SC3
                    self.lc.SetStringItem(rowlc, 17, str(row[21])) #PROVV
                    self.lc.SetStringItem(rowlc, 18, str(row[22])) # CAMBIO
                    self.lc.SetStringItem(rowlc, 19, colli ) # COLLI
                    self.lc.SetStringItem(rowlc, 20, str(row[24])) # PESO
                    self.lc.SetStringItem(rowlc, 21, str(row[25])) # LST
                    self.lc.SetStringItem(rowlc, 22, str(row[26])) # PDC
                    self.lc.SetStringItem(rowlc, 23, str(row[27])) # ANNODOC
                    self.lc.SetStringItem(rowlc, 24, str(row[28])) # TIPODOC
                    self.lc.SetStringItem(rowlc, 25, str(row[29])) # DATADOC
                    self.lc.SetStringItem(rowlc, 26, str(row[30])) # NUMDOC
                    self.lc.SetStringItem(rowlc, 27, str(row[31])) # RIGAORD
                    self.lc.SetStringItem(rowlc, 28, str(row[32])) # RIGAMAG
                    self.lc.SetStringItem(rowlc, 29, str(row[33])) # RAG_DOC
                    self.lc.SetStringItem(rowlc, 30, str(row[34])) # CAMPO1
                    self.lc.SetStringItem(rowlc, 31, str(row[35])) # CAMPO2
                    self.lc.SetStringItem(rowlc, 32, str(row[36])) # STT_DOC
                    self.lc.SetStringItem(rowlc, 33, str(row[3])) # COD_MAG
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndVendCorpo Error %s" % (msg))
        self.CnAz.commit()
        self.CalcTotale(self)
        
    def Modi(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgmodi_doc, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.ModiTxt(self)
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
        if self.num_doc.GetValue()=='1':
            dlg = wx.MessageDialog(self, cfg.msgdele_doc,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal()==wx.ID_YES:
                self.cntr = ""
                vTIPO_DOC = self.vTIPO_DOC.GetValue()
                vanno = self.anno.GetValue()
                vnum_doc = self.num_doc.GetValue()
                vdocu_dele = vTIPO_DOC,vanno,int(vnum_doc)
                try:
                    cr = self.CnAz.cursor()
                    sql = """ delete from docu1  
                              where tipo_doc = "%s" 
                              and anno = "%s" and num_doc = "%s" """                    
                    cr.execute(sql % vdocu_dele)
                except StandardError, msg:
                        self.__MDI__.MsgErr("Vendite"," Dele modi docu1 Error %s" % (msg))
                self.CnAz.commit()
                try:
                    cr = self.CnAz.cursor()
                    sql = """ delete from docu2  
                              where tipo_doc = "%s" 
                              and anno = "%s" and num_doc = "%s" """                      
                    cr.execute(sql % vdocu_dele)  
                except StandardError, msg:
                        self.__MDI__.MsgErr("Vendite"," Dele modi docu2 Error %s" % (msg))
                self.CnAz.commit()
                self.DelAnagTxt(self)
                self.Start(self)
                dlg.Destroy()
            else:
                self.cntr = ""
                dlg.Destroy()

    def OkTestata(self, evt):
        if (self.codcf.GetValue()==""):
            self.Message(cfg.msgnocod,self.ttl)
            self.ragsoc1.SetFocus()
        else:
            self.voktestata = 1
            self.codage.Enable(False)
            self.ccodage.Enable(False)
            self.ragsoc1.Enable(False)
            self.cragsoc1.Enable(False)
            self.nsrif.Enable(False)
            self.vsrif.Enable(False)
            self.note.SetBackgroundColour(self.color)
            self.note.Enable(False)
            self.note_calce.SetBackgroundColour(self.color)
            self.note_calce.Enable(False)

            self.PAGAM.Enable(False)
            self.lc.SetBackgroundColour(wx.Colour(255, 255, 255))
            self.lc.Enable(True)
            if (self.cntr=="new" or self.cntr=="modi"):
                self.OffAnagTxt(self)
                self.oktestata.Show(False)
                self.new.Show(False)
                self.ok.Show(True)
                self.ok.Enable(True)
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
            self.__MDI__.MsgErr("Vendite"," FndAge max Error %s" % (msg))
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
            self.__MDI__.MsgErr("Vendite"," FndAge Error %s" % (msg))
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
        self.PAGAM.SetFocus()

    def FndCodCF(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        cod = self.codcf.GetValue()
        sql = """ select * from anag 
                where cod = "%s" and t_cpart = "%s" """
        valueSql = int(cod), self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1  
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndCodCF Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)
      
    def FndAnag(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().title()
        cod = self.codcf.GetValue()
        sql = """ select * from anag 
                where rag_soc1 like "%s" and t_cpart = "%s" """
        valueSql = '%'+ val +'%', self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndAnag Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
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
        ##self.provv.Enable(False)
        self.colli.Enable(False)
        self.costo.Enable(False)
        self.qt_1.Enable(False)
        self.prezzo.Enable(False)
        self.sc1.Enable(False)
        self.vALIVA.Enable(False)
        self.cALIVA.Enable(False)
        #self.nriga.Enable(False)
        self.peso.Enable(False)
##        self.volume.Enable(False)
        self.totale.Enable(False)
        self.vinprod.Enable(False)
        self.UM.Enable(False)
        self.vMERCE.Enable(False)
        self.vIMBALart.Enable(False)
        self.vCONFEart.Enable(False)
        self.modir.Enable(False)
        self.okart.Enable(False)
        self.modir.Show(True)
        self.okart.Show(False)
        self.intr.Enable(False)
        self.delr.Enable(False)
        self.newr.Enable(True)
        self.newr.SetFocus()
        #self.lc.Enable(False)
        #self.note.SetBackgroundColour(self.color)

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
        #self.vALIVA.Enable(False)
        #self.cvALIVA.Enable(False)
        self.nriga.Enable(False)
        self.peso.Enable(False)
        #self.volume.Enable(False)
        self.totale.Enable(False)
        self.vinprod.Enable(False)
        self.UM.Enable(False)
        self.vMERCE.Enable(False)
        self.vIMBALart.Enable(False)
        self.vCONFEart.Enable(False)
        #self.lc.Enable(False)
        #self.bprezzo.Enable(False)
        #self.note.SetBackgroundColour(self.color)
        
    def OnArtTxt(self, evt):
        self.lc.SetBackgroundColour(self.color)
        self.lc.Enable(False)
        self.codart.Enable(True)
        self.ccodart.Enable(True)
        self.codbar.Enable(True)
        self.ccodbar.Enable(True)
        self.ctesto.Enable(True) # personalizza testo	
        self.ccodinfo.Enable(True)
        self.descriz.Enable(True)
        self.cdescriz.Enable(True)
        self.UM.Enable(True)
        self.mis.Enable(True)
        ##self.provv.Enable(True)
        self.colli.Enable(True)
        self.prezzo.Enable(True)
        self.sc1.Enable(True)
        self.qt_1.Enable(True)
        self.vALIVA.Enable(True)
        self.cALIVA.Enable(True)
              
    def NewRow(self, evt):
        self.OnArtTxt(self)
        self.DelArtTxt(self)
        self.cntr_row = "new"
        #if self.ccodbar.GetValue()==0:self.codart.SetFocus()
        #else:self.codbar.SetFocus()
        if self.ccodbar.GetValue()==False :
            self.codart.Show(True)
            self.codbar.Show(False)
            self.codart.SetFocus()
        else:
            self.codart.Show(False)
            self.codbar.Show(True)
            self.codbar.SetFocus()	
        self.descriz.SetFocus()
        self.newr.Enable(False)
        self.intr.Enable(True)
        self.modir.Enable(False)
        self.okart.Enable(True)
        self.modir.Show(False)
        self.okart.Show(True)
        
    def ModiRow(self, evt):
        self.OnArtTxt(self)   
        self.cntr_row = "modi"
        self.qt_1.SetFocus()
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
        self.qt_1.SetValue('')
##        self.volume.SetValue('')
        self.peso.SetValue('')
        self.colli.SetValue('')
        self.prez_ag.SetValue('0,00')
        #self.vALIVA.SetValue('')


    def CalcSaldo(self,evt):
        if self.prezzo_ac.GetValue()=='':self.prezzo_ac.SetValue('0')
        if self.totaledoc.GetValue()=='':self.totaledoc.SetValue('0')        
        if self.totalepag.GetValue()=='':self.totalepag.SetValue('0') #personaliz
        totordi = self.totaledoc.GetValue()
        accordi = self.prezzo_ac.GetValue()

    def CalcTotale(self,evt):
        tot_colli = 0
        pagare = 0
        importo = 0
        imponibile = 0        
        iva = 0
        for x in range(self.lc.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxt(x, 19))
            colli_row = float(self.__MDI__.val)
            tot_colli+=colli_row	
            self.__MDI__.CnvPM(self.getColTxt(x, 5))
            imponibile_row = float(self.__MDI__.val)
            self.__MDI__.CnvPM(self.getColTxt(x, 6))
            iva_row = self.__MDI__.val              
            if (type(iva_row)==float) :
                iva+=imponibile_row*iva_row/100
            imponibile+=imponibile_row
        racc = self.vRACC.GetValue()
        if racc=='': racc='0' 
        self.__MDI__.CnvPM(racc) 
        iva_racc = self.__MDI__.val  
        importo = imponibile+iva 
        pagare = importo-(imponibile*iva_racc/100)  
        self.__MDI__.CnvVM(imponibile)
        self.totale.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(importo)
        self.totaledoc.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(pagare)  
        self.totalepag.SetValue(self.__MDI__.val)  
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
            #self.lc.SetItemState(self.row, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
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
        self.lc.SetStringItem(self.row, 2, self.qt_1.GetValue())
        self.lc.SetStringItem(self.row, 3, self.prezzo.GetValue())
        self.lc.SetStringItem(self.row, 4, self.sc1.GetValue())
        self.lc.SetStringItem(self.row, 5, self.importo.GetValue())
        self.lc.SetStringItem(self.row, 6, self.vALIVA.GetValue())
        self.lc.SetStringItem(self.row, 7, self.UM.GetValue())        
        self.lc.SetStringItem(self.row, 8, self.mis.GetValue())
        self.lc.SetStringItem(self.row, 9, self.nriga.GetValue())
        self.lc.SetStringItem(self.row, 10, self.codbar.GetValue())
        self.lc.SetStringItem(self.row, 11, self.codmerc.GetValue())
        self.lc.SetStringItem(self.row, 12, self.qt_2.GetValue())
        self.lc.SetStringItem(self.row, 13, self.qt_3.GetValue())
        self.lc.SetStringItem(self.row, 14, self.prez_ag.GetValue())
        self.lc.SetStringItem(self.row, 15, self.sc2.GetValue())
        self.lc.SetStringItem(self.row, 16, self.sc3.GetValue())        
        self.lc.SetStringItem(self.row, 17, self.provv.GetValue())
        self.lc.SetStringItem(self.row, 18, self.cambio.GetValue())
        self.lc.SetStringItem(self.row, 19, self.colli.GetValue())
        self.lc.SetStringItem(self.row, 20, self.peso.GetValue())
        self.lc.SetStringItem(self.row, 21, self.lst.GetValue())
        self.lc.SetStringItem(self.row, 22, self.vPDC.GetValue())
        self.lc.SetStringItem(self.row, 23, self.annodoc.GetValue())        
        self.lc.SetStringItem(self.row, 24, self.tipodoc.GetValue())
        self.lc.SetStringItem(self.row, 25, self.datadoc.GetValue())  
        self.lc.SetStringItem(self.row, 26, self.numdoc.GetValue())
        self.lc.SetStringItem(self.row, 27, self.rigaord.GetValue())
        self.lc.SetStringItem(self.row, 28, self.rigamag.GetValue())
        self.lc.SetStringItem(self.row, 29, self.rag_doc.GetValue())
        self.lc.SetStringItem(self.row, 30, self.campo1_art.GetValue())
        self.lc.SetStringItem(self.row, 31, self.campo2_art.GetValue())
        self.lc.SetStringItem(self.row, 32, self.stt_doc2.GetValue())
        self.lc.SetStringItem(self.row, 33, self.cod_mag.GetValue())

    def OkRow(self, evt):
        cnt_val = 0
        valprezzo = self.prezzo.GetValue().replace(".","")
        valprezzo = valprezzo.replace(",","")
        valprezzo = valprezzo.replace("-","") 
        if (valprezzo!="" and valprezzo.isdigit()== True):
            self.__MDI__.CnvPM5(self.prezzo.GetValue())
            vprezzo = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgprezno,self.ttl)
            self.prezzo.SetFocus()
        sc1 = self.sc1.GetValue().replace(",","")  
        if (sc1!="" and sc1.isdigit()== True):
            self.__MDI__.CnvPM(self.sc1.GetValue())
            vsc1 = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgscno,self.ttl)
            self.sc1.SetFocus()
        qt_1 = self.qt_1.GetValue().replace(",","") 
        if (qt_1!="" and qt_1.isdigit()== True):
            self.__MDI__.CnvPM(self.qt_1.GetValue())
            vqt_1 = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgqtno,self.ttl)
            self.qt_1.SetFocus()
        if (cnt_val==3):
            importo = (vprezzo*vqt_1)-(vprezzo*vqt_1*vsc1/100)
            self.__MDI__.CnvVM(importo)
            self.importo.SetValue(self.__MDI__.val)
            self.OffArtTxt(self)
            if ( self.cntr_row=="new"):
                self.row = self.lc.GetItemCount()
                nriga  = self.row+1
                self.nriga.SetValue(str(nriga*10))
                self.RmpRow(self)
            if ( self.cntr_row==""):
                self.RmpRow(self)
                self.lc.DeleteItem(self.row+1)
                self.lc.SetItemState(self.row-1, wx.LIST_STATE_SELECTED,
                                wx.LIST_STATE_SELECTED)
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
        self.__MDI__.CnvVMPZ(row[7])
        self.costo.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVMPZ(row[5])
        self.prezzo1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVMPZ(row[6])
        self.prezzo2.SetValue(self.__MDI__.val)
        self.prezzo.SetValue(self.prezzo1.GetValue())        
        self.codbar.SetValue(str(row[1]))          
        self.vALIVA.SetValue(str(row[11]))
        self.vMERCE.SetValue(str(row[8]))
        self.vIMBALart.SetValue(str(row[23]))
        self.vCONFEart.SetValue(str(row[24]))
        self.peso.SetValue(str(row[25]))
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
        sql = """ select * from articoli 
                where cod like "%s" order by cod asc """
        valueSql = '%'+cod+'%'
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndCodArt Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
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
        sql = """ select * from articoli 
                where codbar = "%s" order by cod asc """
        valueSql = cod
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1 
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," FndCodBar Error %s" % (msg))
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
            self.__MDI__.MsgErr("Vendite"," FndArt Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelArt(row)

    def FndArtSel(self, evt):
        self.okart.Enable(True)
        self.okart.SetFocus()
    
    #<daniele> 
    def Stampa(self, evt):   
        anno = self.anno.GetValue()
        num_doc = self.num_doc.GetValue()
        tipo_doc = self.vTIPO_DOC.GetValue()
        import skprint
        valueSql = anno,tipo_doc,num_doc
        if self.vRACC.GetValue()!='': tipo_doc = 'f2ra' #personalizza
        skprint.stampaDoc(
              conn = self.CnAz , #connessione
              tipo = tipo_doc, #tipo documento e parametro
              parametriSql = valueSql,
              datiazienda = self.dzDatiAzienda,
              anteprima = True )
    #</daniele>  
    

    def New(self, evt):
        self.IntTestata(self)
        self.NewTxt(self)	
        self.cntr = "new"
        vTIPODOC = self.vTIPO_DOC.GetValue()
        if vTIPODOC=="B1" or vTIPODOC=="B2":
            self.stt_doc1.SetValue("C")
            self.stt_doc2.SetValue("C")
        if vTIPODOC=="B3" :
            self.stt_doc1.SetValue("F")
            self.stt_doc2.SetValue("F")
        registro = vTIPODOC
        anno = self.anno.GetValue()
        chiave = "RVEN"
        ## Funzione Nuovo
        sql = """ select * from libriaz 
                  where chiave = "%s" and anno = "%s"
                  and registro = "%s" """ 
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % (chiave,anno,registro))
            while (1):
                row = cr.fetchone()
                if row==None:
                    break
                if (row[3]==None or row[3] =="") : self.num_doc.SetValue('1')
                else: self.num_doc.SetValue(str(int(row[3])+1))
                if (row[16]==None or row[16] =="") : self.vdata_doc.SetValue(self.data)
                self.vdata_doc.SetValue(row[16])
                self.data_doc.SetValue(self.data)
                self.CntData(self)
                self.data_doc.Enable(True)
                self.data_doc.SetFocus()
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," New num_ord Error %s" % (msg))
        self.CnAz.commit()
        num_doc = int(self.num_doc.GetValue())
        registromag = "R1" 
        anno = self.anno.GetValue()
        chiavemag = "RMAG"   
        vnmov = 0
        ## Funzione Nuovo
        sqlmag = """ select * from libriaz 
                     where chiave = "%s" and anno = "%s"
                     and registro = "%s" """ 
        valueSql = chiavemag,anno,registromag
        try:
            crmag = self.CnAz.cursor ()
            crmag.execute(sqlmag % valueSql)
            while (1):
                rowmag = crmag.fetchone()
                if rowmag==None:
                    break
                if (rowmag[3]==None or rowmag[16] =="") : self.vnum_mov.SetValue('1')
                else: self.vnum_mov.SetValue(str(int(rowmag[3])+1))
                if (rowmag[16]==None or rowmag[16] =="") : self.vdatamov.SetValue(self.data)
                else: self.vdatamov.SetValue(rowmag[16])
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," New num_mov Error %s" % (msg))
        self.CnAz.commit()
        vnummov = int(self.vnum_mov.GetValue())
        self.vdatamov.SetValue(self.vdatamov.GetValue())
            
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
            vTIPO_DOC = self.vTIPO_DOC.GetValue()
            vanno = self.anno.GetValue()
            vnum_doc = int(self.num_doc.GetValue())            
            vdata_doc = self.data_doc.GetValue()
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
            vlst = int(self.lst.GetValue())
            vvsord = self.vs_ord.GetValue()  
            vvsdata = self.vs_data.GetValue()
            vdiv = self.vDIVvend.GetValue()
            vcodage = self.codage.GetValue()
            vPAGAM = self.vPAGAM.GetValue()              
            vvCONSEG = self.vCONSEG.GetValue()
            vvTRASP = self.vTRASP.GetValue()
            vvVETT = self.vVETT.GetValue()
            vvsrif = self.vsrif.GetValue()
            vnsrif = self.nsrif.GetValue()
            vrag_doc = self.rag_doc.GetValue()
            vcambio = 0 #self.cambio.GetValue()
            #vcampo1 = self.campo1.GetValue()
            vRACC = self.vRACC.GetValue()
            vcampo2 = self.campo2.GetValue()
            vnote = self.note.GetValue()
            vsttdoc1 = self.stt_doc1.GetValue()
            vd1_1 = vTIPO_DOC,vanno,vnum_doc,vdata_doc,vcod_cf,vragsoc1,vragsoc2
            vd1_1_modi = vdata_doc,vcod_cf,vragsoc1,vragsoc2
            vd1_2 = vindiriz,vcap,vzona,vlocalit,vpr,vstato,vcodcf1
            vd1_3 = vragsoc3,vragsoc4,vindiriz1,vcap1,vzona1,vlocalit1,vpr1,vstato1        
            vd1_4 = float(vcambio),vlst,vvsord,vvsdata
            vd1_5 = vdiv,vcodage,vPAGAM,vvCONSEG,vvTRASP,vvVETT
            vd1_6 = vvsrif,vnsrif,vrag_doc,vRACC,vcampo2,vnote
            vd1_6_modi = vTIPO_DOC,vanno,vnum_doc
            vdocu1 = vd1_1 + vd1_2 + vd1_3 + vd1_4 + vd1_5 + vd1_6 
            vdocu1_modi = vd1_1_modi + vd1_2 + vd1_3 + vd1_4 + vd1_5  + vd1_6 
            vvIMBAL = self.vIMBAL.GetValue()
            vvASPET = self.vASPET.GetValue()
            vtot_colli = self.tot_colli.GetValue()
            self.__MDI__.CnvPM(vtot_colli)
            vtot_colli = self.__MDI__.val
            vtot_peso = self.tot_peso.GetValue()
            self.__MDI__.CnvPM(vtot_peso)
            vtot_peso = self.__MDI__.val
            vsc1 = 0
            vsc2 = 0
            vsc3 = 0
            vvPDC_SC = self.vPDC_SC.GetValue()
            vcod_imb = self.cod_imb.GetValue()
            viva_imb = self.iva_imb.GetValue()
            vprez_imb = 0 #self.prez_imb.GetValue()
            vcod_spe = self.cod_spe.GetValue()
            viva_spe = self.iva_spe.GetValue()
            vprez_spe = 0 #self.prez_spe.GetValue()
            vcod_riv =  self.cod_riv.GetValue()
            viva_riv = self.iva_riv.GetValue()
            vprez_riv = 0 #self.prez_riv.GetValue()
            vcod_bol = self.cod_bol.GetValue()
            viva_bol = self.iva_bol.GetValue()
            vprez_bol = 0 #self.prez_bol.GetValue()
            vcod_tra = self.cod_tra.GetValue()
            viva_tra = self.iva_tra.GetValue()
            vprez_tra = 0#self.prez_tra.GetValue()
            vdata_tra = self.data_tra.GetValue()
            vora_tra = self.ora_tra.GetValue()           
            vcampo1_calce = 0#self.campo1_calce.GetValue()
            vcampo2_calce = 0#self.campo2_calce.GetValue()
            vnote_calce = self.note_calce.GetValue()
            vd3_1 = vvIMBAL,vvASPET,float(vtot_colli),float(vtot_peso)
            vd3_2 = float(vsc1),float(vsc2),float(vsc3),vvPDC_SC
            vd3_3 = vcod_imb,viva_imb,float(vprez_imb),vcod_spe,viva_spe,float(vprez_spe)
            vd3_4 = vcod_riv,viva_riv,float(vprez_riv)
            vd3_5 = vcod_bol,viva_bol,float(vprez_bol),vcod_tra,viva_tra,float(vprez_tra)
            vd3_6 = vdata_tra,vora_tra,float(vcampo1_calce),float(vcampo2_calce),vnote_calce,vsttdoc1
            vdocu3 = vd3_1 + vd3_2 + vd3_3 +vd3_4 + vd3_5 + vd3_6
            valueSql = vdocu1 + vdocu3
            if(vcntr=="new"):
                try:
                    cr = self.CnAz.cursor()
                    sql = """ insert into docu1
                              values("%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                      "%s","%s","%s","%s","%s","%s","%s","%s",
                                      "%s","%s","%s","%s","%s","%s","%s","%s",
                                      "%s","%s","%s","%s","%s","%s","%s","%s",
                                      "%s","%s","%s","%s","%s","%s","%s","%s",
                                      "%s","%s","%s","%s","%s","%s","%s","%s",
                                      "%s","%s","%s") """
                    cr.execute(sql % valueSql)  
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save insert docu1 Error %s" % (msg))
                self.CnAz.commit()
            if(vcntr=="modi"):
                valueSql = vdocu1_modi + vdocu3 + vd1_6_modi
                try:
                    cr = self.CnAz.cursor()
                    sql = """ update docu1 set data_doc = "%s" ,  
                              cod_cf = "%s" , rag_soc1 = "%s" , rag_soc2 = "%s" ,
                              indiriz = "%s" , cap = "%s" , zona = "%s" ,
                            localit = "%s" , pr = "%s" , stato = "%s" , 
                            cod_dest = "%s" , rag_soc3 = "%s" , 
                            rag_soc4 = "%s" , indiriz1 = "%s" , cap1 = "%s" , 
                            zona1 = "%s" , localit1 = "%s" , pr1 = "%s" ,
                            stato1 = "%s" , cambio = "%s" , lst = "%s" ,
                            vsord = "%s" , vsdata = "%s" , vdiv = "%s" , 
                            cod_age = "%s" , pagam = "%s" , conse = "%s" ,  
                              trasp = "%s" , cod_vet = "%s" , vsrif = "%s" ,
                            nsrif = "%s" , rag_doc = "%s" , campo1 = "%s" , 
                            campo2 = "%s" , note = "%s", imbal = "%s", 
                            aspet = "%s", colli = "%s", peso = "%s", 
                            sc1 = "%s", sc2 = "%s", sc3 = "%s", pdc_sc = "%s",
                              cod_imb = "%s", iva_imb = "%s", prez_imb = "%s", 
                              cod_spe = "%s" , iva_spe = "%s", prez_spe = "%s",
                              cod_riv = "%s", iva_riv = "%s", prez_riv = "%s", 
                              cod_bol = "%s" , iva_bol = "%s", prez_bol = "%s",
                              cod_tra = "%s" , iva_tra = "%s", prez_tra = "%s", 
                            data_tra = "%s", ora_tra = "%s", campo3 = "%s",
                            campo4 = "%s", note1 = "%s", stt_doc = "%s" 
                              where tipo_doc = "%s" and anno = "%s" and num_doc = "%s" """
                    cr.execute(sql % valueSql)
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save update docu1 Error %s" % (msg))
                self.CnAz.commit()
                valueSql = vTIPO_DOC,vanno,vnum_doc
                try:
                    cr = self.CnAz.cursor()
                    sql = """ delete from docu2  
                              where tipo_doc = "%s" and anno = "%s" 
                              and num_doc = "%s" """                   
                    cr.execute(sql % valueSql)
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save dele modi docu2 Error %s" % (msg))
                self.CnAz.commit()
                valueSql = vTIPO_DOC,vanno,str(vnum_doc)
                try:
                    cr = self.CnAz.cursor()
                    sql = """ select * from movmag
                              where tipodoc = "%s" and annodoc = "%s" 
                              and numdoc = "%s" """
                    cr.execute(sql % valueSql)
                    rows = cr.fetchall()
                    for row in rows:
                        self.vnum_mov.SetValue(str(row[1]))
                        self.vdatamov.SetValue(str(row[2]))
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save select num_mov modi movmag Error %s" % (msg))
                self.CnAz.commit()
                vnummov = self.vnum_mov.GetValue()
                valueSql = int(vnummov), vanno
                try:
                    cr = self.CnAz.cursor()
                    sql = """ delete from movmag where num_mov = "%s" and anno = "%s" """                  
                    cr.execute(sql % valueSql)
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save dele modi movmag Error %s" % (msg))
                self.CnAz.commit()
            nrow = self.lc.GetItemCount() 
            for row in range(nrow):
                vcodart = self.getColTxt(row, 0)
                vdescriz = self.getColTxt(row, 1)        
                vqt_1 = self.getColTxt(row, 2)
                self.__MDI__.CnvPM(vqt_1)
                vqt_1 = self.__MDI__.val                  
                vprez_un = self.getColTxt(row, 3)
                self.__MDI__.CnvPM5(vprez_un)
                vprez_un = self.__MDI__.val
                vsc1 = self.getColTxt(row, 4)
                self.__MDI__.CnvPM(vsc1)
                vsc1 = self.__MDI__.val 
                vtot_riga = self.getColTxt(row, 5)
                self.__MDI__.CnvPM(vtot_riga)
                vtot_riga = self.__MDI__.val                
                vALIVA = self.getColTxt(row, 6)
                vUM = self.getColTxt(row, 7)
                if vUM=='':vUM = '--'
                vmis = self.getColTxt(row, 8)
                vnriga = int(self.getColTxt(row, 9))
                vcodbar = self.getColTxt(row, 10)
                vMERCE = self.getColTxt(row, 11)
                vqt_2 = 0 #12
                vqt_3 = 0 #13
                vprez_ag = self.getColTxt(row, 15)
                self.__MDI__.CnvPM5(vprez_ag)
                vprez_ag = self.__MDI__.val
                vsc2 = 0 #15
                vsc3 = 0 #16
                vprovv = self.getColTxt(row, 17)
                self.__MDI__.CnvPM(vprovv)
                vprovv = self.__MDI__.val
                vcambio = self.getColTxt(row, 18)
                self.__MDI__.CnvPM(vcambio)
                vcambio = self.__MDI__.val
                vcolli = self.getColTxt(row, 19)
                self.__MDI__.CnvPM(vcolli)
                vcolli = self.__MDI__.val
                vpeso = self.getColTxt(row, 20)
                self.__MDI__.CnvPM(vpeso)
                vpeso = self.__MDI__.val 
                vlst = self.getColTxt(row, 21)
                vpdc = self.getColTxt(row, 22)
                vannodoc = self.getColTxt(row, 23)                
                vtipodoc = self.getColTxt(row, 24)
                vdatadoc = self.getColTxt(row, 25)
                vnumdoc = self.getColTxt(row, 26)
                vrigadoc = self.getColTxt(row, 27)
                vrigamag = self.getColTxt(row, 28)
                vrag_doc = "A" #self.getColTxt(row, 29)
                vcampo1_corpo = self.getColTxt(row, 30)
                vcampo2_corpo = self.getColTxt(row, 31)
                vsttdoc2 = self.getColTxt(row, 32)
                vcod_mag =  self.getColTxt(row, 33)                
                if vcod_mag=="" : vcod_mag = "1"
                if vlst=="" : vlst = "1"
                if vqt_1==0.0 : vqt_1 = 0
                if vsttdoc2=="" : vsttdoc2 = self.stt_doc2.GetValue()
                vannodoc = vanno
                vd2_1 = vTIPO_DOC,vanno,vnum_doc,vcod_mag,vnriga,vcodart,vcodbar,vMERCE
                vd2_2 = vdescriz,vUM,vmis,vqt_1,vqt_2,vqt_3,vprez_un,vprez_ag
                vd2_3 = vtot_riga,vALIVA,vsc1,vsc2,vsc3,vprovv,vcambio
                vd2_4 = vcolli,vpeso,int(vlst),vpdc,vannodoc,vtipodoc,vdatadoc,vnumdoc
                vd2_5 = vrigadoc,vrigamag,vrag_doc,vcampo1_corpo,vcampo2_corpo,vsttdoc2
                vcauma = '901'#causale di magazzino
                if vTIPO_DOC=="B3" or vTIPO_DOC== "B2" or vTIPO_DOC== "B1":
                    vcauma = '902'#causale di magazzino
                if vTIPO_DOC=="C1":
                    vcauma = '801'#causale di magazzino
                vcfm = self.tcpart #C = cliente F = Fornitore M = magazzino
                vrigadoc = vnriga
                vdatadoc = vdata_doc
                vnumdoc = vnum_doc
                vnummov = self.vnum_mov.GetValue()
                # Valori movmag
                vm1 = vanno,int(vnummov),vdata_doc,vcauma,int(vcod_mag),vcfm,vcod_cf,vnriga
                vm2 = vcodart,vcodbar,vMERCE,vdescriz,vUM,vmis,vqt_1
                vm3 = vprez_un,vprez_ag,vtot_riga,vALIVA,vdiv,vcambio
                vm4 = vsc1,vsc2,vsc3,vlst,vannodoc,vTIPO_DOC,vdatadoc,str(vnumdoc)
                vm5 = vrigadoc,vcampo1_corpo,vcampo2_corpo

                valueSql = vd2_1 + vd2_2 + vd2_3 + vd2_4 + vd2_5
                try:
                    cr = self.CnAz.cursor()
                    sql = """ insert into docu2
                              values("%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s") """
                    cr.execute(sql % valueSql)
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save insert docu2 Error %s" % (msg))
                self.CnAz.commit()
                valueSql = vm1 + vm2 + vm3 + vm4 + vm5        	                            
                try:
                    cr = self.CnAz.cursor()
                    sql = """ insert into movmag
                              values("%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s") """
                    if str(vqt_1)!='0' : cr.execute(sql % valueSql)  
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save insert movmag Error %s" % (msg))
                self.CnAz.commit()
            if(vcntr=="new"):
                vTIPO_DOC = self.vTIPO_DOC.GetValue()
                REG = 0
                if vTIPO_DOC=="B3" or vTIPO_DOC== "B2" or vTIPO_DOC== "B1":
                    registro1 = "B1"
                    registro2 = "B2"
                    registro3 = "B3"
                    REG = 3
                if vTIPO_DOC=="F1" or vTIPO_DOC== "I1" or vTIPO_DOC== "F2":
                    registro1 = "F1"
                    registro2 = "I1"
                    registro3 = "F2"
                    REG = 3
                if vTIPO_DOC=="C1":
                    registro1 = "C1"
                    registro2 = ""
                    registro3 = ""
                    REG = 1
                chiave = "RVEN"
                valueSql1 = vnum_doc,vdata_doc,chiave,vanno,registro1
                valueSql2 = vnum_doc,vdata_doc,chiave,vanno,registro2
                valueSql3 = vnum_doc,vdata_doc,chiave,vanno,registro3
                try:
                    cr = self.CnAz.cursor()
                    sql = """ update libriaz set ultnum = "%s", udatreg = "%s" 
                              where chiave = "%s" and anno = "%s" and registro = "%s" """                    
                    cr.execute(sql % valueSql1)
                    if REG==3:cr.execute(sql % valueSql2)
                    if REG==3:cr.execute(sql % valueSql3) 
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save update lbriaz Error %s" % (msg))
                self.CnAz.commit()
                registro = "R1"
                chiave = "RMAG"
                vdatamov = self.vdata_doc.GetValue()
                vlibaz = int(vnummov),vdatamov,chiave,vanno,registro
                try:
                    cr = self.CnAz.cursor()
                    sql = """ update libriaz set ultnum = "%s", udatreg = "%s" 
                              where chiave = "%s" and anno = "%s" and registro = "%s" """                  
                    cr.execute(sql % vlibaz)  
                except StandardError, msg:
                    self.__MDI__.MsgErr("Vendite","Save update libriaz Error %s" % (msg))
                self.CnAz.commit()
            self.OffAnagTxt(self)
            self.OffArtTxt(self)
            self.OffAll(self)
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
        else:
            self.Message(cfg.msgass,self.ttl) 

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

    # modifica
    def FndRACC(self, evt):
        val = self.vRACC.GetValue()
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
            self.__MDI__.MsgErr("Vendite"," FndRACC Error %s" % (msg))
        self.CnAz.commit()
                
        if (cnt_rec==1 and cnt_rec<2):
            self.dRACC.SetValue(row[2])
            #self.qt_1.SetFocus()
        elif (cnt_rec>1):
            try:
                import srctabg
            except :
                pass
            try:
                import base.srctabg
            except :
                pass
            control = ['Ricerca Cod. IVA',self.vRACC,self.dRACC,self.FndSelRACC,'ALIVA']     
            win = srctabg.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

    def FndSelRACC(self, evt):
        val = self.vRACC.GetValue()
        if val=='0': 
            self.vRACC.SetValue('')
            self.dRACC.SetValue('')
            self.CalcTotale(self)    
        else:
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
                self.__MDI__.MsgErr("Vendite"," FndSelRACC Error %s" % (msg))
            self.CnAz.commit()
            self.CalcTotale(self)
            if (cnt_rec==1 and cnt_rec<2):
                self.dRACC.SetValue(row[2])
                self.colli.SetFocus()
            else:self.FndRACC(self)
        
    def is_look(self):
        if (self.cntr!="new" and self.cntr!="modi"): return False
        else : return True
        
    def data_reload(self,rec,cntrp):
        self.rec=rec
        if cntrp=='':self.tipo_doc = cfg.tipodoc 
        else :self.tipo_doc = cntrp
        self.tcpart = "C"
        if self.tipo_doc =='B3': self.tcpart = "F"
        self.Start(self)

