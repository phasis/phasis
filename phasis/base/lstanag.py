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

ttl = _("Lista Anagrafica")

def create(parent,cnt):
    return LstAnag(parent,cnt)

#---------------------------------------------------------------------------
class LstAnag(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        print "kkkkkkkkkkkkkkkkk"
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #wx.Frame.__init__(self, id = wx.NewId(), name = '',
        #      parent = prnt, pos = wx.Point(0, 0), 
        #      style = wx.DEFAULT_FRAME_STYLE , title = ttl)
        #self.SetIcon(wx.Icon(cfg.path_img + "/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        #self.SetClientSize(wx.Size(680, 410))
        Nid = wx.NewId()
        self.ttl = cnt[0]
        self.tcpart =  cnt[1][0].upper()
        self.esport = 0
        if (self.tcpart=="C"):self.ttl = _("Anagrafica Clienti")
        if (self.tcpart=="F"):self.ttl = _("Anagrafica Fornitori")
        if (self.tcpart=="V"):self.ttl = _("Anagrafica Vettori")
        if (self.tcpart=="A"):self.ttl = _("Anagrafica Agenti")
        if (self.tcpart=="T"):self.ttl = _("Anagrafica Tecnici")
        if (self.tcpart=="C" or self.tcpart=="F" or self.tcpart=="V" or self.tcpart=="T"):
            self.tblanag = "anag"
        if (self.tcpart=="A"): self.tblanag = "agenti"
        self.rec = cnt[2]
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        self.CMD = cnt[5]
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz = self.__MDI__.GetConnAZ() 
        self.annoc = self.__MDI__.GetAnnoC() 
        self.datacon = self.__MDI__.GetDataC()
        self.dzDatiAzienda = self.__MDI__.dzDatiAzienda
        #self.font = self.GetFont()
        self.sAGE = _("Sgegli l'Agente")
        
        self.pnl = wx.Panel(id = wx.NewId(), name = 'panel',
              parent = self, pos = wx.Point(0, 0), size = wx.DLG_SZE(self,680/2,400/2), #size = wx.Size(680, 400),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL )
        self.pnl.SetFont(self.font)
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,110),
              wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,120), 
              wx.DLG_SZE(self.pnl , 335,-1))
        wx.StaticText(self.pnl , -1, _("Rag. Soc.:"), wx.DLG_PNT(self.pnl, 5,127))
        self.rs = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 50,125), 
              wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)
        self.crs = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 155,125), wx.DLG_SZE(self.pnl , 12,12))
        wx.StaticText(self.pnl , -1, _("Localita` :"), wx.DLG_PNT(self.pnl, 5,142))
        self.loc = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 50,140), 
              wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)
        self.cloc = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 155,140), wx.DLG_SZE(self.pnl , 12,12))
        wx.StaticText(self.pnl , -1, _("Telefono :"), wx.DLG_PNT(self.pnl, 5,157))
        self.tel = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 50,155), 
              wx.DLG_SZE(self.pnl , 80, cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)
        self.ctel = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 135,155), wx.DLG_SZE(self.pnl , 12,12))        
        self.all = wx.Button(self.pnl , Nid, cfg.vcall, 
              wx.DLG_PNT(self.pnl , 170,125), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeM1H,cfg.btnSzeV))
        self.ok = wx.Button(self.pnl , Nid, cfg.vcok, 
              wx.DLG_PNT(self.pnl , 193,125), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.int = wx.Button(self.pnl, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 247,125), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 247,125),  
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 300,125), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))
        self.exp = wx.Button(self.pnl , Nid, cfg.vcexp, 
              wx.DLG_PNT(self.pnl , 300,140),
              wx.DLG_SZE(self.pnl,cfg.btnSzeMH,cfg.btnSzeV))

        self.rbCONFER = wx.RadioButton(self.pnl, Nid, cfg.vcCONF,
              wx.DLG_PNT(self.pnl, 180,140), 
              wx.DLG_SZE(self.pnl, 50,10), wx.RB_GROUP )
        self.rbPREVIS = wx.RadioButton(self.pnl, Nid, cfg.vcPREV,
              wx.DLG_PNT(self.pnl, 235,140), wx.DLG_SZE(self.pnl, 50,10))
        self.precon = wx.TextCtrl(self.pnl, -1, "C", 
              wx.DLG_PNT(self.pnl, 280,100))         
        wx.StaticText(self.pnl , -1, _("Rif.:"), wx.DLG_PNT(self.pnl, 155,157))
        self.nsrif = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 170,155), 
              wx.DLG_SZE(self.pnl , 80, cfg.DIMFONTDEFAULT))
        self.AGE = wx.ComboBox(self.pnl, Nid,_("Agente"),
              wx.DLG_PNT(self.pnl, 255,155), 
              wx.DLG_SZE(self.pnl, 85,-1), [],wx.CB_DROPDOWN | wx.CB_SORT )
        self.vAGE = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 275,90))
        wx.StaticText(self.pnl , -1, _("Note :"), wx.DLG_PNT(self.pnl, 5,172))
        self.note = wx.TextCtrl(self.pnl , Nid, "",
               wx.DLG_PNT(self.pnl , 50,170), wx.DLG_SZE(self.pnl , 80, cfg.DIMFONTDEFAULT))
        self.cnote = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
               wx.DLG_PNT(self.pnl , 135,170),wx.DLG_SZE(self.pnl , 12,12))
        self.lpiva = wx.StaticText(self.pnl , -1, _("P.IVA :"), 
               wx.DLG_PNT(self.pnl, 155,172))
        self.piva = wx.TextCtrl(self.pnl , Nid, "",
               wx.DLG_PNT(self.pnl , 180,170), wx.DLG_SZE(self.pnl , 70, cfg.DIMFONTDEFAULT))
        self.cpiva = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
               wx.DLG_PNT(self.pnl , 255,170), wx.DLG_SZE(self.pnl , 12,12))
        self.lcap = wx.StaticText(self.pnl , -1, _("CAP :"), 
               wx.DLG_PNT(self.pnl, 272,172))
        self.cap = wx.TextCtrl(self.pnl , Nid, "",
               wx.DLG_PNT(self.pnl , 293,170), wx.DLG_SZE(self.pnl , 30, cfg.DIMFONTDEFAULT))
        self.ccap = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , Nid, "...", 
               wx.DLG_PNT(self.pnl , 327,170), wx.DLG_SZE(self.pnl , 12,12))

        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        self.lcap.Enable(False)
        self.lpiva.Enable(False)
        self.piva.Enable(False)
        self.cpiva.Enable(False)
        self.cap.Enable(False)
        self.ccap.Enable(False)        
        #self.Fit()
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


        self.AGE.Bind(wx.EVT_COMBOBOX, self.SelAGE)
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.all.Bind(wx.EVT_BUTTON, self.FndSelAll)
        self.int.Bind(wx.EVT_BUTTON, self.FndInt)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.DblClick)
        #self.lc.Bind(wx.EVT_LIST_KEY_DOWN, self.DblClick)
        self.crs.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.cloc.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.ctel.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.cnote.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.rbCONFER.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.rbPREVIS.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        self.rs.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.loc.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.nsrif.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.tel.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.note.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.exp.Bind(wx.EVT_BUTTON, self.ExpAnag)
        self.canc.SetFocus()
        self.Start(self)

    def Stampa(self, evt): 
        precon = self.precon.GetValue()
        rs = "%" + self.rs.GetValue().title() + "%"
        loc = self.loc.GetValue()
        tel = self.tel.GetValue() 
        nsrif = "%" + self.nsrif.GetValue().title() + "%"
        note = "%" + self.note.GetValue().upper() + "%"
        piva = self.piva.GetValue()
        cap = self.cap.GetValue()        
        vage = self.vAGE.GetValue()
        if self.tcpart=="C" : tipodoc = 'lanagc'
        if self.tcpart=="F" : tipodoc = 'lanagf'
        if self.tcpart=="A" : tipodoc = 'lanaga'
        if self.tcpart=="V" : tipodoc = 'lanagv'
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,
              tipo = tipodoc, 
              parametriSql = (self.tcpart, precon, nsrif, rs, note, vage),
              datiazienda = self.dzDatiAzienda,              
              anteprima = True )
       
    def Start(self, evt):
        self.exp.Enable(False)
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Rag. Soc.1 Cognome"))
        self.lc.InsertColumn(2, _("Rag. Soc.2 Nome"))
        self.lc.InsertColumn(3, _("Indirizzo"))
        self.lc.InsertColumn(4, _("Telefono"))
        self.lc.InsertColumn(5, _("Mobile"))
        self.lc.InsertColumn(6, _("Ufficio"))
        self.lc.InsertColumn(7, _("Fax"))
        self.lc.InsertColumn(8, _("Zona"))
        self.lc.InsertColumn(9, _("Note"))
        self.lc.InsertColumn(10, _("Ns Rif."))
        self.lc.InsertColumn(11, _("Localita'"))
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self,  35,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self,  70,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self,  70,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self,  100,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self,  0,-1).width)
        self.lc.SetColumnWidth(8, wx.DLG_SZE(self,  70,-1).width)
        self.lc.SetColumnWidth(9, wx.DLG_SZE(self,  250,-1).width)
        self.lc.SetColumnWidth(10, wx.DLG_SZE(self,  100,-1).width)
        self.lc.SetColumnWidth(11, wx.DLG_SZE(self,  70,-1).width)
        #self.lc.SetFont(self.font)
        self.precon.Show(False)
        self.vAGE.Show(False)
        self.AGE.Show(False)
        self.rs.SetFocus()
        if self.tcpart=="C":self.AGE.Show(True)
        if self.rs.GetValue()!='':
            self.FndSelAnag(self)
            self.rs.SetFocus()
        elif self.loc.GetValue()!='':
            self.FndSelLoc(self)
            self.loc.SetFocus()
        elif self.tel.GetValue()!='':
            self.FndSelTel(self)
            self.tel.SetFocus()
        elif self.nsrif.GetValue()!='':
            self.FndSelNoteNsrif(self)
            self.nsrif.SetFocus()
        elif self.note.GetValue()!='':
            self.FndSelNoteNsrif(self)
            self.note.SetFocus()
        else:
            pass
        self.SelCOMBO(self)
        #self.AGE.Enable(False)

    def SelCOMBO(self, evt):
        ## Funzione Inserisci Combo AGE
        vAGE = self.vAGE.GetValue()
        self.AGE.Clear()
        self.AGE.SetValue(_("Agente"))
        sql = " SELECT * FROM agenti WHERE t_cpart = 'A' "
        self.AGE.Append(_("Sgegli l'Agente"),"0")
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)                   
            rows = cr.fetchall()
            for row in rows:
                if (str(row[1])==vAGE):self.sAGE=str(row[3])+"," + str(row[4])
                self.AGE.Append(str(row[3]) + "," + str(row[4]),str(row[1]))
        except StandardError, msg:
            print "SelCOMBO Error %s" % (msg)
        self.CnAz.commit()
        cntAGE = 0
        cntAGE = self.AGE.FindString(self.sAGE)
        self.AGE.Select(cntAGE)        

    def SelAGE(self, evt):
        self.Sel(evt)
        self.vAGE.SetValue(self.cb_val)        

    def Sel(self, evt):
        self.int.Show(True)
        self.canc.Show(False)        
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str = evt.GetString()
        evt.Skip()
        
    def FndAnag(self, evt):
        self.int.Show(True)
        self.canc.Show(False)
        self.Start(self)

    def ExpAnag(self, evt):
        self.esport = 1
        self.FndAnag(self)
        
    def FndInt(self, evt):
        self.int.Show(False)
        self.canc.Show(True)
        self.vAGE.SetValue('')
        self.sAGE = ''
        self.sAGE = _("Sgegli l'Agente")
        self.loc.SetValue('')
        self.tel.SetValue('')
        self.nsrif.SetValue('')
        self.rs.SetValue('')
        self.Start(self)
        
    def SelRadioB(self, evt):
        if (self.precon.GetValue()==""):
            self.precon.SetValue("C")
            self.rbCONFER.SetValue(True)
            self.rbPREVIS.SetValue(False)            
        if (self.precon.GetValue()=="P"):
            self.rbCONFER.SetValue(False)
            self.rbPREVIS.SetValue(True)
        if (self.precon.GetValue()=="C"):
            self.rbCONFER.SetValue(True)
            self.rbPREVIS.SetValue(False)

    def RadioB(self, evt):
        #print wx.EVT_COMMAND_RADIOBUTTON_SELECTED 
        if (self.rbPREVIS.GetValue()==True):
            self.precon.SetValue("P")
            self.rs.SetFocus()
        if (self.rbCONFER.GetValue()==True):
            self.precon.SetValue("C")
            self.rs.SetFocus()

# < diegom inserita stringa sql per agenti da sistemare

    def FndSelAll(self, evt):
        precon = self.precon.GetValue()
        if self.tcpart!="A": sql = " SELECT * FROM anag ORDER BY RAG_SOC1 DESC "
        else: sql = " SELECT * FROM agenti ORDER BY RAG_SOC1 DESC "
        valueSql = 'ALL'
        control = [sql, valueSql, self.tcpart, precon]
        if self.esport==0 :self.FndLstAnag(control)                            
        else:self.FlExp(control)        

    
    def FndSelAnag(self, evt):
        precon = self.precon.GetValue()
        val = self.rs.GetValue()
        val_diz = string.split(val,"%")
        if self.tcpart!="A": 
            if val[:1]=="%" : 
                sql = """ SELECT * FROM anag WHERE RAG_SOC2 like '%s'
                           ORDER BY RAG_SOC2 DESC """
            else: 
                sql = """ SELECT * FROM anag WHERE RAG_SOC1 like '%s'
                          ORDER BY RAG_SOC1 DESC """
        else:
            if val[:1]=="%" : 
                sql = """ SELECT * FROM agenti WHERE RAG_SOC2 like '%s'
                           ORDER BY RAG_SOC2 DESC """
            else: 
                sql = """ SELECT * FROM agenti WHERE RAG_SOC1 like '%s'
                          ORDER BY RAG_SOC1 DESC """
        valueSql = '%' + val.title() + '%',
        control = [sql, valueSql , self.tcpart, precon]
        if self.esport==0 :self.FndLstAnag(control)
        else:self.FlExp(control)

    def FndSelNoteNsrif(self, evt):
        precon = self.precon.GetValue()
        note = self.note.GetValue()
        nsrif = self.nsrif.GetValue()
        if self.tcpart!="A":
            sql = """ SELECT * FROM anag 
                      WHERE NOTE like '%s' AND NSRIF like '%s'
                      ORDER BY RAG_SOC1 DESC """
        else:
            sql = """ SELECT * FROM agenti 
                      WHERE NOTE like '%s' AND NSRIF like '%s'
                      ORDER BY RAG_SOC1 DESC """

        valueSql = '%' + note.upper() + '%','%' + nsrif.title() + '%',
        control = [sql, valueSql, self.tcpart, precon]
        if self.esport==0 :self.FndLstAnag(control)
        else:self.FlExp(control)

    def FndSelLoc(self, evt):
        precon = self.precon.GetValue()
        val = self.loc.GetValue()
        val_diz = string.split(val,"%")
        if self.tcpart!="A":
            if val[:1]=="%" : 
                sql = """ SELECT * FROM anag WHERE LOCALIT like '%s'
                          ORDER BY RAG_SOC1 DESC """
            else: 
                sql = """ SELECT * FROM anag WHERE ZONA like '%s'
                          ORDER BY RAG_SOC1 DESC """
        else:
            if val[:1]=="%" : 
                sql = """ SELECT * FROM agenti WHERE LOCALIT like '%s'
                          ORDER BY RAG_SOC1 DESC """
            else: 
                sql = """ SELECT * FROM agenti WHERE ZONA like '%s'
                          ORDER BY RAG_SOC1 DESC """

        valueSql = '%' + val.title() + '%',
        control = [sql, valueSql, self.tcpart, precon]
        if self.esport==0 :self.FndLstAnag(control)
        else:self.FlExp(control)

    def FndSelTel(self, evt):
        precon = self.precon.GetValue()
        val = self.tel.GetValue()
        val_diz = string.split(val,"%")
        if self.tcpart!="A":

            if val[:1]=="%" : 
                sql = """ SELECT * FROM anag WHERE MOBILE like '%s'
                          ORDER BY RAG_SOC1 DESC """
            else: 
                sql = """ SELECT * FROM anag WHERE TEL_ABIT like '%s'
                          ORDER BY RAG_SOC1 DESC """
        else:
            if val[:1]=="%" : 
                sql = """ SELECT * FROM agenti WHERE MOBILE like '%s'
                          ORDER BY RAG_SOC1 DESC """
            else: 
                sql = """ SELECT * FROM agenti WHERE TEL_ABIT like '%s'
                          ORDER BY RAG_SOC1 DESC """

        valueSql = '%' + val + '%',
        control = [sql, valueSql, self.tcpart, precon]
        if self.esport==0 :self.FndLstAnag(control)
        else:self.FlExp(control)

# > diegom

        
    def FndLstAnag(self, evt):
        ## Funzione cerca
        #if evt[1]!="ALL" : self.Start(self)       
        sql = evt[0]
        valueSql = evt[1]
        tcpart = evt[2]
        precon = evt[3]
        rowlc = 0
        vage = self.vAGE.GetValue()
        num_campo_precon = 0
        if tcpart!="A": num_campo_precon=47
        else: num_campo_precon=40
        
        try:
            cr = self.CnAz.cursor ()
            if valueSql!="ALL" :cr.execute(sql % valueSql)
            else : cr.execute(sql)
            rows = cr.fetchall()
            for row in rows:
                for rowlc in range(1):
                    if vage=="" and tcpart==str(row[0]) and precon==str(row[num_campo_precon]):
                        #print "1"
                        row_lc = self.lc.GetItemCount()      
                        t_cpart = tcpart
                        cod = str(row[1])
                        print cod 
                        ragsoc1 = row[3].title()
                        ragsoc2 = row[4].title()
                        indiriz = row[6].title()
                        tel_abi = row[18]
                        tel_uff = row[19]
                        mobile = row[20]
                        fax = row[21]
                        if (row[9]=='' or row[9]=='None'):
                            loc = row[8].title()  
                        else:loc = row[9].title()
                        zona = row[8].title()                        
                        self.__MDI__.CnvVM(row[30])  
                        sc1 = self.__MDI__.val
                        if(sc1=="0,00"):sc1 = ""
                        note = row[41]
                        nrif = row[5].title()
                        self.lc.InsertStringItem(rowlc, cod)    
                        self.lc.SetStringItem(rowlc, 1, ragsoc1)
                        self.lc.SetStringItem(rowlc, 2, ragsoc2)
                        self.lc.SetStringItem(rowlc, 3, indiriz)
                        self.lc.SetStringItem(rowlc, 4, tel_abi)
                        self.lc.SetStringItem(rowlc, 5, mobile)
                        self.lc.SetStringItem(rowlc, 6, tel_abi)
                        self.lc.SetStringItem(rowlc, 7, fax)
                        self.lc.SetStringItem(rowlc, 8, loc)
                        self.lc.SetStringItem(rowlc, 9, note)
                        self.lc.SetStringItem(rowlc, 10, nrif)
                        self.lc.SetStringItem(rowlc, 11, zona)
                        self.lc.SetItemData(0,0)
                    if vage!="" and vage==row[38]:
                        #print "2"
                        row_lc = self.lc.GetItemCount()      
                        t_cpart = str(row[0])
                        cod = str(row[1])
                        print cod 
                        ragsoc1 = row[3].title()
                        ragsoc2 = row[4].title()
                        indiriz = row[6].title()
                        tel_abi = row[18]
                        tel_uff = row[19]
                        mobile = row[20]
                        fax = row[21]
                        if row[9]=='' or row[9]=='None':
                            loc = row[8].title()
                        else:loc = row[9].title()
                        zona = row[8].title()  
                        self.__MDI__.CnvVM(row[30])  
                        sc1 = self.__MDI__.val
                        if(sc1=="0,00"):sc1 = ""
                        note = row[41]
                        nsrif = row[5].title()
                        self.lc.InsertStringItem(rowlc, cod)    
                        self.lc.SetStringItem(rowlc, 1, ragsoc1)
                        self.lc.SetStringItem(rowlc, 2, ragsoc2)
                        self.lc.SetStringItem(rowlc, 3, indiriz)
                        self.lc.SetStringItem(rowlc, 4, tel_abi)
                        self.lc.SetStringItem(rowlc, 5, mobile)
                        self.lc.SetStringItem(rowlc, 6, tel_abi)
                        self.lc.SetStringItem(rowlc, 7, fax)
                        self.lc.SetStringItem(rowlc, 8, loc)
                        self.lc.SetStringItem(rowlc, 9, note)
                        self.lc.SetStringItem(rowlc, 10, nsrif)
                        self.lc.SetStringItem(rowlc, 11, zona) 
                        self.lc.SetItemData(0,0)

        except StandardError, msg:
            print "FndLstAnag Error %s" % (msg)
        self.CnAz.commit()
                         
    def Ok(self, evt):
        self.DblClick(self.currentItem)
        
    def Close(self, evt):
        self.AggMenu(True,self.IDMENU)
        wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        #self.Destroy()
              
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()
    
        
    def DblClick(self, evt):
        #ttl = self.ttl
        #Dir = "base"
        #Mod = "anag"
        tbl = self.tcpart
        if (self.tcpart=="C"): idmenu=1002 #self.ttl = "Anagrafica Clienti"
        elif (self.tcpart=="F"): idmenu=1003 #self.ttl = "Anagrafica Fornitori"
        elif (self.tcpart=="V"): idmenu= 3011 #self.ttl = "Anagrafica Vettori"
        #elif (self.tcpart=="A"): idmenu= #self.ttl = "Anagrafica Agenti"
        #elif (self.tcpart=="T"): idmenu= #self.ttl = "Anagrafica Tecnici"
        rec = (self.lc.GetItemText(self.currentItem))
        #AggMenu = self.AggMenu
        #IDMENU = self.IDMENU
        #self.CMD(rec, Dir, Mod, ttl, tbl)
        self.CMD(idmenu,rec,tbl)    
        #self.AggMenu(True,self.IDMENU)
        #self.Destroy()
        
    def LstSlct(self, evt):
        self.currentItem = evt.m_itemIndex

    def LstAct(self, evt):
        self.currentItem = evt.m_itemIndex    
        self.DblClick(self)

    def FlExp(self, evt):
        Dir = cfg.path_tmp
        self.ExpAnag = Dir + "\\" + self.ttl + ".csv"
        fexport = "CSV(delimitato dal separatore di elenco)|*.csv"
        dlg = wx.FileDialog(self, "", "", self.ttl + ".csv",
              fexport, wx.SAVE |wx.MULTIPLE)
        if dlg.ShowModal()==wx.ID_OK:
            paths = dlg.GetPaths()
            for path in paths:
                self.ExpAnag = path
        dlg.Destroy()
       
        nopres = cfg.nopres
        sps = nopres[0]
        spp = ';' #nopres[1]
        neg = nopres[2]
        pos = nopres[3]
        spn = nopres[4]
        sql = evt[0]
        valueSql = evt[1]
        rowlc = 0
        vage = self.vAGE.GetValue()
        #print vage
        flspl = open(self.ExpAnag,"w + ")
        self.ragsoc1age = '-'

        flspl.write(self.ttl.upper() + spp + 'del ' + self.datacon + spn)  
        flspl.write(spn)
        flspl.write(cfg.ttl_tanagexp)

        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                t_cpart = str(row[0])
                codcf = str(row[1])
                ragsoc1 = str(row[3]).title()
                ragsoc2 = str(row[4]).title()
                nsrif = str(row[5]).title()
                indiriz = str(row[6]).title()       
                zona = str(row[8]).title()
                localit = str(row[9]).title()
                cap = string.zfill(str(row[7]).strip(),5)
                if cap=="00000" : cap = ""
                pr = row[10]
                if (ord(pr[0])==0 or ord(pr[1])==0 ):pr = '--'
                stato = str(row[11]).title()
                tabi = str(row[18])
                mob = str(row[20])
                tuff = str(row[19])
                fax = str(row[21])
                piva = str(row[25]).strip()
                codfisc = str(row[24]).strip().upper()
                email = str(row[23])
                web = str(row[22])
                indiriz1 = str(row[12]).title()
                zona1 = str(row[14]).title()
                localit1 = str(row[15]).title()
                cap1 = string.zfill(str(row[13]).strip(),5)#'%05d' % row[13]
                if cap1=="00000" : cap1 = ""
                pr1 = row[10]
                if (ord(pr1[0])==0 or ord(pr1[1])==0 ):pr1 = '--'                
                stato1 = str(row[17]).title()
                banca = str(row[26]).title()
                abi = str(row[28]).strip()
                cab = str(row[29]).strip()
                ncc = str(row[27]).strip()
                if (self.tblanag=="anag"):
                    self.__MDI__.CnvVM(str(row[30]))                                      
                    sc1 = '%-6.6s' % self.__MDI__.val
                    self.__MDI__.CnvVM(str(row[31]))
                    sc2 = '%-6.6s' % self.__MDI__.val
                    codage = str(row[38])
                    vPAGAM = '%-10.10s' % str(row[42])
                    note = str(row[48])
                else: 
                    self.__MDI__.CnvVM(str(row[32]))                                       
                    sc1 = self.__MDI__.val
                    codage = str(row[31])
                    self.__MDI__.CnvVM(str(row[30]))
                    sc2 = '%-6.6s' % self.__MDI__.val
                    note = ''
                flspl.write(ragsoc1 + spp +  ragsoc2 + spp + indiriz + spp + \
               cap + spp + localit + spp + pr + spp + tabi + spp + mob + '\n')

                flspl.write(codage + spp + nsrif + spp + note + '\n')             
                flspl.write(spn)

            flspl.close()
        except StandardError, msg:
            print "FlExp Error %s" % (msg)
        self.CnAz.commit()
        
        self.esport = 0
        self.Start(self)


