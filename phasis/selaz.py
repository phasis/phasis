# -*- coding: iso-8859-1 -*-
#
# Copyright (C) 2003 - 2008  See Open - http://www.seeopen.it/
# Author: Massimo Gerardi <m.gerardi@mgsoft.it>
#
# Released under the terms of the GNU General Public License
# (version 2 or above)
#
# See COPYING for details.
#
# www.phasis.it - info@phasis.it 


import wx
#import wx.lib.buttons as buttons
from cfg import *
import cfg
import fdb
from copyright import *
#import gettext
#_ = gettext.gettext


data = strftime("%d/%m/%Y")
ttlaz = _('Selezione Azienda')

def create(parent,cnt):
    return SelAzienda (parent,cnt)

class SelAzienda(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        wx.ScrolledWindow.__init__(self, parent=prnt,id = -1) #wx.NewId(), name='',
              #parent=prnt, pos=wx.Point(0, 0), size=wx.DefaultSize,  
              #style=wx.CAPTION, title=cnt[0])
        self.SetScrollbars(1,1,100,100)
        self.FitInside()
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
 	
        #self.pnl.SetBackgroundColour(wx.LIGHT_GREY)
        #box = wx.GridSizer(1, 1)
        #box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        #self.SetSizer(box)


        #self.SetIcon(wx.Icon(cfg.path_img + "null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.Center(wx.BOTH)  
        self.SetTTL=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        #self.font=self.GetFont()
        
        #self.font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False)#self.GetFont()
        #self.font=wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
        #y=wx.ScreenDC().MaxY()
        #if y>=1200 : numfont=16
        #elif y>=1024 : numfont=14
        #else : numfont=12
        #if cfg.FONTFISSO!=0 : numfont=cfg.FONTFISSO
        #self.font.SetPointSize(numfont)
        #self.SetFont(self.font)        
        
        Nid=wx.NewId()
        self.sANNODA=''
        self.sANNOA=''
        self.ANNOcont=''#strftime("%Y")
        self.__MDI__=wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font) 
        ##self.CnDBAz = prnt.GetConnDBAZ()
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0), 
              size = wx.DLG_SZE(self,680/2,370/2), #size=wx.Size(680, 370),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)        
        
        self.lpost = wx.StaticText(self.pnl, -1, _("Postazione:"), 
            wx.DLG_PNT(self.pnl, 5,12))
        self.lpost.SetFont(self.font) 
            
        self.npost = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 50,10), wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT))
        self.npost.SetFont(self.font) 
        
        #self.cpost = buttons.GenButton(self.pnl, Nid, "...",#wx.Button(self.pnl, Nid, "...", 
        self.cpost=wx.BitmapButton(self.pnl, -1, png,
              wx.DLG_PNT(self.pnl, 85,10),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        self.post = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 105,10), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))        
        self.post.SetFont(self.font)
        
        self.lute = wx.StaticText(self.pnl, -1, _("Operatore:"),
            wx.DLG_PNT(self.pnl, 5,27))
        self.lute.SetFont(self.font)
                
        self.nute = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 50,25), wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT))
        self.nute.SetFont(self.font)
        
        self.cute = wx.BitmapButton(self.pnl, -1, png,
        #buttons.GenButton(self.pnl, Nid, "...",#wx.Button(self.pnl, Nid, "...",
            wx.DLG_PNT(self.pnl, 85,25),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        self.ute = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 105,25), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))
        self.ute.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Password :"), wx.DLG_PNT(self.pnl, 5,42)).SetFont(self.font)
        
        self.pwd = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 50,40), 
            wx.DLG_SZE(self.pnl, 47,cfg.DIMFONTDEFAULT), wx.TE_PASSWORD)
        self.pwd.SetFont(self.font)
        
        self.laz = wx.StaticText(self.pnl, -1, _("Azienda:"), 
            wx.DLG_PNT(self.pnl, 5,57))
        self.laz.SetFont(self.font)
        
        self.naz = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 50,55), 
            wx.DLG_SZE(self.pnl, 30,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER )
        self.naz.SetFont(self.font)
        
        self.caz = wx.BitmapButton(self.pnl, -1, png,
        #buttons.GenButton(self.pnl, Nid, "...",#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl, 85,55),
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        self.az = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 105,55), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))
        self.az.SetFont(self.font)
        
        self.nsrifaz = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 105,55), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))
        self.nsrifaz.SetFont(self.font)
        
        self.lcontab = wx.StaticText(self.pnl, -1, _("Anni Competenza :"), 
            wx.DLG_PNT(self.pnl, 5,72))
        self.lcontab.SetFont(self.font)
        
        self.ANNODA = wx.ComboBox(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 75,70), 
            wx.DLG_SZE(self.pnl, 35,-1), [],wx.CB_DROPDOWN | wx.CB_SORT)      
        self.ANNODA.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, "/", wx.DLG_PNT(self.pnl, 112,72)).SetFont(self.font)
        
        self.ANNOA = wx.ComboBox(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 117,70), 
            wx.DLG_SZE(self.pnl, 35,-1), [],
            wx.CB_DROPDOWN | wx.CB_SORT |wx.TE_PROCESS_ENTER  ) 
        self.ANNOA.SetFont(self.font)
        
        self.vANNODA = wx.TextCtrl(self.pnl, -1,"",wx.DLG_PNT(self.pnl, 5,95))
        self.vANNOA = wx.TextCtrl(self.pnl, -1,"",wx.DLG_PNT(self.pnl, 140,95))
        self.abl = wx.TextCtrl(self.pnl, -1,"",wx.DLG_PNT(self.pnl, 140,95))
        
        self.ldata = wx.StaticText(self.pnl, -1, _("Data di Lavoro :"),
            wx.DLG_PNT(self.pnl, 5,87))
        self.ldata.SetFont(self.font)
        
        self.datac = wx.TextCtrl(self.pnl, Nid, "",
             wx.DLG_PNT(self.pnl, 75,85), 
            wx.DLG_SZE(self.pnl, 50,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.datac.SetFont(self.font)
        
        self.cdatac = wx.BitmapButton(self.pnl, -1, png,
        #buttons.GenButton(self.pnl, Nid, "...",#wx.Button(self.pnl, Nid, "...", 
            wx.DLG_PNT(self.pnl, 130,85), 
            wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))        
        
        self.count = 0
        
        self.ok = wx.Button(self.pnl, -1, _("Accedi"), 
              wx.DLG_PNT(self.pnl, 45,110), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.ok.SetFont(self.font)
        
        self.canc = wx.Button(self.pnl, -1, _("Esci"), 
              wx.DLG_PNT(self.pnl, 110,110),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))      
        self.canc.SetFont(self.font)

        # spazio massimog
        wx.StaticText(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 120,120)).SetFont(self.font)         
        wx.StaticText(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 195,120)).SetFont(self.font)         
        #self.SetFont(self.font)


        self.pnl.SetBackgroundColour(wx.LIGHT_GREY)
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER | wx.ALL,10)           
        self.SetSizer(box)
      
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)


        self.ok.Bind(wx.EVT_BUTTON, self.OnOk)   
        self.canc.Bind(wx.EVT_BUTTON, self.OnClose)
        self.caz.Bind(wx.EVT_BUTTON, self.FndAZ)
        #EVT_TEXT_ENTER(self.pwd, Nid, self.Save)
        self.naz.Bind(wx.EVT_TEXT_ENTER, self.FndAZ)
        self.ANNODA.Bind(wx.EVT_COMBOBOX, self.SelANNODA)
        self.ANNOA.Bind(wx.EVT_COMBOBOX, self.SelANNOA)
        self.ANNOA.Bind(wx.EVT_TEXT_ENTER, self.SFok)
        #self.Bind(wx.EVT_CLOSE, self.Close)
        self.Start(self)

    def SFok(self, evt):
        self.ok.SetFocus()
     
    def Start(self, evt):  
        #self.lpost.Enable(False)
        self.npost.Enable(False)
        self.cpost.Enable(False)
        self.post.Enable(False)     
        #self.lute.Enable(False)
        self.nute.Enable(False)
        self.cute.Enable(False)
        self.ute.Enable(False)
        self.pwd.Enable(False)       
        #self.laz.Enable(False)
        #self.naz.Enable(False)
        #self.caz.Enable(False)
        self.nsrifaz.Show(False)
        self.abl.Show(False)
        self.vANNODA.Enable(False)     
        self.vANNODA.Show(False)
        self.vANNOA.Enable(False)
        self.vANNOA.Show(False)
        self.datac.Enable(False)
        self.cdatac.Enable(False)
        self.datac.SetValue(data)
        self.ANNODA.Enable(False)
        self.SetFocus()
        self.AT_Aziende()
        #self.pwd.SetFocus()
        #self.ok.SetDefault()        
        self.SelCOMBO(self)    
        self.Ute(self)
        self.Azienda(self)
        self.naz.SetFocus()

    def AT_Aziende(self):
        sql = """ select paese from aziende """	
        try:
            cr =  fdb.CnDBAZ.cursor ()
            cr.execute(sql)
            row = cr.fetchone()
        except StandardError, msg:
            dlg = wx.MessageDialog(self, 
                _("Aggiornamento della tabella ......"), 
                _("Aggiornamento Tabella "), wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            #if dlg.ShowModal()==wx.ID_OK: 
            #dlg.Destroy()	    
            import at_aziende
            #self.AggMenu(True,self.IDMENU )
            #wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        fdb.CnDBAZ.commit()

    def SelCOMBO(self, evt):
        vdata = 0
        vANNODA = self.vANNODA.GetValue()
        self.ANNODA.Clear()
        vANNOA = self.vANNOA.GetValue()
        self.ANNOA.Clear()        
        sql = " SELECT * FROM parcon "
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql)  
            while (1):
                row = cr.fetchone ()
                if row == None: 
                    break
                if (row[0]=="ANNODA"):self.sANNODA=row[1] 
                if (row[0]=="ANNOA"):self.sANNOA=row[1]
                if (row[0]=="POSL"):
                    self.npost.SetValue(str(row[1]))
                    self.post.SetValue(str(row[2]).title())
        except StandardError, msg:
            self.__MDI__.MsgErr("selaz","  SelCOMBO Error %s " % (msg)) 
        fdb.CnDBAZ.commit()
        if self.sANNODA =='':self.sANNODA =strftime("%Y")
        if self.sANNOA =='': self.sANNOA =strftime("%Y")
        self.vANNODA.SetValue(self.sANNODA)
        self.vANNOA.SetValue(self.sANNOA)
        self.ANNOcont=self.sANNOA
        cnt = -1
        valore=range(int(self.sANNODA),int(self.sANNOA)+1)
        for x in (valore):
            val = str(x)
            self.ANNODA.Append(val,val)
            self.ANNOA.Append(val,val)
            cnt+=1
        self.ANNOA.Select(cnt)        
        self.ANNODA.Select(0)
        self.ANNOcont = self.vANNOA.GetValue()
        self.datac.SetValue(strftime("%d/%m/")+self.ANNOcont) 

    def SelANNODA(self, evt):
        self.Sel(evt)
        self.vANNODA.SetValue(self.cb_val)

    def SelANNOA(self, evt):
        self.Sel(evt)
        self.vANNOA.SetValue(self.cb_val)
        self.datac.SetValue(strftime("%d/%m/")+self.cb_val) 
        self.ANNOcont=self.vANNOA.GetValue()
        
    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str= evt.GetString()  
        evt.Skip()
        
    def Ute(self, evt):
        cnt_rec = 0
        sql = " SELECT * FROM utenti ORDER BY cod DESC "
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql)   
            while (1):
                row = cr.fetchone()
                if row == None:
                    break
                cnt_rec+=1
                self.nute.SetValue(str(row[0]))
                self.ute.SetValue(str(row[1]).title())
                self.sel_pwd = str(row[2])
        except StandardError, msg:
            self.__MDI__.MsgErr("selaz"," Ute Error %s " % (msg)) 
        fdb.CnDBAZ.commit()
        if cnt_rec>1:
            self.nute.Enable(True)
            self.cute.Enable(True)
            self.ute.Enable(True)
            self.pwd.Enable(True)
            self.nute.SetFocus()
        else:    
            self.nute.Enable(False)
            self.cute.Enable(False)
            self.ute.Enable(False)
            self.pwd.Enable(False)
            self.naz.SetFocus()
        
    def Azienda(self, evt):
        cnt_rec=0
        sql = " SELECT * FROM aziende ORDER BY cod DESC "
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql)               
            while (1):
                row=cr.fetchone()
                if row == None:
                    break
                cnt_rec+=1
                self.naz.SetValue(str(row[1]))
                self.az.SetValue(str(row[3]).title())
                self.rifaz = str(row[5]).title()
                self.nsrifaz.SetValue(str(row[5]).title())
                self.abl.SetValue('6')
        except StandardError, msg:
            self.__MDI__.MsgErr("selaz"," Azienda Error %s " % (msg)) 
        fdb.CnDBAZ.commit()
        if cnt_rec>1:
            self.naz.Enable(True)
            self.caz.Enable(True)
            self.az.Enable(True)
            self.naz.SetFocus()
            if self.rifaz=='' or self.rifaz=='None':
                sel.az.Show(True)
                self.nsrifaz.Show(False)
            else :
                self.az.Show(False)
                self.nsrifaz.Show(True)
        else:
            self.naz.Enable(False)
            self.caz.Enable(False)
            self.az.Enable(False)
            self.ANNOA.SetFocus()
            
    def FndAZ(self, evt):
        cnt_rec = 0
        cod = int(self.naz.GetValue())
        sql = " SELECT * FROM aziende WHERE cod = '%s' "
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql % cod)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("selaz"," FndAZ Error %s " % (msg)) 
        fdb.CnDBAZ.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,ttlaz)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAz(row)


    def FndSelAz(self, evt):
        row = evt
        self.naz.SetValue(str(row[1]))
        if row[5]=='' or row[5]=='None':
            sel.az.Show(True)
            self.nsrifaz.Show(False)
        else :
            self.az.Show(False)
            self.nsrifaz.Show(True)
        self.az.SetValue(str(row[3]).title())
        self.nsrifaz.SetValue(str(row[5]).title())
        self.rifaz =str(row[5]).title()
        self.rs1az=str(row[3]).title()
        self.rs2az=str(row[4]).title()
        self.indaz=str(row[6]).title()
        self.capaz=str(row[7])
        self.locaz=str(row[9]).title()
        self.praz=str(row[10]).upper()
        self.urlaz=str(row[22])
        self.emailaz=str(row[23])
        self.cfaz=str(row[24])
        self.pivaaz=str(row[25])
        self.telaz=str(row[19])
        self.faxaz=str(row[21])
        self.rea=str(row[34])
        self.abl.SetValue(str(row[35])[:1]) 
        self.ANNOA.SetFocus()
      
    def OnClose(self, evt): 
        #self.Destroy()
        #self.__MDI__.Destroy()
        self.GetParent().Close(None)
            
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttlaz,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
  
    def SelUte(self, evt):
        pass
 
    def OnOk(self, evt):
        if strftime("%Y") < self.ANNOcont : 
            self.vANNODA.SetValue(self.ANNOcont)
            self.vANNOA.SetValue(self.ANNOcont)
            self.ANNODA.SetValue(self.ANNOcont)
            self.ANNOA.SetValue(self.ANNOcont)

        gma= self.datac.GetValue().split('/')
        AA = gma[2]
        if self.ANNOA.GetValue() != self.ANNOcont or AA != self.ANNOcont :
            self.Message('" '+ AA +' "  ' + cfg.msgdatacont,ttlaz)
            self.ANNOA.SetFocus()
        else : self.Save(self)
  
    def Save(self, evt):
        self.FndAZ(self)
        cnt_pwd = 0
        rs1az = self.rs1az
        rs2az = self.rs2az
        indaz = self.indaz   
        capaz = self.capaz
        locaz = self.locaz
        praz = self.praz
        urlaz = self.urlaz
        emailaz = self.emailaz
        rea = self.rea
        cfaz = self.cfaz
        if cfaz == '' or cfaz == 'None' : cfaz = '-'
        cfaz = '%-16.16s' % cfaz
        pivaaz = self.pivaaz
        if pivaaz == '' or pivaaz == 'None' : pivaaz = '-'
        pivaaz = '%-11.11s' % pivaaz
        telaz = self.telaz
        faxaz = self.telaz
        pwd = self.pwd.GetValue().strip()
        nute = self.nute.GetValue()
        ute = self.ute.GetValue()
        naz = self.naz.GetValue()
        az = self.az.GetValue()
        abl = self.abl.GetValue()

        datac = self.datac.GetValue()
        val_az = "Az"+naz+".db"
        npost = self.npost.GetValue()
        post = self.post.GetValue()
        val_hstaz = cfg.path_db+val_az
        val_annoa = self.vANNOA.GetValue()
        val_annoda = self.vANNODA.GetValue()
        if val_annoda > val_annoa : val_annoda = val_annoa
        annoc = val_annoa       
        cod = 'POSL'+ nute
        vparcon = cod,'','',val_annoda,val_annoa,datac,'','',int(naz),0,0.0,0.0
        sql = " DELETE FROM parcon WHERE cod = '%s' "
        #print sql % cod
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql % cod)  
        except StandardError, msg:
            self.__MDI__.MsgErr("selaz"," Dele paracon Error %s " % (msg)) 
        fdb.CnDBAZ.commit()
        sql = """ INSERT INTO parcon 
                  VALUES('%s','%s','%s','%s','%s','%s',
                         '%s','%s','%s','%s','%s','%s') """
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql % vparcon)  
        except StandardError, msg:
            self.__MDI__.MsgErr("selaz"," Ins paracon Error %s " % (msg))
        fdb.CnDBAZ.commit()
        #self.AggMenu(True,self.IDMENU) 
        prmaz = annoc+':'+nute+':'+naz+':'+datac
        prm = longversion+';'+annoc+';'+self.rifaz+';'+ute+';'+az+';'+ prmaz       
        self.SetTTL(prm)  
        #self.GetParent().SashMDIon()
        self.__MDI__.SashMDIon()
        #self.__MDI__.SetStatusText("")
        #self.__MDI__.fmenubar(True)
        #self.__MDI__.ftoolbar(True)
        #self.__MDI__.SetStatusText("Azienda: "+az, 1)
        #self.__MDI__.SetStatusText("Operatore: "+ute, 2)
        #self.__MDI__.SetStatusText("Anno contabile: "+annoc, 3)
        #self.__MDI__.selazon=False  	
        #self.Destroy()
        #import add_scad
        #import at_movcon_2
        #import ImpMovMag


