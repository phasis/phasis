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
import  wx.lib.masked as masked
        
def create(parent,cnt):
    return rmovcon(parent,cnt)
  
class rmovcon(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        #self.Center(wx.BOTH)
        self.ttl=cnt[0]
        #self.vtmod=cnt[1][3].upper()
        self.rec=cnt[2]
        self.sMM=''
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
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
              parent = self, pos = wx.Point(0, 0), 
              size = wx.DLG_SZE(self,680/2,420/2), #size = wx.Size(680, 420),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)

        self.ldataDA = wx.StaticText(self.pnl, -1, "Data Da:", 
                    wx.DLG_PNT(self.pnl, 35,62))
        self.data_docDA = masked.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 65,60), 
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT),wx.ALIGN_RIGHT,
              autoformat='EUDATEDDMMYYYY/')
        self.ldataDA = wx.StaticText(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 55,62))
   
        self.cdata_docDA = wx.Button(self.pnl, -1, "...", 
	      wx.DLG_PNT(self.pnl, 115,60),
	      wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))



###########################
        #wx.StaticText(self.pnl, -1, "Num. Doc. DA", wx.DLG_PNT(self.pnl, 160,62))

        self.num_mov = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 235,60),
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT),wx.ALIGN_RIGHT) 

        self.num_docDA = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 235,60),
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT),wx.ALIGN_RIGHT) 

        #wx.StaticText(self.pnl, -1, "Num. Doc. A", wx.DLG_PNT(self.pnl, 160,82))
        self.num_docA = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 235,80),
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT),wx.ALIGN_RIGHT) 

########################################


        self.ldataA = wx.StaticText(self.pnl, -1, "Data A:", 
              wx.DLG_PNT(self.pnl, 130,62))
        self.data_docA = masked.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 157,60), 
              wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT),wx.ALIGN_RIGHT,
              autoformat='EUDATEDDMMYYYY/')

        self.cdata_docA = wx.Button(self.pnl, -1, "...", 
	      wx.DLG_PNT(self.pnl, 207,60),
	      wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))

        # linea 2  


        wx.StaticText(self.pnl, -1, "Controp.:", 
              wx.DLG_PNT(self.pnl, 35,82)) 
        self.CF = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 65,80), 
              wx.DLG_SZE(self.pnl, 50,-1), [],
              wx.CB_DROPDOWN | wx.CB_SORT )
        self.vCF = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 65,80))






        wx.StaticText(self.pnl, -1, "Somma Totale Dare:", 
              wx.DLG_PNT(self.pnl, 85,102))

        self.tot_docD = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 149,100), wx.DLG_SZE(self.pnl, 70,-1),
              wx.ALIGN_RIGHT)

        wx.StaticText(self.pnl, -1, "Somma Totale Avere:", 
              wx.DLG_PNT(self.pnl, 85,122))

        self.tot_docA = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 149,120), wx.DLG_SZE(self.pnl, 70,-1),
               wx.ALIGN_RIGHT)

        wx.StaticText(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 85,142))


        
        # Crea Button-------------------------------------------------
        #self.ok = wx.Button(self.pnl, -1, cfg.vcok, 
	      #wx.DLG_PNT(self.pnl, 120,10), 
	      #wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))   

        self.canc = wx.Button(self.pnl, -1, cfg.vccanc, 
	      wx.DLG_PNT(self.pnl, 250,60), 
	      wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa = wx.Button(self.pnl, -1, cfg.vcstampa, 
	      wx.DLG_PNT(self.pnl, 250,75), 
	      wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.totale = wx.Button(self.pnl, -1, "Totale", 
	      wx.DLG_PNT(self.pnl, 250,90), 
	      wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
	
        self.SetFont(self.font)
        box_sizer = wx.BoxSizer(wx.VERTICAL)
       	box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,5)
	self.SetAutoLayout(1)
	self.SetSizer(box_sizer)
        box_sizer.Fit(self)


        self.CF.Bind(wx.EVT_COMBOBOX, self.SelCOMBOcfev)
        
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.cdata_docDA.Bind(wx.EVT_BUTTON, self.SrcDocDA) 
        self.cdata_docA.Bind(wx.EVT_BUTTON, self.SrcDocA)
        #self.Bind(wx.EVT_TEXT_ENTER, self.SrcDocDA, self.data_docDA) 
        #self.Bind(wx.EVT_TEXT_ENTER, self.SrcDocA, self.data_docA)
        self.totale.Bind(wx.EVT_BUTTON, self.TotDoc)  
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.Start(self)
                
    def Start(self, evt):
        self.num_mov.Show(False) 
        self.num_mov.SetValue('0') 
        self.data_docDA.Show(True)
        self.cdata_docDA.Show(True)

        self.data = strftime("%d/%m/%Y")        
        #self.data_docDA.SetValue(self.data)    
        self.data_docDA.SetFocus()
        #self.ldata.SetLabel("Mese :")
        #self.data_docDA.Show(False)
        #self.cdata_docDA.Show(False)
        #self.tot_doc.Enable(False)
        self.num_docDA.Show(False)
        self.num_docA.Show(False)  
        self.num_docDA.Enable(False)
        self.num_docA.Enable(False)  
         
        #self.data_docDA.Enable(False)
        self.data_docA.Enable(False)
        self.cdata_docA.Enable(False)
        self.stampa.Enable(False)
        self.totale.Enable(False)

        self.vCF.Show(False)

        self.vCF.SetValue('C')

        self.sCF = ''

        self.SelCOMBOcf(self)

        #self.tipo_doc = "R1"




    def SelCOMBOcf(self, evt):
        vCF = self.vCF.GetValue()
        self.CF.Clear()
        self.CF.Append('Cliente','C')
        self.CF.Append('Fornitore','F')
        self.CF.Append('Agente','A')
        self.CF.Append('Altro','Z')
        if vCF=="C":vCF=0
        if vCF=="F":vCF=1
        if vCF=="A":vCF=2
        if vCF=="Z":vCF=3
        self.CF.Select(vCF)


    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str= evt.GetString()
        evt.Skip()





    def SelCOMBOcfev(self, evt):
        self.Sel(evt)
        self.vCF.SetValue(self.cb_val)




    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.int.SetFocus()
        evt.Skip()

    def EvtCharqt(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr_row==""):self.IntRow(self)
        evt.Skip()
                


##########################################################



    def Stampa(self, evt):
 
        #cod = self.cod.GetValue()
        #merce = self.vMERCE.GetValue()

        vCF = self.vCF.GetValue()

        # DA
        data_mov = self.data_docDA.GetValue()
        data_int = data_mov.split("/")
        data_int = str(data_int[2]) + str(data_int[1]) + str(data_int[0])
        data_mov = data_int
        # A
        data_A = self.data_docA.GetValue()
        data_int_A = data_A.split("/")
        data_int_A = str(data_int_A[2]) + str(data_int_A[1]) + str(data_int_A[0])
        data_A = data_int_A

        
        #tipos='lstart'
        #if self.tipos.GetValue()=='D': tipos='lstartc'
        #valueSql = "%" + cod.upper() + "%"
        #if cod == '' and  merce != "0": 


        valueSql = vCF, int(data_int), int(data_int_A)
        tipos='rmovcon'
        print valueSql
            #if self.tipos.GetValue()=='D': tipos='lstartmc'
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,   #connessione
              tipo = tipos, #tipo documento e parametro
              parametriSql = valueSql,
              datiazienda = self.dzDatiAzienda,
              anteprima = True )

   	
	


    def SrcDocDA(self, evt):
        num_mov = self.num_mov.GetValue()
        # DA
        data_DA = self.data_docDA.GetValue()
        if data_DA == "  /  /    " : data_DA="01/01/" + self.annoc
        data_int = data_DA.split("/")
        data_int = str(data_int[2]) + str(data_int[1]) + str(data_int[0])
        # A
        data_A = self.data_docA.GetValue()
        if data_A == "  /  /    " : data_A="31/12/" + self.annoc
        data_int_A = data_A.split("/")
        data_int_A = str(data_int_A[2]) + str(data_int_A[1]) + str(data_int_A[0])
        data_A = data_int_A

  
        vCF = self.vCF.GetValue()
        anno = self.annoc
        cnt_rec = 0
        if int(num_mov)=='0' or int(num_mov)=="" or int(num_mov)==0: 
            sql = """ select * from movcon
                      where t_cpart = "%s" 
                      and data_int >= "%s" 
                      order by data_int desc """
            valueSql = vCF, int(data_int) 
        else:
            sql = """ select * from movcon where num_mov = "%s" """
            valueSql = int(num_mov)
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec += 1
        except StandardError, msg:
            print "Cerca docu dataDA Error %s" % (msg)
        self.CnAz.commit()
            
        if (num_mov!='0' and num_mov!="" and num_mov!=0):
            #print "entrato 1"
            self.num_mov.SetValue('0')
            self.data_docDA.SetValue(row[12])
            if self.data_docDA.GetValue()=="  /  /    ": self.data_docDA.SetValue(row[2])
            self.data_docA.Enable(True)
            self.cdata_docA.Enable(True)  
            self.cdata_docA.SetFocus()
        elif (num_mov=='0' or num_mov=="" or num_mov==0):
            try:
	        import srcmovconr
            except :
	        pass
            try:
                import ordi.srcmovconr
            except :
                pass
            control = [self.annoc, data_int, self.SrcDocDA, vCF, self.num_mov, data_int_A]
            win = srcmovconr.create(self,control) 
            win.Show(True)
            self.data_docA.Enable(True)
            self.cdata_docA.Enable(True)  
            self.cdata_docA.SetFocus()
        elif cnt_rec==0 : 
            self.Message(cfg.msgdatonull,self.ttl)



    def SrcDocA(self, evt):
        num_mov = self.num_mov.GetValue()
        # DA
        data_DA = self.data_docDA.GetValue()
        if data_DA == "  /  /    " : data_DA="01/01/" + self.annoc
        data_int = data_DA.split("/")
        data_int = str(data_int[2]) + str(data_int[1]) + str(data_int[0])
        # A
        data_A = self.data_docA.GetValue()
        if data_A == "  /  /    " : data_A="31/12/" + self.annoc
        data_int_A = data_A.split("/")
        data_int_A = str(data_int_A[2]) + str(data_int_A[1]) + str(data_int_A[0])
        data_A = data_int_A
        vCF = self.vCF.GetValue()
        anno = self.annoc
        cnt_rec = 0
        if int(num_mov)=='0' or int(num_mov)=="" or int(num_mov)==0:
            if data_A=="31/12/" + self.annoc:
                #print "rmovcon 1 A"

                sql = """ select * from movcon
                          where t_cpart = "%s" 
                          and data_int >= "%s" 
                          order by data_int asc """
                valueSql = vCF, int(data_int)
            else:
                #print "rmovcon 2 A"
                sql = """ select * from movcon
                          where t_cpart = "%s" 
                          and data_int >= "%s"
                          and data_int <= "%s"
                          order by data_int asc """
                valueSql = vCF, int(data_int), int(data_int_A)
        else:
            sql = """ select * from movcon where num_mov = "%s" """
            valueSql = int(num_mov)
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec += 1
        except StandardError, msg:
            print "Cerca docu dataDA Error %s" % (msg)
        self.CnAz.commit()
            
        if (num_mov!='0' and num_mov!="" and num_mov!=0):
            #print "entrato 2"
            self.num_mov.SetValue('0')
            self.data_docA.SetValue(row[12])
            if self.data_docA.GetValue()=="  /  /    ": self.data_docA.SetValue(row[2])
            self.stampa.Enable(True) 
            self.totale.Enable(True)
        elif (num_mov=='0' or num_mov=="" or num_mov==0):
            try:
	        import srcmovconr
            except :
	        pass
            try:
                import ordi.srcmovconr
            except :
                pass
            control = [self.annoc, data_int, self.SrcDocA, vCF, self.num_mov, data_int_A]
            win = srcmovconr.create(self,control) 
            win.Show(True)
        elif cnt_rec==0 : 
            self.Message(cfg.msgdatonull,self.ttl)



    def Close(self, evt):
        self.AggMenu(True,self.IDMENU)
        wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        #self.Destroy()



    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    def TotDoc(self, evt):
        tot_docD=0
        tot_docA=0
        rA=""
        rD=""  
        # DA
        data_DA = self.data_docDA.GetValue()
        if data_DA == "  /  /    " : data_DA="01/01/" + self.annoc
        data_int = data_DA.split("/")
        data_int = str(data_int[2]) + str(data_int[1]) + str(data_int[0])
        # A
        data_A = self.data_docA.GetValue()
        if data_A == "  /  /    " : data_A="31/12/" + self.annoc
        data_int_A = data_A.split("/")
        data_int_A = str(data_int_A[2]) + str(data_int_A[1]) + str(data_int_A[0])
        data_A = data_int_A
        vCF = self.vCF.GetValue()
        anno = self.annoc

        valueSql = self.annoc,vCF,int(data_int),int(data_int_A)
        sql = """ select segno,imporval,data_int,t_cpart,anno from movcon where anno="%s" 
                  and t_cpart="%s" 
                  and data_int>="%s" 
                  and data_int<="%s" """
        #print valueSql
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                print row
                if str(row[0])=="A":tot_docA+=row[1]
                    #rA=str(row[1])
                    #tot_docA+=int(rA)
                if str(row[0])=="D":tot_docD+=row[1]
                    #rD=str(row[1])
                    #tot_docD+=int(rD)
            self.__MDI__.CnvVM(tot_docA)
            tot_docA=self.__MDI__.val
            self.__MDI__.CnvVM(tot_docD)
            tot_docD=self.__MDI__.val
            self.tot_docA.SetValue(tot_docA)
            self.tot_docD.SetValue(str(tot_docD))         
        except StandardError, msg:
            print "Totale D/A Error %s" % (msg)
        self.CnAz.commit()
 
 
    def is_look(self):
        if (self.cntr!="new" and self.cntr!="modi"): return False
        else : return True
        
    def data_reload(self,rec,cntrp):
        self.rec=rec
        #self.tcpart=cntrp.upper()
        self.Start(self)

