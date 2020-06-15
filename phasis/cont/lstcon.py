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
    return LstMov(parent,cnt)

#---------------------------------------------------------------------------
class LstMov(wx.ScrolledWindow):
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
        self.tbl="movcon"
        self.tblart="articoli"
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
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), wx.DLG_SZE(self.pnl , 335,130),
              wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,140), 
              wx.DLG_SZE(self.pnl , 335,-1))



        wx.StaticText(self.pnl, -1, "Contropartita :", 
              wx.DLG_PNT(self.pnl, 10,152))
        self.CF = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 65,150), 
              wx.DLG_SZE(self.pnl, 60,-1),
              [], wx.CB_DROPDOWN | wx.CB_SORT )
        self.vCF = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 65,150))

        self.lc1odcf = wx.StaticText(self.pnl, -1, "Cod.", 
              wx.DLG_PNT(self.pnl, 135,152))
        self.codcf = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 180,150), 
              wx.DLG_SZE(self.pnl , 40, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.ccodcf = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , -1, "...", 
              wx.DLG_PNT(self.pnl , 225,150),
              wx.DLG_SZE(self.pnl , 12,12),wx.TE_PROCESS_ENTER)


        wx.StaticText(self.pnl , -1, _("Rag Soc.:"), 
              wx.DLG_PNT(self, 25,172))
        self.ragsoc1 = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 65,170), 
              wx.DLG_SZE(self.pnl , 100, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.cragsoc1 = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl , -1, "...", 
              wx.DLG_PNT(self.pnl , 170,170),
              wx.DLG_SZE(self.pnl , 12,12),wx.TE_PROCESS_ENTER)

        wx.StaticText(self.pnl , -1, "", 
              wx.DLG_PNT(self, 25,190))


        self.ok = wx.Button(self.pnl , -1, cfg.vcok, 
              wx.DLG_PNT(self.pnl , 300,150), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self.pnl , -1, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 300,165), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.inte = wx.Button(self.pnl , -1, cfg.vcint, 
              wx.DLG_PNT(self.pnl , 300,165), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa = wx.Button(self.pnl, -1, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 300,180), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        
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

        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.inte.Bind(wx.EVT_BUTTON, self.Start)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK,  self.DblClick)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.CF.Bind(wx.EVT_COMBOBOX, self.SelCOMBOcfev)
        #self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndMov)
        #self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndMov)   
        self.ccodcf.Bind(wx.EVT_BUTTON, self.FndMov)
        self.codcf.Bind(wx.EVT_TEXT_ENTER, self.FndMov)   
       
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        
        self.Start(self)

    def Stampa(self, evt): 
        anno = self.annoc
        codcf= self.codcf.GetValue()
        tipodoc = 'lstmovc'
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,   
              tipo = tipodoc, 
              parametriSql = (anno,),
              datiazienda = self.dzDatiAzienda,
              anteprima = True )


    def Start(self, event):
        self.vCF.Show(False)
        self.codcf.SetValue('')
        self.ragsoc1.SetValue('')
        self.vCF.SetValue('C')
        self.sCF = ''
        self.SelCOMBOcf(self)



        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Anno"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(1, _("Num. Mov."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(2, _("Data Mov."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(3, _("Num. Riga"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(4, _("Anno IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(5, _("Div"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(6, _("PDC"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(7, _("Descrizione Operazione"),width=wx.DLG_SZE(self.pnl, 150,-1).width) #
        self.lc.InsertColumn(8, _("Importo"),width=wx.DLG_SZE(self.pnl, 60,-1).width)      #
        self.lc.InsertColumn(9, _("Imponibile"),width=cfg._COLSZ0_)     
        self.lc.InsertColumn(10, _("Anno Doc."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(11, _("Tipo Doc."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(12, _("Data Doc."),width=wx.DLG_SZE(self.pnl, 50,-1).width)#
        self.lc.InsertColumn(13, _("Num Doc."),width=wx.DLG_SZE(self.pnl, 50,-1).width)#
        self.lc.InsertColumn(14, _("Num Doc1."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(15, _("Conto"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(16, _("Totale Doc."),width=wx.DLG_SZE(self.pnl, 60,-1).width)#
        self.lc.InsertColumn(17, _("segno"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(18, _("Tipo CPart"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(19, _("Cod CF"),width=cfg._COLSZ0_)        
        self.lc.InsertColumn(20, _("Cambio"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(21, _("Tipo IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(22, _("Tipo IVA1"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(23, _("Aliq. IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(24, _("Registro"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(25, _("Imponib"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(26, _("Rigagior"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(27, _("Paggior"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(28, _("Note"),width=cfg._COLSZ0_)
        
        font = self.GetFont()
        self.lc.SetFont(font)
        self.inte.Show(False)
        self.canc.Show(True)
        self.ragsoc1.SetFocus()


    def SelCOMBOcf(self, evt):
        vCF = self.vCF.GetValue()
        self.CF.Clear()
        self.CF.Append('Cliente','C')
        self.CF.Append('Fornitore','F')
        if vCF=="C":vCF=0
        if vCF=="F":vCF=1
        self.CF.Select(vCF)


    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str =  evt.GetString()
        evt.Skip()

    def SelCOMBOcfev(self, evt):
        self.Sel(evt)
        self.vCF.SetValue(self.cb_val)



        
    def FndSelMov(self, evt):        
        rowlc = 0
        vragsoc1 = self.ragsoc1.GetValue()
        vcodcf = self.codcf.GetValue()
        vCF = self.vCF.GetValue()
        #if (vragsoc1=="" and vcodcf=="") :
        sql = """ select * from movcon where anno="%s" order by data_int asc"""
        valueSql = self.annoc
        if vcodcf!="":
            sql = """ select * from movcon where anno="%s"  
                      and cpart = "%s" 
                      and t_cpart = "%s" 
                      order by data_int """
            valueSql = self.annoc,int(vcodcf),vCF
        try:
            self.ClearLc(self)
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:

                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()      
                    self.lc.InsertStringItem(rowlc, str(row[0]))
                    self.lc.SetStringItem(rowlc, 1, str(row[1]))
                    self.lc.SetStringItem(rowlc, 2, str(row[2]))
                    self.lc.SetStringItem(rowlc, 3, str(row[3]))
                    self.lc.SetStringItem(rowlc, 4, str(row[4]))
                    self.lc.SetStringItem(rowlc, 5, str(row[5]))
                    self.lc.SetStringItem(rowlc, 6, str(row[6]))
                    self.lc.SetStringItem(rowlc, 7, str(row[7]))
                    self.__MDI__.CnvVM(row[8])
                    imporval=self.__MDI__.val
                    self.__MDI__.CnvVM(row[9])
                    imponval=self.__MDI__.val
                    self.lc.SetStringItem(rowlc, 8, imporval)
                    self.lc.SetStringItem(rowlc, 9, imponval)
                    self.lc.SetStringItem(rowlc, 10, str(row[10]))
                    self.lc.SetStringItem(rowlc, 11, str(row[11]))
                    self.lc.SetStringItem(rowlc, 12, str(row[12]))
                    self.lc.SetStringItem(rowlc, 13, str(row[13]))
                    self.lc.SetStringItem(rowlc, 14, str(row[14]))                    
                    self.lc.SetStringItem(rowlc, 15, str(row[15]))
                    self.__MDI__.CnvVM(row[16])
                    importo=self.__MDI__.val
                    self.lc.SetStringItem(rowlc, 16, importo)        
                    self.lc.SetStringItem(rowlc, 17, str(row[17]))
                    self.lc.SetStringItem(rowlc, 18, str(row[18]))
                    self.lc.SetStringItem(rowlc, 19, str(row[19]))
                    self.lc.SetStringItem(rowlc, 20, str(row[20]))
                    self.lc.SetStringItem(rowlc, 24, str(row[24]))
                    self.lc.SetStringItem(rowlc, 25, str(row[25]))
                    self.lc.SetStringItem(rowlc, 26, str(row[26]))  
                    self.lc.SetStringItem(rowlc, 27, str(row[27]))
                    self.lc.SetStringItem(rowlc, 28, str(row[28])) 
                    self.lc.SetItemData(0,0)

        except StandardError, msg:
            self.__MDI__.MsgErr("lstcon","FndSelMov Error %s " % (msg)) 
        self.CnAz.commit()
        self.currentItem = 0
        self.inte.Show(True)
        self.canc.Show(False)


    def FndCodCF(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        cod = self.codcf.GetValue()
        tcpart = self.vCF.GetValue()
        sql = """ select * from anag where cod = "%s" and t_cpart = "%s" """

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
        self.ClearLc(self) 
        self.FndSelMov(self)



    def FndAnag(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue()
        cod = self.codcf.GetValue()
        tcpart = self.vCF.GetValue()
        print tcpart
        valueSql = tcpart, '%' + val.title() + '%'
        if tcpart=="A":
            sql = """ select * from agenti 
                      where t_cpart = "%s" and rag_soc1 like "%s" 
                      order by rag_soc1 desc """
        else: 
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
            self.tcpart = self.vCF.GetValue()
            control = [self.tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

    def FndSelAnag(self, evt):
        row=evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())


    def ClearLc(self, evt):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Anno"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(1, _("Num. Mov."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(2, _("Data Mov."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(3, _("Num. Riga"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(4, _("Anno IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(5, _("Div"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(6, _("PDC"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(7, _("Descrizione Operazione"),width=wx.DLG_SZE(self.pnl, 150,-1).width) #
        self.lc.InsertColumn(8, _("Importo"),width=wx.DLG_SZE(self.pnl, 60,-1).width)      #
        self.lc.InsertColumn(9, _("Imponibile"),width=cfg._COLSZ0_)     
        self.lc.InsertColumn(10, _("Anno Doc."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(11, _("Tipo Doc."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(12, _("Data Doc."),width=wx.DLG_SZE(self.pnl, 50,-1).width)#
        self.lc.InsertColumn(13, _("Num Doc."),width=wx.DLG_SZE(self.pnl, 50,-1).width)#
        self.lc.InsertColumn(14, _("Num Doc1."),width=cfg._COLSZ0_)
        self.lc.InsertColumn(15, _("Conto"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(16, _("Totale Doc."),width=wx.DLG_SZE(self.pnl, 60,-1).width)#
        self.lc.InsertColumn(17, _("segno"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(18, _("Tipo CPart"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(19, _("Cod CF"),width=cfg._COLSZ0_)        
        self.lc.InsertColumn(20, _("Cambio"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(21, _("Tipo IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(22, _("Tipo IVA1"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(23, _("Aliq. IVA"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(24, _("Registro"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(25, _("Imponib"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(26, _("Rigagior"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(27, _("Paggior"),width=cfg._COLSZ0_)
        self.lc.InsertColumn(28, _("Note"),width=cfg._COLSZ0_)




        
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
        tbl="movcon"
        rec=(self.getColTxt(self.currentItem, 1))
        #AggMenu=self.AggMenu
        #IDMENU=self.IDMENU
        #self.CMD(rec, Dir, Mod, ottl, tbl)       
        self.CMD(2001,rec,tbl)
        #self.AggMenu(True,self.IDMENU)
        #self.Destroy()
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)

    def FndMov(self, event):
        self.FndSelMov(self)
