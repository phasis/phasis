# Project       Phasis
#
# Description
# Gestionale Aziendale Open Source Phasis (R)
#
#*  Copyright (C) 2003, 2004, 2005, 2006, 2007, 2008, 2009
#   See Open - http://www.seeopen.it/
#   Author: Massimo Gerardi <massimog@seeopen.it>
#                           <gnumagnu@gmail.com>
#   Via Michele Rosi 184 - Aranova (Roma)
#   00050 Aranova (Roma) - Italy
#   tel. +39 06 6674756 - fax +39 06 90280221
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   www.phasis.it - info@phasis.it 
#


import wx
import wx.lib.buttons as buttons
import shutil
import os
import sys
from cfg import *
import cfg
from copyright import longversion
import util
import locale
import time
import selaz
#locale.setlocale(locale.LC_MONETARY, '')
import anag
import FlatNotebook as FNB
import fpformat

# <m.gerardi>
LC_M = locale.localeconv()
LC_M['grouping'] = [3,3,0]
LC_M['thousands_sep'] = '.'
LC_M['decimal_point'] = ','
locale.localeconv = lambda: LC_M
# <m.gerardi>

MENU_EDIT_DELETE_PAGE = wx.NewId()
LISTA_MODULI_APERTI = wx.NewId()
DAFRAMEATAB = wx.NewId()



def create():
    return MDIPhasis()
     
class MDIPhasis(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, '', pos=wx.DefaultPosition, 
              size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE)
        self.SetMinSize((640,480))
        self.SetIcon(wx.Icon(cfg.path_img + "phasis.ico", wx.BITMAP_TYPE_ICO))
        self.SetSize(self.GetMaxSize())        
        self.Centre(wx.BOTH)
        self.selazon=True
        self.fstatusbar(True)
        self.notepageID=[]
        self.notepageObj=[]
        self.frampageID=[]
        self.frampageObj=[]
        self.frampageFra=[]
        #self.buttonsbar=[]
        self.destro=True
        self.flagcolmod=cfg.FLAGCOLORPANEL
        self.backcolMDI=cfg.SFONDOCOLOR
        self.backcolmod=cfg.PANELCOLOR
        
        self.SetBackgroundColour(self.backcolMDI)
        
        self.toolbarShow=cfg.toolbar
        self.buttonsbarShow=cfg.buttonsbar
        
        # <daniele>
        # questo serve per la stampa,ad azzerare il pid di acrobat reader
        f = open(cfg.path_tmp + "pid","w")
        f.write("0")
        f.close()
        # </daniele>              
      
        ######################### impostazione font
        self.font = wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False)
        #self.font=wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
        y=wx.ScreenDC().MaxY()
        if y>=1200 : numfont=16
        elif y>=1024 : numfont=14
        else : numfont=12
        if cfg.FONTFISSO!=0 : numfont=cfg.FONTFISSO
        self.font.SetPointSize(numfont)
        self.SetFont(self.font)      
        #################################        
        # <daniele>
        self.__database_azienda=None   # nome e path database azienda 
        self.__dati_azienda =None  # dizionario dati azienda
        self.__cod_utente=0  # codice utente
        self.__nome_utente=None  # nome utente
        self.__abilitazione=0  # abilitazione dell'utente 
        self.__data_contabile=None  # data contabile
        self.__anno_competenza=None  # anno di competenza
        # </daniele>
        self.__AnnoC__ = 0 # tenuto per retrocompatibilita' con la 0.9.7, poi eliminare
        self.Bind(wx.EVT_CLOSE, self.Close)  #EVT_CLOSE(self, self.Close)
        self.Bind(wx.EVT_MENU, self.OnMenu)
        self.CreateRightClickMenu()
        #accell=wx.AcceleratorTable([(wx.ACCEL_CTRL, wx.WXK_TAB,LISTA_MODULI_APERTI)])  # CTRL-L - ultimo parametro e' l'ID menu
        self.accellentry=[]
        self.accellentry.append(wx.AcceleratorEntry(wx.ACCEL_CTRL,ord('Y'),LISTA_MODULI_APERTI))
        #accell=wx.AcceleratorTable([(wx.ACCEL_CTRL,ord('Y'),LISTA_MODULI_APERTI)])
        accell=wx.AcceleratorTable(self.accellentry)
        self.SetAcceleratorTable(accell)
        self.icolistctrl = wx.ImageList(16, 16)
        self.icowin = self.icolistctrl.Add(wx.Image(cfg.path_img+"icowin.png").ConvertToBitmap())
        self.icotab = self.icolistctrl.Add(wx.Image(cfg.path_img+"icotab.png").ConvertToBitmap())
  
    def fstatusbar(self,evt):
        self.statusbar=self.CreateStatusBar(5)
        self.statusbar.SetStatusWidths([-6,-4,-4,-3,130])
        self.statusbar.SetFont(wx.Font(10,wx.SWISS,wx.NORMAL,wx.NORMAL,False))
        bmp = wx.Image(cfg.path_img+"phasis_ico.png").ConvertToBitmap()
        x,y=self.statusbar.GetSizeTuple()
        self.statusicon = wx.StaticBitmap(bitmap=bmp,
              id=-1, name='staticicon',
              parent=self.statusbar, pos=wx.Point(4, (y-16)/2), size=wx.Size(16, 16),
              style=0)
        self.timer = wx.Timer(self)
        self.timer.Start(60000L)
        self.Notify(None)
        self.Bind(wx.EVT_TIMER, self.Notify)         

    def Notify(self,evt):
        t = time.localtime(time.time())
        st = time.strftime(" %d/%m/%Y  %H:%M", t)
        self.SetStatusText(st, 4)

    def fmenubar(self,evt):
        if evt==True: 
            #visualizza il menu
            menubar = wx.MenuBar() 
            abl = '' #int(fdb.abl)
            if abl=='': abl = 3            
            self.dzMENU = cfg.MENU
            self.lstMENUbar = cfg.MENUbar
            for k in self.lstMENUbar :
                vccMENU = self.dzMENU[k[0]]               
                self.menu = wx.Menu()      
                self.submenu = wx.Menu()       
                for ID in vccMENU:
                    vcMENU=ID[1:]
                    if vcMENU[7] == '-':
                        self.menu.AppendSeparator()
                    elif vcMENU[7] == 'sub':
                        mnItem1 = wx.MenuItem(self.submenu, ID[0], vcMENU[0],
                        vcMENU[1])
                        self.submenu.AppendItem(mnItem1)
                        if (int(vcMENU[5])>abl):
                            self.submenu.Enable(ID[0],False)
                    elif vcMENU[7] == '+':
                        self.menu.AppendMenu(ID[0], vcMENU[0], self.submenu)
                        if (int(vcMENU[5])>abl):self.menu.Enable(ID[0],False)
                    else:
                        mnItem = wx.MenuItem(self.menu, ID[0], vcMENU[0], 
                        "         "+vcMENU[1])
                        self.menu.AppendItem(mnItem)
                        if (int(vcMENU[5])>abl):self.menu.Enable(ID[0],False)
                menubar.Append(self.menu, k[1])
            self.menubar=menubar
            lstMENU = []
            for k in MENU.keys():
                for kk in MENU[k]:
                    lstMENU.append((kk[0],kk[1:]))
            self.vcMENU = dict(lstMENU)
            self.SetMenuBar(self.menubar)
            #accell=wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('Y'),LISTA_MODULI_APERTI)])  # CTRL-L - ultimo parametro e' l'ID menu
            #self.SetAcceleratorTable(accell)
        else:
            #cancella il menu
            self.SetMenuBar(None) #wx.MenuBar())
            self.menubar.Destroy()

    def ftoolbar(self,evt):    
        if self.toolbarShow==1:
            if evt==True:        
                # Crea toolbar
                self.toolbar = self.CreateToolBar(wx.TB_HORIZONTAL |
                                                wx.NO_BORDER | wx.TB_FLAT)
                self.toolbar.SetToolBitmapSize(wx.Size(32,32))
                keys=TOOLBAR
                IDD=0
                IDDLEN=len(keys)
                while IDD < IDDLEN :
                #for IDD in keys:
                    sTOOLB = string.split(TOOLBAR[IDD][1],"|")
                    if sTOOLB[0]=='-':
                        self.toolbar.AddSeparator()
                    else:
                        self.toolbar.AddSimpleTool(TOOLBAR[IDD][0],wx.Bitmap(cfg.path_img+sTOOLB[0],wx.BITMAP_TYPE_PNG), sTOOLB[1])
                    if (sTOOLB[5]=="N"):self.toolbar.EnableTool(TOOLBAR[IDD][0],False)
                    IDD=IDD + 1
                self.toolbar.Realize()
            else:
                #cancella toolbar
                self.toolbar.Destroy()
    
    def GetConnAz(self):     
        return cfg.path_db+ self.__database_azienda #self.__ConnAZ__  
 
    def GetConnDbAz(self):   
        """ Ritorna la connessione al database aziende.
        """  
        return util.conn(cfg.path_db+"dbaz.db") #self.__ConnDBAZ__   
                
    def SetAzienda(self,cod_azienda):
        """ Qui arriva il codice azienda viene settato il nome e il percorso
            del database da usare.
        """
        self.__database_azienda = "az000"[:-len(str(cod_azienda))] +\
              str(cod_azienda)+".db"
        lAZ = util.eseguiSql("SELECT * FROM aziende WHERE cod=%s" % cod_azienda,
              connection=self.GetConnDbAz())[0]

        self.__dati_azienda = {
               'rs1az':lAZ[3],
               'rs2az':lAZ[4],
               'indaz':lAZ[6],
               'capaz':lAZ[7],
               'locaz':lAZ[9],
               'praz':lAZ[10],
               'urlaz':"Url: http://" + lAZ[22],
               'emailaz':"Email: " + lAZ[23],
               'cfaz':"Cod. Fisc : " + lAZ[24],
               'pivaaz':"P.IVA : " + lAZ[25],
               'rifaz':lAZ[5],
               'telaz':lAZ[18],
               'faxaz':lAZ[21],
               'rea':"Rea : " + lAZ[34],
               'rsaz':lAZ[3] + " " + lAZ[4],
               'cap_ind_pr':lAZ[6]+ " " +lAZ[7]+ " " +lAZ[9]+ " " +lAZ[10],
               'piva_cfaz':"P.IVA: " +lAZ[25] + " Cod. Fisc.: " + lAZ[24],
               'tel_faxaz':"Tel.: " +lAZ[18] + " Fax: " + lAZ[21],
               'email_urlaz':"e-mail: " + lAZ[23] + " " + lAZ[22],
               'datacon':self.__data_contabile
            }

        rif_az = self.__dati_azienda["rifaz"]
        if rif_az == '' or rif_az == 'None': 
            rif_az = self.__dati_azienda["rs1az"]
        self.SetTitle("%s    "+_("Anno Contabile :")+" %s    %s  -  "+_("Operatore :")+" %s"%
                (longversion,self.__anno_competenza,rif_az,self.__nome_utente))
                
    def GetAzienda(self,voce=None):
        """ Informazioni sull'azienda restituisce il valore della chiave 
            richiesta o tutto.
        """
        if voce:
            ret=self.__dati_azienda[voce]
        else:
            ret=self.__dati_azienda
        return ret

    
    def SetUtente(self,cod_utente,nome_utente,abilitazione):
        self.__cod_utente=cod_utente
        self.__nome_utente=nome_utente
        self.__abilitazione=abilitazione
       
    def GetUtente(self):
        return (self.__cod_utente,self.__nome_utente,self.__abilitazione)
    
    def SetDataContabile(self,data_contabile):
        # data contabile
        self.__data_contabile=data_contabile


    def GetDataContabile(self):
        # data contabile
        return self.__data_contabile
  
  
    def SetAnnoCompetenza(self,anno_competenza):
        # anno di competenza 
        self.__anno_competenza=anno_competenza


    def GetAnnoCompetenza(self):
        return self.__anno_competenza

    #========================================================       
    # tenuti per retrocompabilita' con la 0.9.7, poi da eliminare    
    
    def SetTTL(self, EVT):
        prm = string.split(EVT,";")
        VERS = prm[0]
        annoa = prm[1]
        rifaz = prm[2]
        ute = prm[3]
        az = prm[4]
        prmaz = prm[5]

        if rifaz=='' or rifaz=='None': rifaz = az
        self.SetTitle(VERS + '    '+ _('Anno Contabile :')+' ' + annoa +\
                    '    ' + rifaz +'  -  '+ _('Operatore :')+' '+ ute )
        
        annoc = string.split(prmaz,':')[0]
        naz = string.split(prmaz,':')[2]
        self.naz = naz
        datac = string.split(prmaz,':')[3]

        self.__DataC__ = datac
        self.__AnnoC__ = annoc
        import fdb
        self.__ConnAZ__ = fdb.CnAz(naz)
        ##self.__ConnDBAZ__ = fdb.CnDBAZ()
        self.__dzAZ__ = fdb.dzAz(naz)
        self.__Ute__ = ute
        self.__az__ = az

        lAZ = self.__dzAZ__ 

        self.dzDatiAzienda = {
              'rs1az':lAZ[0],
              'rs2az':lAZ[1],
              'indaz':lAZ[2],
              'capaz':lAZ[3],
              'locaz':lAZ[4],
              'praz':lAZ[5],
              'urlaz':"Url: http://" + lAZ[6],
              'emailaz':"Email: " + lAZ[7],
              'cfaz':"Cod. Fisc : " + lAZ[8],
              'pivaaz':"P.IVA : " + lAZ[9],
              'rifaz':lAZ[10],
              'telaz':lAZ[11],
              'faxaz':lAZ[12],
              'rea':"Rea : " + lAZ[13],
              'rsaz':lAZ[0] + " " + lAZ[1],
              'piva_cfaz':"P.IVA: " +lAZ[9] + " Cod. Fisc.: " + lAZ[8],
              'tel_faxaz':"Tel.: " +lAZ[11] + " Fax: " + lAZ[12],
              'email_urlaz':"e-mail: " + lAZ[7] + " " + lAZ[6],
              'datacon':datac,
               'cap_ind_pr':lAZ[14],
              'zona':lAZ[15],
              'ind_cap_loc_pr':lAZ[16],
              'ind_cap_loc_pr1':lAZ[17],
              'banca':lAZ[18],
              'iban':lAZ[19],
              'ind1':lAZ[20],
                }   

    def GetConnAZ(self):     
        return self.__ConnAZ__  
 
    def GetConnDBAZ(self):     
        return self.__ConnDBAZ__   
            
    def GetAnnoC(self):     # anno competenza
        return self.__AnnoC__   

    def GetDataC(self):     # data contabile
        return self.__DataC__   
    
    def GetdzAZ(self):     # dati azienda completi
        return self.__dzAZ__    

    def SelAnnoC(self, EVT):  
        annoc = self.__AnnoC__ 
    #===================================================================

    
    def Selaz(self):
        if len(self.notepageID)> 0 or len(self.frampageID)>0 :
            #wx.GetApp().SetTopWindow(self.winMDI)
            chiudi=util.ask(self,
            _("Per terminare la sessione devi prima chiudere tutti i moduli attivi")+"\n"+
            _("Sono ancora aperte ") + str(len(self.notepageID)) + _(" schede e ") + str(len(self.frampageID))+
            _(" finestre") + "\n" + _("Vuoi chiudere tutti i moduli attivi automaticamente ?"), _("Attenzione !!!"))
            if (chiudi==True) :
                 
                id=len(self.notepageID)           
                while id>0 :
                    id=id-1
                    new = self.notebook_1.GetSelection()      # codice ripetuto
                    if new!=id :
                        aux=self.notepageObj[new]
                        aux.Hide()
                        self.sizer_6.Detach(aux)
                        topo=self.notepageObj[id]
                        self.sizer_6.Add(topo, 1, wx.EXPAND, 0)
                        topo.Show(True)
                        self.sizer_6.Layout()
                        self.notebook_1.SetSelection(id)        # fine codice ripetuto
                    aux=self.notepageObj[id]
                    aux.SetFocus()  # boh, forse utile                  
                    aux.Close(False) #aggiunto None per retro 0.9.7.
                id=len(self.frampageID)           
                while id>0 :
                    id=id-1
                    finestra=self.frampageFra[id]  #codice ripetuto
                    finestra.Iconize(False)
                    finestra.Raise()
                    finestra.SetFocus()            #fine codice ripetuto
                    finestra.Close(False) # aggiunto None per retro 0.9.7
        if len(self.notepageID) == 0 and len(self.frampageID) == 0 :
            if self.selazon==False: 
                self.BackUp(self)
                self.win_logo_MDI.Hide()
                self.sizer_6.Detach(self.win_logo_MDI)
                self.win_logo_MDI.Destroy()
                #self.sizer_1.Destroy()
                #self.sizer_2.Destroy()
                #self.sizer_4.Destroy()        
                #self.sizer_3.Destroy()        
                #self.sizer_6.Destroy()
                #self.sizer_5.Destroy()
                self.notebook_1.Destroy()
                self.winMDI.Destroy()              
                self.ftoolbar(False)
                self.fmenubar(False)
                self.SetStatusText("", 1)
                self.SetStatusText("", 2)
                self.SetStatusText("", 3)
            self.selazon=True
            self.SetStatusText("        "+_("Seleziona Azienda"))
            self.SetTitle(longversion)
            # === per retrocompatibilita' con la 0.9.7
            rec = self.SetTTL #per retrocompatibilita' con la 0.9.7. poi da eliminare
            control = [_("Seleziona Azienda"),"Z", rec, self.AggMenu,1031, self.CMD]
            win = selaz.create(self, control)
            # ========== fine per la 0.9.7
            self.win=win
            self.SendSizeEvent()
    
    def trasfotab(self,frame):
        TITOLO=4
        win=frame.child
        id=self.frampageObj.index(win)          
        idwin=self.frampageID[id]         
        win.Reparent(self.window_2_pane_2)
        frame.Destroy()
        self.notepageID.append(idwin)
        self.notepageObj.append(win)
        self.panel_1 = wx.Panel(self.notebook_1, -1,size=(0,0))
        self.notebook_1.AddPage(self.panel_1,self.vcMENU[idwin][TITOLO],select=True)
        del self.frampageObj[id]
        del self.frampageID[id]
        del self.frampageFra[id]
        self.Raise()
        win.SetFocus()
    
    
    def OnMenu(self, EVT):
        self.destro=wx.GetKeyState(wx.WXK_CONTROL)
        PACKAGE=2
        MODULO=3
        TITOLO=4
        ABILITAZIONE=5
        TCPART=6
        rec = ""   
        ID = EVT.GetId()
        if ID==MENU_EDIT_DELETE_PAGE: # e' stato premuto sposta in finestra dai tab
            idtab = self.notebook_1.GetSelection()
            idObj=self.notepageObj[idtab]
            idmenu=self.notepageID[idtab]
            self.sizer_6.Detach(idObj)  #chiamare evento close della finestra       
            del self.notepageObj[idtab]
            del self.notepageID[idtab]
            self.chiuditab=True
            self.notebook_1.DeletePage(idtab)
            if len(self.notepageObj)==0 :
                self.notebook_1.Show(False)
                self.sizer_6.Add(self.win_logo_MDI, 1, wx.EXPAND, 0)
                self.sizer_6.Layout()
                self.win_logo_MDI.Show(True)
                self.winMDI.Layout()
                self.tab=False
            somaro=MyFrame(self.winMDI,-1,self.vcMENU[idmenu][TITOLO])
            idObj.Reparent(somaro)
            somaro.child=idObj
            idObj.GetSizer().Fit(idObj)
            somaro.SetClientSize(somaro.child.GetSize())
            somaro.Centre(wx.BOTH)
            somaro.Refresh()
            somaro.Show(True)
            somaro.child.SetFocus()
            self.frampageID.append(idmenu)
            self.frampageObj.append(idObj)
            self.frampageFra.append(somaro)
        elif ID==LISTA_MODULI_APERTI:
            if len(self.notepageID) > 0 or len(self.frampageID) > 0 :
                NavDialog=AllModulNavigation(self)
                NavDialog.Centre(wx.BOTH)
                IDNavDialog=NavDialog.ShowModal()
                NavDialog.Destroy()
                if IDNavDialog>=0 and IDNavDialog!=wx.ID_CANCEL: self.ProcessCommand(IDNavDialog) #ID_CANCEL=5101
        elif ID <= 10000 :        
            self.IDMENU = ID
            vcMENU = self.vcMENU
            if (str(vcMENU[ID][TCPART])=="CLOSE"): 
                self.Close(None) #self.Selaz()
            elif (str(vcMENU[ID][TCPART])=="ABOUT"): self.About()
            elif (str(vcMENU[ID][TCPART])=="EXEC"): wx.Execute(vcMENU[ID][MODULO])
            elif (vcMENU[ID][6]=="PDF"):
                nomeDoc = cfg.path_work + "manuale-utente.pdf"
                if sys.platform == 'win32':
                    nomeDoc = string.replace(nomeDoc,"/","\\")
                    import _winreg
                    acrobat = _winreg.QueryValue(_winreg.HKEY_CLASSES_ROOT, 
                          'AcroExch.Document\shell\open\command')[1:-6]
                    cmd = '"%s" %s'
                    pid = wx.Execute(cmd % (acrobat,nomeDoc))
                elif wx.Platform == '__WXMAC__':
                    #os.popen("open " + nomeDoc)
                    pid=os.system("open " + nomeDoc)
                    #os.startfile(nomeDoc) #sembra fuznionare solo su window
                else:  pid = wx.Execute("evince " + nomeDoc)            
            elif (vcMENU[ID][TCPART]=="URL"):
                url = vcMENU[ID][MODULO]
                #wx.LaunchDefaultBrowser(url)
                try:
                    import webbrowser        
                except ImportError:
                    wx.MessageBox(_('Attenzione:')+' %s' % url)
                else:
                    webbrowser.open(url)
            else:
                self.CMD(ID,rec,vcMENU[ID][TCPART])                                 

    def AggMenu(self,evt,ID): # poi da eliminare - tenuto per retrocompatibilita' 0.9.7-7
        pass
    
    #self.CMD (rec, vcMENU[ID][2],vcMENU[ID][3],vcMENU[ID][4],vcMENU[ID][6])
    #def CMD(self, rec, Dir, Mod, ttl, cntrp):
    
    def CMD(self, idMenu, rec, cntrp):
        # indici di vcMENU
        PACKAGE=2
        MODULO=3
        TITOLO=4
        ABILITAZIONE=5
        TCPART=6
        TIPO_MODULO=8
        if idMenu in self.frampageID:
            id=self.frampageID.index(idMenu)           
            finestra=self.frampageFra[id]
            if rec !="" :
                if finestra.child.is_look()==False:
                    finestra.child.data_reload(rec,cntrp)
                else:
                    util.alert(self,
                    _("Il modulo ' ")+self.vcMENU[idMenu][TITOLO]+_(" ' e' gia' in uso ed e' BLOCCATO")+
                    _(" in quanto e' attualmente in fase di nuovo inserimento o modifica!!!")+"\n"+
                    _("Per fare in modo che l'operazione abbia successo devi prima sbloccare il modulo") +
                    _(" interrompendo l'inserimento o la modifica in corso"), _("Attenzione !!!"))
            finestra.Iconize(False)
            finestra.Raise()
            finestra.SetFocus()
        elif idMenu in self.notepageID:
            id=self.notepageID.index(idMenu)            
            topo=self.notepageObj[id]
            if rec !="" :
                if topo.is_look()==False:
                    topo.data_reload(rec,cntrp)
                else:
                    util.alert(self,
                    _("Il modulo ' ")+self.vcMENU[idMenu][TITOLO]+_(" ' e' gia' in uso ed e' BLOCCATO")+
                    _(" in quanto e' attualmente in fase di nuovo inserimento o modifica!!!")+"\n"+
                    _("Per fare in modo che l'operazione abbia successo devi prima sbloccare il modulo") +
                    _(" interrompendo l'inserimento o la modifica in corso"), _("Attenzione !!!"))
            new = self.notebook_1.GetSelection()
            if new!=id :
                aux=self.notepageObj[new]
                aux.Hide()
                self.sizer_6.Detach(aux)
                #topo=self.notepageObj[id]
                self.sizer_6.Add(topo, 1, wx.EXPAND, 0)
                topo.Show(True)
                self.sizer_6.Layout()
                self.notebook_1.SetSelection(id)
            self.Raise()
            topo.SetFocus()
        else:  
            if  1 == 1 : #self.__abilitazione >= int(self.vcMENU[idMenu][ABILITAZIONE]):  # poi da rimettere terminata transizione da 0.9.7. a 0.9.8
                if (self.vcMENU[idMenu][MODULO] != ""):
                    wx.BeginBusyCursor()
                    try:
                        print self.vcMENU[idMenu][MODULO]
                        module = __import__(self.vcMENU[idMenu][PACKAGE] +\
                              "." + self.vcMENU[idMenu][MODULO],
                              globals,locals,self.vcMENU[idMenu][MODULO])
                    finally:
                        wx.EndBusyCursor()
                    wx.SafeYield()
                    if self.vcMENU[idMenu][TIPO_MODULO]=="3" :  # frame autonomo
                        control = [self.vcMENU[idMenu][TITOLO],
                                   cntrp,
                                   rec, self.AggMenu, idMenu, self.CMD]
                        win = module.create(self.winMDI, control)
                        win.Centre(wx.BOTH) # poi da togliere - solo per migliore visualizzazione su moduli 0.9.7
                        win.Show(True)
                        self.frampageID.append(idMenu)
                        self.frampageObj.append(win)
                        self.frampageFra.append(win)
                    elif self.vcMENU[idMenu][TIPO_MODULO]=="4" :
                        control = [self.vcMENU[idMenu][TITOLO],
                                   cntrp,
                                   rec, self.AggMenu, idMenu, self.CMD]
                        win = module.create(self.winMDI, control)
                        win.Centre(wx.BOTH)
                        win.ShowModal()
                    elif self.destro==True : #self.vcMENU[idMenu][TIPO_MODULO]=="1": # self.destro==True : #self.vcMENU[idMenu][8]=="0":
                        fram=MyFrame(self.winMDI,-1,self.vcMENU[idMenu][TITOLO])
                        control = [self.vcMENU[idMenu][TITOLO],
                                   cntrp,
                                   rec, self.AggMenu, idMenu, self.CMD]
                        win = module.create(fram, control)
                        ########
                        if self.flagcolmod==1 : win.pnl.SetBackgroundColour(self.backcolmod)
                        #########
                        fram.child=win
                        fram.SetClientSize(fram.child.GetSize())
                        fram.Centre(wx.BOTH)
                        fram.Show(True)
                        fram.child.SetFocus()
                        self.frampageID.append(idMenu)
                        self.frampageObj.append(win)
                        self.frampageFra.append(fram)
                    else: 
                        control = [self.vcMENU[idMenu][TITOLO],
                                   cntrp,
                                   rec, self.AggMenu, idMenu, self.CMD]
                        topo = module.create(self.window_2_pane_2, control)
                        ##############
                        if self.flagcolmod==1 : topo.pnl.SetBackgroundColour(self.backcolmod)
                        #for x in topo.pnl.GetChildren(): x.SetBackgroundColour(self.backcolmod)
                        ##############
                        self.notepageID.append(idMenu)
                        self.notepageObj.append(topo)
                        self.panel_1 = wx.Panel(self.notebook_1, -1,size=(0,0))
                        self.notebook_1.AddPage(self.panel_1,self.vcMENU[idMenu][TITOLO],select=True)
                        self.notebook_1.SetSelection(len(self.notepageID)-1)
                        self.Raise()  #nel caso ci sia sopra un frame
                elif ttl=='title' : pass # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
                else:  
                    util.alert(self,_("Funzione non ancora implementata"))
            else:
                util.alert(self,_("Non sei abilitato all'uso di questa funzione"))

                        
    def Close(self, EVT):
        if self.selazon==True:
            self.win.Destroy()
            self.Destroy()
        else: 
            self.Selaz()  
            
    def BackUp(self, EVT):
        ''' # questa e' la versione della 0.9.8 da ripristinare quando sicuri
        valBU=util.eseguiSql(" SELECT VALORE FROM parcon WHERE COD='BACKUP' ",
             connection=self.GetConnDbAz())[0]
        if valBU[0] == 'Y' : # and cfg.cntDB == 'sqlite' : 
        '''
        cnt_rec = 0
        valBU = ''
        import fdb
        try:
            cr = fdb.CnDBAZ.cursor()
            sql = " SELECT COD,VALORE,DESCRIZ FROM parcon WHERE COD = 'BACKUP' "
            cr.execute(sql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.MsgErr("MdiPhasis"," BackUP Error %s " % (msg)) 
        fdb.CnDBAZ.commit()             

        if (cnt_rec!=0): valBU = row[1]

        if valBU=='Y'and cfg.cntDB=='sqlite' :  # fino a qui e' la versione 0.9.7 da ripristinare quando sicuri          
            PathBak = cfg.path_budb
            try:
                week = strftime("%a")
                month = strftime("%b")
                PathBakW = cfg.path_budb+'data.'+week+'/'
                if (os.path.exists (PathBak) == False): os.mkdir(PathBak)
                if (os.path.exists (PathBakW) == False): os.mkdir(PathBakW)
                dstnameaz = PathBakW+'az00' + self.naz + '.db'
                srcnameaz = os.path.join (cfg.path_db + 'az00' + self.naz + '.db')
                dstnamedbaz = PathBakW + 'dbaz.db'
                srcnamedbaz=os.path.join (cfg.path_db + 'dbaz.db')                
                shutil.copyfile(srcnameaz,dstnameaz)
                shutil.copyfile(srcnamedbaz,dstnamedbaz)
            except (IOError, os.error):
                pass

    def MsgErr(self, mod, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        ute = 'NULL'
        data = 'NULL'
        try:
            ute = self.__Ute__
            data = self.__DataC__
        except AttributeError: 
            pass
        t = time.localtime(time.time())	    
        st = time.strftime(" %d/%m/%Y  %H:%M", t)
        ferr = open (cfg.path_logs+ "err_" + mod +".log","a")
        err = st + "  " +  evt + "  " + ute
        print err            
        ferr.write(err+'\n')
        ferr.close()

    def CnvPM(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        self.val = "0"
        if evt=='FC' or evt=='E74' or evt=='E72' or evt=='20C' : evt = "0"
        #if evt=='FC': evt = 0
        if(evt!=""):  ####
            vl = evt.replace(".","")  ####
            val = vl.replace(",",".")  ####
            self.val = fpformat.fix(val,2)  ####
            #print '-'+ val + '-'
            #if val!="": 0
            self.val = float(val)  ####            

    def CnvPM5(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        self.val = "0"
        if(evt!=""):
            vl = evt.replace(".","")
            val = vl.replace(",",".")
            self.val = fpformat.fix(val,cfg.cdec)
            self.val = float(val)
 
    def CnvPMQT(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        self.val = "0"
        if(evt!=""):
            vl = evt.replace(".","")
            val = vl.replace(",",".")
            self.val = fpformat.fix(val,cfg.cdecQT)
            self.val = float(val)

    def CnvPMPZ(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        self.val = "0"
        if(evt!=""):
            vl = evt.replace(".","")
            val = vl.replace(",",".")
            self.val = fpformat.fix(val,cfg.cdecPZ)
            self.val = float(val)
            
    def CnvVM5(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        #print evt
        val = float(evt)
        self.val = locale.format("%." + str(cfg.cdec) + "f",val,1)
        if (self.val=='0,00' or self.val=='0,000'  or self.val=='0,0000'  
           or self.val=='0,00000' or self.val=='0,000000') : self.val=''

    def CnvNone(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        if(evt==None or evt=="None" or evt==0):self.val = ""
        else:self.val = evt

    def CnvVMPZ(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        #print evt
        val=float(evt)
        self.val= locale.format("%."+str(cfg.cdecPZ)+"f",val,1)
        if (self.val=='0,00' or self.val=='0,000'  or self.val=='0,0000'  
           or self.val=='0,00000' or self.val=='0,000000') : self.val=''

    def CnvVMQT(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        val=float(evt)
        self.val= locale.format("%."+str(cfg.cdecQT)+"f",val,1)
        if (self.val=='0,00' or self.val=='0,000'  or self.val=='0,0000'  
           or self.val=='0,00000' or self.val=='0,000000') : self.val=''


    def CnvVM(self, evt): # tenuto per retrocompatibilita' con la 0.9.7, poi da eliminare
        #print evt
        val=float(evt)
        self.val= locale.format("%."+str(cfg.cdec)+"f",val,1)
        if (self.val=='0,00' or self.val=='0,000'  or self.val=='0,0000'  
           or self.val=='0,00000' or self.val=='0,000000') : self.val=''

    def SashMDIon(self):
        self.tab=False
        self.selazon=False
        self.win.Destroy()
        self.winMDI=wx.Panel(self,-1)
        self.SetStatusText("")        
        # per compatibilita' con la 0.9.7 
        self.SetStatusText(_("Azienda: ")+self.__az__, 1)
        self.SetStatusText(_("Operatore: ")+ self.__Ute__, 2)
        self.SetStatusText(_("Anno contabile: ")+self.__AnnoC__, 3)
        # =========
        self.fmenubar(True)
        if wx.Platform == '__WXMAC__':
            # servono per mac per fare vsualizzare subito il menu (??????????????????????? non capisco il modivo)
            #self.GetMenuBar().Refresh() # non va
            #1^ soluzione
            fram=wx.Frame(self,-1,"Mac",size=(0,0))
            fram.Show(True)
            fram.Destroy()
            # 2^ soluzione
            ####self.Iconize(True)  # provvisori su mac per fare vedere il menu subito
            ####self.Iconize(False) # provvisori su mac per fare vedere il menu subito
            # ===============================================
        self.ftoolbar(True)
        self.Sash()

    def Sash(self):      
        self.window_1 = wx.SplitterWindow(self.winMDI, -1, style=wx.SP_3DSASH)#wx.SP_3DSASH)
        #self.window_1.SetSashSize(5)
        self.window_1_pane_2 = wx.ScrolledWindow(self.window_1, -1, style=wx.SUNKEN_BORDER)
        self.window_1_pane_1 = wx.Panel(self.window_1, -1)
        self.window_2 = wx.SplitterWindow(self.window_1_pane_1, -1, style=wx.SP_3DSASH)#wx.SP_3DSASH)#wx.SP_BORDER
        #self.window_2.SetSashPosition(0)        
        #self.window_2.SetSashSize(5)
        bookStyle = FNB.FNB_NODRAG
        #bookStyle &= ~(FNB.FNB_NODRAG)
        #bookStyle |= FNB.FNB_ALLOW_FOREIGN_DND 
        bookStyle |= FNB.FNB_X_ON_TAB
        bookStyle |= FNB.FNB_FF2
        #bookStyle |= FNB.FNB_SMART_TABS
        self.notebook_1 = FNB.FlatNotebook(self.winMDI, wx.ID_ANY, style=bookStyle)
        #self.notebook_1.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False)) 
        self.notebook_1.SetRightClickMenu(self._rmenu)
        self.notebook_1.Bind(FNB.EVT_FLATNOTEBOOK_PAGE_CHANGED, self.CambiaTab)
        self.notebook_1.Bind(FNB.EVT_FLATNOTEBOOK_PAGE_CLOSING, self.ChiudendoTab)
        self.chiuditab=False

        self.panel_1 = wx.Panel(self.notebook_1, -1,size=(0,0))

        self.window_2_pane_1 = wx.ScrolledWindow(self.window_2, -1, style=wx.SUNKEN_BORDER)
        self.window_2_pane_2 = wx.Panel(self.window_2, -1)
        
        #self.window_2_pane_1.SetScrollRate(10, 10)
        #self.window_1_pane_2.SetMinSize((376, 0))
        #self.window_1_pane_2.SetScrollRate(10, 10)
        
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_1=sizer_1
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_2=sizer_2
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_4=sizer_4        
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_3=sizer_3        
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_6=sizer_6
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_5=sizer_5
        
        sizer_5.Add(self.notebook_1, 1, wx.BOTTOM|wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        sizer_1.Add(sizer_5, 0, wx.BOTTOM|wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        self.window_2.SplitVertically(self.window_2_pane_1, self.window_2_pane_2,200)
        self.window_2.Unsplit(self.window_2_pane_1) # disabilitata
        #self.window_2.SetSashPosition(1)           
        
        sizer_3.Add(self.window_2, 1, wx.EXPAND, 0)
        self.window_1_pane_1.SetSizer(sizer_3)
        self.window_1_pane_2.SetSizer(sizer_4)        
        self.window_2_pane_2.SetSizer(sizer_6)    ### per nuovo pannello        
        self.window_1.SplitHorizontally(self.window_1_pane_1, self.window_1_pane_2,-100)
        #self.window_1.SetSashPosition(-10)    
        self.window_1.Unsplit(self.window_1_pane_2) # disabilitata
        
        sizer_1.Add(self.window_1, 1, wx.EXPAND, 0)
        
        # ======================= gestione bar button =============================================
        self.buttonsbar=[]
        keys=BUTTONSBAR
        IDD=0
        IDDLEN=len(keys)
        while IDD < IDDLEN :
        #for IDD in keys:
            sBUTTONSB = string.split(BUTTONSBAR[IDD][1],"|")
            idmenu=BUTTONSBAR[IDD][0]
            labelbuttons=sBUTTONSB[0]
            tooltipbuttons=sBUTTONSB[1]
            winbutton=buttons.GenButton(self.winMDI, -1, labelbuttons,style=wx.FULL_REPAINT_ON_RESIZE)                     
            winbutton.SetFont(self.font)
            winbutton.SetToolTip(wx.ToolTip(tooltipbuttons))
            self.buttonsbar.append(winbutton)
            sizer_2.Add(winbutton, 1, wx.EXPAND, 0)
            winbutton.Bind(wx.EVT_BUTTON,self.OnButtonsBar) #,id=idmenu)
            IDD=IDD + 1
        # =========================================================================================

        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)  #decommentare la linea per mettere bottoni
        self.winMDI.SetSizer(sizer_1)
        self.SendSizeEvent() #fondamentale ##################################################
        self.notebook_1.Show(False)
        
        if self.buttonsbarShow==0:
            for x in self.buttonsbar : x.Show(False)
        
        self.win_logo_MDI=mdi_logo(self.window_2_pane_2)
        self.sizer_6.Add(self.win_logo_MDI, 1, wx.EXPAND, 0)
        self.sizer_6.Layout()
        self.win_logo_MDI.Show(True)
    
    def OnButtonsBar(self,event):
        id=self.buttonsbar.index(event.GetButtonObj())          
        idmenu=BUTTONSBAR[id][0]
        self.ProcessCommand(idmenu)

    def CambiaTab(self, event):
        if self.tab==False :
           self.win_logo_MDI.Hide()
           self.sizer_6.Detach(self.win_logo_MDI)
           self.notebook_1.Show(True)
           self.winMDI.Layout()
           self.tab=True
        old = event.GetOldSelection()       
        if old>=0 :
            aux=self.notepageObj[old]
            aux.Hide()
            self.sizer_6.Detach(aux)
        new = event.GetSelection()
        topo=self.notepageObj[new]
        self.sizer_6.Add(topo, 1, wx.EXPAND, 0)
        topo.Show(True)
        self.sizer_6.Layout()
        topo.SetFocus()
        event.Skip()

    def CloseTabObj(self,EVT):
        idObj=EVT
        if idObj in self.notepageObj:
            id=self.notepageObj.index(idObj)            
            idObj.Hide()
            self.sizer_6.Detach(idObj)  #chiamare evento close della finestra       
            del self.notepageObj[id]
            del self.notepageID[id]
            self.chiuditab=True
            self.notebook_1.DeletePage(id)
            idObj.Destroy()
            if len(self.notepageObj)==0 :
                self.notebook_1.Show(False)
                self.winMDI.Layout()
                self.tab=False
                self.sizer_6.Add(self.win_logo_MDI, 1, wx.EXPAND, 0)
                self.sizer_6.Layout()
                self.win_logo_MDI.Show(True)
                if len(self.frampageFra) > 0 :
                    for x in self.frampageFra:
                        x.Iconize(False)
                        x.Raise()
                    x.SetFocus()
        elif idObj in self.frampageObj:
            id=self.frampageObj.index(idObj)            
            idObj=self.frampageFra[id]
            del self.frampageObj[id]
            del self.frampageID[id]
            del self.frampageFra[id]
            idObj.Destroy()
          
    def ChiudendoTab(self,event):
        if self.chiuditab==False :
          new = event.GetSelection()
          aux=self.notepageObj[new]
          aux.Close(0)
          event.Veto()
        else :
          self.chiuditab=False
          event.Skip()

    def CreateRightClickMenu(self):
        self._rmenu = wx.Menu()
        item = wx.MenuItem(self._rmenu, MENU_EDIT_DELETE_PAGE, _("Sposta in finestra"), _("Sposta in finestra"))
        self._rmenu.AppendItem(item)

    def About(self):
        import about
        control = []
        win = about.create(self,control) 
        win.Centre(wx.BOTH)
        win.Show(True)      


    def About1(self):
        import copyright
        info = wx.AboutDialogInfo()
        #info.SetIcon(wx.Icon('icons/.png', wx.BITMAP_TYPE_PNG))
        info.SetName(copyright.longversion)
        #info.SetVersion(copyright.version)
        #info.SetDescription(copyright.disclaimer)
        info.SetCopyright(copyright.copyright)
        info.SetWebSite('http://www.phasis.it')
        info.SetLicence(copyright.license)
        info.AddDeveloper(copyright.developer)
        info.AddDocWriter(copyright.docwriter)
        #info.AddArtist('')
        info.AddTranslator('')

        wx.AboutBox(info)

#---------------------------------------------------------------------------

class AllModulNavigation(wx.Dialog):
    def __init__(self, parent=None):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "", style=0)
        self.__MDI__= wx.GetApp().GetPhasisMdi()
        self.SetFont(self.__MDI__.font)
        sz = wx.BoxSizer(wx.VERTICAL)
        self.NavListBox = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DLG_SZE(self, 220/2,250/2), # wx.Size(200, 150), 
                                    style= wx.LC_REPORT | wx.LC_NO_HEADER | wx.LC_SINGLE_SEL)
        self.NavListBox.SetImageList(self.__MDI__.icolistctrl, wx.IMAGE_LIST_SMALL)
        self.NavListBox.InsertColumn(0, "")
        self.NavListBox.SetFont(self.__MDI__.font)
        self.NavListBox.SetColumnWidth(0,wx.DLG_SZE(self,200/2,-1).width)
        #self.IDItem = -1
        self.IDMap = []
        x=0
        for i in self.__MDI__.notepageID: 
            self.NavListBox.InsertImageStringItem(x," "+self.__MDI__.vcMENU[i][4],self.__MDI__.icotab)
            self.IDMap.append(i)
            x=x+1
        for i in self.__MDI__.frampageID: 
            self.NavListBox.InsertImageStringItem(x," "+self.__MDI__.vcMENU[i][4],self.__MDI__.icowin)
            self.IDMap.append(i)
            x=x+1
        testo=wx.StaticText(self,wx.ID_ANY,_("MODULI APERTI"),style=wx.ALIGN_CENTRE)
        testo.SetFont(self.__MDI__.font)
        testo.Centre(wx.HORIZONTAL)
        testo.SetBackgroundColour(wx.RED)
        testo.ClearBackground()
        sz.Add(testo,0, wx.EXPAND)
        sz.Add(self.NavListBox, 1, wx.EXPAND | wx.ALL,10)
        self.SetSizer(sz)
        sz.Fit(self)
        sz.SetSizeHints(self)
        sz.Layout()
        self.NavListBox.Focus(0)
        self.NavListBox.Select(0)
        self.NavListBox.Bind(wx.EVT_LIST_KEY_DOWN,self.EvtChar)
        self.NavListBox.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemSelected)

    def EvtChar(self, evt):
        evt_char = evt.GetKeyCode()
        if evt_char==wx.WXK_ESCAPE: self.EndModal(wx.ID_CANCEL)
        evt.Skip()

    def OnItemSelected(self, event):
        self.IDItem=event.GetIndex()        
        self.EndModal(self.IDMap[self.IDItem])
        

#---------------------------


class MyFrame(wx.Frame):
    def __init__(
            self, parent, ID, title, pos=wx.DefaultPosition,
            size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE #| wx.STAY_ON_TOP
            ): 
        wx.Frame.__init__(self, parent, ID, title, pos, size, style)
        #self.SetBackgroundColour(wx.GetApp().GetPhasisMdi().backcolmod)
        self.__MDI__=wx.GetApp().GetPhasisMdi()
        self.child=None
        self.accellentry=[]
        self.accellentry.append(wx.AcceleratorEntry(wx.ACCEL_CTRL,ord('T'),DAFRAMEATAB))
        #self.accellentry.append(wx.AcceleratorEntry(wx.ACCEL_CTRL,ord('Y'),LISTA_MODULI_APERTI))
        self.accellentry=self.accellentry + self.__MDI__.accellentry
        #accell=wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('T'),DAFRAMEATAB),(wx.ACCEL_CTRL,ord('Y'),LISTA_MODULI_APERTI)])  # CTRL-T - ultimo parametro e' l'ID menu
        accell=wx.AcceleratorTable(self.accellentry)
        self.SetAcceleratorTable(accell)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Bind(wx.EVT_MENU, self.OnMenu)
        
    def OnCloseWindow(self, event):
        self.child.Close(0)
        
    def SetChild(self,child):
        self.child=child
        
    def GetChild(self):
        return self.child
        
    def OnMenu(self, event):
        ID = event.GetId()
        if ID == DAFRAMEATAB : self.__MDI__.trasfotab(self)
        else : event.Skip()

#--------------------

class mdi_logo(wx.ScrolledWindow):
    def __init__(self, prnt):
        wx.ScrolledWindow.__init__(self, id = wx.NewId(),
              parent = prnt, size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100)
        self.FitInside()
        
        png = wx.Image((cfg.path_img + "phasis_MDI.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        immagine=wx.StaticBitmap(self, -1, png)
        box = wx.GridSizer(1, 1)
        box.Add(immagine, 0, wx.ALIGN_CENTER | wx.ADJUST_MINSIZE | wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)


#=====================================

