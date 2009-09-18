# Copyright (C) 2003 - 2007  See Open - http://www.seeopen.it/
# Author: Massimo Gerardi <m.gerardi@mgsoft.it>
#
# Released under the terms of the GNU General Public License
# (version 2 or above)
#
# See COPYING for details.
#
# www.phasis.it - info@phasis.it 

import wx
import  wx.lib.masked as masked
from cfg import *
import cfg
import string 


def create(parent,cnt):
    return LstScad(parent,cnt)

#---------------------------------------------------------------------------
class LstScad(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        #wx.Frame.__init__(self, id=wx.NewId(), name='',
        #      parent=prnt, pos=wx.Point(0, 0), 
        #      style=wx.DEFAULT_FRAME_STYLE , title=cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        Nid = wx.NewId()
        self.ttl=cnt[0]
        self.tipoord =cnt[1]
        self.tcpart="C"
        #self.ottl="Gestione Movimenti"
        self.tbl="scad"
        #self.tblart="articoli"
        self.rec=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        self.CMD=cnt[5]       
        #self.font=self.GetFont()
        #self.SetClientSize(wx.Size(680, 400))
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz=self.__MDI__.GetConnAZ() 
        self.annoc=self.__MDI__.GetAnnoC() 
        self.datacon= self.__MDI__.GetDataC()
        self.dzDatiAzienda= self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel1',
              parent=self, pos=wx.Point(0, 0), size = wx.DLG_SZE(self,680/2,400/2), #size=wx.Size(680, 400),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        btnSzeL = wx.DLG_SZE(self.pnl, 70,16)    
        btnSzeM = wx.DLG_SZE(self.pnl, 80,16)
        btnSzeM1 = wx.DLG_SZE(self.pnl, 60,16)
        btnSzeS = wx.DLG_SZE(self.pnl, 16,16)
        btnSzeD = wx.DLG_SZE(self.pnl, 60,14)        
        #self.pnl.SetFont(self.font)


        data_att_int=self.datacon.split("/")
        data_att_int=str(data_att_int[2]) + str(data_att_int[1]) + str(data_att_int[0])
        valueSql = int(data_att_int)
        sql = """ select data_scad,data_scad_int from scad 
                  where data_scad_int<='%s'
                  and stt_scad!='S' 
                  and stt_scad!='Z'"""

        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
	    row = cr.fetchone()
            if row:
	        self.CnAz.commit()
                sql = """ update scad set stt_scad='Z' 
                where data_scad_int<='%s' and stt_scad!='S'
                and stt_scad!='Z'  """ 
                cr.execute(sql % valueSql)  
                dlg = wx.MessageDialog(self, 
	        "Aggiornamento Scadenzario ......", 
		"Aggiornamento Tabella Scadenzario ", 
                wx.ID_OK | wx.ICON_INFORMATION)
                if dlg.ShowModal()==wx.ID_OK: dlg.Destroy()
                wx.GetApp().GetPhasisMdi().CloseTabObj(self)
                self.CnAz.commit()
        except StandardError, msg:
            print "Scadenzario"," New Error %s"  % (msg)
	
         




        self.lc = wx.ListCtrl(self.pnl , -1,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,110),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,120), 
              wx.DLG_SZE(self.pnl , 335,-1))


        # < diegom linea 1
        #wx.StaticText(self.pnl , -1, _("Tipologia Scad.:"), 
              #wx.DLG_PNT(self, 25,147))

        self.lscad = wx.StaticText(self.pnl, -1, "Num. :", 
              wx.DLG_PNT(self.pnl, 5,127))
        self.num_scad = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 27,125), 
              wx.DLG_SZE(self.pnl, 35,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) 
        self.cnum_scad = wx.BitmapButton(self.pnl, -1, png, 
              wx.DLG_PNT(self.pnl, 64,125),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV), wx.TE_PROCESS_ENTER)


        self.ldata_scad=wx.StaticText(self.pnl, -1, _("Scad.:"), 
              wx.DLG_PNT(self.pnl, 66,127))
        self.ldata_scad.SetFont(self.font)
        self.data_scad = masked.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 85,125), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT,autoformat='EUDATEDDMMYYYY/')
        self.vdata_scad = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 85, 125))
        self.cdata_scad = wx.BitmapButton(self.pnl, -1, png, 
              wx.DLG_PNT(self.pnl, 146,125),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV), wx.TE_PROCESS_ENTER)



        self.TIPO_SCAD = wx.ComboBox(self.pnl, 300,"",
              wx.DLG_PNT(self.pnl, 157,125), wx.DLG_SZE(self.pnl, 90,-1),[],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vTIPO_SCAD = wx.TextCtrl(self.pnl , -1, "",
              wx.DLG_PNT(self.pnl , 157,125), 
              wx.DLG_SZE(self.pnl , 0, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)

        self.cTIPO_SCAD = wx.BitmapButton(self.pnl, -1, png, 
              wx.DLG_PNT(self.pnl, 250,125),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV), wx.TE_PROCESS_ENTER)

        self.all = wx.Button(self.pnl , Nid, cfg.vcall, 
              wx.DLG_PNT(self.pnl , 269,125), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeM1H,cfg.btnSzeV))


        # < diegom linea 2


        #wx.StaticText(self.pnl, -1, "Pagamento :", 
              #wx.DLG_PNT(self.pnl, 155,147))



        wx.StaticText(self.pnl, -1, "Controp.:", 
              wx.DLG_PNT(self.pnl, 5,142)) 
        self.CF = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 35,140), wx.DLG_SZE(self.pnl, 50,-1), [],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vCF = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 35,140))


        self.lc1odcf = wx.StaticText(self.pnl, -1, "Cod.", 
              wx.DLG_PNT(self.pnl, 90,142))
        self.codcf= wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 107, 140), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT))

        self.lragsoc1 = wx.StaticText(self.pnl,-1,"Rag.Soc.1:", 
              wx.DLG_PNT(self.pnl, 150,142))
        self.ragsoc1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 187,140), 
              wx.DLG_SZE(self.pnl, 80,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.cragsoc1 = wx.BitmapButton(self.pnl, -1, png,
              wx.DLG_PNT(self.pnl, 269,140),

        # < diegom linea 3

              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))     
        self.lragsoc2 = wx.StaticText(self.pnl, -1, "Rag. Soc.2:", 
              wx.DLG_PNT(self.pnl, 5,157))
        self.ragsoc2 = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 42, 155), 
              wx.DLG_SZE(self.pnl, 90,cfg.DIMFONTDEFAULT)) 
        self.ragsoc4 = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 42, 155), 
              wx.DLG_SZE(self.pnl, 90,cfg.DIMFONTDEFAULT))

        self.PAGAM = wx.ComboBox(self.pnl, -1,"",
              wx.DLG_PNT(self.pnl, 140,155), wx.DLG_SZE(self.pnl, 120,-1),
              [],wx.CB_DROPDOWN | wx.CB_SORT )
        self.vPAGAM = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 140,155))




        # < diegom linea 4


        self.ltipodoc = wx.StaticText(self.pnl, -1, "Tipo Documento.:", 
              wx.DLG_PNT(self.pnl, 5,172))

        self.TIPO_DOC = wx.ComboBox(self.pnl, 300,"",
              wx.DLG_PNT(self.pnl, 63,170), wx.DLG_SZE(self.pnl, 110,-1),[],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vTIPO_DOC =  wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 63,172))

        self.stt_doc1 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 63,170))  
        self.stt_doc2 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 63,170))  


        self.ldoc = wx.StaticText(self.pnl, -1, "N.Doc.:", 
              wx.DLG_PNT(self.pnl, 176,172))

        self.num_doc = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 198,170), 
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)    

        self.cnum_doc = wx.BitmapButton(self.pnl, -1, png,
              wx.DLG_PNT(self.pnl, 230,170),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.vnum_doc = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 230, 170))


        self.rbREG = wx.RadioButton(self.pnl, -1, "Registrato",
              wx.DLG_PNT(self.pnl, 269,155), 
              wx.DLG_SZE(self.pnl, 60,10))
        self.rbSALD = wx.RadioButton(self.pnl, -1, "Saldato",
              wx.DLG_PNT(self.pnl, 310,155), 
              wx.DLG_SZE(self.pnl, 60,10))
        self.rbSCAD = wx.RadioButton(self.pnl, -1, "Scaduti",
              wx.DLG_PNT(self.pnl, 269,170), 
              wx.DLG_SZE(self.pnl, 60,10))
        self.rbALL = wx.RadioButton(self.pnl, -1, "Tutti",
              wx.DLG_PNT(self.pnl, 310,170), 
              wx.DLG_SZE(self.pnl, 60,10))

        # < diegom linea 5

        wx.StaticText(self.pnl, -1, "Totale Entrate", 
              wx.DLG_PNT(self.pnl, 5,187))
        self.tot_E = wx.StaticText(self.pnl, -1, "0,00", 
              wx.DLG_PNT(self.pnl, 55, 187), 
              wx.DLG_SZE(self.pnl, 55,10))

        wx.StaticText(self.pnl, -1, "Saldo Totale:", 
              wx.DLG_PNT(self.pnl, 110,187))
        self.tot_sald_E = wx.StaticText(self.pnl, -1, "0,00", 
              wx.DLG_PNT(self.pnl, 160, 187), 
              wx.DLG_SZE(self.pnl, 60,10))

        wx.StaticText(self.pnl, -1, "Da Saldare:", 
              wx.DLG_PNT(self.pnl, 216,187))
        self.tot_nsald_E = wx.StaticText(self.pnl, -1, "0,00", 
              wx.DLG_PNT(self.pnl, 265, 187), 
              wx.DLG_SZE(self.pnl, 60,10))



        wx.StaticText(self.pnl, -1, "Totale Uscite:", 
              wx.DLG_PNT(self.pnl, 5,200))
        self.tot_U = wx.StaticText(self.pnl, -1, "0,00", 
              wx.DLG_PNT(self.pnl, 55,200 ), 
              wx.DLG_SZE(self.pnl, 55,10))

        wx.StaticText(self.pnl, -1, "Saldo Totale:", 
              wx.DLG_PNT(self.pnl, 110,200))
        self.tot_sald_U = wx.StaticText(self.pnl, -1, "0,00", 
              wx.DLG_PNT(self.pnl, 160, 200), 
              wx.DLG_SZE(self.pnl, 60,10))

        wx.StaticText(self.pnl, -1, "Da Saldare:", 
              wx.DLG_PNT(self.pnl, 216,200))
        self.tot_nsald_U = wx.StaticText(self.pnl, -1, "0,00", 
              wx.DLG_PNT(self.pnl, 265, 200), 
              wx.DLG_SZE(self.pnl, 60,10))
        










        # pulsanti
        self.ok = wx.Button(self.pnl , -1, cfg.vcok, 
              wx.DLG_PNT(self.pnl , 295,125), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self.pnl , -1, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 295,140), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.inte = wx.Button(self.pnl , -1, cfg.vcint, 
              wx.DLG_PNT(self.pnl , 295,140), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa = wx.Button(self.pnl, -1, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 295,155), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))


        wx.StaticText(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 5,195))
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        self.canc.SetFocus()
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

        self.TIPO_SCAD.Bind(wx.EVT_COMBOBOX, self.SelCOMBOtiposcadev)
        self.CF.Bind(wx.EVT_COMBOBOX, self.SelCOMBOcfev)
        self.PAGAM.Bind(wx.EVT_COMBOBOX, self.SelPAGAMev)
        self.TIPO_DOC.Bind(wx.EVT_COMBOBOX, self.SelCOMBOtipodocev)  
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.inte.Bind(wx.EVT_BUTTON, self.Start)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK,  self.DblClick)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)

        #self.cTIPO_SCAD.Bind(wx.EVT_BUTTON, self.FndSelGen)
        self.all.Bind(wx.EVT_BUTTON, self.FndSelScadAll)
        self.cTIPO_SCAD.Bind(wx.EVT_BUTTON, self.FndSelScad)
        self.cnum_scad.Bind(wx.EVT_BUTTON, self.FndSelScad)
        self.cdata_scad.Bind(wx.EVT_BUTTON, self.FndSelScad)
        self.cnum_doc.Bind(wx.EVT_BUTTON, self.FndSelScad)

        #self.cnum_scad.Bind(wx.EVT_BUTTON, self.FndSelCod)
        #self.cdata_scad.Bind(wx.EVT_BUTTON, self.FndSelDataScad)

        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        
        self.Start(self)


    def Stampa(self, evt): 
        anno = self.annoc
        tipodoc = 'lstmovc'
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,   
              tipo = tipodoc, 
              parametriSql = (anno,),
              datiazienda = self.dzDatiAzienda,
              anteprima = True )


    def Start(self, event):
        #self.rbREG.Enable(False)
        #self.rbSALD.Enable(False)
        self.rbREG.SetValue(True)
        self.rbSALD.SetValue(False)
        self.rbSCAD.SetValue(False)
        self.rbALL.SetValue(False)
        self.cnum_scad.Show(False)
        self.cdata_scad.Show(False)

        self.stampa.Show(False)
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.ragsoc4.SetValue('')
        self.ragsoc4.Show(False)
        self.codcf.SetValue('')
        
        self.data = self.datacon   
        self.data_scad.SetValue(self.data)

        self.num_scad.SetValue('')
        self.num_scad.Enable(True)
        self.cnum_scad.Enable(True)
        self.TIPO_SCAD.Enable(True)


        self.vTIPO_DOC.Show(False)
        self.vPAGAM.Show(False)
        self.stt_doc1.Show(False)
        self.stt_doc2.Show(False)
        self.vTIPO_SCAD.Show(False) 
        self.vdata_scad.Show(False) 
        self.vnum_doc.Show(False)
        self.vCF.Show(False)

        self.TIPO_DOC.Enable(False)
        self.num_doc.Enable(False)
        self.cnum_doc.Enable(False)
        #self.codcf.Enable(False)

        self.vPAGAM.SetValue('PAG00')
        self.vTIPO_DOC.SetValue('I1')
        self.vTIPO_SCAD.SetValue('S01')
        #self.vCF.SetValue('C')  

        self.sPAGAM = ''
        self.sTIPO_DOC = ''
        self.sTIPO_SCAD = ''
        self.sDA = ''

        self.SelPAGAM(self)
        self.SelCOMBOtipodoc(self)
        self.SelCOMBOtiposcad(self)
        #self.SelCOMBOcf(self)


        self.vPAGAM.SetValue('')
        self.vTIPO_DOC.SetValue('')
        self.vTIPO_SCAD.SetValue('')
        self.vCF.SetValue('')
        self.PAGAM.SetValue('')
        self.TIPO_DOC.SetValue('')
        self.TIPO_SCAD.SetValue('')
        self.CF.SetValue('')

        self.codcf.SetValue('')

        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Num."),width=wx.DLG_SZE(self.pnl, 30,-1).width)
        self.lc.InsertColumn(1, _("Data Scad."),width=wx.DLG_SZE(self.pnl, 42,-1).width)
        self.lc.InsertColumn(2, _("Tipo Scad."),width=wx.DLG_SZE(self.pnl, 45,-1).width)
        self.lc.InsertColumn(3, _("Condizioni di pagamento"),width=wx.DLG_SZE(self.pnl, 85,-1).width)
        self.lc.InsertColumn(4, _("Ragione Sociale"),width=wx.DLG_SZE(self.pnl, 70,-1).width)

        self.lc.InsertColumn(5, _("D/A"),width=wx.DLG_SZE(self.pnl, 18,-1).width)
        self.lc.InsertColumn(6, _("Totale"),width=wx.DLG_SZE(self.pnl, 40,-1).width)
        self.lc.InsertColumn(7, _("Stato"),width=wx.DLG_SZE(self.pnl, 52,-1).width)

        self.lc.InsertColumn(8, _("Data Doc."),width=wx.DLG_SZE(self.pnl, 38,-1).width)
        self.lc.InsertColumn(9, _("Tipo Doc."),width=wx.DLG_SZE(self.pnl, 70,-1).width)
        self.lc.InsertColumn(10, _("Num. Doc."),width=wx.DLG_SZE(self.pnl,38,-1).width)

   
        font = self.GetFont()
        self.lc.SetFont(font)
        self.inte.Show(False)
        self.canc.Show(True)


    def SelCOMBOtiposcad(self, evt):   
        vTIPO_SCAD = self.vTIPO_SCAD.GetValue()
        self.TIPO_SCAD.Clear()
        sql = """ select * from scadenze """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)                 
            while (1):
                row = cr.fetchone () 
                if row==None: 
                    break
                if (row[0]=="SCAD"):
                    if (row[1]==vTIPO_SCAD):
                        self.sTIPO_SCAD = row[2]
                    self.TIPO_SCAD.Append(row[2],row[1])
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," Cerca PAGAM Error %s" % (msg))
        self.CnAz.commit()
        cntTIPO_SCAD = 0
        cntTIPO_SCAD = self.TIPO_SCAD.FindString(self.sTIPO_SCAD)
        self.TIPO_SCAD.Select(cntTIPO_SCAD)
        self.ContSeltiposcad(self)




    def SelPAGAM(self, evt):      
        vPAGAM = self.vPAGAM.GetValue()
        self.PAGAM.Clear()
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
        except StandardError, msg:
            self.__MDI__.MsgErr("pagamenti"," Cerca PAGAM Error %s" % (msg))
        self.CnAz.commit()
        cntPAGAM = 0
        cntPAGAM = self.PAGAM.FindString(self.sPAGAM)
        self.PAGAM.Select(cntPAGAM)



    def SelCOMBOtipodoc(self, evt):
        vTIPO_DOC = self.vTIPO_DOC.GetValue()
        self.TIPO_DOC.Clear()
        self.TIPO_DOC.Append('Ordine Clienti','PC')
        self.TIPO_DOC.Append('Ordine Fornitori','PF')
        self.TIPO_DOC.Append('Fattura accompagnatoria','I1')
        self.TIPO_DOC.Append('Documento di trasporto (DDT)','B1')
        self.TIPO_DOC.Append('Doc.trasporto - Reso fornitore','B3')
        self.TIPO_DOC.Append('Fattura differita (da DDT)','F1')
        self.TIPO_DOC.Append('Fattura senza doc.trasporto','F2')
        if vTIPO_DOC=="PC":vTIPO_DOC=0
        if vTIPO_DOC=="PF":vTIPO_DOC=1
        if vTIPO_DOC=="I1":vTIPO_DOC=2
        if vTIPO_DOC=="B1":vTIPO_DOC=3
        if vTIPO_DOC=="B3":vTIPO_DOC=4
        if vTIPO_DOC=="F1":vTIPO_DOC=5
        if vTIPO_DOC=="F2":vTIPO_DOC=6
        self.TIPO_DOC.Select(vTIPO_DOC)
        self.sTIPO_DOC=self.TIPO_DOC.GetValue()




    def SelCOMBOcf(self, evt):
        vCF = self.vCF.GetValue()
        self.CF.Clear()
        self.CF.Append('Cliente','C')
        self.CF.Append('Fornitore','F')
        self.CF.Append('Agente','A')
        self.CF.Append('Altro','Z')
        self.CF.Append('Tutti','T')
        if vCF=="C":vCF=0
        if vCF=="F":vCF=1
        if vCF=="A":vCF=2
        if vCF=="Z":vCF=3
        if vCF=="T":vCF=4
        self.CF.Select(vCF)





    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str =  evt.GetString()     
        evt.Skip()

        
    def SelPAGAMev(self, evt):
        self.Sel(evt)
        self.vPAGAM.SetValue(self.cb_val)

    def SelCOMBOtipodocev(self, evt):
        self.Sel(evt)
        self.vTIPO_DOC.SetValue(self.cb_val)
        self.ContTipoDoc(self)


    def SelCOMBOtiposcadev(self, evt):
        self.Sel(evt)
        self.vTIPO_SCAD.SetValue(self.cb_val)
        self.ContSeltiposcad(self)

    def SelCOMBOcfev(self, evt):
        self.Sel(evt)
        self.vCF.SetValue(self.cb_val)
        if self.vCF.GetValue()=="Z":
            self.cragsoc1.Enable(False) 
        else:
            self.cragsoc1.Enable(True)





    def ContSeltiposcad(self, evt):
        cnt_rec=0
        sql = """ select * from scadenze where valore='%s' """
        valore = self.vTIPO_SCAD.GetValue()
        self.val1=""
        self.val2=""
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valore) 
            rows = cr.fetchall()
            for row in rows:cnt_rec+=1
            if (row[0]!="" and cnt_rec==1):
                self.sTIPO_SCAD = row[2]
                self.val1 = row[3]
                self.val2 = row[4]
        except StandardError, msg:
            self.__MDI__.MsgErr("Vendite"," Cerca PAGAM Error %s" % (msg))
        self.CnAz.commit()


        if self.val1=="T": self.OnFndDoc(self)
        elif self.val1=="Z":
            self.OffFndDoc(self)
            self.vCF.SetValue(self.val1)
            self.SelCOMBOcf(self)
            #self.CF.Enable(False)
            self.cragsoc1.Show(False)
            self.codcf.Show(False)
        else:
            self.OffFndDoc(self)
            self.vCF.SetValue(self.val1)
            self.SelCOMBOcf(self)
            #self.CF.Enable(False)
            self.cragsoc1.Show(True)
            self.codcf.Show(True)


     
         
    def ContTipoDoc(self, evt):
        tipo_doc = self.vTIPO_DOC.GetValue()
        if tipo_doc=="PF" or tipo_doc=="B3":
            self.vCF.SetValue('F')
        else:
            self.vCF.SetValue('C')
        self.SelCOMBOcf(self)




    def FndCodCF(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        cod = self.codcf.GetValue()
        tcpart = self.vCF.GetValue()
        self.tcpart = self.vCF.GetValue()
        if tcpart=="A": sql = """ select * from agenti where cod = "%s" and t_cpart = "%s" """
        else: sql = """ select * from anag where cod = "%s" and t_cpart = "%s" """

        valueSql = int(cod),tcpart
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
        self.tcpart = self.vCF.GetValue()
        if tcpart=="A":
            valueSql = tcpart, '%' + val.title() + '%'
            sql = """ select * from agenti 
                      where t_cpart = "%s" and rag_soc1 like "%s" 
                      order by rag_soc1 desc """
        else: 
            valueSql = tcpart, '%' + val.title() + '%'
            sql = """ select * from anag 
                      where t_cpart = "%s" 
                      and rag_soc1 like "%s" 
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

            control = [self.tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)


    def FndSelAnag(self, evt):
        row=evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc2.SetValue(str(row[4]).title())
        self.ragsoc1.SetValue(str(row[3]).title())

    # INIZIO FUNZIONI FIND 
        



    def FndSelScad(self, evt): 
        anno = self.annoc 
        num_scad = self.num_scad.GetValue()
        data_scad = self.data_scad.GetValue()
        if data_scad!="  /  /    ": 
            data_scad_int = data_scad.split("/")
            data_scad_int = str(data_scad_int[2]) + str(data_scad_int[1]) + str(data_scad_int[0])  
        TIPO_SCAD = self.vTIPO_SCAD.GetValue()
        codcf = self.codcf.GetValue()
        vCF = self.vCF.GetValue()
        ragsoc1 = self.ragsoc1.GetValue()
        ragsoc2 = self.ragsoc2.GetValue()
        ragsoc4 = self.ragsoc4.GetValue()
        vPAGAM = self.vPAGAM.GetValue()
        vTIPO_DOC = self.vTIPO_DOC.GetValue()
        num_doc = self.num_doc.GetValue()
        anno = self.annoc

        sql = "select * from scad where anno='" + anno + "'" 

        if TIPO_SCAD!="": sql = sql + " and tipo_scad = '" +  TIPO_SCAD + "'"
        if codcf!="": sql = sql + " and cod_cf = " + codcf
        #if ragsoc1!="": sql = sql + " and rag_soc1 like '%" + ragsoc1  + "%'"
        #if ragsoc2!="": sql = sql + " and rag_soc2 like '" + ragsoc2  + "'"
        if ragsoc4!="": sql = sql + " and rag_soc1 like '" + ragsoc4  + "'"
        elif ragsoc1!="": sql = sql + " and rag_soc1 like '%" + ragsoc1  + "%'"
        if ragsoc2!="": sql = sql + " and rag_soc2 like '" + ragsoc2  + "'"
        if vCF!="" and vCF!="T": sql = sql + " and t_cpart = '" + vCF + "'" 
        if num_scad != "": sql = sql + " and cod = '" + num_scad  + "'"
        if data_scad != "  /  /    " and data_scad!=self.datacon: 
            sql = sql + " and data_scad_int <= '" + data_scad_int + "'"
        if vPAGAM!="": sql = sql + " and pagam = '" + vPAGAM + "'" 

        if vTIPO_DOC!="": sql = sql + " and tipo_doc = '" + vTIPO_DOC + "'"
        if num_doc!="": sql = sql + " and num_doc = '" + num_doc + "'"
        if self.rbREG.GetValue(): sql = sql + " and stt_scad = 'R'"
        if self.rbSALD.GetValue(): sql = sql + " and stt_scad = 'S'"
        if self.rbSCAD.GetValue(): sql = sql + " and stt_scad = 'Z'"

        sql = sql + " order by data_scad_int desc" 

        #print sql
    
        self.ClearLc(self) 
        self.RmpLc(sql)

    def FndSelScadAll(self, evt):
        anno = self.annoc
        sql = "select * from scad where anno='" + anno + "' order by data_scad_int desc" 
        self.ClearLc(self) 
        self.RmpLc(sql)



    def ClearLc(self, evt):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Num."),width=wx.DLG_SZE(self.pnl, 30,-1).width)
        self.lc.InsertColumn(1, _("Data Scad."),width=wx.DLG_SZE(self.pnl, 42,-1).width)
        self.lc.InsertColumn(2, _("Tipo Scad."),width=wx.DLG_SZE(self.pnl, 45,-1).width)
        self.lc.InsertColumn(3, _("Condizioni di pagamento"),width=wx.DLG_SZE(self.pnl, 85,-1).width)
        self.lc.InsertColumn(4, _("Ragione Sociale"),width=wx.DLG_SZE(self.pnl, 70,-1).width)
        self.lc.InsertColumn(5, _("D/A"),width=wx.DLG_SZE(self.pnl, 18,-1).width)
        self.lc.InsertColumn(6, _("Totale"),width=wx.DLG_SZE(self.pnl, 40,-1).width)
        self.lc.InsertColumn(7, _("Stato"),width=wx.DLG_SZE(self.pnl, 52,-1).width)
        self.lc.InsertColumn(8, _("Data Doc."),width=wx.DLG_SZE(self.pnl, 38,-1).width)
        self.lc.InsertColumn(9, _("Tipo Doc."),width=wx.DLG_SZE(self.pnl, 70,-1).width)
        self.lc.InsertColumn(10, _("Num. Doc."),width=wx.DLG_SZE(self.pnl,38,-1).width)




    def RmpLc(self, evt):
        tot_E=[0,0,0]
        tot_U=[0,0,0]

        rowlc = 0
        sql = evt
        rec_vCF=self.vCF.GetValue()
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            rows = cr.fetchall()
            #print rows
            for row in rows:
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount() 
  
                    self.lc.InsertStringItem(rowlc, str(row[0]))
                    self.lc.SetStringItem(rowlc, 1, str(row[2]))

                    recupera=self.TIPO_SCAD.GetValue()
                    self.vTIPO_SCAD.SetValue(str(row[3]))
                    self.SelCOMBOtiposcad(self)
                    self.lc.SetStringItem(rowlc, 2, str(self.sTIPO_SCAD))
                    if recupera=="": 
                        self.TIPO_SCAD.SetValue('')
                        self.vTIPO_SCAD.SetValue('')
                        self.sTIPO_SCAD=''

                    #self.lc.SetStringItem(rowlc, 2, str(row[3]))

                    recupera=self.PAGAM.GetValue()
                    self.vPAGAM.SetValue(str(row[4]))
                    self.SelPAGAM(self)
                    self.lc.SetStringItem(rowlc, 3, str(self.sPAGAM))
                    if recupera=="":
                        self.PAGAM.SetValue('')
                        self.vPAGAM.SetValue('')
                        self.sPAGAM=''

                    #self.lc.SetStringItem(rowlc, 3, str(row[4]))
                    self.lc.SetStringItem(rowlc, 4, row[7])
                    self.lc.SetStringItem(rowlc, 5, str(row[12]))
                    self.__MDI__.CnvVM(row[13])
                    totale=self.__MDI__.val
                    self.lc.SetStringItem(rowlc, 6, totale)

                    if row[14]=="R":
                        self.lc.SetStringItem(rowlc, 7, "Registrato")
                        self.lc.SetItemBackgroundColour(rowlc,"White")
                    elif row[14]=="S":
                        self.lc.SetStringItem(rowlc, 7, "Saldato")
                        self.lc.SetItemBackgroundColour(rowlc,"LightGreen")
                    elif row[14]=="Z":
                        self.lc.SetStringItem(rowlc, 7, "Scaduto")
                        self.lc.SetItemBackgroundColour(rowlc,"Orange")

                    self.lc.SetStringItem(rowlc, 8, str(row[9]))

                    if row[10]!="":
                        recupera=self.TIPO_DOC.GetValue()
                        self.vTIPO_DOC.SetValue(str(row[10])) 
                        self.SelCOMBOtipodoc(self)
                        self.lc.SetStringItem(rowlc, 9, str(self.sTIPO_DOC))
                        if recupera=="":
                             self.TIPO_DOC.SetValue('')
                             self.vTIPO_DOC.SetValue('')
                             self.sTIPO_DOC=''


                    if row[11]!=0: self.lc.SetStringItem(rowlc, 10, str(row[11]))
                    recupera=""
                    if row[12]=="A": 
                        tot_E[0]+=row[13]
                        if row[14]=="S": tot_E[1]+=row[13]
                        if row[14]=="R" or row[14]=="Z": tot_E[2]+=row[13]
                    else:
                        tot_U[0]+=row[13]
                        if row[14]=="S": tot_U[1]+=row[13]
                        if row[14]=="R" or row[14]=="Z": tot_U[2]+=row[13]

                    self.lc.SetItemData(0,0)
        except StandardError, msg:
            self.__MDI__.MsgErr("lstscad","RmpLc Error %s " % (msg))
        if not rows: self.Message("Dati non presenti",self.ttl) 
        if rec_vCF=="" or rec_vCF=="T":
            self.vCF.SetValue('T')
            self.SelCOMBOcf(self)
        cnt_tot=0
        while cnt_tot<=2:
            if tot_E[cnt_tot]!=0:
                self.__MDI__.CnvVM(tot_E[cnt_tot])
                tot_E[cnt_tot]=self.__MDI__.val
            if tot_U[cnt_tot]!=0:
                self.__MDI__.CnvVM(tot_U[cnt_tot])
                tot_U[cnt_tot]=self.__MDI__.val
            cnt_tot+=1


        self.tot_U.SetLabel(str(tot_U[0]))
        self.tot_sald_U.SetLabel(str(tot_U[1]))
        self.tot_nsald_U.SetLabel(str(tot_U[2]))
        self.tot_E.SetLabel(str(tot_E[0]))
        self.tot_sald_E.SetLabel(str(tot_E[1]))
        self.tot_nsald_E.SetLabel(str(tot_E[2]))

        self.CnAz.commit()
        self.currentItem = 0
        self.inte.Show(True)
        self.canc.Show(False)



        # FINE FUNZIONE FIND


    def OnFndDoc(self, evt):
        #self.TIPO_SCAD.Enable(False)
        self.TIPO_DOC.Enable(True)
        self.num_doc.Enable(True)
        self.cnum_doc.Enable(True)
        #if self.TIPO_DOC.GetValue()=="":
            #self.CF.Enable(False)
            #self.vCF.SetValue('C')
            #self.SelCOMBOcf(self)
        self.inte.Show(True)
        self.canc.Show(False)


    def OffFndDoc(self, evt):
        self.TIPO_DOC.Enable(False)
        self.num_doc.Enable(False)
        self.cnum_doc.Enable(False)
        self.TIPO_DOC.SetValue('')
        self.vTIPO_DOC.SetValue('')
        self.sTIPO_DOC=''
        self.num_doc.SetValue('')
        self.vnum_doc.SetValue('')

        #self.inte.Show(False)
        #self.canc.Show(True)





    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()



        
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
            
    def Ok(self, event):
        self.DblClick(self.currentItem)
        
    def Close(self, event):
        self.AggMenu(True,self.IDMENU)
        wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        #self.Destroy()
              
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

    def DblClick(self, event):
        #ottl=self.ottl
        #Dir="cont"
        #Mod="movcon"
        tbl="scad"
        rec=(self.getColTxt(self.currentItem, 0))
        #AggMenu=self.AggMenu
        #IDMENU=self.IDMENU
        #self.CMD(rec, Dir, Mod, ottl, tbl)       
        self.CMD(2009,rec,tbl)
        #self.AggMenu(True,self.IDMENU)
        #self.Destroy()
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)


