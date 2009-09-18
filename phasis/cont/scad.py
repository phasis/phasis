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
#from wxPython.wx import *
from cfg import *
import cfg
import string 
import  wx.lib.masked as masked
import datetime


def create(parent,cnt):
    return scad(parent,cnt)
 
class scad(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) 
        self.FitInside()  
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        self.cnt = cnt
        self.ttl=cnt[0]
        self.rec=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        #self.font=self.GetFont()
        self.vCodTblG= cnt[1]
        Nid = wx.NewId()
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz=self.__MDI__.GetConnAZ()

        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon= self.__MDI__.GetDataC()



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
            print "Scad"," New Error %s"  % (msg)

        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL) 
        self.pnl.SetFont(self.font)
   
   
        # linea 1

        self.sbox_reg = wx.StaticBox(self.pnl, Nid, " Registrazione ",
              wx.DLG_PNT(self.pnl, 5,7), wx.DLG_SZE(self.pnl, 275,30))

        self.lscad = wx.StaticText(self.pnl, -1, "Num. :", 
              wx.DLG_PNT(self.pnl, 10,20))
        self.num_scad = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 35,18), wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) 
        self.cnum_scad = wx.BitmapButton(self.pnl, -1, png, 
              wx.DLG_PNT(self.pnl, 77,18),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV), wx.TE_PROCESS_ENTER)



        self.ldata_scad=wx.StaticText(self.pnl, -1, _("Data Scad.:"), 
              wx.DLG_PNT(self.pnl, 93,20))
        self.ldata_scad.SetFont(self.font)
        self.data_scad = masked.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 130,18), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT,autoformat='EUDATEDDMMYYYY/')
        self.vdata_scad = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 130, 18))


        self.TIPO_SCAD = wx.ComboBox(self.pnl, 300,"",
              wx.DLG_PNT(self.pnl, 181,18), wx.DLG_SZE(self.pnl, 90,-1),[],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vTIPO_SCAD = wx.TextCtrl(self.pnl , -1, "",
              wx.DLG_PNT(self.pnl , 181,18), 
              wx.DLG_SZE(self.pnl , 0, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)



        #  linea 2

        self.sbox_pag = wx.StaticBox(self.pnl, Nid, " Pagamento ",
              wx.DLG_PNT(self.pnl, 5,38), wx.DLG_SZE(self.pnl, 275,30))


        self.lPAGAM = wx.StaticText(self.pnl, -1, "Cond. Pag.:", 
              wx.DLG_PNT(self.pnl, 10,52))

        self.PAGAM = wx.ComboBox(self.pnl, -1,"",
              wx.DLG_PNT(self.pnl, 48,50), wx.DLG_SZE(self.pnl, 100,-1),
              [],wx.CB_DROPDOWN | wx.CB_SORT )
        self.vPAGAM = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 48,50))


        self.lDA = wx.StaticText(self.pnl, -1, "D/A:", 
              wx.DLG_PNT(self.pnl, 151,52))

        self.DA = wx.ComboBox(self.pnl, 300,"",
              wx.DLG_PNT(self.pnl, 166,50), wx.DLG_SZE(self.pnl, 40,-1),[],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vDA = wx.TextCtrl(self.pnl , -1, "",
              wx.DLG_PNT(self.pnl , 166,50), 
              wx.DLG_SZE(self.pnl , 0, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)


        self.ltotale = wx.StaticText(self.pnl, -1, "Tot.:", 
              wx.DLG_PNT(self.pnl, 214,52))
        self.totale = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 228,50),     
              wx.DLG_SZE(self.pnl, 45,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) 

        # linea 3

        wx.StaticText(self.pnl, -1, "Contropartita:", 
              wx.DLG_PNT(self.pnl, 5,77)) 
        self.CF = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 55,75), wx.DLG_SZE(self.pnl, 50,-1), [],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vCF = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 55,75))

        self.lc1odcf = wx.StaticText(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 110,77))
        self.codcf= wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 170, 75), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT))



        # linea 4

        self.lragsoc1 = wx.StaticText(self.pnl,-1,"Rag.Soc.1:", 
              wx.DLG_PNT(self.pnl, 5,92))
        self.ragsoc1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 42,90), 
              wx.DLG_SZE(self.pnl, 80,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.cragsoc1 = wx.BitmapButton(self.pnl, -1, png,
              wx.DLG_PNT(self.pnl, 125,90),


              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))     
        self.lragsoc2 = wx.StaticText(self.pnl, -1, "Rag. Soc.2:", 
              wx.DLG_PNT(self.pnl, 150,92))
        self.ragsoc2 = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 187, 90), 
              wx.DLG_SZE(self.pnl, 90,cfg.DIMFONTDEFAULT))  

        self.ragsoc4 = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 42, 90), 
              wx.DLG_SZE(self.pnl, 90,cfg.DIMFONTDEFAULT)) 


        self.rbREG = wx.RadioButton(self.pnl, -1, "Registrato",
              wx.DLG_PNT(self.pnl, 285,75), 
              wx.DLG_SZE(self.pnl, 60,10))
        self.rbSALD = wx.RadioButton(self.pnl, -1, "Saldato",
              wx.DLG_PNT(self.pnl, 285,90), 
              wx.DLG_SZE(self.pnl, 60,10))
        self.rbSCAD = wx.RadioButton(self.pnl, -1, "Scaduto",
              wx.DLG_PNT(self.pnl, 285,105), 
              wx.DLG_SZE(self.pnl, 60,10))
 
        # linea 5

        self.sbox_doc = wx.StaticBox(self.pnl, Nid, " Documento Phasis ",
              wx.DLG_PNT(self.pnl, 5,108), wx.DLG_SZE(self.pnl, 275,45))


        self.ltipodoc = wx.StaticText(self.pnl, -1, "Tipo Documento.:", 
              wx.DLG_PNT(self.pnl, 10,122))
        self.TIPO_DOC = wx.ComboBox(self.pnl, 300,"",
              wx.DLG_PNT(self.pnl, 68,120), wx.DLG_SZE(self.pnl, 110,-1),[],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vTIPO_DOC =  wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 68,120))

        self.stt_doc1 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 68,120))  
        self.stt_doc2 = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 68,120))  


        self.ldoc = wx.StaticText(self.pnl, -1, "N.Doc.:", 
              wx.DLG_PNT(self.pnl, 181,122))

        self.num_doc = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 203,120), 
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)    

        self.cnum_doc = wx.BitmapButton(self.pnl, -1, png,
              wx.DLG_PNT(self.pnl, 235,120),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.vnum_doc = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 235, 120))

        self.ldata_doc=wx.StaticText(self.pnl, -1, _("Data Doc.:"), 
              wx.DLG_PNT(self.pnl, 10,137))
        self.ldata_doc.SetFont(self.font)
        self.data_doc = masked.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 68,135), 
              wx.DLG_SZE(self.pnl, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT,autoformat='EUDATEDDMMYYYY/')
        self.vdata_doc = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 130, 135))


        wx.StaticText(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 181,150))





        #pulsanti
              
        self.new = wx.Button(self.pnl, Nid, cfg.vcnew, 
              wx.DLG_PNT(self.pnl, 285,10), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.new.SetFont(self.font)
              
        self.ok = wx.Button(self.pnl, Nid, cfg.vcok, 
              wx.DLG_PNT(self.pnl, 285,10), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))    
        self.ok.SetFont(self.font)
                                    
        self.inte = wx.Button(self.pnl, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 285,25), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.inte.SetFont(self.font)
              
        self.canc = wx.Button(self.pnl, Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 285,25), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFont(self.font)
              
        self.modi = wx.Button(self.pnl, Nid, cfg.vcmodi, 
              wx.DLG_PNT(self.pnl, 285,40), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.modi.SetFont(self.font)
                        
        self.dele = wx.Button(self.pnl, Nid, cfg.vcdele, 
              wx.DLG_PNT(self.pnl, 285,40), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.dele.SetFont(self.font)
              
        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 285,55), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa.SetFont(self.font)
              
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)
        
        #self.rbREG.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        #self.rbSALD.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.TIPO_SCAD.Bind(wx.EVT_COMBOBOX, self.SelCOMBOtiposcadev)
        self.PAGAM.Bind(wx.EVT_COMBOBOX, self.SelPAGAMev)
        self.TIPO_DOC.Bind(wx.EVT_COMBOBOX, self.SelCOMBOtipodocev)
        self.DA.Bind(wx.EVT_COMBOBOX, self.SelCOMBOdaev)
        self.CF.Bind(wx.EVT_COMBOBOX, self.SelCOMBOcfev)
        self.cnum_doc.Bind(wx.EVT_BUTTON, self.FndDocPha)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.cnum_scad.Bind(wx.EVT_BUTTON, self.FndScad)
        self.ok.Bind(wx.EVT_BUTTON, self.Save)
        self.new.Bind(wx.EVT_BUTTON, self.New)  
        self.inte.Bind(wx.EVT_BUTTON, self.Intscad) 
        self.modi.Bind(wx.EVT_BUTTON, self.Modi)      
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.dele.Bind(wx.EVT_BUTTON, self.CntrDele)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.Start(self)

    def Stampa(self, evt):  # tutto da sistemare modulo non esiste. errori vari. impossibile capitarci
        tbl=self.tbl
        #import VPrtTblcf   
        #control = [codgen,valore,tbl]
        #win = VPrtTblcf.create(self,control)
        #win.Centre(wx.BOTH)
        #win.Show(True)
        
    def Start(self, evt):
        self.rbREG.Enable(False)
        self.rbSALD.Enable(False)
        self.rbSCAD.Enable(False)
        self.rbREG.SetValue(True)
        self.rbSALD.SetValue(False)
        self.rbSCAD.SetValue(False)
        self.stampa.Show(False)
        #self.data = self.datacon   
        #self.data_scad.SetValue(self.data)
        self.data_scad.SetValue('  /  /    ')
        self.num_scad.SetValue('')
        self.num_scad.Enable(True)
        self.cnum_scad.Enable(True)

        self.vTIPO_DOC.Show(False)
        self.vdata_doc.Show(False)
        self.vDA.Show(False)
        self.vPAGAM.Show(False)
        self.stt_doc1.Show(False)
        self.stt_doc2.Show(False)
        self.vTIPO_SCAD.Show(False) 
        self.vdata_scad.Show(False) 
        self.vnum_doc.Show(False)
        self.vnum_doc.SetValue('')
        self.num_doc.SetValue('')
        self.vCF.Show(False)
 
        self.TIPO_SCAD.Enable(False)
        self.data_scad.Enable(False)
        self.PAGAM.Enable(False)
        self.DA.Enable(False)
        self.totale.Enable(False)
        self.CF.Enable(False)
        self.ragsoc1.Enable(False)
        self.cragsoc1.Enable(False)
        self.ragsoc4.Show(False)
        self.ragsoc2.Enable(False)
        self.codcf.Enable(False)

        self.TIPO_DOC.Enable(False)
        self.num_doc.Enable(False)
        self.cnum_doc.Enable(False)
        self.data_doc.Enable(False)

        self.DelTxt(self)
        #self.OnTxt(self)
        self.dele.Enable(False)
        self.dele.Show(False) # aggiunto per errore visualizzione mac
        self.stampa.Enable(False)
        self.modi.Enable(False)
        self.new.Show(True)
        self.ok.Show(False)
        self.inte.Show(False)
        self.canc.Show(True)

        self.cntr=""

        self.vPAGAM.SetValue('PAG00')
        self.vTIPO_DOC.SetValue('PC')
        self.vTIPO_SCAD.SetValue('S01')
        self.vCF.SetValue('C')
        self.vDA.SetValue('D')

        self.sPAGAM = ''
        self.sTIPO_DOC = ''
        self.sTIPO_SCAD = ''
        self.sDA = ''
        self.sCF = ''

        self.SelPAGAM(self)
        self.SelCOMBOtipodoc(self)
        self.SelCOMBOtiposcad(self)
        self.SelCOMBOda(self)
        self.SelCOMBOcf(self)

        self.num_scad.SetFocus()
        if (self.rec!=""):
            self.num_scad.SetValue(self.rec)
            self.FndScad(self)


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


    def SelCOMBOtiposcad(self, evt):   
        vTIPO_SCAD = self.vTIPO_SCAD.GetValue()
        self.TIPO_SCAD.Clear()
        sql = """ select * from scadenze order by descriz asc """
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


    def SelCOMBOda(self, evt):
        vDA = self.vDA.GetValue()
        self.DA.Clear()
        self.DA.Append('Dare','D')
        self.DA.Append('Avere','A')
        if vDA=="D":vDA=0
        if vDA=="A":vDA=1
        self.DA.Select(vDA)

    def SelCOMBOcf(self, evt):
        vCF = self.vCF.GetValue()
        self.CF.Clear()
        self.CF.Append('Cliente','C')
        self.CF.Append('Fornitore','F')
        self.CF.Append('Agente','A')
        self.CF.Append('Altro','Z')
        if vCF=="C":
            vCF=0
            self.lc1odcf.SetLabel(" Codice Cliente:")
            self.codcf.Show(True)
        if vCF=="F":
            vCF=1
            self.lc1odcf.SetLabel(" Codice Fornitore:")
            self.codcf.Show(True)
        if vCF=="A":
            vCF=2
            self.lc1odcf.SetLabel(" Codice Agente:")
            self.codcf.Show(True)
        if vCF=="Z":
            vCF=3
            self.lc1odcf.SetLabel("")
            self.codcf.Show(False)
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


    def SelCOMBOdaev(self, evt):
        self.Sel(evt)
        self.vDA.SetValue(self.cb_val)

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
            self.vCF.SetValue(self.val1)
            self.SelCOMBOcf(self)
            self.CF.Enable(False)
            self.cragsoc1.Show(False)
            self.codcf.Show(False)
        else:
            self.vCF.SetValue(self.val1)
            self.SelCOMBOcf(self)
            self.CF.Enable(False)
            self.cragsoc1.Show(True)
            self.codcf.Show(True)




    def ContTipoDoc(self, evt):
        tipo_doc = self.vTIPO_DOC.GetValue()
        if tipo_doc=="PF" or tipo_doc=="B3":
            self.vCF.SetValue('F')
            self.vDA.SetValue('D')
        else:
            self.vCF.SetValue('C')
            self.vDA.SetValue('A')
        self.SelCOMBOcf(self)
        self.SelCOMBOda(self)
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.codcf.SetValue('')
        self.vnum_doc.SetValue('')
        self.num_doc.SetValue('')
        self.totale.SetValue('')
        self.data_doc.SetValue('  /  /    ')
        self.vdata_doc.SetValue('')
        self.vPAGAM.SetValue('PAG00')
        self.SelPAGAM(self)

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
        if  tcpart=="A": self.lc1odcf.SetLabel(" Cod. Agente. :")
        if  tcpart=="Z": self.lc1odcf.SetLabel(" Cod.:")



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





    def FndDocPha(self, evt):
        TipoIns=0
        cnt_rec = 0
        self.tblDoc=""
        vTIPO_DOC = self.vTIPO_DOC.GetValue()
        rag_soc1 = self.ragsoc1.GetValue()
        rag_soc2 = self.ragsoc2.GetValue()       
        cod_cf = self.codcf.GetValue()
        anno = self.annoc
        if cod_cf=="":cod_cf=0


        if vTIPO_DOC=="PC" or vTIPO_DOC=="PF":
            self.tblDoc = "ordi1"
            self.campoTblTipo = "tipo_ord"
            self.campoTblNum = "num_ord"
            self.tipoDoc=vTIPO_DOC
        else:
            self.tblDoc = "docu1"
            self.campoTblTipo = "tipo_doc"
            self.campoTblNum = "num_doc"
            self.tipoDoc=vTIPO_DOC

        if self.vnum_doc.GetValue()=="" and self.num_doc.GetValue()=="":
            #if self.tblDoc=="ordi1":
            if rag_soc1=="": 
                sql = """ select * from "%s" where "%s" = "%s" and anno = "%s" """
                valueSql = self.tblDoc, self.campoTblTipo, self.tipoDoc, anno
            else:
                #print "num_doc != vuoto"
                sql = """ select * from "%s" 
                          where "%s" = "%s" 
                          and rag_soc1 like "%s" 
                          and cod_cf = "%s" 
                          and anno = "%s" """
                valueSql = self.tblDoc, self.campoTblTipo, self.tipoDoc, \
                           rag_soc1, int(cod_cf), anno

            #elif self.tblDoc=="docu1": 
                #sql = """ select * from "%s" where tipo_doc = "%s" """
                #valueSql = self.tblDoc,self.tipoDoc

        else:
            cnt_rec=0
            data_doc = self.data_doc.GetValue()
            TIPO_DOC = self.vTIPO_DOC.GetValue()
            num_doc = self.vnum_doc.GetValue()
            sql = """ select * from scad where num_doc= "%s" 
                      and tipo_doc = "%s" and anno = "%s" """
            valueSql = num_doc,TIPO_DOC,anno
            cr = self.CnAz.cursor()
            cr.execute(sql % valueSql)
            rows = cr.fetchall() 
            for row in rows:cnt_rec+=1
            if cnt_rec!=0:
                TipoIns=1 
                self.Message("Attenzione Scadenza presente in archivio",self.ttl) 
            else: 
                self.CnAz.commit()
                if self.vnum_doc.GetValue()=="": 
                    self.vnum_doc.SetValue(self.num_doc.GetValue()) 
                valueSql = self.tblDoc, self.campoTblNum, \
                           self.vnum_doc.GetValue(), \
                           self.campoTblTipo, self.tipoDoc, anno
                sql = """ select * from "%s" where "%s" = "%s" 
                          and "%s" = "%s" and anno = "%s" """
        try:
            cnt_rec=0
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows: cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("scad","FndDocPha Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2 and TipoIns==0): self.FndSelDoc(row)
        elif (cnt_rec==1 and cnt_rec<2 and TipoIns==1): self.FndSelScad(row)
        elif (cnt_rec>1):
            try:
	        import srcscad
            except:
                pass
            control = [self.tblDoc,self.tipoDoc,self.vnum_doc,
                      rag_soc1,rag_soc2,cod_cf,self.FndDocPha]
            win = srcscad.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)



        

    def FndSelDoc(self, evt):
        self.vnum_doc.SetValue('')
        row=evt
        tbl = self.tblDoc
        if tbl=="ordi1":
            self.num_doc.SetValue(str(row[2]))
            self.codcf.SetValue(str(row[4]))
            self.ragsoc1.SetValue(str(row[5]))
            self.ragsoc2.SetValue(str(row[6]))
            self.CalcolaScad(self,row[3],row[29])
            self.data_doc.SetValue(row[3])
        elif tbl=="docu1":
            self.num_doc.SetValue(str(row[2]))
            self.codcf.SetValue(str(row[4]))
            self.ragsoc1.SetValue(str(row[5]))
            self.ragsoc2.SetValue(str(row[6]))
            self.CalcolaScad(self,row[3],row[28])
            self.data_doc.SetValue(row[3])
        self.CalcolaTot(self)


    def CalcolaScad(self, evt, a, b):
        data = a.split("/")
        data_doc = datetime.date(int(data[2]), int(data[1]), int(data[0]))

        tot_giorni = 0
        if b=="RD03" or b=="RD07" or b=="RD08" or b=="RD09":tot_giorni=30
        if b=="RD05":tot_giorni=60
        if b=="RD06":tot_giorni=90


        data_scad = datetime.timedelta(days=tot_giorni)
        data_scad = data_doc + data_scad
        val = str(data_scad)
        val = val.split("-") 
        data_scad = val[2] + "/" + val[1] + "/" + val[0]
        self.data_scad.SetValue(str(data_scad))
        self.vPAGAM.SetValue(b)
        self.SelPAGAM(self)
 

    def CalcolaTot(self, evt):
        totale=0
        tblDoc2 = self.tblDoc.replace("1","2") 
        valueSql=tblDoc2,self.campoTblTipo,self.tipoDoc,self.campoTblNum,self.num_doc.GetValue()
        sql = """ select tot_riga from "%s" where "%s"="%s" and "%s"="%s" """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:totale+=row[0]
            self.__MDI__.CnvVM(totale)
            totale=self.__MDI__.val
        except StandardError, msg:
            #self.__FRM__.MsgErr("SrcAnag"," Cerca Error %s"  % (msg))
            print "Totale D/A Error %s" % (msg) 
        self.totale.SetValue(str(totale))
        self.CnAz.commit()


    def FndSelScad(self, evt):
        row=evt
        self.num_scad.SetValue(str(row[0]))
        # INSERIRE ANNO 
        self.data_scad.SetValue(row[2])
        self.vTIPO_SCAD.SetValue(row[3])
        self.SelCOMBOtiposcad(self)
        self.vPAGAM.SetValue(row[4])
        self.SelPAGAM(self)
        self.vCF.SetValue(row[5])
        self.SelCOMBOcf(self) 
        self.codcf.SetValue(str(row[6]))
        self.ragsoc1.SetValue(row[7])
        self.ragsoc2.SetValue(row[8])

        if row[14]=="R":
            self.rbREG.SetValue(True)
            self.rbSALD.SetValue(False)
            self.rbSCAD.SetValue(False)
        elif row[14]=="S":
            self.rbREG.SetValue(False)
            self.rbSALD.SetValue(True)
            self.rbSCAD.SetValue(False)
        elif row[14]=="Z":
            self.rbREG.SetValue(False)
            self.rbSALD.SetValue(False)
            self.rbSCAD.SetValue(True)

        if self.vTIPO_SCAD.GetValue()=="S03":
            self.data_doc.SetValue(row[9])
            self.vTIPO_DOC.SetValue(row[10])
            self.SelCOMBOtipodoc(self)
            self.num_doc.SetValue(str(row[11]))
            self.vnum_doc.SetValue(str(row[11]))


        self.vDA.SetValue(row[12])
        self.SelCOMBOda(self)      
        self.__MDI__.CnvVM(row[13])
        totale=self.__MDI__.val 
        self.totale.SetValue(totale)
        #self.stt_scad.SetValue(row[14]) # da fare
        self.OffTxt(self)
        self.dele.Show(False)
        self.modi.Show(True)
        self.modi.Enable(True)
        self.modi.SetFocus()
        self.canc.Show(False)
        self.inte.Show(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(False)



    def OnFndDoc(self, evt):
        #print "OnFndDoc"
        self.TIPO_SCAD.Enable(False)
        #self.data_scad.Enable(False)
        #self.PAGAM.Enable(False)
        self.TIPO_DOC.Enable(True)
        self.data_doc.Enable(True)
        self.num_doc.Enable(True)
        self.cnum_doc.Enable(True)
        self.CF.Enable(False)
        self.vCF.SetValue('C')
        self.vDA.SetValue('A')
        self.SelCOMBOcf(self)
        self.SelCOMBOda(self)

    def Intscad(self, evt):
        self.rec=""
        self.Start(self)
        self.canc.Show(True)
        self.new.Show(True)
        self.ok.Show(False)
        self.dele.Show(False)
        self.dele.Enable(False)
        self.stampa.Enable(False)
            
    def NewTxt(self, evt):
        self.OnTxt(self)
        self.Ins_Cont(self)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.dele.Show(False)
        self.TIPO_SCAD.SetFocus()


       
    def Ins_Cont(self, evt):
        cnt_rec=0
        num_scad=0 
        sql = " SELECT * FROM scad ORDER BY cod ASC"
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec += 1
            if cnt_rec!=0: num_scad = row[0]
            if num_scad=="": num_scad=1
            else: num_scad+=1
            self.num_scad.SetValue(str(num_scad))
        except StandardError, msg:
            self.__MDI__.MsgErr("scad"," Ins cont Error %s " % (msg)) 
        self.CnAz.commit()

        


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
        self.Start(self)

    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()
        
    def OffTxt(self, evt):
        self.cntr=""

    def OnTxt(self ,evt):
        self.num_scad.Enable(True)
        self.cnum_scad.Enable(True)
        self.data_scad.Enable(True)
        self.TIPO_SCAD.Enable(True)
        self.PAGAM.Enable(True)
        self.DA.Enable(True)
        self.totale.Enable(True)
        self.CF.Enable(True)
        self.ragsoc1.Enable(True)
        self.cragsoc1.Enable(True)
        self.ragsoc2.Enable(True)
        self.num_scad.Enable(False)
        self.cnum_scad.Enable(False)
        self.codcf.Enable(True)
        self.rbREG.Enable(True)
        self.rbSALD.Enable(True)
        self.rbSCAD.Enable(True)

    def DelTxt(self, evt):
        self.cntr=""
        self.totale.SetValue('')
        self.num_doc.SetValue('')
        self.codcf.SetValue('')
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.num_doc.SetValue('')
        self.vdata_doc.SetValue('')
        self.data_doc.SetValue('')


    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
            
    def SetFcs(self, evt):
        evt.Skip()
        
            
    def Close(self, evt):
        if (self.TIPO_SCAD.GetValue()!=""):
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
        dlg = wx.MessageDialog(self, cfg.msgmodi_tbl, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.ModiTxt(self)
            self.cntr="modi"
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()
 
    def New(self, evt):
        self.DelTxt(self)     
        self.cntr="new"
        self.NewTxt(self)
        sql = " SELECT COUNT(cod) FROM scad "
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            while (1):
                row=cr.fetchone()
                if row == None:
                    break
                if (row[0] == None) : cnt_rec=1
        except StandardError, msg:
            self.__MDI__.MsgErr("scad"," New Error %s " % (msg)) 
        self.CnAz.commit()

       
          
 ################ da fare       
    def Save(self, evt):
        vcntr=self.cntr
        num_scad = self.num_scad.GetValue()
        anno = self.__MDI__.GetAnnoC()
        data_scad = self.data_scad.GetValue()
        TIPO_SCAD = self.vTIPO_SCAD.GetValue()
        PAGAM = self.vPAGAM.GetValue()
        CF = self.vCF.GetValue()
        codcf = self.codcf.GetValue()
        ragsoc1 = self.ragsoc1.GetValue().title()
        ragsoc2 = self.ragsoc2.GetValue().title()
        ragsoc4 = self.ragsoc4.GetValue().title()

        if ragsoc4!="":ragsoc1=ragsoc4;ragsoc2=""


        if codcf=="": codcf=0


        DA = self.vDA.GetValue()

        totale = self.totale.GetValue()
        self.__MDI__.CnvPM(totale)
        totale=self.__MDI__.val


        # inserire controlli
        data_scad = self.data_scad.GetValue()

        if data_scad=="  /  /    ": 
            controlli = 0
            self.data_scad.SetFocus() 
        else:
            data_scad_int = data_scad.split("/")
            data_scad_int = str(data_scad_int[2]) + str(data_scad_int[1]) + str(data_scad_int[0])
            data_att_int=self.datacon.split("/")
            data_att_int=str(data_att_int[2]) + str(data_att_int[1]) + str(data_att_int[0])  
            controlli=1


        if self.rbREG.GetValue():
            stt_scad = "R" # da fare  
        elif self.rbSALD.GetValue():
            stt_scad = "S"
        elif self.rbSCAD.GetValue():
            stt_scad = "Z"

        if data_scad_int<=data_att_int and self.rbSCAD.GetValue()=="False": stt_scad = "Z"


        if self.val1=="T":
            cnt_rec=0
            data_doc = self.data_doc.GetValue()
            TIPO_DOC = self.vTIPO_DOC.GetValue()
            num_doc = self.num_doc.GetValue()
        else:
            data_doc = ""
            TIPO_DOC = ""
            num_doc = 0


        if totale=="0" and controlli==1: controlli=0; self.totale.SetFocus()
        if codcf=="" and controlli==1 and CF!="Z": controlli=0; self.ragsoc1.SetFocus()
        if ragsoc1=="" and controlli==1: controlli=0; self.ragsoc1.SetFocus()
         

        if (controlli==0):
            self.Message(cfg.msgcmp_null,self.ttl)
        else:
            self.SaveTxt(self)
            if(vcntr=="new"):
                cicli=1 
                tot_giorni = 30
                if PAGAM=="RD07": cicli=2;# tot_giorni = 30
                elif PAGAM=="RD08": cicli=3;# tot_giorni = 30
                elif PAGAM=="RD09": cicli=4;# tot_giorni = 30
                #elif PAGAM=="RD03": cicli=1;# tot_giorni = 30
                elif PAGAM=="RD05": cicli=1; tot_giorni = 60
                elif PAGAM=="RD06": cicli=1; tot_giorni = 90

                totale=totale/cicli

                cont=1

                while cont<=cicli:
                    if cicli>1 and cont>1:    
                        data = data_scad.split("/")
                        data_doc_mod = datetime.date(int(data[2]), int(data[1]), int(data[0]))
                        data_scad = datetime.timedelta(days=tot_giorni)
                        data_scad = data_doc_mod + data_scad
                        val = str(data_scad)
                        val = val.split("-") 
                        data_scad = val[2] + "/" + val[1] + "/" + val[0]
                        data_scad_int = data_scad.split("/")
                        data_scad_int = str(data_scad_int[2]) + str(data_scad_int[1]) + str(data_scad_int[0])
                    group1 = int(num_scad), anno, data_scad, TIPO_SCAD, PAGAM, CF, int(codcf)
                    group2 = ragsoc1, ragsoc2, data_doc, TIPO_DOC, int(num_doc), DA
                    group3 = float(totale), stt_scad, int(data_scad_int)

                    valueSql = group1 + group2 + group3
                    cont+=1
                    num_scad=int(num_scad) + 1

                    try:
                        cr = self.CnAz.cursor()
                        sql = """ INSERT INTO scad VALUES("%s","%s","%s","%s","%s",
                                                          "%s","%s","%s","%s","%s",
                                                          "%s","%s","%s","%s","%s","%s") """
                        cr.execute(sql % valueSql)  
                    except StandardError, msg:
                        self.__MDI__.MsgErr("scad"," Save New Error %s " % (msg)) 
                    self.CnAz.commit()

            if(vcntr=="modi"):
                group1_modi = anno, data_scad, TIPO_SCAD, PAGAM, CF, int(codcf)
                group2_modi = ragsoc1, ragsoc2, data_doc, TIPO_DOC, int(num_doc)
                group3_modi = DA, float(totale), stt_scad, int(data_scad_int), int(num_scad)

                valueSql_modi = group1_modi + group2_modi + group3_modi
                try:
                    cr = self.CnAz.cursor()
                    sql = """ UPDATE scad SET anno = '%s', 
                              data_scad = '%s', tipo_scad = '%s', 
                              pagam = '%s', t_cpart = '%s', 
                              cod_cf = '%s', rag_soc1 = '%s', 
                              rag_soc2 = '%s', data_doc = '%s', 
                              tipo_doc = '%s', num_doc = '%s', 
                              da = '%s', totale = '%s', 
                              stt_scad = '%s', data_scad_int = '%s' WHERE cod = '%s' """
                    cr.execute(sql % valueSql_modi)  
                except StandardError, msg:
                    self.__MDI__.MsgErr("scad"," Save Modi Error %s " % (msg)) 
                self.CnAz.commit()



    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgnodele_valtbl, self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr=""
            dlg.Destroy()
            
    def Dele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdele_valtbl,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.cntr="dele"
            num_scad = self.num_scad.GetValue()
            #codgen = self.codgen.GetValue()
            valueSql = num_scad 
            sql = " DELETE FROM scad WHERE COD = '%s' "
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
            except StandardError, msg:
                self.__MDI__.MsgErr("scad"," Dele Error %s " % (msg)) 
            self.CnAz.commit()
            self.Intscad(self)
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()

    def FndScad(self, evt):
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec=0
            num_scad = self.num_scad.GetValue()
            #des = self.descriz.GetValue()
            sql = """ SELECT * FROM scad WHERE COD = '%s' 
                      ORDER BY data_scad_int DESC """
            valueSql = num_scad
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql )
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                self.__MDI__.MsgErr("scad"," FndDescriz Error %s " % (msg)) 
            self.CnAz.commit()
            if (cnt_rec==0):                
                import srclstscad
                control = [self.annoc,self.num_scad,self.FndScad]
                win = srclstscad.create(self,control) 
                win.Centre(wx.BOTH)
                win.Show(True)
            if (cnt_rec==1 and cnt_rec<2):self.FndSelScad(row)




    def is_look(self):
        if (self.cntr!="new" and self.cntr!="modi"): return False
        else : return True
        
    def data_reload(self,rec,cntrp):
        self.rec=rec
        #self.tcpart=cntrp.upper()
        self.Start(self)

