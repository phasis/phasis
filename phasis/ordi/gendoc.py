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
    return ConsolidaOrd(parent,cnt)
  
class ConsolidaOrd(wx.ScrolledWindow):
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
        #self.SetClientSize(wx.Size(600, 455))
        self.ttl = cnt[0]
        self.tcpart = "C"
        self.tblart = "articoli"
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        #self.font = self.GetFont()
        self.color = self.GetBackgroundColour()
        Nid = wx.NewId()
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz = self.__MDI__.GetConnAZ()
        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon = self.__MDI__.GetDataC()
        self.dzDatiAzienda = self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id = wx.NewId(), name = '',
              parent = self, pos = wx.Point(0, 0),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        self.lnum_ord = wx.StaticText(self.pnl, -1, _("Numero Ordine :"), 
              wx.DLG_PNT(self.pnl, 7,12))
        self.num_ord = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 65,10), 
              wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.cnum_ord = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...",  
              wx.DLG_PNT(self.pnl, 130,10),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))        
        self.rbFATTF2 = wx.RadioButton(self.pnl, Nid, _("Fattura Immediata"),
              wx.DLG_PNT(self.pnl, 150,5), 
              wx.DLG_SZE(self.pnl, 120,10))
        self.rbFATTI1 = wx.RadioButton(self.pnl, Nid, _("Fattura Accompagnatoria"),
              wx.DLG_PNT(self.pnl, 150,15), 
              wx.DLG_SZE(self.pnl, 120,10) )
        self.rbBOLL = wx.RadioButton(self.pnl, Nid, cfg.vcBOLL,
              wx.DLG_PNT(self.pnl, 150,25), 
              wx.DLG_SZE(self.pnl, 120,10))
        self.sbox_cf = wx.StaticBox(self.pnl, Nid, _(' Cliente '),
              wx.DLG_PNT(self.pnl, 5,35), wx.DLG_SZE(self.pnl, 265,65))
        self.lcodcf = wx.StaticText(self.pnl, -1, _("Codice"), 
              wx.DLG_PNT(self.pnl, 10,45))
        self.codcf = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 10, 55), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.codcf1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 10, 55), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT))
        self.ccodcf = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 55,55),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lragsoc = wx.StaticText(self.pnl, -1, _("Cessionario :"),       
              wx.DLG_PNT(self.pnl, 75,45))
        self.ragsoc1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 75,55), 
              wx.DLG_SZE(self.pnl, 120,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)    
        self.cragsoc1 = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 200,55),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc3 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 75,55), 
              wx.DLG_SZE(self.pnl, 120,cfg.DIMFONTDEFAULT))    
        self.cragsoc3 = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 200,55),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc2 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 148, 55), 
              wx.DLG_SZE(self.pnl, 100,cfg.DIMFONTDEFAULT))          
        self.ragsoc4 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 148, 55), 
              wx.DLG_SZE(self.pnl, 100,cfg.DIMFONTDEFAULT))          
        self.lindiriz = wx.StaticText(self.pnl, -1, _("Indirizzo :"), 
              wx.DLG_PNT(self.pnl, 10,72))
        self.indiriz = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,70), 
              wx.DLG_SZE(self.pnl, 170,cfg.DIMFONTDEFAULT))
        self.cdest = wx.Button(self.pnl, Nid,  _(' Cliente '), 
              wx.DLG_PNT(self.pnl, 218,70),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.rdest1 = wx.Button(self.pnl, Nid, _("Annulla"), 
              wx.DLG_PNT(self.pnl, 218,55),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        wx.StaticText(self.pnl, -1, _("Citta' :"), 
              wx.DLG_PNT(self.pnl, 10,87))
        self.zona = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,85), 
              wx.DLG_SZE(self.pnl, 100,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl, -1, _("CAP :"), 
              wx.DLG_PNT(self.pnl, 150,87))
        self.cap = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 180, 85), 
              wx.DLG_SZE(self.pnl, 35,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl, -1, _("PR :"),  
              wx.DLG_PNT(self.pnl, 225,87))
        self.pr = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 243, 85),
              wx.DLG_SZE(self.pnl, 20,cfg.DIMFONTDEFAULT))
        self.indiriz1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,70), 
              wx.DLG_SZE(self.pnl, 170,cfg.DIMFONTDEFAULT))
        self.zona1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,85), 
              wx.DLG_SZE(self.pnl, 100,cfg.DIMFONTDEFAULT))
        self.cap1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 180, 85), 
              wx.DLG_SZE(self.pnl, 35,cfg.DIMFONTDEFAULT))
        self.pr1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 243, 85), 
              wx.DLG_SZE(self.pnl, 20,cfg.DIMFONTDEFAULT))
        self.localit = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 280,37))
        self.stato = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 280,37))
        self.localit1 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 280,37))        
        self.stato1 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 280,37))       
        self.data_ord = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))                             
        self.codage = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))
        self.vPAGAM = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))
        self.data_tra = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))
        self.ora_tra = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))
        self.vTIPO_DOC = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))   
        self.vTIPO_ORD = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))           
        self.anno = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))   
        self.fndvTIPO_ORD = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 285,117))  	        
        self.vdata_ord = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 285,117))        
        self.lgendoc = wx.StaticText(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 7,182))
        self.lc = wx.ListCtrl(self.pnl, Nid,
              wx.DLG_PNT(self.pnl, 5,105), wx.DLG_SZE(self.pnl, 323,70),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)   
        self.ltotale = wx.StaticText(self.pnl, -1, _("Totale Documento:"), 
              wx.DLG_PNT(self.pnl, 185,182))
        #self.ltotale.SetFont(self.font)
        self.totale = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 262,180), 
              wx.DLG_SZE(self.pnl, 65, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        #self.totale.SetFont(self.font)
        self.stt_doc1 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 5,160))
        self.stt_doc2 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 5,170))  
        self.inte = wx.Button(self.pnl, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 275,10), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV)) 
        self.canc = wx.Button(self.pnl, Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 275,10), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.okconf = wx.Button(self.pnl, Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl, 275,25),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.join = wx.Button(self.pnl, Nid, cfg.vcjoin, 
              wx.DLG_PNT(self.pnl, 275,40), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV)) 
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

        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.num_ord.Bind(wx.EVT_TEXT_ENTER, self.FndOrd)
        self.cnum_ord.Bind(wx.EVT_BUTTON, self.FndOrd)
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.inte.Bind(wx.EVT_BUTTON, self.Start)
        self.okconf.Bind(wx.EVT_BUTTON, self.OkGDoc)
        self.join.Bind(wx.EVT_BUTTON, self.OkUnisci)
        self.rbFATTF2.Bind(wx.EVT_RADIOBUTTON, self.RadioB)        
        self.rbFATTI1.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.rbBOLL.Bind(wx.EVT_RADIOBUTTON, self.RadioB)    
        self.cdest.Bind(wx.EVT_BUTTON, self.CDest)
        self.rdest1.Bind(wx.EVT_BUTTON, self.RDest)     
        self.Bind(wx.EVT_CLOSE, self.Close)
        
        self.Start(self)
        
    def Start(self, evt):
        self.lc.Show(True)
        self.lc.Enable(False)
        self.cdest.SetLabel(_('Destinatario')) ####### mettere in cfg
        self.indiriz.SetValue('')
        self.zona.SetValue('')
        self.cap.SetValue('')
        self.localit.SetValue('')        
        self.pr.SetValue('--')        
        self.stato.SetValue('')
        self.indiriz1.SetValue('')
        self.zona1.SetValue('')
        self.cap1.SetValue('')
        self.localit1.SetValue('')        
        self.pr1.SetValue('--')        
        self.stato1.SetValue('')
        self.codage.SetValue('')
        self.vPAGAM.SetValue('')
        self.ragsoc2.SetValue('')    
        self.totale.SetValue('0,00')
        self.vTIPO_DOC.SetValue('B1')#str(cfg.tipodocGDoc))
        self.vTIPO_ORD.SetValue('OC')	
        self.rbFATTI1.SetValue(False)     
	self.rbFATTF2.SetValue(False)
        self.rbBOLL.SetValue(True)	
        self.stt_doc1.SetValue('')
        self.stt_doc2.SetValue('')
        self.lgendoc.SetLabel('')
        self.codcf.SetValue('')
        self.ragsoc1.SetValue('')
        self.num_ord.SetValue('')
        self.data_tra.SetValue('')
        self.ora_tra.SetValue('00:00:00')
        self.okconf.Show(True)
        self.ragsoc1.SetFocus()
        self.canc.Show(True)
        self.canc.Enable(True)
        self.LC_clear(self)
        self.lc.Enable(False)
        self.sbox_cf.SetLabel(_(' Cliente '))
        self.ShowFalse(self)
        self.EnableFalse(self)
	self.anno.SetValue(self.annoc)
	self.rbFATTI1.Enable(True)     
	self.rbFATTF2.Enable(True)
        self.rbBOLL.Enable(True)
	self.codcf.Enable(True)
	self.ccodcf.Enable(True)
	self.cragsoc1.Enable(True)
	self.ragsoc1.Enable(True)
	self.cnum_ord.Enable(True)
	self.num_ord.Enable(True)
        self.ragsoc1.SetFocus()


    def LC_clear(self, evt):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Descrizione"))
        self.lc.InsertColumn(2, _("Q.ta`"))
        self.lc.InsertColumn(3, _("Prezzo Un"))
        self.lc.InsertColumn(4, _("Importo"))
        self.lc.InsertColumn(5, _("Iva"))
        self.lc.InsertColumn(6, _("Sc%"))
        self.lc.InsertColumn(7, _("NRiga"))
        self.lc.InsertColumn(8, "")
        self.lc.InsertColumn(9, "")
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
        self.lc.InsertColumn(31, "")
        self.lc.InsertColumn(32, "")
        self.lc.InsertColumn(33, "")
        #self.lc.InsertColumn(34, "")
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self.pnl, 60,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self.pnl, 150,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self.pnl, 40,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self.pnl, 80,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self.pnl, 80,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self.pnl,  40,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self.pnl, 40,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(8, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(9, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(10, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(11, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(12, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(13, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(14, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(15, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(16, wx.DLG_SZE(self.pnl,  0,-1).width)
        self.lc.SetColumnWidth(17, wx.DLG_SZE(self.pnl,  0,-1).width)
        self.lc.SetColumnWidth(18, wx.DLG_SZE(self.pnl,  0,-1).width)
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
        #self.lc.SetColumnWidth(34, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetFont(self.font)
        self.lc.SetBackgroundColour(self.color)


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
        self.data_ord.Show(False)
        self.vTIPO_DOC.Show(False)
        self.vTIPO_ORD.Show(False)
        self.fndvTIPO_ORD.Show(False)        
	self.vdata_ord.Show(False)
        self.anno.Show(False)
        self.codage.Show(False)
        self.vPAGAM.Show(False)
        self.inte.Show(False)
        self.data_tra.Show(False)
        self.ora_tra.Show(False)
        self.stt_doc2.Show(False)
        self.stt_doc1.Show(False)
        
    def EnableFalse(self, evt):
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
        self.codage.Enable(False)
        self.vPAGAM.Enable(False)
        self.totale.Enable(False)
        self.vTIPO_DOC.Enable(False)    
        self.stt_doc1.Enable(False)        
        self.stt_doc2.Enable(False)
        self.okconf.Enable(False)
        self.inte.Enable(False)
        self.join.Enable(False)

    def CDest(self, evt):
        if self.cdest.GetLabel()== _('Destinatario'):
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

    def RadioB(self, evt):
	if self.rbFATTF2.GetValue()==True:
            self.vTIPO_DOC.SetValue("F2")
            self.rbFATTI1.SetValue(False)            
	    self.rbFATTF2.SetValue(True)
            self.rbBOLL.SetValue(False)
	    self.stt_doc1.SetValue('E')
            self.stt_doc2.SetValue('E')	
        elif self.rbBOLL.GetValue()==True:
            self.vTIPO_DOC.SetValue("B1")
            self.rbFATTI1.SetValue(False)            
	    self.rbFATTF2.SetValue(False)
            self.rbBOLL.SetValue(True)
            self.stt_doc1.SetValue('C')
            self.stt_doc2.SetValue('C')
        elif self.rbFATTI1.GetValue()==True:
            self.vTIPO_DOC.SetValue("I1")
            self.rbFATTI1.SetValue(True)            
	    self.rbFATTF2.SetValue(False)
            self.rbBOLL.SetValue(False)
            self.stt_doc1.SetValue('E')
            self.stt_doc2.SetValue('E')
        self.ragsoc1.SetFocus()
            
    def CalcTotale(self,evt):
        importo = 0
        for x in range(self.lc.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxt(x, 4))
            importo_row = float(self.__MDI__.val)  
            importo+=importo_row
        self.__MDI__.CnvVM(importo)
        self.totale.SetValue(self.__MDI__.val)

    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

    def OkUnisci(self, evt):
        self.LC_clear(self)
        nriga = 0
        nnriga = 0
        rowlc = 0
        vnord = 0
        cnt_rec = 0
        qt_tot = 0
        codcf = self.codcf.GetValue()
        vTIPO_ORD = "OC"
        vsttord = "C"
        sql = """ select tord, aaaa, nord, cod_mag, num_rig, cod, codbar, codmerc,
                  descriz,um,mis, sum(qt_ord) as qt,qt_con,qt_eva, prez_un,prez_ag, 
		  ((prez_un * sum(qt_ord))-((prez_un * sum(qt_ord)) * (sc1/100)))  as totale,
                  aliva, sc1, sc2, sc3, provv, datacons, colli, peso, lst, pdc, stt_ord,
                  annodoc,tipodoc,datadoc,numdoc,campo1,campo2
                  from 
		  (select tipo_ord as tord,anno as aaaa, num_ord as nord 
                   from ordi1 
                   where anno = "%s" and tipo_ord = "%s" and cod_cf = "%s" and stt_ord = "%s"  ),ordi2
                   where anno = aaaa and tipo_ord = tord and num_ord = nord  group by cod """
        valueSql = self.annoc, vTIPO_ORD, codcf, vsttord
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()
                    nnriga+=10
                    self.__MDI__.CnvVM(row[11])
                    qt_ord = self.__MDI__.val
                    self.__MDI__.CnvVM(row[12])
                    qt_con = self.__MDI__.val
                    self.__MDI__.CnvVM(row[13])
                    qt_eva = self.__MDI__.val
                    self.__MDI__.CnvVM5(row[14])
                    prez_un = self.__MDI__.val
                    self.__MDI__.CnvVM(row[18])
                    sc1 = self.__MDI__.val
                    if (sc1==""):sc1 = "0,0"
                    self.__MDI__.CnvVM(row[19])
                    sc2 = self.__MDI__.val
                    self.__MDI__.CnvVM(row[20])
                    sc3 = self.__MDI__.val
                    self.__MDI__.CnvVM(row[16])
                    tot_riga = self.__MDI__.val
                    self.lc.InsertStringItem(rowlc, str(row[5]))
                    self.lc.SetStringItem(rowlc, 1, str(row[8]))
                    self.lc.SetStringItem(rowlc, 2, str(qt_ord))
                    self.lc.SetStringItem(rowlc, 3, str(prez_un))
                    self.lc.SetStringItem(rowlc, 4, str(tot_riga))
                    self.lc.SetStringItem(rowlc, 5, str(row[17]))
                    self.lc.SetStringItem(rowlc, 6, str(sc1))
                    self.lc.SetStringItem(rowlc, 7, str(nnriga))
                    self.lc.SetStringItem(rowlc, 8, str(row[7]))
                    self.lc.SetStringItem(rowlc, 9, str(row[9]))        
                    self.lc.SetStringItem(rowlc, 10, str(row[10]))
                    self.lc.SetStringItem(rowlc, 11, str(row[3]))
                    self.lc.SetStringItem(rowlc, 12, str(row[12]))
                    self.lc.SetStringItem(rowlc, 13, str(row[13]))
                    self.lc.SetStringItem(rowlc, 14, str(row[6]))
                    self.lc.SetStringItem(rowlc, 15, str(row[15]))
                    self.lc.SetStringItem(rowlc, 16, str(row[2]))
                    self.lc.SetStringItem(rowlc, 17, str(row[1]))
                    self.lc.SetStringItem(rowlc, 18, str(row[0]))
                    self.lc.SetStringItem(rowlc, 19, str(row[19]))        
                    self.lc.SetStringItem(rowlc, 20, str(row[20]))
                    self.lc.SetStringItem(rowlc, 21, str(row[21]))
                    self.lc.SetStringItem(rowlc, 22, str(row[22]))
                    self.lc.SetStringItem(rowlc, 23, str(row[23]))
                    self.lc.SetStringItem(rowlc, 24, str(row[24]))
                    self.lc.SetStringItem(rowlc, 25, str(row[25]))
                    self.lc.SetStringItem(rowlc, 26, str(row[26]))  
                    self.lc.SetStringItem(rowlc, 27, str(row[27]))
                    self.lc.SetStringItem(rowlc, 28, str(row[28]))
                    self.lc.SetStringItem(rowlc, 29, str(row[29]))
                    self.lc.SetStringItem(rowlc, 30, str(row[30]))
                    self.lc.SetStringItem(rowlc, 31, str(row[31]))
                    self.lc.SetStringItem(rowlc, 32, str(row[32]))
                    self.lc.SetStringItem(rowlc, 33, str(row[33]))
                    #self.lc.SetStringItem(rowlc, 34, str(row[4]))
        except StandardError, msg:
            self.__MDI__.MsgErr("gendoc"," OKUnisci Error %s " % (msg))
        self.CnAz.commit()
        self.lc.Enable(True)
        self.CalcTotale(self)
        
    def FndOrdCorpo(self, evt):
        nriga = 0
        nnriga = 0
        rowlc = 0
        vnord = 0
        cnt_rec = 0
        qt_tot = 0
        codcf = self.codcf.GetValue()
        vTIPO_ORD = "OC"
        vsttord = "C"
        vnumord = self.num_ord.GetValue()
        if vnumord!='' :
            sql1 = """ select * from ordi1
                       where num_ord = "%s" and tipo_ord = "%s"
                       and anno = "%s" and stt_ord = "%s" 
                       order by num_ord desc """
            valueSql1 = int(vnumord), vTIPO_ORD, self.annoc, vsttord
        else:
            sql1 = """ select * from ordi1 
                       where cod_cf = "%s" and tipo_ord = "%s"
                       and anno = "%s" and stt_ord = "%s" 
                       order by num_ord desc """
            valueSql1 = codcf, vTIPO_ORD, self.annoc, vsttord
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql1 % valueSql1)
            rows1 = cr.fetchall()
            if rows1==[]:
                self.Message(cfg.msgdatonocons,self.ttl)
                self.Start(self)
            else:
                self.rbFATTI1.Enable(False)     
                self.rbFATTF2.Enable(False)
                self.rbBOLL.Enable(False)
                self.codcf.Enable(False)
                self.ccodcf.Enable(False)
                self.cragsoc1.Enable(False)
                self.ragsoc1.Enable(False)
	        self.cnum_ord.Enable(False)
	        self.num_ord.Enable(False)	    
            for row1 in rows1:
                stt_ord = row1[13]
                vnumord = str(row1[2])
                dataord = str(row1[3])
                self.dataord = dataord
                self.codage.SetValue(str(row1[27]))
                self.vPAGAM.SetValue(str(row1[29]))
                if vTIPO_ORD=='OC': ttl = _("Ordine n.")   ######
		#if vTIPO_ORD=='OC': ttl = "Previsione d'ordine n."
		#if vTIPO_ORD=='IC': ttl = "Rapporto d'intervento n."
		sql2 = """ select * from ordi2 
	                   where num_ord = "%s" and tipo_ord = "%s"
		           and anno = "%s" order by num_rig desc """
	        valueSql2 = int(vnumord), vTIPO_ORD, self.annoc #, vsttord
		try:
		    cr = self.CnAz.cursor ()
		    cr.execute(sql2 % valueSql2)
		    rows = cr.fetchall()
		    for row in rows:
		        if row[5]!="--":
			    for rowlc in range(1):
			        row_lc = self.lc.GetItemCount()
			        nnriga+=10
			        if row_lc==0:
		                    self.lc.InsertStringItem(rowlc, "")
			            self.lc.SetStringItem(rowlc, 0,"--")
			            self.lc.SetStringItem(rowlc, 1, ttl +\
				          vnumord+ " del "+ dataord)
                                elif row[2]<vnord:
		                    self.lc.InsertStringItem(rowlc, "")
			            self.lc.SetStringItem(rowlc, 0,"--")
			            self.lc.SetStringItem(rowlc, 1, ttl +\
				          vnumord+ " del "+ dataord)
                                vnord = row[2]
				self.__MDI__.CnvVM(row[11])
				qt_ord = self.__MDI__.val
				self.__MDI__.CnvVM(row[12])
				qt_con = self.__MDI__.val
				self.__MDI__.CnvVM(row[13])
				qt_eva = self.__MDI__.val
				self.__MDI__.CnvVM5(row[14])
				prez_un = self.__MDI__.val
				self.__MDI__.CnvVM(row[18])
				sc1 = self.__MDI__.val
				if (sc1==""):sc1 = "0,0"
				self.__MDI__.CnvVM(row[19])
				sc2 = self.__MDI__.val
				self.__MDI__.CnvVM(row[20])
				sc3 = self.__MDI__.val
				self.__MDI__.CnvVM(row[16])
				tot_riga = self.__MDI__.val
				self.lc.InsertStringItem(rowlc, str(row[5]))
				self.lc.SetStringItem(rowlc, 1, str(row[8]))
				self.lc.SetStringItem(rowlc, 2, str(qt_ord))
				self.lc.SetStringItem(rowlc, 3, str(prez_un))
				self.lc.SetStringItem(rowlc, 4, str(tot_riga))
				self.lc.SetStringItem(rowlc, 5, str(row[17]))
				self.lc.SetStringItem(rowlc, 6, str(sc1))
				self.lc.SetStringItem(rowlc, 7, str(nnriga))
				self.lc.SetStringItem(rowlc, 8, str(row[7]))
				self.lc.SetStringItem(rowlc, 9, str(row[9]))  
				self.lc.SetStringItem(rowlc, 10, str(row[10]))
				self.lc.SetStringItem(rowlc, 11, str(row[3]))
				self.lc.SetStringItem(rowlc, 12, str(row[12]))
				self.lc.SetStringItem(rowlc, 13, str(row[13]))
				self.lc.SetStringItem(rowlc, 14, str(row[6]))
				self.lc.SetStringItem(rowlc, 15, str(row[15]))
				self.lc.SetStringItem(rowlc, 16, str(row[2]))
				self.lc.SetStringItem(rowlc, 17, str(row[1]))
				self.lc.SetStringItem(rowlc, 18, str(row[0]))
				self.lc.SetStringItem(rowlc, 19, str(row[19]))
				self.lc.SetStringItem(rowlc, 20, str(row[20]))
				self.lc.SetStringItem(rowlc, 21, str(row[21]))
				self.lc.SetStringItem(rowlc, 22, str(row[22]))
				self.lc.SetStringItem(rowlc, 23, str(row[23]))
				self.lc.SetStringItem(rowlc, 24, str(row[24]))	
				self.lc.SetStringItem(rowlc, 25, str(row[25]))
				self.lc.SetStringItem(rowlc, 26, str(row[26])) 
				self.lc.SetStringItem(rowlc, 27, str(row[27]))
				self.lc.SetStringItem(rowlc, 28, str(row[28]))
				self.lc.SetStringItem(rowlc, 29, str(row[29]))	
				self.lc.SetStringItem(rowlc, 30, str(row[30]))
				self.lc.SetStringItem(rowlc, 31, str(row[31]))
				self.lc.SetStringItem(rowlc, 32, str(row[32]))
				self.lc.SetStringItem(rowlc, 33, str(row[33]))
				#self.lc.SetStringItem(rowlc, 34, str(row[34]))
                except StandardError, msg:
                    self.__MDI__.MsgErr("gendoc"," FndOrdCorpo ordi2 Error %s " % (msg))
                self.CnAz.commit()			
        except StandardError, msg:
	    self.__MDI__.MsgErr("gendoc"," FndOrdCorpo ordi1 Error %s " % (msg)) 
        self.CnAz.commit()
        self.lc.Enable(True)
        self.CalcTotale(self)
       
    def FndAnag(self, evt):
        cnt_rec = 0
        self
        val = self.ragsoc1.GetValue()
        self.tcpart = "C"
        sql = """ select * from anag 
                  where rag_soc1 like "%s" and t_cpart = "%s" """
        valueSql = '%'+val.title()+'%', self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("gendoc"," FndAnag Error %s " % (msg))
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
            control = [self.tcpart, self.codcf, self.ragsoc1, self.FndCodCF]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else:
            self.ragsoc1.SetFocus()

    def FndCodCF(self, evt):
        cnt_rec = 0
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
            self.__MDI__.MsgErr("gendoc"," FndCodCF Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)

    def FndSelAnag(self, evt):
        row = evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.indiriz.SetValue(str(row[6]).title())
        self.zona.SetValue(str(row[8]).title())
        cap = string.zfill(str(row[7]).strip(),5) 
        self.cap.SetValue(cap)
        self.pr.SetValue(str(row[10]).upper())           
        self.okconf.Show(True)
        self.okconf.Enable(True)
        self.okconf.SetFocus()
        self.inte.Show(True)
        self.cdest.Enable(True)
        self.inte.Enable(True)
        ##self.join.Enable(True)
        self.canc.Enable(False)
        self.canc.Show(False)
        self.FndOrdCorpo(self)
                
    def EvtChar(self, evt):
        evt_char = evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()

    def EvtCharqt(self, evt):
        evt_char = evt.GetKeyCode()
        if (evt_char==27 and self.cntr_row==""):self.IntRow(self)
        evt.Skip()
                       
    def FndOrd(self, evt):
        cnt_rec = 0
        vnumord = self.num_ord.GetValue()
        if vnumord=='' :vnumord = 0
        vTIPO_ORD = "OC"
        sttord = "C"
        sql = """ select * from ordi1 where num_ord = "%s" and tipo_ord = "%s"
                  and anno = "%s" and stt_ord = "%s" """
        valueSql = int(vnumord), vTIPO_ORD, self.annoc, sttord
	if vnumord!=0:
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                self.__MDI__.MsgErr("gendoc"," FndOrd Error %s " % (msg))
            self.CnAz.commit()
	    if cnt_rec==0 :
	        self.Message(cfg.msgdatonocons,self.ttl)
                self.Start(self)
            elif (cnt_rec==1 and cnt_rec<2 ):
                self.num_ord.SetValue(str(row[2]))
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
                    cap1 = string.zfill(str(row[17]),5)
                    self.cap1.SetValue(cap1)
                self.__MDI__.CnvNone(row[18])
                self.zona1.SetValue(self.__MDI__.val)
                self.__MDI__.CnvNone(row[19])
                self.localit1.SetValue(self.__MDI__.val)
                self.__MDI__.CnvNone(row[20])
                self.pr1.SetValue(self.__MDI__.val)
                self.__MDI__.CnvNone(row[21])
                self.stato1.SetValue(self.__MDI__.val)
                codage = str(row[27])
                self.codage.SetValue(codage)
                self.okconf.Show(True)
                self.okconf.Enable(True)
                self.okconf.SetFocus()
                self.inte.Show(True)
                self.inte.Enable(True)
                self.canc.Enable(False)
                self.canc.Show(False)
                ##self.join.Enable(True)
                self.FndOrdCorpo(self)
	else: 
	    stt_ord = "C" 
            import srcord
	    control = [self.vTIPO_ORD, self.anno, self.num_ord,
	               self.vdata_ord, self.FndOrd, stt_ord, self.fndvTIPO_ORD]   	    
            win = srcord.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
		

    def OkGDoc(self, evt):
        dlg = wx.MessageDialog(self,cfg.msgconsdoc, self.ttl,
                    wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            dlg.Destroy()
            self.Save(self)
        else:
            dlg.Destroy()

        
    def Close(self, evt):
        if self.ragsoc1.GetValue()!="" or self.num_ord.GetValue()!="" :
            dlg = wx.MessageDialog(self,cfg.msgesci, self.ttl,
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

    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal()==wx.ID_OK:
            dlg.Destroy()

    def Save(self, evt):
        if(self.lc.GetItemCount()!=0 or self.codcf.GetValue()!="" ):
            vnriga = 0
            vnriga_uns = 0
            registro = self.vTIPO_DOC.GetValue() 
            chiave = "RVEN"   
            sql = """ select * from libriaz 
                      where chiave = "%s" and  anno = "%s" and  registro = "%s" """
            valueSql = chiave, self.annoc, registro
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
                while (1):
                    row = cr.fetchone()
                    if row==None:
                        break
                    if (row[3]==None) : vnum_doc = 1
                    if (row[3]!=None) : vnum_doc = (str(int(row[3])+1))
                    #if (row[16]==None) : vdata_doc = self.datacon
                    #if (row[16]!=None) : vdata_doc = row[16]
            except StandardError, msg:
                self.__MDI__.MsgErr("gendoc"," Save new num_doc Error %s " % (msg))
            self.CnAz.commit()
            vdata_doc = self.datacon
            vTIPO_DOC = registro
            vcod_cf = self.codcf.GetValue()
            vragsoc2 = self.ragsoc2.GetValue()
            vragsoc1 = self.ragsoc1.GetValue()
            vcodcf1 = ''
            vragsoc3 = ''
            vragsoc4 = ''
            vindiriz = self.indiriz.GetValue()
            vcap = int(self.cap.GetValue())
            vzona = self.zona.GetValue()
            vlocalit = self.localit.GetValue()
            vpr = self.pr.GetValue()
            vstato = self.stato.GetValue()
            vindiriz1 = self.indiriz1.GetValue()
            vcap1 = self.cap1.GetValue()
            if vcap1=='':vcap1 = 0
            else: vcap1 = int(vcap1)
            vzona1 = self.zona1.GetValue()
            vlocalit1 = self.localit1.GetValue()
            vpr1 = self.pr1.GetValue()
            vstato1 = self.stato1.GetValue()            
            vlst = 1
            vvsord = self.num_ord.GetValue()
            vvsdata = self.data_ord.GetValue()
            vdiv = "EU"
            vcodage = self.codage.GetValue()
            vPAGAM = self.vPAGAM.GetValue()              
            vvCONSEG = "POR1"
            vvTRASP = "TRA1"
            vvVETT = "1"
            vvsrif = ""
            vnsrif = ""
            vrag_doc = ""
            vcambio = 0
            vcampo1 = ""
            vcampo2 = ""
            vnote = ""
            vd1_1 = vTIPO_DOC,self.annoc,int(vnum_doc),vdata_doc,vcod_cf,vragsoc1,vragsoc2
            vd1_1_modi = vdata_doc,vcod_cf,vragsoc1,vragsoc2
            vd1_2 = vindiriz,vcap,vzona,vlocalit,vpr,vstato,vcodcf1
            vd1_3 = vragsoc3,vragsoc4,vindiriz1,vcap1,vzona1,vlocalit1,vpr1,vstato1                 
            vd1_4 = vcambio,vlst,vvsord,vvsdata
            vd1_5 = vdiv,vcodage,vPAGAM,vvCONSEG,vvTRASP,vvVETT
            vd1_6 = vvsrif,vnsrif,vrag_doc,vcampo1,vcampo2,vnote
            vd1_6_modi = vTIPO_DOC,self.annoc,int(vnum_doc)
            valueSql1 = vd1_1 + vd1_2 + vd1_3 + vd1_4 + vd1_5 + vd1_6
            valueSql_modi1 = vd1_1_modi + vd1_2 + vd1_3 + vd1_4 + vd1_5 + vd1_6 
            vvASPET = "CFSF"
            vvIMBAL = "IMBVS"
            vtot_colli = 0
            vtot_peso = 0
            vsc1 = 0
            vsc2 = 0
            vsc3 = 0
            vvPDC_SC = "6105"
            vcod_imb = ""
            viva_imb = ""
            vprez_imb = 0
            vcod_spe = ""
            viva_spe = ""
            vprez_spe = 0
            vcod_riv = ""
            viva_riv = ""
            vprez_riv = 0
            vcod_bol = ""
            viva_bol = ""
            vprez_bol = 0
            vcod_tra = ""
            viva_tra = ""
            vprez_tra = 0
            vdata_tra = self.data_tra.GetValue()
            vora_tra = self.ora_tra.GetValue()
            vcampo1_calce = 0
            vcampo2_calce = 0
            vnote_calce = ""
            vsttdoc1 = "C" #self.stt_doc1.GetValue()
            vd3_1 = vvIMBAL,vvASPET,vtot_colli,vtot_peso
            vd3_2 = vsc1,vsc2,vsc3,vvPDC_SC
            vd3_3 = vcod_imb,viva_imb,vprez_imb,vcod_spe,viva_spe,vprez_spe
            vd3_4 = vcod_riv,viva_riv,vprez_riv
            vd3_5 = vcod_bol,viva_bol,vprez_bol,vcod_tra,viva_tra,vprez_tra
            vd3_6 = vdata_tra,vora_tra,vcampo1_calce,vcampo2_calce,vnote_calce,vsttdoc1
            valueSql3 = vd3_1 + vd3_2 + vd3_3 +vd3_4 + vd3_5 + vd3_6
            registro = "R1" 
            chiave = "RMAG" 
            sql = """ select * from libriaz 
                      where chiave = "%s" and  anno = "%s" and  registro = "%s" """
            valueSql = chiave, self.annoc, registro
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
                while (1):
                    row = cr.fetchone()
                    if row==None:
                        break
                    if (row[3]==None) : self.vnum_mov = 1
                    if (row[3]!=None) : self.vnum_mov = str(int(row[3])+1)
                    #if (row[16]==None) : self.vdatamov = self.datacon
                    #if (row[16]!=None) : self.vdatamov = row[16]
            except StandardError, msg:
                self.__MDI__.MsgErr("gendoc"," Save new num_mov Error %s " % (msg))
            self.CnAz.commit()
            self.vdatamov = self.datacon
            valueSql = valueSql1 + valueSql3
            try:
                cr = self.CnAz.cursor()
                sql =  """ insert into docu1
                           values("%s","%s","%s","%s","%s","%s","%s","%s","%s",
                                  "%s","%s","%s","%s","%s","%s","%s","%s","%s",
                                  "%s","%s","%s","%s","%s","%s","%s","%s","%s",
                                  "%s","%s","%s","%s","%s","%s","%s","%s","%s",
                                  "%s","%s","%s","%s","%s","%s","%s","%s","%s",
                                  "%s","%s","%s","%s","%s","%s","%s","%s","%s",
                                  "%s","%s","%s","%s","%s","%s","%s","%s","%s",
                                  "%s","%s","%s","%s") """
                cr.execute(sql % valueSql)       
            except StandardError, msg:
                self.__MDI__.MsgErr("gendoc"," Save insert docu1  Error %s " % (msg))
            self.CnAz.commit()
            nrow = self.lc.GetItemCount() 
            for row in range(nrow):
                valtipoord = self.getColTxt(row, 18)
                valanno = self.getColTxt(row, 17)
                valnumord = self.getColTxt(row, 16)
                if valnumord!="": valnumord = int(valnumord)
                vcod_mag = 1
                vnriga+=10     
                vcodart = self.getColTxt(row, 0)
                vdescriz = self.getColTxt(row, 1)  
                vqt_doc = self.getColTxt(row, 2)
                self.__MDI__.CnvPM(vqt_doc)
                vqt_1 = float(self.__MDI__.val)                  
                vqt_2 = 0
                vqt_3 = 0
                vprez_un = self.getColTxt(row, 3)
                self.__MDI__.CnvPM5(vprez_un)
                vprez_un = float(self.__MDI__.val)
                vtot_riga = self.getColTxt(row, 4)
                self.__MDI__.CnvPM(vtot_riga)
                vtot_riga = float(self.__MDI__.val)
                vALIVA = self.getColTxt(row, 5)
                vsc1 = self.getColTxt(row, 6)
                self.__MDI__.CnvPM(vsc1)
                vsc1 = float(self.__MDI__.val) 
                vsc2 = 0
                vsc3 = 0
                vMERCE = self.getColTxt(row, 8)
                vUM = self.getColTxt(row, 9)
                if vUM=='':vUM = '--'
                vmis = self.getColTxt(row, 10)
                vcodbar = self.getColTxt(row, 14)
                vprez_ag = self.getColTxt(row, 15)
                self.__MDI__.CnvPM5(vprez_ag)
                vprez_ag = float(self.__MDI__.val)
                vcambioart = 0
                vannodoc = self.getColTxt(row, 17)  
                vTIPO_ORD = self.getColTxt(row, 18)
                valSTT_ORD = vTIPO_ORD ,valanno,valnumord		
                vprovv = self.getColTxt(row, 21)
                self.__MDI__.CnvPM(vprovv)
                vprovv = float(self.__MDI__.val)
                vdatacons = self.getColTxt(row, 22)
                vcolli = self.getColTxt(row, 23)
                self.__MDI__.CnvPM(vcolli)
                vcolli = float(self.__MDI__.val)
                vpeso = self.getColTxt(row, 24)
                self.__MDI__.CnvPM(vpeso)
                vpeso = float(self.__MDI__.val) 
                vlst = 1
                vpdc = '7501' #self.getColTxt(row, 26)
                vrag_doc = "A"
                vdatadoc = self.dataord 
                vnumdoc = self.getColTxt(row, 16)
                vrigadoc = self.getColTxt(row, 7)
                if vrigadoc=="" :vrigadoc = 0
                vrigamag = vnriga 
                vcampo1_corpo = self.getColTxt(row, 32)
                vcampo2_corpo = self.getColTxt(row, 33)
                vsttdoc2 = "C" #self.stt_doc2.GetValue()
                vd2_1 = vTIPO_DOC,self.annoc,int(vnum_doc),vcod_mag,vnriga,vcodart,vcodbar,vMERCE
                vd2_2 = vdescriz,vUM,vmis,vqt_1,vqt_2,vqt_3,vprez_un,vprez_ag
                vd2_3 = vtot_riga,vALIVA,vsc1,vsc2,vsc3,vprovv,vcambioart
                vd2_4 = vcolli,vpeso,vlst,vpdc,vannodoc,vTIPO_ORD,vdatadoc,str(vnumdoc)
                vd2_5 = int(vrigadoc),vrigamag,vrag_doc,vcampo1_corpo,vcampo2_corpo,vsttdoc2
                valueSql2 = vd2_1 + vd2_2 + vd2_3 + vd2_4 + vd2_5
                try:
                    cr = self.CnAz.cursor()
                    sql = """ insert into docu2
                              values("%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s") """
                    cr.execute(sql % valueSql2)
            	except StandardError, msg:
                    self.__MDI__.MsgErr("gendoc"," Save insert docu2 Error %s " % (msg))
                self.CnAz.commit()
                vcauma = '901'
                vcfm = "C" 
                vrigadoc = vnriga
                vdatadoc = vdata_doc
                vnumdoc = int(vnum_doc)
                vannodoc = self.annoc
                vnummov = int(self.vnum_mov)
                vm1 = self.annoc,vnummov,vdata_doc,vcauma,int(vcod_mag),vcfm,vcod_cf,vnriga
                vm2 = vcodart,vcodbar,vMERCE,vdescriz,vUM,vmis,vqt_1
                vm3 = vprez_un,vprez_ag,vtot_riga,vALIVA,vdiv,vcambioart
                vm4 = vsc1,vsc2,vsc3,vlst,vannodoc,vTIPO_DOC,vdatadoc,str(vnumdoc)
                vm5 = vrigadoc,vcampo1_corpo,vcampo2_corpo
                valueSql = vm1 + vm2 + vm3 + vm4 + vm5
                if vcodart!="--":
                    try:
                        cr = self.CnAz.cursor()
                        sql = """ insert into movmag
                                  values("%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s")"""
                        cr.execute(sql % valueSql) 
                    except StandardError, msg:
                        self.__MDI__.MsgErr("gendoc"," Save insert movmag Error %s " % (msg))
                    self.CnAz.commit()
                if valnumord!="" :
                    try:
                        cr = self.CnAz.cursor()
                        sql2 = """ update ordi2 set stt_ord = 'E' 
                                   where tipo_ord = "%s" and  anno = "%s" 
                                   and  num_ord = "%s" """
                        sql1 = """ update ordi1 set stt_ord = 'E' 
                                   where tipo_ord = "%s" and  anno = "%s" 
                                   and  num_ord = "%s" """
                        cr.execute(sql2 % valSTT_ORD)                
                        cr.execute(sql1 % valSTT_ORD)
                    except StandardError, msg:
                        self.__MDI__.MsgErr("gendoc","Save update STT Error %s " % (msg))
                    self.CnAz.commit()
            val = self.vTIPO_DOC.GetValue()              
            if val=="I1" or val=="F2":
                registro1 = "F1"
                registro2 = "I1"
                registro3 = "F2"
            if val=="B1":
                registro1 = "B1"
                registro2 = "B2"
                registro3 = "B3"                
            chiave = "RVEN"
            valueSql1 = vnumdoc, vdata_doc, chiave, self.annoc, registro1
            valueSql2 = vnumdoc, vdata_doc, chiave, self.annoc, registro2
            valueSql3 = vnumdoc, vdata_doc, chiave, self.annoc, registro3
            self.lgendoc.SetLabel("Documento Generato " + str(vnumdoc))
            try:
                cr = self.CnAz.cursor()
                sql = """ update libriaz set ultnum = "%s", udatreg = "%s" 
                          where chiave = "%s" and  anno = "%s" 
                          and  registro = "%s" """                   
                cr.execute(sql % valueSql1)
                cr.execute(sql % valueSql2)
                cr.execute(sql % valueSql3) 
            except StandardError, msg:
                self.__MDI__.MsgErr("gendoc","Save update libriaz Error %s " % (msg))
            self.CnAz.commit()
            registro = "R1"
            chiave = "RMAG"
            vdatamov = vdata_doc 
            valueSql = vnummov, vdatamov, chiave, self.annoc, registro
            try:
                cr = self.CnAz.cursor()
                sql = """ update libriaz set ultnum = "%s", udatreg = "%s" 
                          where chiave = "%s" and  anno = "%s" 
                          and  registro = "%s" """                    
                cr.execute(sql % valueSql) 
            except StandardError, msg:
                self.__MDI__.MsgErr("gendoc"," Save update libriaz maga Error %s " % (msg))
            self.CnAz.commit()
            self.lgendoc.SetLabel(_("Documento Generato n. ") + str(vnumdoc))
	    self.okconf.Enable(False)

            
