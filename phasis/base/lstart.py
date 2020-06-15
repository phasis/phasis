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

ttl=_("Lista Articoli")

def create(parent,cnt):
    return LstArt(parent,cnt)

#---------------------------------------------------------------------------
class LstArt(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #wx.Frame.__init__(self, id=wx.NewId(), name='',
        #      parent=prnt, pos=wx.Point(0, 0), 
        #      style=wx.DEFAULT_FRAME_STYLE, title=ttl)
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.SetClientSize(wx.Size(680, 400))
        
        self.cnt = cnt
        Nid = wx.NewId()
        self.ttl=cnt[0]
        tcpart=cnt[1][0].upper()
        self.t_cpart=tcpart
        self.tcpart=tcpart+"1"
        self.rec=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        self.CMD=cnt[5]
        #self.font=self.GetFont()
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz=self.__MDI__.GetConnAZ() 
        self.annoc=self.__MDI__.GetAnnoC() 
        self.datacon= self.__MDI__.GetDataC()
        self.dzDatiAzienda= self.__MDI__.dzDatiAzienda
        self.sMERCE=""
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel1',
              parent=self, pos=wx.Point(0, 0) , size = wx.DLG_SZE(self,680/2,400/2), #size=wx.Size(680, 400),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL )
        self.pnl.SetFont(self.font)
        
        self.lc = wx.ListCtrl(self.pnl , Nid,
              wx.DLG_PNT(self, 5,5), 
              wx.DLG_SZE(self.pnl , 335,130),wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,140), 
              wx.DLG_SZE(self.pnl , 335,-1))
        self.lcod=wx.StaticText(self.pnl , -1, _("Codice :"), 
              wx.DLG_PNT(self.pnl, 5,147))
        self.cod = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 55,145), 
              wx.DLG_SZE(self.pnl , 70, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.codbar = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl , 55,145), 
              wx.DLG_SZE(self.pnl , 70, cfg.DIMFONTDEFAULT))
        wx.StaticText(self.pnl , -1, _("Descrizione :"), 
              wx.DLG_PNT(self.pnl, 5,162))
        self.descriz = wx.TextCtrl(self.pnl , Nid, "",
              wx.DLG_PNT(self.pnl ,55,160), 
              wx.DLG_SZE(self.pnl , 125, cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.rbSEMP = wx.RadioButton(self.pnl, Nid, cfg.vcSEMP,
              wx.DLG_PNT(self.pnl, 180,145), 
              wx.DLG_SZE(self.pnl, 50,10), wx.RB_GROUP )
        self.rbDETT = wx.RadioButton(self.pnl, Nid, cfg.vcDETT,
              wx.DLG_PNT(self.pnl, 230,145), wx.DLG_SZE(self.pnl, 50,10))
        self.tipos = wx.TextCtrl(self.pnl, -1, "S", 
              wx.DLG_PNT(self.pnl, 280,145))      
        self.ccod=wx.BitmapButton(self.pnl, -1, png,#buttons.GenButton(self.pnl, Nid, "...",#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 130,145),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.ccodbar=buttons.GenToggleButton(self.pnl, Nid, "|''|'|", 
              wx.DLG_PNT(self.pnl, 145,145),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.cdes=wx.BitmapButton(self.pnl, -1, png,#buttons.GenButton(self.pnl, Nid, "...",#wx.Button(self.pnl , Nid, "...", 
              wx.DLG_PNT(self.pnl , 185,160),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl, -1, _("Cat. Merc. :"), 
              wx.DLG_PNT(self.pnl, 5,182))
        self.MERCE = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 55,180), 
              wx.DLG_SZE(self.pnl, 100,-1),
                    [],wx.CB_DROPDOWN | wx.CB_SORT )     
        self.vMERCE = wx.TextCtrl(self.pnl, -1, "", 
              wx.DLG_PNT(self.pnl, 155,180))      

        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 275,145), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.ok = wx.Button(self.pnl , Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl , 210,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc=wx.Button(self.pnl , Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl , 275,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        
        self.canc.SetFocus()
        #self.SetFont(self.font)
        
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,5)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)

        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)

        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ok.Bind(wx.EVT_BUTTON, self.Ok)        
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.DblClick)
        self.cdes.Bind(wx.EVT_BUTTON, self.FndArt) 
        self.rbSEMP.Bind(wx.EVT_RADIOBUTTON, self.RadioB)
        self.rbDETT.Bind(wx.EVT_RADIOBUTTON, self.RadioB)       
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct)
        self.descriz.Bind(wx.EVT_TEXT_ENTER, self.FndArt)
        self.cod.Bind(wx.EVT_TEXT_ENTER, self.FndArt)
        self.codbar.Bind(wx.EVT_TEXT_ENTER, self.FndArt)
        self.ccodbar.Bind(wx.EVT_BUTTON, self.SelCodBar) 
        self.ccod.Bind(wx.EVT_BUTTON, self.FndArt) 
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.MERCE.Bind(wx.EVT_TEXT_ENTER, self.MERCESF)
        self.MERCE.Bind(wx.EVT_COMBOBOX, self.SelMERCE)
        self.Start(self)

    def Start(self, evt):
        self.vMERCE.Enable(False)
        self.vMERCE.Show(False)
        self.vMERCE.SetValue("0")
        self.codbar.Show(False)
        self.tipos.Show(False)
        self.ClearLC(self)
        self.SelCOMBO(self)
        self.cod.SetFocus()

    def ClearLC(self, evt):
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Descriz"))
        self.lc.InsertColumn(2, _("UM"))
        self.lc.InsertColumn(5, _("TG"))
        self.lc.InsertColumn(3, _("Imponibile"))
        self.lc.InsertColumn(4, _("Prezzo"))
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self,  50,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self, 145,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self, 20,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self, 20,-1).width)        
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self,  60,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self,  60,-1).width)
        #self.lc.SetFont(self.font)

    def RadioB(self, evt):
        if (self.rbSEMP.GetValue()==True):
            self.tipos.SetValue("S")
            self.stampa.SetFocus()
        if (self.rbDETT.GetValue()==True):
            self.tipos.SetValue("D")
            self.stampa.SetFocus()

    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()

    def SelCodBar(self, evt):
        if self.ccodbar.GetValue()==0 :
            self.ccodbar.SetToggle(False)
            self.cod.Show(True)
            self.codbar.Show(False)
            self.lcod.SetLabel(_("Codice"))
            self.cod.SetFocus()
            self.codbar.SetValue('')
        else:
            self.ccodbar.SetToggle(True)
            self.cod.Show(False)
            self.codbar.Show(True)
            self.lcod.SetLabel(_("Cod. a Barre"))
            self.codbar.SetFocus()
            self.cod.SetValue('')
        
    def FndArt(self, evt):
        self.Start(self)
        self.FndSelArt(self)

    def FndSelArt(self, evt):
        ## Funzione Cerca Articolo
        rowlc=0
        self.tblart='articoli'
        val = self.descriz.GetValue().upper()
        cod = self.cod.GetValue().upper()
        codbar = self.codbar.GetValue().upper()
        vMERCE = self.vMERCE.GetValue()
        sql = """ SELECT * FROM articoli 
                  WHERE descriz like '%s' ORDER BY descriz DESC """
        sfval=1
        if val == "" and cod != "" and vMERCE == '0':
            sfval=0
            sql = """ SELECT * FROM articoli 
                      WHERE cod like '%s' ORDER BY cod DESC  """
            val=cod
        if val == "" and codbar != "" and vMERCE == '0':
            sfval=0
            sql = """ SELECT * FROM articoli 
                      WHERE codbar like '%s' ORDER BY descriz DESC  """
            val=codbar
        if vMERCE != '0':
            sfval=0
            sql = """ SELECT * FROM articoli 
                      WHERE merce like '%s' ORDER BY descriz DESC  """
            val=vMERCE
        valueSql = '%' + val + '%',
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            if rows == []:
                self.Message(cfg.msgdatonull,self.ttl)
                if sfval==1:self.descriz.SetFocus()
                else:self.cod.SetFocus()
            for row in rows:
                for rowlc in range(1):
                    rowlc = self.lc.GetItemCount()     
                    codart = str(row[0])
                    codbar = str(row[1])
                    descriz = str(row[2])
                    UM= str(row[3])
                    if (row[4]==None):tg=""
                    else: tg=str(row[4])
                    self.lc.InsertStringItem(rowlc, codart)    
                    self.lc.SetStringItem(rowlc, 1, descriz)
                    self.lc.SetStringItem(rowlc, 2, UM)
                    self.lc.SetStringItem(rowlc, 5, tg)
                    self.__MDI__.CnvVMPZ(row[5])
                    price1=self.__MDI__.val
                    self.__MDI__.CnvVMPZ(row[6])
                    price2=self.__MDI__.val
                    self.__MDI__.CnvVMPZ(row[7])
                    costo=self.__MDI__.val
                    self.lc.SetStringItem(rowlc, 3, price1)
                    self.lc.SetStringItem(rowlc, 4, price2)
        except StandardError, msg:
            print "Error %s" % (msg)
        self.CnAz.commit()
                                        
        self.currentItem = 0
                   
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
        #ttl="Anagrafica Articoli"
        #Dir="base"
        #Mod="articoli"
        tbl=self.t_cpart
        rec=(self.lc.GetItemText(self.currentItem))
        #AggMenu=self.AggMenu
        #IDMENU=self.IDMENU
        #self.CMD(rec, Dir, Mod, ttl, tbl)
        self.CMD(1001,rec,tbl)    
        #self.AggMenu(True,self.IDMENU)
        #self.Destroy()
        
    def LstSlct(self, event):
        self.currentItem = event.m_itemIndex

    def LstAct(self, event):
        self.currentItem = event.m_itemIndex    
        self.DblClick(self)

    #<daniele> 
    def Stampa(self, evt): 
        cod = self.cod.GetValue()
        merce = self.vMERCE.GetValue()
        tipos='lstart'
        if self.tipos.GetValue()=='D': tipos='lstartc'
        valueSql = "%" + cod.upper() + "%"
        if cod == '' and  merce != "0": 
            valueSql = merce
            tipos='lstartm'
            if self.tipos.GetValue()=='D': tipos='lstartmc'
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,   #connessione
              tipo = tipos, #tipo documento e parametro
              parametriSql = valueSql,
              datiazienda = self.dzDatiAzienda,
              anteprima = True )
    #</daniele>       

    def MERCESF(self, evt):
        pass   

    def SelCOMBO(self, evt):
        ## Funzione Cerca TabGen
        vMERCE=self.vMERCE.GetValue()
        self.MERCE.Clear()
        sql = " SELECT COD, VALORE, DESCRIZ FROM tabgen "
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            self.MERCE.Append(' --','0')
                 
            while (1):
                row = cr.fetchone () 
                if row == None: 
                    break          
                if (row[0]=="MERCE"):
                    if (vMERCE=='0'): self.sMERCE=' --'
                    if (row[1]==vMERCE):self.sMERCE=row[2]
                    self.MERCE.Append(row[2],row[1])
        except StandardError, msg:
            self.__MDI__.MsgErr("LstArt"," Cerca TabGen Error %s"  % (msg))                   
        self.CnAz.commit()
           
        cntMERCE=0
        cntMERCE=self.MERCE.FindString(self.sMERCE)
        self.MERCE.Select(cntMERCE)

    def SelMERCE(self, evt):
        self.Sel(evt)
        self.vMERCE.SetValue(self.cb_val)
        self.descriz.SetValue('')
        self.cod.SetValue('')
        self.codbar.SetValue('')
        self.ClearLC(self)                
        self.FndSelArt(self)

    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str= evt.GetString()
        evt.Skip()


