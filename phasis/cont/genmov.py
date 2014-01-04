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


def create(parent,cnt):
    return ConsolidaMov(parent,cnt)
  
class ConsolidaMov(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######

        #wx.Frame.__init__(self, id=wx.NewId(), name='',
        #      parent=prnt, pos=wx.Point(0, 0), 
        #      style=wx.DEFAULT_FRAME_STYLE  , title=cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.SetClientSize(wx.Size(600, 455))
        self.ttl = cnt[0]
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        #self.font = self.GetFont()
        self.color = self.GetBackgroundColour()
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz=self.__MDI__.GetConnAZ()
        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon = self.__MDI__.GetDataC()
        self.dzDatiAzienda = self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id=wx.NewId(),name='',parent=self,pos=wx.Point(0,0),
            style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)       
        self.pnl.SetFont(self.font)

        self.sbox = wx.StaticBox(self.pnl, -1,'',
              wx.DLG_PNT(self.pnl, 140,5), wx.DLG_SZE(self.pnl, 100,40))
        self.rbFT = wx.RadioButton(self.pnl, -1, _("Fatture"),
              wx.DLG_PNT(self.pnl, 150,10),
              wx.DLG_SZE(self.pnl, 120,10))
        self.rbNC = wx.RadioButton(self.pnl, -1, _("Note di Credito"),
              wx.DLG_PNT(self.pnl, 150,20), 
              wx.DLG_SZE(self.pnl, 120,10) )
        self.rbRF = wx.RadioButton(self.pnl, -1, _("Ricevute Fiscali"),
              wx.DLG_PNT(self.pnl, 150,30),
              wx.DLG_SZE(self.pnl, 120,10))    
        self.tdoc = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 60,45))
    
        wx.StaticText(self.pnl, -1, _("Mese :"), wx.DLG_PNT(self.pnl, 40,12))
        self.lbldoc = wx.StaticText(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 10,45))
        self.MM = wx.ComboBox(self.pnl, -1,"",
              wx.DLG_PNT(self.pnl, 60,10), wx.DLG_SZE(self.pnl, 65,-1),[],
              wx.CB_DROPDOWN )
        self.vMM = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 60,30))
        self.MMmov = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 60,45))
        self.lc = wx.ListCtrl(self.pnl, -1,
              wx.DLG_PNT(self.pnl, 5,60), wx.DLG_SZE(self.pnl, 323,120),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)   
        self.inte = wx.Button(self.pnl, -1, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 275,10), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV)) 
        self.canc = wx.Button(self.pnl, -1, cfg.vccanc,
              wx.DLG_PNT(self.pnl, 275,10),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.ok = wx.Button(self.pnl, -1, cfg.vcconf, 
              wx.DLG_PNT(self.pnl, 275,25),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.sele = wx.Button(self.pnl, -1, cfg.vcselez, 
              wx.DLG_PNT(self.pnl, 275,25),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
       
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)
        
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Save) 
        self.sele.Bind(wx.EVT_BUTTON, self.FndDoc) 
        self.inte.Bind(wx.EVT_BUTTON, self.Start) 
        self.MM.Bind(wx.EVT_COMBOBOX, self.SelMM)   
        self.MM.Bind(wx.EVT_CHAR, self.EvtChar)   

        self.rbFT.Bind(wx.EVT_RADIOBUTTON, self.RadioB)        
        self.rbNC.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.rbRF.Bind(wx.EVT_RADIOBUTTON, self.RadioB)   
	self.AT_MovCon()	         
        self.Start(self)

    def AT_MovCon(self):
        sql = """ select causa from movcon """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            row = cr.fetchone () 
        except StandardError, msg:
            #print "Anag"," New Error %s"  % (msg)
            dlg = wx.MessageDialog(self, 
	          "Aggiornamento della tabella ......", 
		  "Aggiornamento Tabella ", wx.ID_OK | wx.ICON_INFORMATION)
            if dlg.ShowModal()==wx.ID_OK: dlg.Destroy()	    
	    import at_movcon
            self.AggMenu(True,self.IDMENU )
            wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        
    def Start(self, evt):
        self.MM.Clear()
        self.vMM.SetValue("0")
        self.MMmov.SetValue("0")
        self.SelCOMBO(self)
        self.canc.Show(True)
        self.canc.Enable(True)
        self.inte.Show(False)
        self.inte.Enable(False)
        self.ok.Show(False)
        self.ok.Enable(False)
        self.sele.Show(True)
        self.sele.Enable(False)
        self.lc.Show(True)
        self.lc.Enable(False)
        self.LC_clear(self)
        self.lc.Enable(False)
        self.vMM.Show(False)
        self.MMmov.Show(False)
        self.tdoc.SetValue("FT")        
        self.tdoc.Show(False)
        self.rbFT.SetValue(True)
        self.rbNC.SetValue(False)            
        self.rbRF.SetValue(False)
        self.lbldoc.SetLabel("")
        self.descriz = _("Fattura di vendita")
        self.rbFT.Enable(True)
        self.rbNC.Enable(True)
        self.rbRF.Enable(True)

    def RadioB(self, evt):
	if self.rbFT.GetValue()==True:	    
            self.rbFT.SetValue(True)
            self.rbNC.SetValue(False)            
            self.rbRF.SetValue(False)
            self.tdoc.SetValue("FT")
            self.descriz = _("Fattura di vendita")
        elif self.rbNC.GetValue()==True:
            self.rbFT.SetValue(False)
            self.rbNC.SetValue(True)    
	    self.rbRF.SetValue(False)
            self.tdoc.SetValue("NC")
            self.descriz = _("Nota di Credito")
        elif self.rbRF.GetValue()==True:
            self.rbFT.SetValue(False)
	    self.rbNC.SetValue(False)
            self.rbRF.SetValue(True) 
            self.tdoc.SetValue("RF")
            self.descriz = _("Ricevuta Fiscale")         
        self.MM.SetFocus()

    def SelCOMBO(self, evt):
        gma = self.datacon.split('/')
        mm = int(gma[1])
        cnt=0
        self.MM.Append('--','0')
        for sMM in cfg.mesi:
            cnt+=1
            self.MM.Append(sMM,str(cnt))
        cntMM=0
        cntMM = mm #self.MM.FindString('--')
        self.MM.Select(cntMM)

    def SelMM(self, evt):
        self.Sel(evt)
        val = int(self.cb_val)
        self.vMM.SetValue(str(val))
        self.inte.Show(True)
        self.inte.Enable(True) 
        self.canc.Show(False)
        self.canc.Enable(False)
        self.sele.Enable(True)
        self.sele.SetFocus()
        self.rbFT.Enable(False)
        self.rbNC.Enable(False)
        self.rbRF.Enable(False)


    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str= evt.GetString()
        evt.Skip()

    def LC_clear(self, evt):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Anno"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(1, _("Numero."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(2, _("Data Reg."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(3, _("Num. Riga"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(4, _("Anno IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(5, _("Cod. Div"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(6, _("Causale"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(7, _("Descrizione Operazione"),width=wx.DLG_SZE(self.pnl, 150,-1).width) #
        self.lc.InsertColumn(8, _("Importo"),width=cfg._COLSZ0_) 
        self.lc.InsertColumn(9, _("Imponibile"),width=cfg._COLSZ0_)     
        self.lc.InsertColumn(10, _("Anno Doc."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(11, _("Tipo Doc."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(12, _("Data Doc."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(13, _("Num Doc."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(14, _("Num Doc1."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(15, _("Conto"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(16, _("Importo"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(17, _("Segno"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(18, _("CPartita"),width=cfg._COLSZ0_)   
        self.lc.InsertColumn(19, _("Cambio"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(20, _("Tipo IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(21, _("Tipo IVA1"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(22, _("Aliq. IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(23, _("Registro"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(24, _("Imponibile"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(25, _("Rigagior"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(26, _("Paggior"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(27, _("Note"),width=cfg._COLSZ0_)        
        self.lc.InsertColumn(28, _("STT_MOV"),width=cfg._COLSZ0_)        
        self.lc.InsertColumn(29, _("Conto Dare/Avere"),width=wx.DLG_SZE(self.pnl, 60,-1).width) #
        self.lc.InsertColumn(30, _("Importo Dare"),width=wx.DLG_SZE(self.pnl, 50,-1).width) #
        self.lc.InsertColumn(31, _("Importo Avere"),width=wx.DLG_SZE(self.pnl, 50,-1).width) #


        self.lc.SetBackgroundColour(self.color)
        self.lc.Enable(False)

    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        evt.Skip()
         
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

    def CntData(self, evt):
        data_mov=self.data_mov.GetValue().strip()
        cnt_gma=0
        gma = data_mov.split('/')
        self.valmm = int(gma[1]) 

    def FndDoc(self, evt):
        self.sele.Show(False)
        self.sele.Enable(False) 
        self.ok.Show(True)
        self.ok.Enable(False)
        anno = self.annoc
        chiave = "RVEN"
        #vTIPODOC = "I1"
        note = ""
        paggior = ""
        rigagior = ""
        imponib = "0"
        registro = ""
        aliva = ""
        tipoiva = ""
        tipoiva1 = ""
        cambio = "0"
        segno = ""
        conto = "10"
        numdoc1 = ""
        #descriz = _("Fattura di vendita")
        vCAUSA = "110"        
        vDIV = "EU"
        nriga = 10
        registro="R1" 
        chiave="RMOV"   
        stt_mov = "C"
        sql = """ select * from libriaz 
                  where chiave = "%s" and  anno = "%s" 
                  and registro = "%s" """
        valueSql = chiave, anno, registro
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            while (1):
                row=cr.fetchone()
                if row == None:
                    break
                if (row[3] == None) : self.nummov = "1"
                if (row[3] != None) : self.nummov = str(int(row[3])+1)
        except StandardError, msg:
            self.__MDI__.MsgErr("genmov","FndDoc nummov Error %s " % (msg)) 
        self.CnAz.commit()
        #print self.tdoc.GetValue()
        if self.tdoc.GetValue()=="RF": 
            sql = """  select ifnull(min(num_doc),0), ifnull(max(num_doc),0)
                       from docu1 
                       where anno = "%s" and stt_doc="E"
                       and tipo_doc="R1" and (substr(data_doc,4,2)) = "%s" """
            sql1 = """ select stt_doc, num_doc, data_doc, cod_cf, pagam, 
                       anno, tipo_doc                     
                       from docu1 where num_doc = "%s" and anno = "%s" 
                       and tipo_doc="R1" and stt_doc="E" """
            sql2= """  select round(sum(docu.d_imp),2) as tot_merce,
                       round(sum(docu.imp_iva),2) as tot_iva, 
                       round((sum(docu.d_imp)+sum(docu.imp_iva)),2) as tot_doc,
                       tipo_doc
                       from
                       (select  sum(docu2.tot_riga) as d_imp, 
                       (sum(docu2.tot_riga) * docu2.aliva /100) as imp_iva,
                       tipo_doc
                       from docu2 where anno = "%s"  
                       and num_doc = "%s" and tipo_doc="R1"
                       group by aliva) as docu """

        elif self.tdoc.GetValue()=="NC": 
            sql = """  select ifnull(min(num_doc),0), ifnull(max(num_doc),0)
                       from docu1 
                       where anno = "%s" and stt_doc="E"
                       and tipo_doc="C1" and (substr(data_doc,4,2)) = "%s" """
            sql1 = """ select stt_doc, num_doc, data_doc, cod_cf, pagam, 
                       anno, tipo_doc                     
                       from docu1 where num_doc = "%s" and anno = "%s" 
                       and tipo_doc="C1" and stt_doc="E" """
            sql2= """  select round(sum(docu.d_imp),2) as tot_merce,
                       round(sum(docu.imp_iva),2) as tot_iva, 
                       round((sum(docu.d_imp)+sum(docu.imp_iva)),2) as tot_doc,
                       tipo_doc
                       from
                       (select  sum(docu2.tot_riga) as d_imp, 
                       (sum(docu2.tot_riga) * docu2.aliva /100) as imp_iva,
                       tipo_doc
                       from docu2 where anno = "%s" and tipo_doc="C1"
                       and num_doc = "%s" group by aliva) as docu """
        else :
            sql = """  select ifnull(min(num_doc),0), ifnull(max(num_doc),0)
                       from docu1 
                       where anno = "%s" and stt_doc="E"
                       and ((substr(tipo_doc,0,1))="F" or 
                       (substr(tipo_doc,0,1))="I") 
                       and (substr(data_doc,4,2)) = "%s" """
            sql1 = """ select stt_doc, num_doc, data_doc, cod_cf, pagam, 
                       anno, tipo_doc                     
                       from docu1 where num_doc = "%s" and anno = "%s" 
                       and ((substr(tipo_doc,0,1))="F" 
                       or (substr(tipo_doc,0,1))="I") and stt_doc="E" """
            sql2= """  select round(sum(docu.d_imp),2) as tot_merce,
                       round(sum(docu.imp_iva),2) as tot_iva, 
                       round((sum(docu.d_imp)+sum(docu.imp_iva)),2) as tot_doc,
                       tipo_doc
                       from
                       (select  sum(docu2.tot_riga) as d_imp, 
                       (sum(docu2.tot_riga) * docu2.aliva /100) as imp_iva,
                       tipo_doc
                       from docu2 where anno = "%s"  
                       and num_doc = "%s" 
                       and ((substr(tipo_doc,0,1))="F" or 
                       (substr(tipo_doc,0,1))="I") group by aliva) as docu """

        mm = string.zfill(str(self.vMM.GetValue()).strip(),2)
        #print mm
        #valueSql = vTIPODOC, anno , mm        
        valueSql = anno , mm
        #print sql % valueSql
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                da_numdoc = int(row[0])
                a_numdoc = int(row[1])
        except StandardError, msg:
            self.__MDI__.MsgErr("genmov","FndDoc ultnum Error %s " % (msg)) 
        self.CnAz.commit()
        #print da_numdoc, a_numdoc, mm
        for vnumdoc in range(da_numdoc, a_numdoc+1):
            #print vnumdoc
            valueSql1 = int(vnumdoc), anno 
            #print sql1 % valueSql1
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql1 % valueSql1)
                rows1 = cr.fetchall()
                for row1 in rows1:
                    #print row1
                    vSTT_DOC = str(row1[0])
                    vnumdoc = str(row1[1])
                    datadoc = str(row1[2])
                    cod_cf = str(row1[3])
                    cpart = conto + cod_cf
                    pagam = str(row1[4])
                    tipodoc = str(row1[6])
                    gma =  datadoc.split('/')
                    mm = int(gma[1]) 
                    valueSql2 = anno, int(vnumdoc)
                    descriz = self.descriz + " N. " + vnumdoc + " - " + datadoc
                    #print sql2 % valueSql2
                    #print mm, self.vMM.GetValue()#,vSTT_DOC
                    ##try:
                        ##cr = self.CnAz.cursor ()
                        ##cr.execute(sql1 % valueSql1)
                        ##rows1 = cr.fetchall()
                        ##for row2 in rows2:
                    ##except StandardError, msg:
                        ##self.__MDI__.MsgErr("genmov","piacon Error %s " % (msg)) 
                    try:
                        cr = self.CnAz.cursor ()                           
                        cr.execute(sql2 % valueSql2)
                        rows = cr.fetchall()
                        for row in rows:                           
                            self.__MDI__.CnvVM(row[1])
                            importo_iva = self.__MDI__.val
                            self.__MDI__.CnvVM(row[0])
                            imponibile = self.__MDI__.val
                            self.__MDI__.CnvVM(row[2])
                            importo = self.__MDI__.val
                            imporval = "0"
                            imponval = "0"
                            #if pagam!="PAG02" : vCAUSA = "--"
                            for rowlc in range(1):
                                row_lc = self.lc.GetItemCount()
                                if importo_iva!="": 
                                    row_lc+=1
                                    nriga1=nriga+10
                                    #print str(nriga1) + "1"
                                    self.lc.InsertStringItem(rowlc, str(anno))
                                    self.lc.SetStringItem(rowlc, 1, str(self.nummov))
                                    self.lc.SetStringItem(rowlc, 2, datadoc)
                                    self.lc.SetStringItem(rowlc, 3, str(nriga1))
                                    self.lc.SetStringItem(rowlc, 4, str(anno))
                                    self.lc.SetStringItem(rowlc, 5, vDIV)
                                    self.lc.SetStringItem(rowlc, 6, vCAUSA)
                                    self.lc.SetStringItem(rowlc, 7, descriz)
                                    self.lc.SetStringItem(rowlc, 8, imporval)
                                    self.lc.SetStringItem(rowlc, 9, imponval)
                                    self.lc.SetStringItem(rowlc, 10, str(anno))
                                    self.lc.SetStringItem(rowlc, 11, tipodoc)
                                    self.lc.SetStringItem(rowlc, 12, datadoc)
                                    self.lc.SetStringItem(rowlc, 13, vnumdoc)
                                    self.lc.SetStringItem(rowlc, 14, numdoc1)
                                    self.lc.SetStringItem(rowlc, 15, "5001")
                                    self.lc.SetStringItem(rowlc, 16, str(importo))
                                    self.lc.SetStringItem(rowlc, 17, segno)
                                    self.lc.SetStringItem(rowlc, 18, cod_cf) #cpart
                                    self.lc.SetStringItem(rowlc, 19, cambio)
                                    self.lc.SetStringItem(rowlc, 20, tipoiva1)
                                    self.lc.SetStringItem(rowlc, 21, tipoiva)
                                    self.lc.SetStringItem(rowlc, 22, aliva)
                                    self.lc.SetStringItem(rowlc, 23, registro)
                                    self.lc.SetStringItem(rowlc, 24, imponib)
                                    self.lc.SetStringItem(rowlc, 25, rigagior)
                                    self.lc.SetStringItem(rowlc, 26, paggior)
                                    self.lc.SetStringItem(rowlc, 27, note)                                    
                                    self.lc.SetStringItem(rowlc, 28, stt_mov)
                                    self.lc.SetStringItem(rowlc, 29, "5001", wx.LIST_FORMAT_RIGHT)
                                    self.lc.SetStringItem(rowlc, 30, imponibile,wx.LIST_FORMAT_RIGHT) #impdare               
                                    self.lc.SetStringItem(rowlc, 31, "", wx.LIST_FORMAT_RIGHT)#impavere
                                    row_lc+=1
                                    nriga2=nriga+20
                                    #print str(nriga2)+ "2"
                                    self.lc.InsertStringItem(rowlc, str(anno))
                                    self.lc.SetStringItem(rowlc, 1, str(self.nummov))
                                    self.lc.SetStringItem(rowlc, 2, datadoc)
                                    self.lc.SetStringItem(rowlc, 3, str(nriga2))
                                    self.lc.SetStringItem(rowlc, 4, str(anno))
                                    self.lc.SetStringItem(rowlc, 5, vDIV)
                                    self.lc.SetStringItem(rowlc, 6, vCAUSA)
                                    self.lc.SetStringItem(rowlc, 7, descriz)
                                    self.lc.SetStringItem(rowlc, 8, imporval)
                                    self.lc.SetStringItem(rowlc, 9, imponval)
                                    self.lc.SetStringItem(rowlc, 10, str(anno))
                                    self.lc.SetStringItem(rowlc, 11, tipodoc)
                                    self.lc.SetStringItem(rowlc, 12, datadoc)
                                    self.lc.SetStringItem(rowlc, 13, vnumdoc)
                                    self.lc.SetStringItem(rowlc, 14, numdoc1)
                                    self.lc.SetStringItem(rowlc, 15, "1202")
                                    self.lc.SetStringItem(rowlc, 16, str(importo))
                                    self.lc.SetStringItem(rowlc, 17, segno)
                                    self.lc.SetStringItem(rowlc, 18, cod_cf) #cpart
                                    self.lc.SetStringItem(rowlc, 19, cambio)
                                    self.lc.SetStringItem(rowlc, 20, tipoiva1)
                                    self.lc.SetStringItem(rowlc, 21, tipoiva)
                                    self.lc.SetStringItem(rowlc, 22, aliva)
                                    self.lc.SetStringItem(rowlc, 23, registro)
                                    self.lc.SetStringItem(rowlc, 24, imponib)
                                    self.lc.SetStringItem(rowlc, 25, rigagior)
                                    self.lc.SetStringItem(rowlc, 26, paggior)
                                    self.lc.SetStringItem(rowlc, 27, note)                                    
                                    self.lc.SetStringItem(rowlc, 28, stt_mov)
                                    self.lc.SetStringItem(rowlc, 29, "1202", wx.LIST_FORMAT_RIGHT)
                                    self.lc.SetStringItem(rowlc, 30, importo_iva, wx.LIST_FORMAT_RIGHT) #impdare 
                                    self.lc.SetStringItem(rowlc, 31, "", wx.LIST_FORMAT_RIGHT)#impavere
                                #print str(nriga)+ "3"
                                self.lc.InsertStringItem(rowlc, str(anno))
                                self.lc.SetStringItem(rowlc, 1, str(self.nummov))
                                self.lc.SetStringItem(rowlc, 2, datadoc)
                                self.lc.SetStringItem(rowlc, 3, str(nriga))
                                self.lc.SetStringItem(rowlc, 4, str(anno))
                                self.lc.SetStringItem(rowlc, 5, vDIV)
                                self.lc.SetStringItem(rowlc, 6, vCAUSA)
                                self.lc.SetStringItem(rowlc, 7, descriz)
                                self.lc.SetStringItem(rowlc, 8, imporval)
                                self.lc.SetStringItem(rowlc, 9, imponval)
                                self.lc.SetStringItem(rowlc, 10, str(anno))
                                self.lc.SetStringItem(rowlc, 11, tipodoc)
                                self.lc.SetStringItem(rowlc, 12, datadoc)
                                self.lc.SetStringItem(rowlc, 13, vnumdoc)
                                self.lc.SetStringItem(rowlc, 14, numdoc1)
                                self.lc.SetStringItem(rowlc, 15, conto)
                                self.lc.SetStringItem(rowlc, 16, str(importo))
                                self.lc.SetStringItem(rowlc, 17, segno)
                                self.lc.SetStringItem(rowlc, 18, cod_cf) #cpart
                                self.lc.SetStringItem(rowlc, 19, cambio)
                                self.lc.SetStringItem(rowlc, 20, tipoiva1)
                                self.lc.SetStringItem(rowlc, 21, tipoiva)
                                self.lc.SetStringItem(rowlc, 22, aliva)
                                self.lc.SetStringItem(rowlc, 23, registro)
                                self.lc.SetStringItem(rowlc, 24, imponib)
                                self.lc.SetStringItem(rowlc, 25, rigagior)
                                self.lc.SetStringItem(rowlc, 26, paggior)
                                self.lc.SetStringItem(rowlc, 27, note)                                    
                                self.lc.SetStringItem(rowlc, 28, stt_mov)
                                self.lc.SetStringItem(rowlc, 29, conto + cod_cf, wx.LIST_FORMAT_RIGHT)
                                self.lc.SetStringItem(rowlc, 30, "", wx.LIST_FORMAT_RIGHT) #impdare    
                                self.lc.SetStringItem(rowlc, 31, importo, wx.LIST_FORMAT_RIGHT)#impavere
                                self.nummov=int(self.nummov)+1
                    except StandardError, msg:
                        self.__MDI__.MsgErr("genmov","corpo Doc Error %s " % (msg)) 
                        print "corpo Doc Error %s" % (msg)
                if vnumdoc!=0:
                    self.lbldoc.SetLabel(_("Ultimo documento elaborato n. :") + str(vnumdoc))
                    self.ok.Enable(True)
                else : self.lbldoc.SetLabel(_("Nessun documento da elaborare"))
            except StandardError, msg:
                self.__MDI__.MsgErr("genmov","testata Doc Error %s " % (msg)) 
            self.CnAz.commit()
            self.lc.Enable(True)

    def Close(self, evt):
        if self.MMmov.GetValue()!="0":
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

    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    def Save(self, evt):
        if(int(self.lc.GetItemCount())!=0):
            chiave="RMOV"
            registro="R1"          
            nrow=self.lc.GetItemCount() 

            for row in range(nrow):
                vanno = self.getColTxt(row, 0)  
                vnum_mov = int(self.getColTxt(row, 1))  
                vdatamov = self.getColTxt(row, 2)  
                vnriga = int(self.getColTxt(row, 3))  
                vannoiva = self.getColTxt(row, 4)
                valDIV = self.getColTxt(row, 5)
                vCAUSA = self.getColTxt(row, 6)
                vdCAUSA = self.getColTxt(row, 7)
                vimporval=self.getColTxt(row, 8)
                self.__MDI__.CnvPM(vimporval)
                vimporval=self.__MDI__.val
                vimponval=self.getColTxt(row, 9)
                self.__MDI__.CnvPM(vimponval)
                vimponval=self.__MDI__.val

                vannodoc = self.getColTxt(row, 10)
                vtipodoc = self.getColTxt(row, 11)
                vdatadoc = self.getColTxt(row, 12)
                vnumdoc = self.getColTxt(row, 13)
                vnumdoc1 = self.getColTxt(row, 14)
                vCONTO = self.getColTxt(row, 15)
                vimporto = self.getColTxt(row, 16)
                self.__MDI__.CnvPM(vimporto)
                vimporto=self.__MDI__.val
                vimporto 
                vsegno=self.getColTxt(row, 17)
                vcpart=self.getColTxt(row, 18)
                vcodcf=self.getColTxt(row, 19) 
                vCAMBIO = self.getColTxt(row, 20)
                vtipoiva = self.getColTxt(row, 21)
                vtipoiva1 = self.getColTxt(row, 22)
                vALIVA = self.getColTxt(row, 23)
                vregistro = self.getColTxt(row, 24)
                vimponib = self.getColTxt(row, 25)
                vdconto =""
                self.__MDI__.CnvPM(vimponib)
                vimponib = self.__MDI__.val
                vrigagior="0" 
                vpaggior="0" 
                vnote=self.getColTxt(row, 28)
                vstt_mov=self.getColTxt(row, 28)
                vm0=vanno,vnum_mov,vdatamov
                vm1=vnriga,vannoiva,valDIV,vCAUSA,vdCAUSA,vimporval,vimponval
                vm2=vannodoc,vtipodoc,vdatadoc,vnumdoc,vnumdoc1,vCONTO,vimporto
                vm3=vsegno,vcpart,vCAMBIO,vtipoiva,vtipoiva1,vALIVA
                vm4=vregistro,vimponib,int(vrigagior),int(vpaggior),vnote, vstt_mov,vdconto
                valueSql = vm0 + vm1 + vm2 + vm3 + vm4
                try:
                    cr = self.CnAz.cursor()
                    sql = """ insert into movcon
                              values("%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s")"""
                    cr.execute(sql % valueSql) 
                except StandardError, msg:
                    print "Insert movcon Error %s" % (msg)
                self.CnAz.commit()
                valueSql = vanno, vnumdoc, vtipodoc
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

            valueSql = self.nummov,vdatamov,chiave,vanno,registro
            try:
                cr = self.CnAz.cursor()
                sql = """ update libriaz set ultnum = "%s", udatreg = "%s" 
                          where chiave = "%s" and anno = "%s" 
                          and registro = "%s" """                    
                cr.execute(sql % valueSql) 
            except StandardError, msg:
                print "Update Libriaz Error %s" % (msg)
            self.CnAz.commit()            
            self.Start(self)

