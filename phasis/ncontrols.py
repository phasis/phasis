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
import util
import types
import string
from cfg import *
import cfg
#import gettext
#_ = gettext.gettext


# Costanti dello stato dell'interfaccia di inserimento
NORMAL = 0
NEW = 2
SELECT = 3 
MODIFY = 1 
ALL_CONTROL=6
def stateButton(state):
    l=("NORMAL", "MODIFY", "NEW", "SELECT", "SELECT_ON_EMBEDDED_PANEL", "MODIFY_ON_EMBEDDED_PANEL","ALL_CONTROL")
    return l[state]

# Costanti dei valori degli eventi dei bottoni nuovo ecc...
STAMPA = 0
NUOVO = 1
AGGIORNA = 2 
SALVA = 3 
INTERROMPI = 4
INTERROMPI_MODIFICA = 5
ANNULLA = 6
MODIFICA = 7
CANCELLA = 8 
SCHEDA = 9 



myEVT_CLICK_ON_PANEL_BUTTONS = wx.NewEventType()
EVT_CLICK_ON_PANEL_BUTTONS = wx.PyEventBinder(myEVT_CLICK_ON_PANEL_BUTTONS, 1)


# #########################################
# #########################################
class nButtons(wx.Panel):
    '''questo pannello raggruppa i pulsanti 
    standard nuovo modifica annulla ecc...
    e i meccanismi per abilitarli e disabilitarli
    genera l'evento 
    EVT_CLICK_ON_PANEL_BUTTONS che inoltra la richiesta
    dell'utente alla business logic
    la proprieta' GetState contiene l'informazione
    sullo stato attuale dei pulsanti e quindi della finestra
    che sono:
    NORMAL la finestra e' vuota e i campi disabilitati ,si possono effettuare ricerche
    MODIFY i campi sono editabili 
    NEW si sta editando un nuovo record
    SELECT c'e un record caricato in maschera i controlli sono disabilitati
     '''
    def __init__(self,parent,pos,name='',isVerticale=True):

        style=wx.TAB_TRAVERSAL
        wx.Panel.__init__(self,parent,pos=pos,name=name,style=wx.TAB_TRAVERSAL)
        self.font=wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False)
        self.SetFont(self.font)
        self.msgModifica = None
        self.msgDelete = _("Vuoi cancellare i dati selezionati")
        self.MyEvt = util.MyEvent(myEVT_CLICK_ON_PANEL_BUTTONS, self.GetId())         
        self.isMODIFICA = False
        self.isVERTICALE=isVerticale
        self.__state = NORMAL
        self.__pre_state=None#immagazzina il penultimo stato per errori nei pannelli
        #abilita o no la stampa o la scheda
        self.PermettiScheda=False
        self.PermettiStampa=True
        if self.isVERTICALE:
            self.__vertical()
        else:#=0
            self.__horizontal()
        self.adjustButton()
        
    #interfacce bottoni
    def __horizontal(self):
        '''bottoni in orizzontale'''
        self.SetSize((500,40))
        self.nuovo = wx.Button(self, -1, _("Nuova &Riga"), wx.DLG_PNT(self, 5,5), 
                                wx.DLG_SZE(self,cfg.btnSzeL1H,cfg.btnSzeV)) 
        self.Bind(wx.EVT_BUTTON, self.OnNuovo, self.nuovo)
        
        self.ok = wx.Button(self, -1, _("Con&ferma Riga"), wx.DLG_PNT(self, 67,5), 
                                wx.DLG_SZE(self,cfg.btnSzeL1H,cfg.btnSzeV))
        self.ok.Show(False)
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.ok) 
                               
        self.modifica = wx.Button(self, -1, _("Modifica &Riga"), wx.DLG_PNT(self, 67,5), 
                                wx.DLG_SZE(self,cfg.btnSzeL1H,cfg.btnSzeV))
        self.Bind(wx.EVT_BUTTON, self.OnModifica, self.modifica) 
                                      
        self.interrompi = wx.Button(self, -1, _("&Interrompi"), wx.DLG_PNT(self, 130,5), 
                                wx.DLG_SZE(self,cfg.btnSzeLH,cfg.btnSzeV))
        #self.interrompi.Show(False)
        self.Bind(wx.EVT_BUTTON, self.OnInterrompi, self.interrompi)  
                              
        self.cancella = wx.Button(self, -1, _("&Elimina"), wx.DLG_PNT(self, 182,5), 
                                wx.DLG_SZE(self,cfg.btnSzeLH,cfg.btnSzeV))
                                
        #self.cancella.Show(False)
        self.Bind(wx.EVT_BUTTON, self.OnCancella, self.cancella)
        #questi bottoni non verranno mai visualizzati ma vengono comunque richiesti 
        #in vari punti
        self.annulla = wx.Button(self, -1)
        self.annulla.Show(self.isVERTICALE)
        self.stampa = wx.Button(self,-1)
        self.stampa.Show(False)
        self.scheda = wx.Button(self,-1)
        self.scheda.Show(False)
        
    def __vertical(self):
        '''bottoni in verticale'''
        #nuovo ok
        self.SetSize((150,200))
        self.msgModifica = _("Vuoi modificare i dati selezionati")
        
        self.nuovo = wx.Button(self,-1,_("&Nuovo"),
                        wx.DLG_PNT(self, 0, 0),
                        wx.DLG_SZE(self,cfg.btnSzeLH,cfg.btnSzeV ))
        self.Bind(wx.EVT_BUTTON, self.OnNuovo, self.nuovo)
        
        self.ok = wx.Button(self, -1, _("&Ok"), 
                        wx.DLG_PNT(self, 0, 0),
                        wx.DLG_SZE(self,cfg.btnSzeLH,cfg.btnSzeV ))
        self.ok.Show(False)
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.ok)
        
        #annulla
        self.annulla = wx.Button(self, -1, _("&Annulla"), 
                        wx.DLG_PNT(self, 0, 15),
                        wx.DLG_SZE(self,cfg.btnSzeLH,cfg.btnSzeV ))
        self.annulla.SetDefault()
        self.Bind(wx.EVT_BUTTON, self.OnAnnulla, self.annulla)
        
        
        self.interrompi = wx.Button(self,-1,_("&Interrompi"), 
                        wx.DLG_PNT(self, 0, 15),
                        wx.DLG_SZE(self, cfg.btnSzeLH, cfg.btnSzeV))
        self.interrompi.Show(False)
        self.Bind(wx.EVT_BUTTON, self.OnInterrompi, self.interrompi)
        
        #modifica_cancella
        self.modifica = wx.Button(self,-1,_("&Modifca"), 
                        wx.DLG_PNT(self, 0, 30),
                        wx.DLG_SZE(self, cfg.btnSzeLH, cfg.btnSzeV))
        self.Bind(wx.EVT_BUTTON, self.OnModifica, self.modifica)
        
        self.cancella = wx.Button(self,-1,_("&Cancella"), 
                        wx.DLG_PNT(self, 0, 30),
                        wx.DLG_SZE(self, cfg.btnSzeLH, cfg.btnSzeV))
        self.cancella.Show(False)
        self.Bind(wx.EVT_BUTTON, self.OnCancella, self.cancella)
        
        #stampa
        self.stampa = wx.Button(self,-1,_("&Stampa"),
                        wx.DLG_PNT(self, 0, 45),
                        wx.DLG_SZE(self, cfg.btnSzeLH, cfg.btnSzeV))
        self.Bind(wx.EVT_BUTTON, self.OnStampa, self.stampa)

        self.scheda = wx.Button(self,-1,_("Sche&da"),
                        wx.DLG_PNT(self, 0, 60),
                        wx.DLG_SZE(self, cfg.btnSzeLH, cfg.btnSzeV))
        self.Bind(wx.EVT_BUTTON, self.OnScheda, self.scheda)
        

        
    def GetClassName(self):
        return "nButtons"

# gestione Bottoni
    def OnScheda(self,event):
        self.MyEvt.SetValue(SCHEDA)
        self.GetEventHandler().ProcessEvent(self.MyEvt)

    def OnStampa(self,event): 
        self.MyEvt.SetValue(STAMPA)
        self.GetEventHandler().ProcessEvent(self.MyEvt)
        
        
    def OnNuovo(self,event): 
        ####print "OnNuovo"
        self.MyEvt.SetValue(NUOVO)
        self.isMODIFICA =False
        self.SetState(NEW,True)
        #self.adjustButton()

    def OnOk(self,event): 
        print "OnOk"
        if self.isMODIFICA:
            self.MyEvt.SetValue(AGGIORNA)
            self.isMODIFICA = False
        else:    
            self.MyEvt.SetValue(SALVA)  
        self.SetState(NORMAL,True)
        #self.adjustButton()
                
    def OnModifica(self,event):
        print "OnModifica"
        print self.msgModifica
        if self.msgModifica :
            if util.ask(self, self.msgModifica,":o", self.modifica.GetPosition()):
                self.MyEvt.SetValue(MODIFICA)
                self.isMODIFICA = True
                self.SetState(MODIFY,True)
                #self.adjustButton()
        else:
            self.MyEvt.SetValue(MODIFICA)
            self.isMODIFICA = True
            self.SetState(MODIFY,True)
            #self.adjustButton()
            
    def OnCancella(self,event):
        ####print "OnCancella"
        if self.msgDelete :
            if util.ask(self,self.msgDelete,self.cancella.GetPosition()):
                self.MyEvt.SetValue(CANCELLA)
                #self.adjustButton()
                self.SetState(NORMAL,True)
        else:
            self.MyEvt.SetValue(CANCELLA)
            #self.adjustButton()
            self.SetState(NORMAL,True) 
    def OnInterrompi(self,event): 
        ####print "OnInterrompi"
        self.MyEvt.SetValue(INTERROMPI)
        if self.isMODIFICA:
            self.isMODIFICA = False
        self.SetState(NORMAL,True)

            
    def OnAnnulla(self,event): 
        ####print "OnAnnulla"
        self.MyEvt.SetValue(ANNULLA)
        self.SetState(NORMAL,True)
        
        #self.adjustButton()
        
    def adjustButton(self, raiseEvent = True):
        if self.__state == NORMAL:
            print "NORMAL"
            self.ok.Show(False)
            self.nuovo.Show(True)
            self.nuovo.Enable(True)
            
            self.annulla.SetFocus()
            self.annulla.Show(self.isVERTICALE)
            self.annulla.Enable(True)
            
            self.interrompi.Show( not self.isVERTICALE)
            self.interrompi.Enable( self.isVERTICALE)
            
            self.modifica.Show(True)
            self.modifica.Enable(False)
            
            self.cancella.Show(not self.isVERTICALE)
            self.cancella.Enable( self.isVERTICALE)
            
            self.stampa.Enable(False)
            self.scheda.Enable(False)
            
        elif self.__state == MODIFY:
            print "MODIFY"
            self.nuovo.Show(not self.isVERTICALE)
            self.nuovo.Enable(False)
            
            self.ok.Show(True)
            self.ok.Enable(True)
            
            self.annulla.Show(False)
            
            self.interrompi.Show(True)
            self.interrompi.Enable(True)
            
            self.modifica.Show(False)
            
            self.cancella.Show(True)
            self.cancella.Enable(True)
            
            self.stampa.Enable(False)
            self.scheda.Enable(False)

            self.isMODIFICA =True
            
        elif self.__state == NEW:
            print "NEW"
            self.nuovo.Show(not self.isVERTICALE)
            self.nuovo.Enable(False)
            
            self.ok.Show(True)
            self.ok.Enable(True)
            
            self.annulla.Show(False)
            
            self.interrompi.Show(True)
            self.interrompi.Enable(True)
            
            self.modifica.Show(False)
            self.modifica.Enable(False)
            
            self.cancella.Show(not self.isVERTICALE)
            self.cancella.Enable(False)
            
            self.stampa.Enable(False)
            self.scheda.Enable(False)
            self.isMODIFICA = False

        elif self.__state == SELECT:
            print "SELECT" 
            self.nuovo.Show(not self.isVERTICALE)
            self.nuovo.Enable(not self.isVERTICALE)
            
            self.ok.Show(self.isVERTICALE)
            self.ok.Enable(not self.isVERTICALE)
            
            self.annulla.Show(False)
            
            self.interrompi.Show(True)
            self.interrompi.Enable(True)
            
            self.modifica.Show(True)
            self.modifica.Enable(True)
            
            self.cancella.Show(not self.isVERTICALE)
            self.cancella.Enable(self.isVERTICALE)
            
            self.stampa.Enable(self.PermettiStampa)
            self.scheda.Enable(self.PermettiScheda)

        if raiseEvent:
            self.GetEventHandler().ProcessEvent(self.MyEvt)
        ######print self.stato
            
    def GetState (self):
        return self.__state
        
    def SetState (self,nuovo_stato,raise_event=False):
        if nuovo_stato in (NORMAL,NEW,SELECT,MODIFY):
            self.__pre_state = self.__state
            self.__state = nuovo_stato
            self.adjustButton(raise_event)
            
    def SetPreState (self,raise_event=False):           
        self.__state = self.__pre_state
        self.adjustButton(raise_event) 
# #########################################
# #########################################

class nProperty:
    '''definizione dei campi del database e altre proprieta' '''
    def __init__(self):
        self.table=None
        self.maxlen=0
        self.decimals=0
        self.type=types.StringType
        self.isSearch=False
        self.isKey=False
        self.isNotNull=False
        self.isFixedKey=False
        self.default=None
        self.associate_control=None
        self.remember_last_value=False
        
    def SetFieldDef(self,table=None,maxlen=0,decimals=0,type=types.StringType,isSearch=False,isKey=False,isNotNull=False,isFixedKey=False,default=None):
        '''
        table :string la tabella in cui legge-scrive i dati                
        maxlen :integer numero massimo di caratteri
        
        decimals :integer numero massimo di decimali
        
        isNotNull :boolean se True il controllo in fase di edit deve essere obbligatoriamente riempito
        
        isKey :boolean se True e' un campo 'primary key' il suo contenuto non potra essere cambiato in fase di modifica
        
        isSearch :boolean se True e' un campo da cui si effettua la ricerca dei record 
         
        type :Types il tipo di dato del campo con GetValue le stringhe saranno racchiuse da apici
        
        isFixedKey : boolean nPanel non cambia o azzera mai il suo valore
        
        default :var valore di default viene inserito al Clear()

        '''
        self.table=table
        if self.__dict__.has_key("SetMaxLength"):
            self.SetMaxLength(maxlen)
        ######self.maxlen=maxlen ???combobox
        self.decimals=decimals
        self.type=type
        self.isSearch=isSearch
        self.isKey=isKey
        self.isNotNull=isNotNull
        self.isFixedKey=isFixedKey
        self.default=default
        
    def SetAssociateControl(self,controls):
        """controls :var
            uno o piu'controlli con proprieta' SetValue 
            dove Questo controllo scrivera' il suo stesso contenuto
        """
        if type(controls) not in (types.TupleType,types.ListType):
            controls=(controls,)
        self.associate_control=controls
           
    
class nComboBox(wx.ComboBox,nProperty):
    def __init__(self,*args,**kwrds):
        wx.ComboBox.__init__(self,*args,**kwrds)
        nProperty.__init__(self)
        
        
        self.rows=None
        
        self.Bind(wx.EVT_SET_FOCUS,self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS,self.OnKillFocus)
        self.Bind(wx.EVT_WINDOW_DESTROY,self.OnDestroy)
       
####        
    def OnDestroy(self,event):
        print "te dico che ce sto"
        #event.Skip()
        if self.remember_last_value:
            util.StoreLastValue(self.GetName(),self.default)
    def OnSetFocus(self,event): 
        event.Skip()
        self.SetBackgroundColour("#f7ffa2")

    def OnKillFocus(self,event): 
        event.Skip()
        if self.isNotNull and wx.TextCtrl.GetValue(self)=="":
            self.SetBackgroundColour("#ffa7a7")
        else:
            self.SetBackgroundColour(wx.NullColour)
            
    def SetNProperty(self,sql,connessione=None):
        '''
        sql :string la query sql completa con cui verra popolata la lista del combo box
                se la query e' composta da due campi il primo verra' visualizzato nella lista 
                    e il secondo verra' scritto nel database 
                se la query e' composta da un campo verra' visualizzato nella lista  e scritto nel database
        connessione: una connessione aperta gestibile da util.eseguiSql
        '''
        
        self.rows=util.eseguiSql(sql,connection=connessione)
        if self.rows:
            for row in self.rows:
                wx.ComboBox.Append(self,row[0])
            


        
    def SetValue(self,var):
        """qui arriva la 'chiave'"""
        trovato=False
        ######controlla se ci sono voci nella lista
        if self.rows:
            for row in self.rows:#se c'e corrispondenza
                if len(row)>1:
                    if var == row[1]:
                        trovato=True
                        wx.ComboBox.SetValue(self,str(row[0]))
            if not trovato:wx.ComboBox.SetValue(self,"-----------------------")
            
            if self.associate_control:
                for control in self.associate_control:
                    control.SetValue(str(var))
            
    def GetValue(self,state=0,format=True):
        """restituisce il valore contenuto o se e' presente la chiave
        """
        val=""
        if wx.ComboBox.GetValue(self) != "":
            
            if len(self.rows[0])>1:
                #index=wx.ComboBox.FindString(self,wx.ComboBox.GetValue(self))
                index=self.GetSelection()
                val=self.rows[index][1]
            else:
                val=wx.ComboBox.GetValue(self)
        self.default=val
        
        return GetValue(self,val,format)
    
        
    def GetClassName(self):
        return "nComboBox"
        
        
    def Clear(self,state):
        print stateButton(state)
##        if (state == NEW and not self.isKey) or  (state == NORMAL):
##            self.SetValue(self.default)
        if not (state == NEW and self.isKey):
            self.SetValue(self.default)

                
    def Enable(self,enable,state):
        """se e' un campo da cui si fanno ricerche
            e non si sta editando il record deve rimanere enable=True
        """
##        print self.GetName()
##        if state == ALL_CONTROL:
##            print"allContr"
##            wx.ComboBox.Enable(self,enable)
##        elif state == SELECT:
##            print"select"
##            wx.ComboBox.Enable(self,enable)  
##        else:
##            if self.isSearch:
##                print "sear"
##                wx.ComboBox.Enable(self,True)
##            else:
##                print"no searc"
##                wx.ComboBox.Enable(self,enable)   
##        if state in (NEW,MODIFY) and self.isKey:
##            print "new ecc"
##            wx.ComboBox.Enable(self,False)
            
 
        #if state in (ALL_CONTROL,SELECT):
        wx.ComboBox.Enable(self,enable)  
        if self.isSearch:
            wx.ComboBox.Enable(self,True)  
        if state in (NEW,MODIFY) and self.isKey:
            wx.ComboBox.Enable(self,False) 
            
# ###########################################
# ###########################################
class nTextCtrl(wx.TextCtrl,nProperty):
    def __init__(self,*args,**kwrds):
                
        wx.TextCtrl.__init__(self,*args,**kwrds)
        nProperty.__init__(self)
        
        self.Bind(wx.EVT_SET_FOCUS,self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS,self.OnKillFocus)

    def Navigate(self):#,event):
        #event.Skip()
        #se e' un campo ricerca pigia il search button seguente
        if self.isSearch:
            prossimo_controllo=self.GetParent().FindWindowById(self.NextControlId(self.GetId()))
            if prossimo_controllo.GetClassName()=="nSearchButton":
                prossimo_controllo.OnButton()
        wx.TextCtrl.Navigate(self)

    def OnSetFocus(self,event): 
        event.Skip()
        self.SetBackgroundColour("#f7ffa2")

    def OnKillFocus(self,event): 
        event.Skip()
       
        if self.isNotNull and wx.TextCtrl.GetValue(self)=="":
            self.SetBackgroundColour("#ffa7a7")
        else:
            self.SetBackgroundColour(wx.NullColour)
            
        
    def SetValue(self,var):
        """SetValue(self, String value)
            setta il valore del controllo 
            se ci sono dei controlli associati
            con setAssociateControl
            inserisce in essi gli stessi valori
        """
        wx.TextCtrl.SetValue(self,str(var))
        if self.associate_control:
            for control in self.associate_control:
                control.SetValue(str(var))
            
    def GetValue(self,state=0,format=True):
        """GetValue(self,state int ) -> il tipo restituito dipende da come e' impostata
            la variabile type in setExtraProperty
            se e' un campo stringa il valore viene restituito tra apici singoli
            """
        #non uso piu state
        val=wx.TextCtrl.GetValue(self)
        return GetValue(self,val,format)
        
        
    def GetClassName(self):
        return "nTextCtrl"
        
    def __clear__(self):
        if self.default:
            self.SetValue(self.default)
        else:
            if self.type ==types.IntType:
                self.SetValue(0)
            elif self.type ==types.StringType:
                self.SetValue("")
            elif self.type ==types.FloatType:
                self.SetValue("0.%s"%string.zfill("0",self.decimals))
        
    def Clear(self,state):
        #print "clear"
        if state == ALL_CONTROL:
            self.__clear__()
            return
        if not self.isFixedKey:
            if state == NEW and not self.isKey:
                self.__clear__()
            if state == NORMAL:
                self.__clear__()
                if self.isSearch:self.SetValue("")
                
    def Enable(self,enable,state):
        """se e' un campo da cui si fanno ricerche
            e non si sta editando il record deve rimanere enable=True
            ALL_ALL_CONTROL False
        """
        wx.TextCtrl.Enable(self,enable)  
        if self.isSearch:
            wx.TextCtrl.Enable(self,True)  
        if state in (NEW,MODIFY) and self.isKey:
            wx.TextCtrl.Enable(self,False) 

            
            
class nRadioBox(wx.RadioBox,nProperty):
    def __init__(self,*args,**kwrds):
                
        wx.RadioBox.__init__(self,*args,**kwrds)
        nProperty.__init__(self)

        self.idVoci=None
  
    def SetNProperty(self,choice):
        '''
        choice: Tuple le voci che visualizzera (("label","id"),("label1","id1"),) or ("label","label1",)
        '''
        self.idVoci=choice
        
    def SetValue(self,var):
        """qui arriva la 'chiave'"""
        x=0
        for idVoce in self.idVoci:#se c'e corrispondenza
            if idVoce==var:
                    wx.RadioBox.SetSelection(self,x)
            x=x+1

            
    def GetValue(self,state=0,format=True):
        """se ce'restituisce il valore associato
        al radiobutton scelto altrimenti restituisce la label"""
        id = self.idVoci[wx.RadioBox.GetSelection(self)]
        
        return  GetValue(self,id,format) 
    
        
    def GetClassName(self):
        return "nRadioBox"
        
        
    def Clear(self,state):
        if self.default:
            wx.RadioBox.SetSelection(self,self.default)
        else:
            wx.RadioBox.SetSelection(self,0)

                
    def Enable(self,enable,state):
        """se e' un campo da cui si fanno ricerche
            e non si sta editando il record deve rimanere enable=True
        """
        if state in (NEW,MODIFY) :
            wx.RadioBox.Enable(self,True)
        else:
            wx.RadioBox.Enable(self,False)
            
#al posto dei campi invisibili
class nGenControl(nProperty):
    def __init__(self,value=None):
        nProperty.__init__(self)
        self.__value=value

       
    def SetValue(self,var):
        """"""

        self.__value=var
            
    def GetValue(self,state=0,format=True):
        """ """
                    
        return  GetValue(self,self.__value,format)
            
    def GetClassName(self):
        return "nGenControl"
        
        
    def Clear(self,state):
        pass

                
    def Enable(self,enable,state):
        pass
        


# #####################################
# ####################################        
myEVT_CLICK_SEARCH_BUTTON = wx.NewEventType()
EVT_CLICK_SEARCH_BUTTON = wx.PyEventBinder(myEVT_CLICK_SEARCH_BUTTON, 1)

class nSearchButton(wx.Button):
    def __init__(self,parent,pos = wx.Point(0,0), size = wx.Size(20,20)):
        wx.Button.__init__(self,parent,-1,pos=pos,size=size)#,pos=pos,size=size)
        self.Bind(wx.EVT_BUTTON,self.OnButton)

        self.SetLabel("...")

        self.__sql=None
        self.__grid_layout=None
        self.__keyfields=None
        self.__searchfields=None
        self.__return_values=None
        self.associate_controls=None
        self.MyEvt = util.MyEvent(myEVT_CLICK_SEARCH_BUTTON, self.GetId()) 
        self.__values=None

    def GetClassName(self):
        return "nSearchButton"   
 
    def OnButton(self,event=0): 
        where_ricerca=""
        where_key=""
        where=""
        a_n_d=""
        order_by=""
        #guardo nei controlli che contengono i dati da cercare
        for field,control in self.__searchfields:
            
             if control.GetValue(format=False)!="":
                #se non e' vuoto a seconda del tipo aggiungo istruzioni sql
                if control.type!= types.StringType:
                    where_ricerca=where_ricerca+" %s = %s OR"% (field,control.GetValue(format=False))
                else:
                    where_ricerca=where_ricerca+" %s LIKE '%%%s%%' OR"% (field,control.GetValue(format=False))
        #tolgo l'OR in piu'            
        if where_ricerca :
            a_n_d=" AND "
            order_by = "ORDER BY "+ self.__searchfields[0][0]
            where_ricerca=where_ricerca[:-2]
            
        #####print where_ricerca
        
        #compongo l'espressione where AND
        if self.__keyfields:
            for field,control in self.__keyfields:
                where_key = where_key +"%s = %s AND "%(field,control.GetValue(0))
            #tolgo l'AND in piu'
            where_key = where_key[:-4]
        else:
            a_n_d = ""
            
        if where_key or where_ricerca:
            where=" WHERE " + where_ricerca + a_n_d +where_key+order_by

        sql=self.__sql+where
        rows=util.eseguiSql(sql,1)
        if len(rows)==1:#un record
            self.__values=[]
            #####print "return values %s"%str(self.__return_values)
            for field,col in self.__return_values:
                self.__values.append((field,rows[0][col]))
        elif len(rows)==0:#nessun record
            util.alert(self.GetParent(),_("Nessun dato corrispondente "),_("Non trovato..."))
        else:#molti record
            #passo il risultato della query alla lista
            self.__values=None
            
            if -1==-1:
                dlg=listdialog(self ,layout=self.__grid_layout,return_values=self.__return_values,rows=rows)
                dlg.ShowModal()
            else:
                pandlg=listpanel(self.__parent ,layout=self.__grid_layout,return_values=self.__return_values,rows=rows,princ=self)
        '''
        if self.associate_controls:
            pass
        else:
            if self.__values:
                self.MyEvt.SetValue(self.__values)
                self.GetEventHandler().ProcessEvent(self.MyEvt)
        '''
    def selected(self,var):
        self.__values=var
        
        if self.associate_controls:
            pass
        else:
            if self.__values:
                self.MyEvt.SetValue(self.__values)
                self.GetEventHandler().ProcessEvent(self.MyEvt)
        
        
        

    def SetNProperty(self,sql,grid_layout,keyfields,searchfields,return_values,associate_controls=None,parent=-1):#textbox,table,field,sql=None,grid_layout=None,fixedKeysControls=None):
        ''' sql : string ,la query sql senza clausola where
            grid_layout: tuple, label delle colonne della griglia
                ("label1","label2","",...)
                per avere la colonna piu' larga si possono aggiungere spazi in label
                se label="" il campo non verra' mostrato nella lista 
            keyfields:tuple, dei campi che compongono la WHERE con l'operatore AND
                (("campo",var),...)
                il campo e' il nome del campo per la clausola where var puo essere una costante
                del tipo del campo o un controllo con la proprieta' GetValue()
            searchfields:tuple ,insieme dei campi che compongono la WHERE di ricerca 
                (("campo",controllo),..)
                
                i campi per ricavare la where di ricerca e il controllo dove attinge
                i dati le stringe vengono valutate con l'operatore LIKE altri tipi con =
                piu' campi vengono collegati con l'operatore OR
                N.B. il primo elemento deve corrispondere al text box vicino a bottone 
                perche verra' usato per la clausola order by
            return_values: tuple,insieme degli indici dei campi che devono
                            ritornare dalla ricerca
                            se = None ritorna tutto il record scelto
        '''
        ##### per inserire solamente dei valori nei controllo
        #### si puo aggiungere una tupla associate_controls con i nomi dei 
        #### ncontrol nello stesso ordine di returnvalue
        #### e non richiamare l'evento
        #### i controlli devono essere nel parent
        #### oppure passare se richiamare set value o meno
        
        '''si potrebbe anche ricavare la query dalle informazioni date dalle proprieta dei controlli
            usando soltanto gridlayout
        '''
        self.__sql=sql
        self.__grid_layout=grid_layout
        self.__keyfields=keyfields
        self.__searchfields=searchfields
        self.__return_values=return_values
        self.associate_controls=associate_controls
        self.__parent=parent
        
    def Enable(self,enable,state):
        """determina se e' in uno stato dove e' attiva la ricerca o no
        """

        if state in (NEW,MODIFY,ALL_CONTROL):
            wx.Button.Enable(self,False)
        else:
            wx.Button.Enable(self,True)
    def Clear(self,state):
        pass

# #################################
# LISTA
# #################################

# ############################
# costanti parametro degli eventi che la lista rimanda al pannello
# 
NLIST_GET_VALUE_ERROR=0
NLIST_SELECTED_ITEM=1

myEVT_SELECTED = wx.NewEventType()
EVT_SELECTED = wx.PyEventBinder(myEVT_SELECTED, 1)

myEVT_NLIST = wx.NewEventType()
EVT_NLIST = wx.PyEventBinder(myEVT_NLIST, 1)


class nList(wx.ListCtrl):
    def __init__(self,parent,id=-1,pos=wx.Point(0,0),size=wx.Size(695,425),
                sql=None,
                layout=None,
                return_values=None,
                associate_control=None,
                rows=None):
        wx.ListCtrl.__init__(self,
                            parent=parent,
                            pos = pos, 
                            size = size, 
                            style = wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES)
        ####print rows
                            
        self.__rows=rows #####rivedere
        self.__sql=sql
        #### sistemare meglio layout
        self.__column_property=None
        self.__layout=layout
        self.associate_control=associate_control
        self.__return_values=return_values
        self.__values=None
        
        self.__currentItem=None
        
        self.__myevt_nlist=util.MyEvent(myEVT_NLIST,self.GetId())
        

        
        self.Bind(wx.EVT_LEFT_DCLICK,self.OnDoubleClick)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED,self.OnItemSelected)
        self.Show(True)


##    def OnSize(self,event): 
##        w,h = self.GetClientSizeTuple()
##        self.SetDimensions(0, 0, w, h)
    def GetClassName(self):
        return "nList"
    def GetCurrentRow(self):
        return self.__currentItem

    def OnItemSelected(self,event): 
        self.__currentItem = event.m_itemIndex
        if self.associate_control:
            #se c'e  uno o piu' controlli associati vengono settaticon i valori della griglia
            for control,col in self.associate_control:
                control.SetValue(self.getColumnText(self.__currentItem,col))
##        col=0
##        if self.__column_property:
##            for prop in self.__column_property:
##                if prop[ASSOCIATE_CONTROL]:
##                    prop[ASSOCIATE_CONTROL].SetValue(self.getColumnText(self.__currentItem,col))
##                col=col+1
        #invia l'indice della riga
        self.__myevt_nlist.SetValue(NLIST_SELECTED_ITEM)
        self.GetEventHandler().ProcessEvent(self.__myevt_nlist)
        
    def OnDoubleClick(self,event): 
        #controllare cosa fare per associate vuoto
        self.__values=[]
        for field,col in self.__return_values:
            self.__values.append((field,self.getColumnText(self.__currentItem,col)))

        myevt=util.MyEvent(myEVT_SELECTED,self.GetId())
        myevt.SetValue(self.__values)
        self.GetEventHandler().ProcessEvent(myevt)
        
    def GetValue(self,all=False):
        return self.__values
        
    def getColumnText(self, index, col):
        item = self.GetItem(index, col)
        return item.GetText()
    


    def SetNProperty(self,column_property):
        '''column_property(caption="",size=-1,field=None,table=None,type=types.StringType,decimals=0,associate_control=None)
        specifica le proprieta' delle colonne della nList 
        (index =-1 :int indice zero_based della colonna se e' -1= nuova colonna ,
        caption="":string intestazione della colonna ,
        size=-1:int larghezza della colonna viene convertita in wx.DLG_SZE -1=larghezza della caption
        field=None:srting nome del campo in cui andranno scritti i dati
        table=None:string tabella in cui andranno inseriti i dati contenuti in questa colonna 
                    se table="" la tabella della colonna precedente
        type=types.StringType: types il tipo serve per la formattazione dlle query insert update
        decimals=0:int numero di decimali forse serve
        associate_control=None:wxcontrol o ncontrol con proprieta setValue() 
                    al comando LoadFromAssociateControl()la colonna verra riempita con il valore contenuto nel suo controllo associato
                    mentre all'evento wx.EVT_LIST_ITEM_SELECTED questa colonna riempira il suo controllo_associato  
        '''
        self.__layout=[]
        self.associate_control=[]
        self.__field_property=[]
        col=0
        for caption,size,field,table,type,decimals,associate_control in column_property:
            self.__layout.append((caption,size))
            if associate_control:
                self.associate_control.append((associate_control,col))
            self.__field_property.append((field,table,type,decimals))
            col=col+1

        
    def SetLayout(self):
        ''' SetLayout(self)
            setta il layout della lista dalle specifiche contenute 
            in self.__layout
            (caption="",size=-1)
        '''
        # setto il layout
        col=0
        for caption,size in self.__layout:
            if size==None:
                w,h=self.GetTextExtent(caption)
                w=w+15
            elif size== -1:
                w=-1
            elif size==0:#controllare se c'e' la caption"" cosa fa dlg_sze
                w=0
            else:
                w=wx.DLG_SZE(self,size,-1)[0]+15
                
            self.InsertColumn(col, caption,w)
            col=col+1
            
                
                
    def PopulateList(self):
        '''prepara il layout della griglia e la riempie'''
        
        self.SetLayout()
        self.LoadRecords()
        
    def LoadRecords(self,sql=None):
        if not sql:
            if self.__rows:#####rivedere
                rows=self.__rows
            else:
                rows = util.eseguiSql(self.__sql,1)
        else:
            rows = util.eseguiSql(sql,1)
        for row in rows:
            self.LoadRow(row)#carica le righe
        self.__currentItem = 0
                
    def LoadFromAssociateControl(self,inCurrentRow=False):#row=None):
        '''LoadFromAssociateControl riempie le celle della lista
            se row=None crea una nuova riga
            altrimenti se c'e sostituisce la riga row con 
            i valori dei controlli associati'''
        #preparo la riga
        data=[""]*self.GetColumnCount()
        for control,id in self.associate_control:
            #####print control
            val=control.GetValue(format=False)
            
            if val==False:
                return False#errore nei dati nei textbox ecc..
            else:
                
                data[id]=val
        self.LoadRow(data,inCurrentRow)
        return True
                

            
    def LoadRow(self,data,inCurrentRow=False): 
        if  inCurrentRow:
            row=self.__currentItem
            firstCol=0
        else:             
            row = self.GetItemCount()
            self.InsertStringItem(row, str(data[0]))
            firstCol=1
        for i in range(firstCol,self.GetColumnCount() ):
            self.SetStringItem(row, i, str(data[i]))
       
    def DeleteRow(self):
        self.DeleteItem(self.__currentItem)

    def SumCol(self,col_index):
        ret=0
        for i in range(0,self.GetItemCount()):
            ret=ret+ float(self.getColumnText(i,col_index))
        return ret
    def GetInsertSql(self):
        #prepara la struttura della lista
        #self.__field_property.append((field,table,type,decimals))
##        record=[]
##        for col in range(0,self.GetColumnCount()
##            self.__field_property[col][2]#controllo se vanno le virgolette
        rows=[]
        record=[]
        for row in range(0,self.GetItemCount()):
            for col in range(0,self.GetColumnCount()):
                table=self.__field_property[col][1]
                field=self.__field_property[col][0]
                if table:
                    if self.__field_property[col][2]==types.StringType:
                        
                        data="'%s'"%self.getColumnText(row,col)
                    else:
                        data="%s"%self.getColumnText(row,col)
                    record.append((table,(field,data)))
            rows.append(record)
            record=[]
        #print rows
        return util.createSqlInsert(rows)
    def Clear(self):
        self.ClearAll()
        self.SetLayout()
        pass
# #################################
# #################################



class listdialog(wx.Dialog):
    def __init__(self,parent,sql=None,layout=None,return_values=None,rows=None,titolo=""):
        wx.Dialog.__init__(self, 
                            parent=parent,
                            size = wx.Size(600,400), 
                            style = wx.DEFAULT_DIALOG_STYLE,
                            title=_("Cerca per")+" %s..."% titolo)

        self.Center(wx.BOTH) 
        
        self.list = nList(self,-1,wx.Point(5,10),wx.Size(580,305),layout=layout,return_values=return_values,rows=rows)
        self.Bind(EVT_SELECTED,self.selected,self.list)
        self.list.PopulateList()
        
        self.bt_ok = wx.Button(self,-1,"",wx.Point(130,330),wx.Size(125,30))
        self.bt_ok.SetLabel(_("&Ok"))
        self.Bind(wx.EVT_BUTTON,self.OnOK,self.bt_ok)
        
        self.bt_annulla = wx.Button(self,-1,"",wx.Point(290,330),wx.Size(105,30))
        self.bt_annulla.SetLabel(_("&Annulla"))
        self.Bind(wx.EVT_BUTTON,self.OnAnnulla,self.bt_annulla)
        


    def OnOK(self,event): 
        self.list.OnDoubleClick(0)
        
    def OnAnnulla(self,event):
        self.Destroy() 

    def selected(self,var):
        self.GetParent().selected(var.GetValue())
        self.Destroy()


class listpanel(wx.Panel):
    def __init__(self,parent,sql=None,layout=None,return_values=None,rows=None,titolo="",princ=-1):
        wx.Panel.__init__(self, 
                            parent=parent,id=-1,
                            size = wx.Size(900,400)) 
                            #style = wx.DEFAULT_DIALOG_STYLE,
                            #name="Cerca per %s..."% titolo)

        #self.Center(wx.BOTH) 
        self.princ=princ
        self.list = nList(self,-1,wx.Point(5,10),wx.Size(880,305),layout=layout,return_values=return_values,rows=rows)
        self.Bind(EVT_SELECTED,self.selected,self.list)
        self.list.PopulateList()
        
        self.bt_ok = wx.Button(self,-1,"",wx.Point(130,330),wx.Size(125,30))
        self.bt_ok.SetLabel(_("&Ok"))
        self.Bind(wx.EVT_BUTTON,self.OnOK,self.bt_ok)
        
        self.bt_annulla = wx.Button(self,-1,"",wx.Point(290,330),wx.Size(105,30))
        self.bt_annulla.SetLabel(_("&Annulla"))
        self.Bind(wx.EVT_BUTTON,self.OnAnnulla,self.bt_annulla)
        self.list.Fit()
        self.Fit()


    def OnOK(self,event): 
        self.list.OnDoubleClick(0)
        
    def OnAnnulla(self,event):
        self.Destroy() 

    def selected(self,var):
        self.princ.selected(var.GetValue())
        self.Destroy()





# ################
# ###############
#tutti i controlli di  scelta wx e tutti i controlli n se settati
#richiameranno questo evento 
myEVT_GEN_CONTROL = wx.NewEventType()
EVT_GEN_CONTROL = wx.PyEventBinder(myEVT_GEN_CONTROL, 1)

myEVT_FROM_NPANEL_BUTTONS = wx.NewEventType()
EVT_FROM_NPANEL_BUTTONS= wx.PyEventBinder(myEVT_FROM_NPANEL_BUTTONS, 1)

myEVT_NPANEL_FOUND_RECORD = wx.NewEventType()
EVT_NPANEL_FOUND_RECORD= wx.PyEventBinder(myEVT_NPANEL_FOUND_RECORD, 1)

myEVT_NLIST_CONTROL = wx.NewEventType()
EVT_NLIST_CONTROL= wx.PyEventBinder(myEVT_NLIST_CONTROL, 1)
class nPanel(wx.Panel):
    def __init__(self, *args, **kwds):
        wx.Panel.__init__(self, *args, **kwds)
        self.controls=[]#contiene i nomi dei controlli collegati al database
        self.allControls=[]#contiene i nomi di tutti i controlli coinvolti da clear e enable
        self.whereFields=[]
        self.buttons=None
        self.sqlLoad=None
        self.embedded=False
        self.autoload=True
        self.autoSetOnSearch=True#serve per settare automaticamente i controlli 
                                #quando carica un record dalle ricerche
        

    def FindControl(self):
        '''cerca i controlli attinenti al database e li cataloga in self.controls
           collega i bottoni nuovo ecc alla funzione OnClickButtons
            collega tutti i wxButton alla funzione onClickWxButton 
            gli eventi dei bottoni vengono redirezionati al contenitore di nPanel
            e si crea la query sql per caricare il record da riguardare o passarla come parametro'''
        table=[]
        
        #print  self.__dict__.keys()
        for k in self.__dict__.keys(): 
            #print k                                        
            if k not in ("autoSetOnSearch","autoload","this","allControls","controls","embedded",'font', 'whereFields', 'sqlLoad',"buttons","thisown" ): 
                control=self.__dict__[k] 
                #print k                                 
                if control.GetClassName() in ("nTextCtrl","nComboBox","nRadioBox","nGenControl"):
                    if control.table:#se sono usati per il database devono avere table not none
                        self.controls.append(k)#soltanto controlli  IO database
                        if control.table not in (table):
                            table.append(control.table)#se e' una tabella diversa la mette nlla lista delle tabelle
                        if control.isKey:#campo chiave primaria
                            self.whereFields.append(k)
                    #field.append(" %s.%s "%(k,control.table))
                    
                    self.allControls.append(k)#aggiungo per operazioni clear enable ecc
                    
                    #se e' richiesto carica il dato salvato dall'ultima sessione
                    if control.remember_last_value:
                        self.SetLastValue(control)
                    #evento per la navigazione tra i controlli
                    #nGenControl e' scartato perche' non e' un derivato wx
                    if control.GetClassName() !="nGenControl":
                        self.Bind(wx.EVT_TEXT_ENTER,self.OnTextEnter,control)
                    
                ###### la lista inserirla in controls con table ecc ccc
                elif control.GetClassName()=="nList":
                    control.SetLayout() 
                    self.Bind(EVT_NLIST,self.RaiseListEvent,control)
                        
                elif control.GetClassName()=="nButtons":
                    self.buttons=control  
                    self.Bind(EVT_CLICK_ON_PANEL_BUTTONS,self.OnClickButtons,control)
                      
                elif control.GetClassName()=="nSearchButton":
                    self.allControls.append(k)#aggiungo per operazioni clear enable ecc
                    self.Bind(EVT_CLICK_SEARCH_BUTTON,self.OnSearch,control)
                    
                if control.GetClassName()=="wxButton":
                    self.Bind(wx.EVT_BUTTON,self.RaiseGenControlEvent,control)
                       
                elif control.GetClassName()in ("nComboBox","wxComboBox"):
                    self.Bind(wx.EVT_COMBOBOX,self.RaiseGenControlEvent,control)

        #self.sqlLoad="SELECT "+string.join(field,",")+" FROM "+string.join(table,",")
        if len(self.controls)>0:
            self.sqlLoad="SELECT "+string.join(self.controls,",")+" FROM "+string.join(table,",")
    
    
    def OnTextEnter(self,event):
        ''' navigazione tra i controlli'''
        event.GetEventObject().Navigate()
    
    def OnClickButtons(self,event):
        """redireziona le chiamate dei bottoni nuovo ecc
        """
        
        ev = util.MyEvent(myEVT_FROM_NPANEL_BUTTONS, self.GetId()) 
        ev.SetValue(event.GetValue())
        self.GetEventHandler().ProcessEvent(ev)
        
    def RaiseGenControlEvent(self,event):
        """redireziona le chiamate dei controlli di comando alla business logic
        """
        ######## controllare gli eventi
        ev = util.MyEvent(myEVT_GEN_CONTROL, self.GetId()) 
        #ev.SetValue(event.GetValue())
        ev.SetEventObject(event.GetEventObject())
        self.GetEventHandler().ProcessEvent(ev)

    def RaiseListEvent  (self,event):
        ev = util.MyEvent(myEVT_NLIST_CONTROL, self.GetId()) 
        ev.SetValue(event.GetValue())
        self.GetEventHandler().ProcessEvent(ev)
        
    def GetClassName(self):
        return "nPanel"
   
    def OnSearch(self,event):
        """OnSearch (self,dict event.GetValue()record ): 
            viene richiamata dai searchButton per comunicare 
            al form il record da caricare passa come parametro 
            una tupla con i valori per i campi chiave (nome_campo,valore)
            questi valori vengono inseriti nei giusti controlli con setValue"""
        self.SetValue(event.GetValue()) #qui o dentro la if ?
        
        if self.autoload:
            #aggiusta i bottoni
            self.Load()
                              
        ev = util.MyEvent(myEVT_NPANEL_FOUND_RECORD , self.GetId()) 
        ev.SetValue(event.GetValue())
        self.GetEventHandler().ProcessEvent(ev)
        
    def GetValue(self,state):
        """GetValue(self,state)->list((table,field,value))
            restituisce una lista con i valori pronti per dbData
            i dati restituiti sono quelli indicati dalle variabili
            self.table,self.whereFields
        """
        ret =[]
        for field in self.returnData:
            ret.append((self.table,field,self.__dict__[field].GetValue(state)))
        return ret
        #se returnData e' vuoto = tutti
        
    def SetValue(self,keys_e_value):
        """SetValue(self,keys_e_value)
        keys_e_value tupla ((campo,valore),)
        inserisce il valore nel controllo col nome del campo specificato
        """
        for field,value in keys_e_value:
            print "field %s  value %s "%(field,value)
            self.__dict__[field].SetValue(value)
            
    def Load(self):
        '''carica il record nel form
        viene creata la clausola where della query sql
        i controlli che contengono i parametri della where
        contengono gia' i valori
        '''
          
        where=""
        if len(self.whereFields)>0:
            where=" WHERE "
            for field in self.whereFields:
                where=where+" %s = %s AND"%(field,self.__dict__[field].GetValue())
            where=where[:-3]
        sql=self.sqlLoad+where
        row=util.eseguiSql(sql,0)
        if row:
            for field in row.keys():
                field1=field.lower()#i campi possono essere scritti in maiuscolo i controlli in minuscolo
                if self.__dict__.has_key(field1):
                    self.__dict__[field1].SetValue(row[field])
                    
        if self.autoSetOnSearch :
            self.buttons.SetState(SELECT)
            self.Enable(False,self.buttons.GetState())

    def Clear(self,state):
        """richiama Clear(self,state)per ripulire i controlli
        """
        for control in self.allControls:
            control=self.__dict__[control] 
            control.Clear(state)
            # ####################################### 
            # inserito nei controlli con default
            #if control.__dict__.has_key("remember_last_value"):
            #    if control.remember_last_value:
            #        self.SetLastValue(control)
                
    def SetLastValue(self,control):
        val=util.LoadLastValue(control.GetName())
        if control.type==types.IntType:val=int(val)
        #control.SetValue(val)
        control.default=val
        
    def Enable(self,enable,state):
        """abilita e disabilita i controlli
        """
        for control in self.allControls:
            self.__dict__[control].Enable(enable,state)
     


#########metodi
def GetValue(control,val,format):
    #se format e' false il controllo si comporta come un 
    #wxtextcontrol senza controllo della chiave ecc
    if format:
        if control.isNotNull and val =="":
                control.SetFocus()
                prnt = control.GetParent()
                m = prnt.FindWindowById(control.PrevControlId(control.GetId()))                   
                msg = _("Il campo") +"%s" + _("""deve essere\n 
                       obbligatoriamente riempito """) % m.GetLabel() 
                util.alert(control.GetParent(),msg,_("Errore nell'immissione dei dati"))
                ret = False
        else:
            ret=val
            if control.type == types.StringType:
                ret="'%s'" % val
    else:
        ret=val
    return ret



