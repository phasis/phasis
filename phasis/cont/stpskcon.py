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
from cfg import *
import cfg

def create(parent,cnt):
    return StpSchedeMov(parent,cnt)

#---------------------------------------------------------------------------
class StpSchedeMov(wx.ScrolledWindow):
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
        self.color=self.GetBackgroundColour()
        self.cnt = cnt
        Nid = wx.NewId()
        self.ttl=cnt[0]
        self.tipoord =cnt[1]
        self.tcpart="C"
        self.ottl="Stampa Schede"
        self.tbl="movcon"
        self.tblart="articoli"
        self.rec=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        
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
        wx.StaticText(self.pnl, -1, "Contropartita :", 
              wx.DLG_PNT(self.pnl, 10,27))
        self.CFM = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 65,25), wx.DLG_SZE(self.pnl, 60,-1),
              [], wx.CB_DROPDOWN | wx.CB_SORT )
        self.vCFM = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 275,20))
        self.lcodcf = wx.StaticText(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 135,27))
        self.codcf = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 185, 25), wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT))
        self.ccodcf = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 250,25),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lragsoc1 = wx.StaticText(self.pnl, -1, 
              "Rag. Sociale1 ( Cognome ) :", wx.DLG_PNT(self.pnl, 12,40))
        self.ragsoc1 = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 10,50), 
              wx.DLG_SZE(self.pnl, 120,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)    
        self.cragsoc1 = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, -1, "...", 
              wx.DLG_PNT(self.pnl, 135,50),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lragsoc2 = wx.StaticText(self.pnl, -1,
              "Rag. Sociale2 ( Nome ) :", wx.DLG_PNT(self.pnl, 155,40))
        self.ragsoc2 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 153, 50), wx.DLG_SZE(self.pnl, 110,cfg.DIMFONTDEFAULT))      
        self.MM = wx.ComboBox(self.pnl, -1,"",
              wx.DLG_PNT(self.pnl, 40,70), wx.DLG_SZE(self.pnl, 65,-1),
              [],wx.CB_DROPDOWN )
        self.vMM = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 150,70))
        self.lc1 = wx.ListCtrl(self.pnl , -1,
              wx.DLG_PNT(self.pnl, 10,75), wx.DLG_SZE(self.pnl , 300,80),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)


        wx.StaticText(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 120,202))


        wx.StaticText(self.pnl, -1, "Conto Avere:", 
              wx.DLG_PNT(self.pnl, 10,182))
        self.avere = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 50,180), 
              wx.DLG_SZE(self.pnl, 65, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        wx.StaticText(self.pnl, -1, "Conto Dare:", 
              wx.DLG_PNT(self.pnl, 120,182))
        self.dare = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 160,180), 
              wx.DLG_SZE(self.pnl, 65, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        wx.StaticText(self.pnl, -1, "Totale:", 
              wx.DLG_PNT(self.pnl, 245,182))
        self.totale = wx.TextCtrl(self.pnl, Nid, "0,00",
              wx.DLG_PNT(self.pnl, 270,180), 
              wx.DLG_SZE(self.pnl, 65, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.ok = wx.Button(self.pnl , -1, cfg.vcok, 
              wx.DLG_PNT(self.pnl , 275,10), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.inte = wx.Button(self.pnl , -1, cfg.vcint, 
              wx.DLG_PNT(self.pnl , 275,25), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.inte.SetFocus()      
        self.canc = wx.Button(self.pnl , -1, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 275,25), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFocus()      
        self.stampa = wx.Button(self.pnl, -1, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 275,40),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))   
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
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

        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.inte.Bind(wx.EVT_BUTTON, self.Start)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.Bind(wx.EVT_CLOSE, self.Close)
        #self.lc.Bind(wx.EVT_LEFT_DCLICK,  self.DblClick)
        self.CFM.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_CFM)        
        self.CFM.Bind(wx.EVT_COMBOBOX, self.SelCFM)  
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.MM.Bind(wx.EVT_COMBOBOX, self.SelMM) 
 
 
 

        self.Start(self)

    def Start(self, event):
        self.vCFM.Show(False)
        if (self.tcpart=="C"):self.lcodcf.SetLabel(" Cod. Cliente :")
        self.vCFM.SetValue("C")
        self.sCFM = ""
        self.vMM.SetValue("0")
        self.MM.Show(False)
        self.SelCOMBO(self)
        self.CFM.Enable(True)
        self.codcf.Enable(False)
        self.ccodcf.Enable(False)
        self.stampa.Enable(False)
        self.MM.Enable(False)
        self.dare.Enable(False)
        self.avere.Enable(False)
        self.totale.Enable(False)
        self.ok.Enable(False)
        self.vMM.Show(False)
        self.inte.Show(False)
        self.inte.Enable(False)
        self.canc.Show(True)
        self.canc.Enable(True)
        self.codcf.SetValue('')
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.totale.SetValue('0,00')
        self.dare.SetValue('0,00')
        self.avere.SetValue('0,00')
        self.ragsoc1.Enable(True)
        self.ragsoc2.Enable(True)
        self.ragsoc1.SetFocus()
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
        

    def Stampa(self, evt):
        tcpart= self.tcpart
        codcf = self.codcf.GetValue()
        vCFM = self.vCFM.GetValue()
        #print vCFM
        if vCFM=="C":tipodoc = 'skconc'
        if vCFM=="F":tipodoc = 'skconf'
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,   
              tipo = tipodoc, 
              parametriSql = (self.annoc, codcf),
              datiazienda = self.dzDatiAzienda,
              anteprima = True )








    def SelCOMBO(self, evt):
        vCFM = self.vCFM.GetValue()
        self.CFM.Clear()
        for item in cfg.vcCFM:
            if (item[:1]==vCFM):self.sCFM = item  
            self.CFM.Append(item, item[:1])      
        cntCFM = 0
        cntCFM = self.CFM.FindString(self.sCFM)
        self.CFM.Select(cntCFM)
        cnt=0
        self.MM.Append('--','0')
        for sMM in cfg.mesi:
            cnt+=1
            self.MM.Append(sMM,str(cnt))
        cntMM=0
        cntMM=self.MM.FindString('--')
        self.MM.Select(cntMM)

    def SelMM(self, evt):
        self.Sel(evt)
        self.vMM.SetValue(self.cb_val)
        self.FndMovCorpolc(self)

    def SelCFM(self, evt):
        self.Sel(evt)
        self.vCFM.SetValue(self.cb_val)
        if self.vCFM.GetValue()=="F": self.lcodcf.SetLabel(" Cod. Fornit. :")
        if self.vCFM.GetValue()=="C": self.lcodcf.SetLabel(" Cod. Cliente :")

    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str =  evt.GetString()
        evt.Skip()

        
    def KillFcs_CFM(self, evt):  
        if self.vCFM.GetValue()=="M" :self.num_doc.SetFocus()
        else: self.ragsoc1.SetFocus()
        
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
              



    def FndSelMov(self, evt):
        #print "fndselmov"  
        row=evt
        self.anno.SetValue(str(row[0]))
        # < diegom
        self.vCF.SetValue(str(row[15]))
        self.codcf.SetValue(str(row[18]))
        self.FndMovCorpolc(self) 
        self.inte.Show(True)        


    def FndMovCorpolc(self, evt):
        #print "fndmovcorpolc1"
        #print self.lc_Slct
        totaleA=0
        totaleD=0
        codcf=self.codcf.GetValue()
        rowlc=0
        cnt_rec=0
        #num_mov = self.num_mov.GetValue()
        anno = self.annoc
        vCF=self.vCFM.GetValue()

        sql = """ select * from movcon where cpart = "%s" 
                  and anno = "%s" and t_cpart = "%s" 
                  order by data_int desc """
        valueSql = codcf, anno, vCF
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
                    self.lc1.SetStringItem(rowlc, 28, row[28])
                    if str(row[17])=="D":
                        self.__MDI__.CnvVM(row[8])
                        importoD=self.__MDI__.val
                        self.lc1.SetStringItem(rowlc, 30, importoD)
                        if row[6]!="120": totaleD+=row[8]
                    elif str(row[17])=="A":
                        self.__MDI__.CnvVM(row[8])
                        importoA=self.__MDI__.val
                        self.lc1.SetStringItem(rowlc, 31, importoA)
                        if row[6]!="110": totaleA+=row[8]
                    self.lc1.SetStringItem(rowlc, 32, str(row[29]))
  
        except StandardError, msg:
            self.__MDI__.MsgErr("movcon","FndMovCorpo Error %s " % (msg))
        self.CnAz.commit()
        #print totaleA
        #print totaleD
        vCF = self.vCFM.GetValue()
        sbilancio = totaleD - totaleA
        #print sbilancio
        self.__MDI__.CnvVM(totaleD)
        totaleD=self.__MDI__.val
        self.__MDI__.CnvVM(totaleA)
        totaleA=self.__MDI__.val
        if sbilancio!=0.0:
            self.__MDI__.CnvVM(sbilancio)
            sbilancio=self.__MDI__.val
        else: sbilancio = '0,00'
        #print sbilancio
        self.dare.SetValue(totaleD)
        self.avere.SetValue(totaleA)
        self.totale.SetValue(sbilancio)
        self.ragsoc1.Enable(False)
        self.ragsoc2.Enable(False)
        self.stampa.Enable(True)
        self.stampa.SetFocus()
        self.CFM.Enable(False)
        self.lc1.SetBackgroundColour('white')
        self.lc1.Enable(True)

       




    def FndCodCF(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        cod = self.codcf.GetValue()
	if cod=='' or cod=='None' or cod=='Null': cod = '0'
        tcpart = self.vCFM.GetValue()
        sql = """ select * from anag where cod = "%s" and t_cpart = "%s" """ 
        valueSql = int(cod), tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1  
        except StandardError, msg:
            self.__MDI__.MsgErr("stpskcon","FndCodCF Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==0 and tcpart!="M"):self.Message(cfg.msgdatono,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)
        if  tcpart=="F": self.lcodcf.SetLabel(" Cod. Fornit. :")
        if  tcpart=="C": self.lcodcf.SetLabel(" Cod. Cliente :")

    def FndAnag(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue()
        cod = self.codcf.GetValue()
        self.tcpart = self.vCFM.GetValue()
        sql = """ select * from anag 
                  where rag_soc1 like "%s" and t_cpart = "%s" """ 
        valueSql = '%' + val.title() + '%', self.tcpart  
           
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("stpskcon","FndAnag Error %s " % (msg))
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
            self.inte.Show(True)
            self.inte.Enable(True)
            self.canc.Show(False)
            self.canc.Enable(False)
            self.FndMovCorpolc(self)
            self.ragsoc1.Enable(False)
            self.ragsoc2.Enable(False)

    def FndSelAnag(self, evt):
        row = evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.inte.Show(True)
        self.inte.Enable(True)
        self.canc.Show(False)
        self.canc.Enable(False)
        self.ragsoc1.Enable(False)
        self.ragsoc2.Enable(False)
        self.FndMovCorpolc(self)


           
    def CalcTotale(self,evt):
        dare = 0
        avere = 0
        totale = 0
        for x in range(self.lc.GetItemCount()):
            self.__MDI__.CnvPM(self.getColTxt(x, 9))
            importo_row = float(self.__MDI__.val)  
            self.__MDI__.CnvPM(self.getColTxt(x, 5))
            imporval_row = float(self.__MDI__.val)  
            dare+=importo_row
            avere+=imporval_row
            totale = avere - dare
        self.__MDI__.CnvVM(dare)
        if self.__MDI__.val=='': vdare = '0,00'
        else : vdare = self.__MDI__.val
        self.dare.SetValue(vdare)
        self.__MDI__.CnvVM(avere)
        if self.__MDI__.val=='': vavere = '0,00'
        else : vavere = self.__MDI__.val
        self.avere.SetValue(vavere)
        self.__MDI__.CnvVM(totale)
        if self.__MDI__.val=='': vtotale = '0,00'
        else : vtotale = self.__MDI__.val
        self.totale.SetValue(vtotale)

    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)



