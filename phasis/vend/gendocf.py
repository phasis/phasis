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
import string 
from cfg import *
import cfg

def create(parent,cnt):
    return ConsolidaDoc(parent,cnt)
  
class ConsolidaDoc(wx.ScrolledWindow):
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
        self.ttl = cnt[0]
        self.tcpart = "C"   
        self.tblart = "articoli"
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        #self.SetClientSize(wx.Size(680, 425))
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
        #self.pnl = wx.Panel(id = wx.NewId(), name = '',
        #parent = self, pos = wx.Point(0, 0), size = wx.Size(420, 150))
        
        self.pnl = wx.Panel(id = wx.NewId(), name = '',
              parent = self, pos = wx.Point(0, 0),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)#, size = wx.Size(680, 420))        
        self.pnl.SetFont(self.font)
        
        self.lnumdoc = wx.StaticText(self.pnl, -1, _("Numero DDT :"), 
              wx.DLG_PNT(self.pnl, 7,12))
        self.num_doc = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 65,10), 
              wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.cnum_doc = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 130,10),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.data_doc = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 264,5))	      
        self.codcf = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 30,25))
        self.lragsoc1 = wx.StaticText(self.pnl, -1, _("Rag. Sociale1 ( Cognome ) :"), 
              wx.DLG_PNT(self.pnl, 7,25))
        self.ragsoc1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 5,35), 
	      wx.DLG_SZE(self.pnl, 120,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.cragsoc1 = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 130,35),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ragsoc2 = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 7,162))
        self.stato = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 7,162))
        self.localit = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 7,162))
        wx.StaticText(self.pnl, -1, _("Indirizzo :"), wx.DLG_PNT(self.pnl, 10,52))
        self.indiriz = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,50), wx.DLG_SZE(self.pnl, 218,cfg.DIMFONTDEFAULT))  
        wx.StaticText(self.pnl, -1, _("Citta' :"), wx.DLG_PNT(self.pnl, 10,69))
        self.zona = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,67), wx.DLG_SZE(self.pnl, 100,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl, -1, _("CAP :"), wx.DLG_PNT(self.pnl, 150,69))
        self.cap = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 180, 67), wx.DLG_SZE(self.pnl, 35,cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl, -1, _("PR :"), wx.DLG_PNT(self.pnl, 225,69))
        self.pr = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 243, 67), wx.DLG_SZE(self.pnl, 20,cfg.DIMFONTDEFAULT))
        self.codage = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))
        self.vPAGAM = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))
        self.vTIPO_DOC = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))      
        self.TIPO_DOC = wx.TextCtrl(self.pnl, -1, "B1", 
              wx.DLG_PNT(self.pnl, 7,162))     	      
        self.lgendoc = wx.StaticText(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 7,162))
        self.lc = wx.ListCtrl(self.pnl, Nid,
              wx.DLG_PNT(self.pnl, 5,85), 
              wx.DLG_SZE(self.pnl, 323,70), 
              wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)   
        #wx.StaticLine(self.pnl, -1, wx.DLG_PNT(self.pnl, 5,155), 
        #      wx.DLG_SZE(self.pnl, 283,-1)) 
        #self.importo = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 262,172))     
        self.ltotale = wx.StaticText(self.pnl, -1, _("Totale Documento:"), 
              wx.DLG_PNT(self.pnl, 185,162))
        #self.ltotale.SetFont(self.font)
        #self.ltotale.SetForegroundColour(wx.Colour(128, 128, 128))
        self.totale = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 262,160), 
	      wx.DLG_SZE(self.pnl, 65, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        #self.totale.SetFont(self.font)
        self.stt_doc1 = wx.TextCtrl(self.pnl, -1, "E", wx.DLG_PNT(self.pnl, 5,160))
        self.stt_doc2 = wx.TextCtrl(self.pnl, -1, "E", wx.DLG_PNT(self.pnl, 5,170))
        self.vCONSEG = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.vTRASP = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.vVETT = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.nsrif = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.vsrif = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.note = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.vIMBAL = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.vASPET = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.tot_colli = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.tot_peso = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.data_tra = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.ora_tra = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.scf1 = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))
        self.anno = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))	
        self.val = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,170))

        #self.ok = wx.Button(self.pnl, Nid, cfg.vcok, 
        #     wx.DLG_PNT(self.pnl, 120,10), btnSzeL )      
        self.int = wx.Button(self.pnl, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 275,10),##             
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV)) 
        self.canc = wx.Button(self.pnl, Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 275,10), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.okanag = wx.Button(self.pnl, Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl, 275,25),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.okndoc = wx.Button(self.pnl, Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl, 275,25),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        self.pnl.Fit()
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)

        
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.num_doc.Bind(wx.EVT_TEXT_ENTER, self.FndDoc)
        self.cnum_doc.Bind(wx.EVT_BUTTON, self.FndDoc)
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.int.Bind(wx.EVT_BUTTON, self.Start)
        self.okanag.Bind(wx.EVT_BUTTON, self.OkGDoc)
        self.okndoc.Bind(wx.EVT_BUTTON, self.OkGDoc)
        self.Bind(wx.EVT_CLOSE, self.Close)
        
        self.Start(self)
                
    def Start(self, evt):
        self.indiriz.SetValue('')
        self.zona.SetValue('')
        self.stato.SetValue('')
        self.stato.Show(False)
        self.stato.Enable(False)
        self.codage.Show(False)
        self.codage.Enable(False)
        self.codage.SetValue('')
        self.vPAGAM.Show(False)
        self.vPAGAM.Enable(False)
        self.vPAGAM.SetValue('')
        self.localit.SetValue('')
        self.localit.Show(False)
        self.localit.Enable(False)
        self.ragsoc2.SetValue('')
        self.ragsoc2.Show(False)
        self.ragsoc2.Enable(False)
        self.cap.SetValue('')
        self.pr.SetValue('--')
        self.indiriz.Enable(False)
        self.zona.Enable(False)
        self.cap.Enable(False)
        self.pr.Enable(False)
        self.vCONSEG.Show(False)
        self.vTRASP.Show(False)
        self.vVETT.Show(False)
        self.vsrif.Show(False)
        self.nsrif.Show(False)
        self.note.Show(False)
        self.vIMBAL.Show(False)
        self.vASPET.Show(False)
        self.tot_colli.Show(False)
        self.tot_peso.Show(False)
        self.data_tra.Show(False)
        self.ora_tra.Show(False)
        self.scf1.Show(False)
        self.totale.SetValue('0,00')
        self.totale.Enable(False)
        self.TIPO_DOC.Show(False)
        self.vTIPO_DOC.Show(False)
        self.vTIPO_DOC.Enable(False)
        self.vTIPO_DOC.SetValue('F1')
        self.stt_doc1.Show(False)
        self.stt_doc1.Enable(False)
        self.stt_doc2.Show(False)
        self.data_doc.Show(False)
        self.stt_doc2.Enable(False)
        self.val.Show(False)
        self.LC_clear(self)
        self.lc.Enable(False)
        self.lgendoc.SetLabel('')
        self.codcf.SetValue('')
        self.ragsoc1.SetValue('')
        self.num_doc.SetValue('')
        self.okndoc.Show(False)
        self.okndoc.Enable(False)
        self.okanag.Show(True)
        self.okanag.Enable(False)
        self.ragsoc1.SetFocus()
        self.codcf.Show(False)
        self.int.Show(False)
        self.int.Enable(False)
        self.canc.Show(True)
        self.canc.Enable(True)
        self.anno.Show(False)
        self.anno.SetValue(self.annoc)
        self.codcf.Enable(True)
        self.cragsoc1.Enable(True)
        self.ragsoc1.Enable(True)
        self.cnum_doc.Enable(True)
        self.num_doc.Enable(True)
        self.ragsoc1.SetFocus()


    def LC_clear(self, evt):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(1, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(2, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(3, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(4, _("NRiga"),width=wx.DLG_SZE(self.pnl, 30,-1).width)
        self.lc.InsertColumn(5, _("Codice"),width=wx.DLG_SZE(self.pnl, 60,-1).width)
        self.lc.InsertColumn(6, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(7, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(8, _("Descrizione"),width=wx.DLG_SZE(self.pnl, 100,-1).width)
        self.lc.InsertColumn(9, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(10, "",width=cfg._COLSZ0_)   
        self.lc.InsertColumn(11, _("QT"),width=wx.DLG_SZE(self.pnl, 27,-1).width)
        self.lc.InsertColumn(12, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(13, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(14, _("Prezzo"),width=wx.DLG_SZE(self.pnl, 50,-1).width)
        self.lc.InsertColumn(15, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(16, _("Importo"),width=wx.DLG_SZE(self.pnl, 50,-1).width)
        self.lc.InsertColumn(17, _("Iva"),width=wx.DLG_SZE(self.pnl, 25,-1).width)
        self.lc.InsertColumn(18, _("Sc%"),width=wx.DLG_SZE(self.pnl, 25,-1).width)
        self.lc.InsertColumn(19, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(20, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(21, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(22, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(23, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(24, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(25, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(26, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(27, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(28, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(29, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(30, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(31, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(32, "",width=cfg._COLSZ0_)
        self.lc.InsertColumn(33, "",width=cfg._COLSZ0_)
        #self.lc.SetColumnWidth(0, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(1, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(2, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(3, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(4, wx.DLG_SZE(self.pnl, 30,-1).width)
        #self.lc.SetColumnWidth(5, wx.DLG_SZE(self.pnl,  60,-1).width)
        #self.lc.SetColumnWidth(6, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(7, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(8, wx.DLG_SZE(self.pnl, 100,-1).width)
        #self.lc.SetColumnWidth(9, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(10, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(11, wx.DLG_SZE(self.pnl, 27,-1).width)
        #self.lc.SetColumnWidth(12, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(13, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(14, wx.DLG_SZE(self.pnl, 50,-1).width)
        #self.lc.SetColumnWidth(15, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(16, wx.DLG_SZE(self.pnl,  50,-1).width)
        #self.lc.SetColumnWidth(17, wx.DLG_SZE(self.pnl,  25,-1).width)
        #self.lc.SetColumnWidth(18, wx.DLG_SZE(self.pnl,  25,-1).width)
        #self.lc.SetColumnWidth(19, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(20, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(21, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(22, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(23, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(24, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(25, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(26, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(27, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(28, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(29, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(30, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(31, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(32, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetColumnWidth(33, wx.DLG_SZE(self.pnl, 0,-1).width)
        #self.lc.SetFont(self.font)
        self.lc.SetBackgroundColour(self.color)
        self.lc.Enable(False)

    def CalcTotale(self,evt):
        importo = 0
        for x in range(self.lc.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxt(x, 16))
            importo_row = float(self.__MDI__.val)            
            importo+=importo_row
        self.__MDI__.CnvVM(importo)
        self.totale.SetValue(self.__MDI__.val)

    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

    def FndDocCorpo(self, evt):
        nriga = 0
        rowlc = 0
        vndoc = 0
        cnt_rec = 0
        codcf = self.codcf.GetValue()        
        vTIPO_DOC = "B1"
        vsttdoc = "C"
	vnumdoc = self.num_doc.GetValue()
        if vnumdoc!='' :
            sql1 = """ select * from docu1
	               where num_doc = "%s" and tipo_doc = "%s"
                       and anno = "%s" and stt_doc = "%s" 
		       order by num_doc desc """
            valueSql1 = int(vnumdoc), vTIPO_DOC, self.annoc, vsttdoc
	else:
	    sql1 = """ select * from docu1
	              where cod_cf = "%s"  and tipo_doc = "%s"  
		      and anno = "%s" and stt_doc = "%s" 
		      order by num_doc desc """
            valueSql1 = codcf, vTIPO_DOC, self.annoc, vsttdoc
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql1 % valueSql1)
            rows1 = cr.fetchall()
            if rows1==[]:
                self.Message(cfg.msgdatonocons,self.ttl)
                self.Start(self)
            else:
	        self.codcf.Enable(False)
	        self.cragsoc1.Enable(False)
	        self.ragsoc1.Enable(False)
	        self.cnum_doc.Enable(False)
	        self.num_doc.Enable(False)			
            for row1 in rows1:
                stt_doc = row1[13]
                vnumdoc = str(row1[2])
                data_doc = str(row1[3])
                self.codage.SetValue(str(row1[18]))
		sql2 = """ select * from docu2 
		          where num_doc = "%s"  and tipo_doc = "%s"
			  and anno = "%s" order by num_rig desc """
		valueSql2 = int(vnumdoc), vTIPO_DOC, self.annoc
                try:
                    cr = self.CnAz.cursor ()
                    cr.execute(sql2 % valueSql2)
                    rows = cr.fetchall()
                    for row in rows:
                        if row[5]!="--":
                            for rowlc in range(1):
                                row_lc = self.lc.GetItemCount()
                                if row_lc==0:
                                    self.lc.InsertStringItem(rowlc, "")
                                    self.lc.SetStringItem(rowlc, 5,"--")
                                    self.lc.SetStringItem(rowlc, 8, _("DDT n. ") +\
				          vnumdoc+ _(" del ") + data_doc)
                                elif row[2]<vndoc:
                                    self.lc.InsertStringItem(rowlc, "")
                                    self.lc.SetStringItem(rowlc, 5,"--")
                                    self.lc.SetStringItem(rowlc, 8, _("DDT n. ") +\
				          vnumdoc+ _(" del ") + data_doc)
                                vndoc = row[2]
                                self.__MDI__.CnvVMQT(row[11])
                                qt_doc = self.__MDI__.val
                                self.__MDI__.CnvVMQT(row[12])
                                qt_con = self.__MDI__.val
                                self.__MDI__.CnvVMQT(row[13])
                                qt_eva = self.__MDI__.val
                                self.__MDI__.CnvVMPZ(row[14])
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
                                self.lc.InsertStringItem(rowlc, row[0])
                                self.lc.SetStringItem(rowlc, 1, row[1])
                                self.lc.SetStringItem(rowlc, 2, str(row[2]))
                                self.lc.SetStringItem(rowlc, 3, str(row[3]))
                                self.lc.SetStringItem(rowlc, 4, str(row[4]))
                                self.lc.SetStringItem(rowlc, 5, row[5])
                                self.lc.SetStringItem(rowlc, 6, str(row[6]))
                                self.lc.SetStringItem(rowlc, 7, row[7])
                                self.lc.SetStringItem(rowlc, 8, row[8])
                                self.lc.SetStringItem(rowlc, 9, row[9])        
                                self.lc.SetStringItem(rowlc, 10, row[10])
                                self.lc.SetStringItem(rowlc, 11, qt_doc)
                                self.lc.SetStringItem(rowlc, 12, str(row[12]))
                                self.lc.SetStringItem(rowlc, 13, str(row[13]))
                                self.lc.SetStringItem(rowlc, 14, prezzo)
                                self.lc.SetStringItem(rowlc, 15, str(row[15]))
                                self.lc.SetStringItem(rowlc, 16, tot_riga)
                                self.lc.SetStringItem(rowlc, 17, row[17])
                                self.lc.SetStringItem(rowlc, 18, sc1)
                                self.lc.SetStringItem(rowlc, 19, sc2)        
                                self.lc.SetStringItem(rowlc, 20, sc3)
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
        	except StandardError, msg:
            	    self.__MDI__.MsgErr("gendocf","FndDocCorpo docu2 Error %s" % (msg))
                self.CnAz.commit()
        except StandardError, msg:
            self.__MDI__.MsgErr("gendocf","FndDocCorpo docu1 Error %s" % (msg))
        self.CnAz.commit()
        self.lc.Enable(True)
        self.CalcTotale(self)
    
        
    def FndAnag(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue()
        tcpart = "C"
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
            self.__MDI__.MsgErr("gendocf","FndAnag Error %s" % (msg))
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
            self.ragsoc1.SetFocus()

    def FndCodCF(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        vcodcf = self.codcf.GetValue()
        tcpart = self.tcpart
        sql = """ select * from anag 
                  where cod = "%s" and t_cpart = "%s" """
        valueSql = int(vcodcf), self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1    
        except StandardError, msg:
            self.__MDI__.MsgErr("gendocf","FndCodCF Error %s" % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)

    def FndSelAnag(self, evt):
        row = evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.indiriz.SetValue(str(row[6]).title())
        self.zona.SetValue(str(row[8]).title())
        cap = string.zfill(str(row[7]).strip(),5) #'%05d' % row[7]
        if cap=="00000" : cap = ""
        self.cap.SetValue(cap)
        self.pr.SetValue(str(row[10]).upper())           
        self.num_doc.SetValue('')
        self.okndoc.Enable(False)
        self.okndoc.Show(False)
        self.okanag.Show(True)
        self.okanag.Enable(True)
        self.okanag.SetFocus()
        self.int.Show(True)
        self.int.Enable(True)
        self.canc.Enable(False)
        self.canc.Show(False)
        self.FndDocCorpo(self)
                
    def EvtChar(self, evt):
        evt_char = evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.int.SetFocus()
        evt.Skip()

    def EvtCharqt(self, evt):
        evt_char = evt.GetKeyCode()
        if (evt_char==27 and self.cntr_row==""):self.IntRow(self)
        evt.Skip()
                       
    def FndDoc(self, evt):
        cnt_rec = 0
        vnumdoc = self.num_doc.GetValue()
        print "inizio FndDoc"
        print vnumdoc
        if vnumdoc=='':vnumdoc = 0
        vtipo_doc = "B1"
        sttdoc = "C"
        self.tbl = "docu1"
	sql = """ select * from docu1
	          where num_doc = "%s" and tipo_doc = "%s"  
		  and anno = "%s" and stt_doc = "%s" """
        valueSql = int(vnumdoc), vtipo_doc, self.annoc, sttdoc
	if vnumdoc!=0:
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                self.__MDI__.MsgErr("gendocf","FndDoc Error %s" % (msg))
            self.CnAz.commit()
	    if cnt_rec==0 :
	        self.Message(cfg.msgdatonocons,self.ttl)
                self.Start(self)
            elif (cnt_rec==1 and cnt_rec<2):
                if self.num_doc.GetValue()=='':self.num_doc.SetValue(str(row[2]))
                if self.data_doc=='':self.data_doc = row[3]
                if self.codcf.GetValue()=='':self.codcf.SetValue(row[4])
                self.ragsoc1.SetValue(row[5])
                self.ragsoc2.SetValue(row[6])
		self.indiriz.SetValue(row[7])
		cap = string.zfill(str(row[8]).strip(),5)
		if cap=="00000" : cap = ""
		self.cap.SetValue(cap)
		self.zona.SetValue(row[9])   
		self.localit.SetValue(row[10])
		self.pr.SetValue(row[11])
		self.stato.SetValue(row[12])
		self.codage.SetValue(row[27])
		self.vPAGAM.SetValue(str(row[28]))
		self.vCONSEG.SetValue(str(row[29]))
		self.vTRASP.SetValue(str(row[30]))
		self.vVETT.SetValue(str(row[31]))
		self.vsrif.SetValue(str(row[32]))
		self.nsrif.SetValue(str(row[33]))
		self.note.SetValue(str(row[37]))
		##  DATI CALCE
		self.vIMBAL.SetValue(str(row[38]))
		self.vASPET.SetValue(str(row[39]))
		self.tot_colli.SetValue(str(row[40]))
		self.tot_peso.SetValue(str(row[41]))    
		self.scf1.SetValue(str(row[42]))       
		self.data_tra.SetValue(str(row[61]))
		self.ora_tra.SetValue(str(row[62]))   
		self.okanag.Show(False)
		self.okanag.Enable(False)
		self.okndoc.Show(True)
		self.okndoc.Enable(True)
		self.okndoc.SetFocus()
		self.int.Show(True)
		self.int.Enable(True)
		self.canc.Enable(False)
		self.canc.Show(False)
		self.FndDocCorpo(self)
		self.TIPO_DOC.SetValue('B1')
	else:
	    stt_doc = 'C'
	    import srcdoc
	    control = [self.TIPO_DOC, self.anno, self.num_doc,
	          self.data_doc, self.FndDoc, stt_doc, self.val ]       
            # < diegom rientra di 4 spazi perch rimane aperta la finestra dopo inserimento       
            win = srcdoc.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
            # > diegom
            
    def OkGDoc(self, evt):
        dlg = wx.MessageDialog(self,cfg.msgconsdoc, self.ttl,
                    wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            dlg.Destroy()
            self.Save(self)
            #self.lgendoc.SetLabel("Documento Generato ")
        else:
            dlg.Destroy()

    def Close(self, evt):
        if self.ragsoc1.GetValue()!="" or self.num_doc.GetValue()!="" :
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
        if(self.lc.GetItemCount()!=0 or self.codcf.GetValue()!=""):
            vnriga = 0
            registro = "F1" 
            chiave = "RVEN"   
            sql = """ select * from libriaz
	              where chiave = "%s" and  anno = "%s" 
		      and  registro = "%s" """
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
                    if (row[16]==None) : vdata_doc = self.datacon
                    if (row[16]!=None) : vdata_doc = row[16]
            except StandardError, msg:
                self.__MDI__.MsgErr("gendocf","save new num_mov Error %s" % (msg))
            self.CnAz.commit()
            # valori docu1
            vTIPO_DOC = "F1"
            vanno = self.annoc #self.anno.GetValue()
            vcod_cf = self.codcf.GetValue()
            vragsoc2 = self.ragsoc2.GetValue()
            vragsoc1 = self.ragsoc1.GetValue()
            vindiriz = self.indiriz.GetValue()
            vcap = self.cap.GetValue()
            vzona = self.zona.GetValue()
            vlocalit = self.localit.GetValue()
            vpr = self.pr.GetValue()
            vstato = self.stato.GetValue()
            vlst = 1
            vvsdoc = "" 
            vvsdata = ""
            vdiv = "EU"
            vcodage = self.codage.GetValue()
            vPAGAM = 'RD01' #self.vPAGAM.GetValue()              
            vvCONSEG = self.vCONSEG.GetValue()
            vvTRASP = self.vTRASP.GetValue()
	    if self.vVETT.GetValue()=='':  vvVETT='1'
            else: vvVETT = self.vVETT.GetValue()
            vvsrif = ""
            vnsrif = ""
            vrag_doc = ""
            vcambio = 0
            vcampo1 = ""
            vcampo2 = ""
            vnote = ""
            vcodcf1 = ""
            vragsoc3 = ""
            vragsoc4 = "" 
            vindiriz1 = ""
            vcap1 = ""
            vzona1 = ""
            vlocalit1 = ""
            vpr1 = ""
            vstato1 = ""
            vvsord = ""
            vsc1 = ""
            vsc2 = ""
            vsc3 = ""
            vsttdoc1 = ""
	    vdata_doc = self.datacon
            vd1_1 = vTIPO_DOC,vanno,vnum_doc,vdata_doc,vcod_cf,vragsoc1,vragsoc2
            vd1_1_modi = vdata_doc,vcod_cf,vragsoc1,vragsoc2
            vd1_2 = vindiriz,vcap,vzona,vlocalit,vpr,vstato,vcodcf1
            vd1_3 = vragsoc3,vragsoc4,vindiriz1,vcap1,vzona1,vlocalit1,vpr1,vstato1        
            vd1_4 = vcambio,vlst,vvsord,vvsdata
            vd1_5 = vdiv,vcodage,vPAGAM,vvCONSEG,vvTRASP,vvVETT
            vd1_6 = vvsrif,vnsrif,vrag_doc,vcampo1,vcampo2,vnote
            vd1_6_modi = vTIPO_DOC,vanno,vnum_doc
            vdocu1 = vd1_1 + vd1_2 + vd1_3 + vd1_4 + vd1_5 + vd1_6 
            vdocu1_modi = vd1_1_modi + vd1_2 + vd1_3 + vd1_4 + vd1_5  + vd1_6 
            vvIMBAL = self.vIMBAL.GetValue()
            vvASPET = self.vASPET.GetValue()      
            vtot_colli = self.tot_colli.GetValue()
            self.__MDI__.CnvPM(vtot_colli)
            vtot_colli = float(self.__MDI__.val)     
            vtot_peso = self.tot_peso.GetValue()
            self.__MDI__.CnvPM(vtot_peso)
            vtot_peso = float(self.__MDI__.val)   
            vscf1 = self.scf1.GetValue()
            vdata_tra = self.data_tra.GetValue()
            vora_tra = self.ora_tra.GetValue()
            self.__MDI__.CnvPM(vscf1)
            vscf1 = float(self.__MDI__.val)
            vscf2 = 0
            vscf3 = 0
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
            vcampo1_calce = 0
            vcampo2_calce = 0
            vnote_calce = ""
            vstt_doc1 = "E"
            vd3_1 = vvIMBAL,vvASPET,vtot_colli,vtot_peso
            vd3_2 = vsc1,vsc2,vsc3,vvPDC_SC
            vd3_3 = vcod_imb,viva_imb,vprez_imb,vcod_spe,viva_spe,vprez_spe
            vd3_4 = vcod_riv,viva_riv,vprez_riv
            vd3_5 = vcod_bol,viva_bol,vprez_bol,vcod_tra,viva_tra,vprez_tra
            vd3_6 = vdata_tra,vora_tra,vcampo1_calce,vcampo2_calce,vnote_calce,vstt_doc1
            vdocu3 = vd3_1 + vd3_2 + vd3_3 +vd3_4 + vd3_5 + vd3_6
            registro = "R1" 
            chiave = "RMAG"   
            sql = """ select * from libriaz 
                      where chiave = "%s" and anno = "%s" 
		      and registro = "%s" """
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
                    if (row[16]==None) : self.vdatamov = self.datacon
                    if (row[16]!=None) : self.vdatamov = row[16]
            except StandardError, msg:
                self.__MDI__.MsgErr("gendocf","save new num_mov libriaz Error %s" % (msg))
            self.CnAz.commit()
            valueSql = vdocu1 + vdocu3
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
		#print "docu1", valueSql
            except StandardError, msg:
                self.__MDI__.MsgErr("gendocf","save insert docu1 Error %s" % (msg))
            self.CnAz.commit()
            nrow = self.lc.GetItemCount() 
            for row in range(nrow):
                valtipodoc = self.getColTxt(row, 0)
                valanno = self.getColTxt(row, 1)
                valnumdoc = self.getColTxt(row, 2)
                if valnumdoc!="": valnumdoc = int(valnumdoc)
                valSTT_DOC = valtipodoc,valanno,valnumdoc
                vcod_mag = 1
                vnriga+=10 #int(self.getColTxt(row, 9))    
                vcodart = self.getColTxt(row, 5)
                vcodbar = self.getColTxt(row, 6)
                vMERCE = self.getColTxt(row, 7)
                vdescriz = self.getColTxt(row, 8)        
                vUM = self.getColTxt(row, 9)
                if vUM=='':vUM = '--'
                vmis = self.getColTxt(row, 10)
                vqt_doc = self.getColTxt(row, 11)
                self.__MDI__.CnvPM(vqt_doc)
                vqt_1 = float(self.__MDI__.val)                  
                vqt_2 = 0
                vqt_3 = 0
                vprez_un = self.getColTxt(row, 14)
                self.__MDI__.CnvPM5(vprez_un)
                vprez_un = float(self.__MDI__.val)
                vprez_ag = self.getColTxt(row, 15)
                self.__MDI__.CnvPM5(vprez_ag)
                vprez_ag = float(self.__MDI__.val)
                vcambioart = 0
                vtot_riga = self.getColTxt(row, 16)
                self.__MDI__.CnvPM(vtot_riga)
                vtot_riga = float(self.__MDI__.val)
                vALIVA = self.getColTxt(row, 17)
                vsc1 = self.getColTxt(row, 18)
                self.__MDI__.CnvPM(vsc1)
                vsc1 = float(self.__MDI__.val) 
                vsc2 = 0
                vsc3 = 0
                vprovv = self.getColTxt(row, 21)
                self.__MDI__.CnvPM(vprovv)
                vprovv = float(self.__MDI__.val)
                vdatacons = self.getColTxt(row, 21)
                vcolli = self.getColTxt(row, 23)
                self.__MDI__.CnvPM(vcolli)
                vcolli = float(self.__MDI__.val)
                vpeso = self.getColTxt(row, 24)
                self.__MDI__.CnvPM(vpeso)
                vpeso = float(self.__MDI__.val) 
                vlst = 1#int(self.getColTxt(row, 22))
                vpdc = self.getColTxt(row, 26)
                vrag_doc = ""#self.getColTxt(row, 24)
                vannodoc = self.getColTxt(row, 1)                
                vtipodoc = self.getColTxt(row, 0)
                vdatadoc = self.data_doc.GetValue()#self.getColTxt(row, 27)
                vnumdoc = self.getColTxt(row, 2)
                vrigadoc = self.getColTxt(row, 4)
                if vrigadoc=="" :vrigadoc = 0
                vrigamag = vnriga #self.getColTxt(row, 28)
                vcampo1_corpo = self.getColTxt(row, 29)
                vcampo2_corpo = self.getColTxt(row, 30)
                vstt_doc2 = "E"
                if vannodoc=='': vannodoc = self.annoc
                vd2_1 = vTIPO_DOC,self.annoc,int(vnum_doc),vcod_mag,vnriga,vcodart,vcodbar,vMERCE
                vd2_2 = vdescriz,vUM,vmis,vqt_1,vqt_2,vqt_3,vprez_un,vprez_ag
                vd2_3 = vtot_riga,vALIVA,vsc1,vsc2,vsc3,vprovv,vcambioart
                vd2_4 = vcolli,vpeso,vlst,vpdc,vannodoc,vtipodoc,vdatadoc,str(vnumdoc)
                vd2_5 = int(vrigadoc),vrigamag,vrag_doc,vcampo1_corpo,vcampo2_corpo,vstt_doc2
                vcauma = '903'#causale di magazzino
                vcfm = "C" #C = cliente F = Fornitore M = magazzino
                vrigadoc = vnriga
                vdatadoc = vdata_doc
                vnumdoc = int(vnum_doc)
                vnummov = int(self.vnum_mov)
                ## Valori movmag
                vm1 = self.annoc,vnummov,vdata_doc,vcauma,int(vcod_mag),vcfm,vcod_cf,vnriga
                vm2 = vcodart,vcodbar,vMERCE,vdescriz,vUM,vmis,vqt_1
                vm3 = vprez_un,vprez_ag,vtot_riga,vALIVA,vdiv,vcambioart
                vm4 = vsc1,vsc2,vsc3,vlst,vannodoc,vTIPO_DOC,vdatadoc,str(vnumdoc)
                vm5 = vrigadoc,vcampo1_corpo,vcampo2_corpo
		try:
                    cr = self.CnAz.cursor()
                    sql = """insert into docu2
                             values("%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                    "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s") """
                    valueSql = vd2_1 + vd2_2 + vd2_3 + vd2_4 + vd2_5
                    cr.execute(sql % valueSql) 
		    #print "docu2 ", valueSql
            	except StandardError, msg:
                    self.__MDI__.MsgErr("gendocf","save insert docu2 Error %s" % (msg))
            	self.CnAz.commit()
                if vcodart!="--":
                    try:
                        cr = self.CnAz.cursor()
                        sql = """insert into movmag
                                 values("%s","%s","%s","%s","%s","%s","%s",
				        "%s","%s","%s","%s","%s","%s","%s",
					"%s","%s","%s","%s","%s","%s","%s",
					"%s","%s","%s","%s","%s","%s","%s",
					"%s","%s","%s","%s") """
			valueSql = vm1 + vm2 + vm3 + vm4 + vm5		
                        cr.execute(sql % valueSql) 
			#print "movmag ", valueSql
            	    except StandardError, msg:
                        self.__MDI__.MsgErr("gendocf","save insert movmag Error %s" % (msg))
            	    self.CnAz.commit()
                if valnumdoc!="" :
                    try:
                        cr = self.CnAz.cursor()
                        sql1 = """ update docu1 set stt_doc = 'E' 
                                   where tipo_doc = "%s" and anno = "%s" 
                                   and num_doc = "%s" """
                        sql2 = """ update docu2 set stt_doc = 'E' 
                                   where tipo_doc = "%s" and anno = "%s" 
                                   and num_doc = "%s" """
                        cr.execute(sql1 % valSTT_DOC)                
                        cr.execute(sql2 % valSTT_DOC)
            	    except StandardError, msg:
                        self.__MDI__.MsgErr("gendocf","save update STT Error %s" % (msg))
                    self.CnAz.commit()
	    chiave = "RVEN"
            registro1 = "F1"
            registro2 = "I1"
            registro3 = "F2"
            valueSql1 = vnumdoc, vdata_doc, chiave, self.annoc, registro1
            valueSql2 = vnumdoc, vdata_doc, chiave, self.annoc, registro2
            valueSql3 = vnumdoc, vdata_doc, chiave, self.annoc, registro3
	    #print "-->", str(vnumdoc)
            self.lgendoc.SetLabel(_("Documento Generato N.") + str(vnumdoc))
	    try:
                cr = self.CnAz.cursor()
                sql = """ update libriaz set ultnum = "%s", udatreg = "%s" 
                          where chiave = "%s" and  anno = "%s" 
                          and  registro = "%s" """                   
                cr.execute(sql % valueSql1)
                cr.execute(sql % valueSql2)
                cr.execute(sql % valueSql3) 		
            except StandardError, msg:
                self.__MDI__.MsgErr("gendocf","Update Libriaz Error %s" % (msg))
            self.CnAz.commit()
	    #print "1 ", valueSql1
	    #print "2 ", valueSql2
	    #print "3 ", valueSql3
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
                self.__MDI__.MsgErr("gendocf","Update Mag Error %s" % (msg))
            self.CnAz.commit()
	    #print "libriaz ", valueSql

