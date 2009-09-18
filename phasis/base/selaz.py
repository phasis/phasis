# Copyright (C) 2003 - 2006  Phasis - http://www.phasis.it/
#
# Developer:
# Massimo Gerardi <m.gerardi@seeopen.it>
# Daniele Cicchinelli <d.cicchinelli@seeopen.it>
# Alessandro Satanassi <alessandro@cittini.it>
#
#
# Released under the terms of the GNU General Public License
# (version 2 or above)
#
# See COPYING for details.

#

import wx
from ncontrols import *
import cfg
import time
import gettext
_ = gettext.gettext


data = time.strftime("%d/%m/%Y")
ttlaz = _("Selezione Azienda")

def create(parent,titolo,tcpart,nome):
    return SelAzienda (parent,titolo,tcpart,nome)

class SelAzienda(wx.ScrolledWindow):
    def __init__(self, prnt, titolo,tcpart,nome):
        selazDialog=wx.ScrolledWindow.__init__(self, parent=prnt,id = -1)# , size = self.GetMaxSize())
        #name=nome,
        #      pos=wx.Point(0, 0), size=wx.Size(420, 325),  
        #      style=wx.CAPTION|wx.STAY_ON_TOP|wx.SYSTEM_MENU , title=titolo)
        #self.SetIcon(wx.Icon(cfg.path_img + "phasis.ico", wx.BITMAP_TYPE_ICO))
        #self.SetIcon(wx.Icon(cfg.path_img + "null.ico", wx.BITMAP_TYPE_ICO))
        #self.CentreOnParent()
        #self.CenterOnScreen(wx.BOTH)
        #self.SetSize(self.GetMaxSize())
        self.SetScrollbars(1,1,100,100)
        #self.FitInside()

        self.selaz=panel_selaz(self)
        #self.selaz.SetSize(self.selaz.GetBestSize())
        self.selaz.SetBackgroundColour(wx.LIGHT_GREY) #wx.Colour(255, 0, 0))
        #self.selaz.SetForegroundColour(wx.BLACK)        
        #self.selaz.SetWindowStyleFlag(wx.SUNKEN_BORDER)
        #self.selaz.Refresh()
        # wx.StaticBox(self.selaz, -1, "",(0,0), self.selaz.GetSize())

        # box = wx.StaticBox(self.selaz, -1, "Login",size=self.selaz.GetSize())
        #bsizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        #bsizer.Add(self.selaz, 0, wx.TOP|wx.LEFT, 10)


        
        '''
        self.selaz=panel_selaz(self)
        self.selaz.SetSize(self.selaz.GetBestSize())
        '''
        #self.FitInside()
        
        #box = wx.BoxSizer(wx.VERTICAL)
        box = wx.GridSizer(1, 1)
        #box.Add(SampleWindow(win, "two"), 0, wx.ALIGN_CENTER)        
        # #######
        # box.Add(bsizer, 0, wx.ALIGN_CENTER)     
        box.Add(self.selaz, 0, wx.ALIGN_CENTER|wx.ALL,10)     
        
        self.SetSizer(box)
        #box.LayOut()
        #self.Fit()
        #self.CenterOnScreen(wx.BOTH)
        #self.Center(wx.BOTH)

        self.selaz.ute.SetValue(int(util.LoadLastValue('selaz_ute',utente=0)))
        self.selaz.az.SetValue(int(util.LoadLastValue('selaz_az',utente=0)))
        
        self.OnChangeAzienda(0)
        
        self.Bind(wx.EVT_TEXT_ENTER, self.EvtEnter,self.selaz.pwd)
        self.selaz.pwd.SetFocus()
        
        """ In attesa di istruzioni viene settata l'azienda dal combo box.        
        """
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.selaz.ok)
        self.Bind(wx.EVT_BUTTON, self.OnEsci, self.selaz.canc)
        self.Bind(wx.EVT_COMBOBOX,self.OnChangeAzienda,self.selaz.az)
        #self.Bind(wx.EVT_CLOSE, self.OnEsci)
        
    def EvtEnter(self, evt):
        self.OnOk(None)
    
    def OnOk(self,event):
        
        codice_utente=self.selaz.ute.GetValue(format=False)
        dati_utente=util.eseguiSql("SELECT ute,pwd,abl FROM utenti WHERE cod = %s"%codice_utente,0,
                                connection=self.GetParent().GetConnDbAz())
        
        #nome_utente=dati_utente[0]
        #password=dati_utente[1]
        #abilitazione=dati_utente[2]
       
        if self.selaz.pwd.GetValue(format=False)==dati_utente['PWD']:
            #mdi=self.GetParent()
            #SetAzienda(
            
            self.GetParent().SetDataContabile(self.selaz.datac.GetValue().Format('%d/%m/%Y'))#format=False))
            
            anno= self.selaz.anno_a.GetValue(format=False)
            if not anno:anno=time.strftime("%Y")
            self.GetParent().SetAnnoCompetenza(anno)
            self.GetParent().SetUtente(codice_utente,dati_utente['UTE'],dati_utente['ABL'])
            self.GetParent().SetAzienda(self.selaz.az.GetValue(format=False))#codice azienda
            '''
            self.GetParent().SetStatusText("")
            self.GetParent().fmenubar(True)
            self.GetParent().ftoolbar(True)
            self.GetParent().SetStatusText(anno, 1)
            
            rif_az = self.GetParent().GetAzienda("rifaz")
            if rif_az == '' or rif_az == 'None': 
                rif_az = self.GetParent().GetAzienda("rs1az")            
            
            self.GetParent().SetStatusText(rif_az,2)
            self.GetParent().SetStatusText(dati_utente['UTE'], 3)
            self.GetParent().selazon=False
            #self.GetParent().SashMDIon()
            '''
            

            self.OnClose(0)
        else:
            util.alert(self,_("Password errata"),"Autenticazione fallita !!")
            self.selaz.pwd.SetValue('')
            #self.selaz.pwd.SetSelection(-1,-1)
            self.selaz.pwd.SetFocus()
        
    def OnChangeAzienda(self,event):
        # una idea
        cod_az= self.selaz.az.GetValue(format=False)
        ####db=cfg.path_db+"az000"[:-len(str(cod_az))]+str(cod_az)+".db"
        ####conn=util.conn(db)
        ####self.selaz.anno_a.SetNProperty("SELECT anno FROM docu1 GROUP BY anno",
        ####                                connessione=conn)
        # si posiziona sull'ultimo elemento
        ###self.selaz.anno_a.SetSelection(self.selaz.anno_a.GetCount()-1)
        # anno ,il primo elemento
        anno_da="2006" #self.selaz.anno_a.GetString(0)
        self.selaz.anno_da.SetValue(anno_da)
        self.selaz.anno_a.SetValue(anno_da)

    def OnClose(self,evt):
        util.StoreLastValue('selaz_az',self.selaz.az.GetValue(format=False),utente=0)
        util.StoreLastValue('selaz_ute',self.selaz.ute.GetValue(format=False),utente=0)
        self.GetParent().SashMDIon()
        #self.Destroy()

    def OnEsci(self,evt):
        #self.Destroy()
        self.GetParent().Close(None) #Destroy()

class panel_selaz(nPanel):
    def __init__(self,parent):
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))        
        nPanel.__init__(self, parent=parent, id=-1, name='', 
              pos=wx.Point(0, 0), size=parent.GetSize())
        self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
                
        wx.StaticText(self, -1, _("Azienda:"), wx.DLG_PNT(self, 5,12))
        self.az = nComboBox(self, -1, "", wx.DLG_PNT(self, 50,10), 
              wx.DLG_SZE(self, 150,-1))
        #carico la lista delle aziende
        self.az.SetNProperty("SELECT rag_soc1,cod FROM aziende ",
                connessione=self.GetGrandParent().GetConnDbAz())
        
        wx.StaticText(self, -1, _("Postazione:"), wx.DLG_PNT(self, 5,27))
        self.post = nComboBox(self, -1, "",
                      wx.DLG_PNT(self, 50,25), wx.DLG_SZE(self, 150,-1))        
        self.post.Enable(False,ALL_CONTROL)
        
        wx.StaticText(self, -1, _("Operatore:"), wx.DLG_PNT(self, 5,42))
        self.ute = nComboBox(self, -1, "",
                      wx.DLG_PNT(self, 50,40), wx.DLG_SZE(self, 150,-1),[], 
              wx.TE_PROCESS_ENTER )    
 
        self.ute.SetNProperty("SELECT UTE, cod  FROM utenti",
                            connessione=self.GetGrandParent().GetConnDbAz())
        
        wx.StaticText(self, -1, _("Password :"), wx.DLG_PNT(self, 5,57))
        self.pwd = nTextCtrl(self, -1, "",
                      wx.DLG_PNT(self, 50,55), wx.DLG_SZE(self, 47,-1),
                      wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        
        
        wx.StaticText(self, -1, _("Anni Competenza :"), wx.DLG_PNT(self, 5,72))
        self.anno_da = nTextCtrl(self, -1, "",
              wx.DLG_PNT(self, 75,70), wx.DLG_SZE(self, 35,-1))
        self.anno_da.Enable(False,ALL_CONTROL) 
        #self.anno_da.SetValue(util.eseguiSql(sql))
                                     
        wx.StaticText(self, -1, "/", wx.DLG_PNT(self, 112,72))
        self.anno_a = nComboBox(self, -1, "", wx.DLG_PNT(self, 117,70), 
              wx.DLG_SZE(self, 35,-1), [], 
              wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER ) 
        self.anno_a.Enable(False,ALL_CONTROL) 
        #self.anno_a.SetNProperty(sql)        
        self.abl = nGenControl(self)
        wx.StaticText(self, -1, _("Data di Lavoro :"), wx.DLG_PNT(self, 5,87))        
        self.datac  = wx.DatePickerCtrl(self, pos=wx.DLG_PNT(self, 75,85),
                                        size= wx.DLG_SZE(self, 80,-1),
                                        style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY | wx.TE_PROCESS_ENTER)      

        self.ok = wx.Button(self, -1,_("Accedi"), wx.DLG_PNT(self, 45,110), 
              wx.DLG_SZE(self,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self, -1,_("Esci"), wx.DLG_PNT(self, 110,110), 
              wx.DLG_SZE(self,cfg.btnSzeLH,cfg.btnSzeV))      

