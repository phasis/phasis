# Copyright (C) 2003 - 2006  Phasis - http://www.phasis.it/
#
# Released under the terms of the GNU General Public License
# (version 2 or above)
#
# See COPYING for details.


########################################################################
#
# Questo file di configurazione deve essere rivisto con la possibilita'
# che in futuro si possa eliminare
# contiene riferimento delle directory e dimensioni dei form e tasti
#
########################################################################

import wx
import os
import sys


path_work = os.path.abspath(os.path.dirname(sys.argv[0]))

sys.path.append(os.path.join(path_work,"phasis","base"))
sys.path.append(os.path.join(path_work,"phasis","cont"))
sys.path.append(os.path.join(path_work,"phasis","maga"))
sys.path.append(os.path.join(path_work,"phasis","vend"))
sys.path.append(os.path.join(path_work,"phasis","ordi"))
sys.path.append(os.path.join(path_work,"phasis","inte"))
sys.path.append(os.path.join(path_work,"phasis","utils"))
sys.path.append(os.path.join(path_work,"phasis","finc"))
# l'ultimo campo di join "" serve per inserire anche
# il '/' o '\' a seconda del s.o.
#if wx.Platform == '__WXMAC__': 
#   path_db = os.path.join("/Users","alessandro","Documents","data","")
#else:
path_db = os.path.join(path_work,"data","")  
path_budb = os.path.join(path_work,"data.bak","") 
path_utils = os.path.join(path_work,"phasis","utils","")
path_tmp = os.path.join(path_work,"tmp","")
path_logs = os.path.join(path_work,"logs","")
path_spool = os.path.join(path_work,"spool","")
path_img = os.path.join(path_work,"images","")
path_finc = os.path.join(path_work,"phasis","finc","")

if os.path.isfile(os.path.join(path_work,"phasis","menuset.py")):
    from menuset import*
else: from menu import*

try:
    pathdb = cfg.get('Dbase','dirDB')
    if pathdb != 0: path_work = pathdb
except: 
    pass


path_db = os.path.join(path_work,"data","")
path_budb = os.path.join(path_work,"data.bak","")




# from menu import*

from time import *


# impostazione dei colori
# cambia colore del panel flag 0=non cambiare nulla - 1=cambia colori
if wx.Platform == '__WXMSW__': FLAGCOLORPANEL=1
else: FLAGCOLORPANEL=0

#colore del panel
PANELCOLOR=wx.Colour( 236, 233, 216) #wx.LIGHT_GREY

#colore dello sfondo
SFONDOCOLOR=SFONDOCOLOR=wx.Colour( 236, 233, 216)# wx.WHITE

# dimensione del font di default

#wx.SystemSettings_GetFont(wx.SYS_DEFAULT_GUI_FONT)
DIMFONTDEFAULT=12

# FONTFISSO: 0 oppure da 12 in su .... forza il font alla dimensione indicata a meno che il valore sia 0
FONTFISSO=12

# imposta dimensioni form
if wx.Platform == '__WXMSW__': 
    NTBKH=680
    NTBKV=420
    NTBKH1=540
    NTBKV1=260
    _COLSZ0_=0
elif wx.Platform == '__WXMAC__': #arrangiamento per problemi visualizzaione su mac in attesa 0.9.8 
    NTBKH=680
    NTBKV=420
    NTBKH1=540
    NTBKV1=260
    _COLSZ0_=-10
else:
    NTBKH=850 #NTBKH_lnx
    NTBKV=480
    NTBKH1=650 #NTBKH1_lnx
    NTBKV1=280
    _COLSZ0_=-10

NTBKH1TUTTI=540
NTBKV1TUTTI=240 #330
NTBKHTUTTI=680
NTBKVTUTTI=420


# imposta dimensioni tasti
btnSzeLH = 50
btnSzeL1H = 60
btnSzeV = 12
btnSzeMH = 40
btnSzeM1H = 20
btnSzeSH = 12
btnSzeS1H = 6
btnSzeDH = 10

tipodoc = cfg.get('ModuloFRM','Tipodoc')
tipodoc_lst = cfg.get('ModuloFRM','Tipodoc_lst')
tipodocGDoc = cfg.get('ModuloFRM','TipodocGDoc') 
tipopagam = cfg.get('ModuloFRM','Tipopagam')
cdecPZ = int(cfg.get('DecimalPZ','Number')) 
cdecQT = int(cfg.get('DecimalQT','Number'))
cdec = int(cfg.get('Decimal','Number'))
cntDB = cfg.get('Dbase','cntDB')
logofinc = cfg.get('LogoFinc','logofinc')
toolbar = int(cfg.get('ToolBar','toolbar'))
buttonsbar = int(cfg.get('ButtonsBar','buttonsbar'))
smtp_server = cfg.get('InvFaxMail','smtp_server')
mail_mittente = cfg.get('InvFaxMail','mail_mittente')

date = strftime("_%d%m%Y")
mesi=('gennaio','febbraio','marzo','aprile','maggio','giugno',
        'luglio','agosto','settembre','ottobre','novembre','dicembre')

# voci bottoni
vcexp = "Es&porta"
vcnewr = "Nuova &Riga"
vcokr = "Con&ferma Riga"
vcmodir = "Modifica &Riga"
vcintr = "&Interrompi"
vcdeler = "&Elimina"
vcconf = "Con&ferma"
vcselez = "&Seleziona"
vcnew = "&Nuovo"
vcok = "&Ok"
vcall = "Tutti"
vcjoin = "&Unisci"
vcint = "&Interrompi"
vccanc = "&Chiudi"
vcmodi = "&Modifica"
vcdele = "Cance&lla"
vcscheda = "Sche&da"
vcstampa = "&Stampa"
vcanag = "&Anagrafica"
vcstpcont = "Con&tabile"
vcinvfax = "&Invia fax"
vcdemo = "&Versione Demo"
vcselfl = "&Trova File"
vcCONF = "Confermato"
vcPREV = "Previsione"
vcDETT = "Dettaglio"
vcSEMP = "Semplice"
vcFATT = "Fattura accompagnatoria"
vcBOLL = "Documento di trasporto(DDT)"
vcEVA = "Consolidato"
vcNOEVA = "Da Consolidare"
vcttlWEEK = "Salvataggio settimanale"
vcttlMONTH = "Salvataggio mensile"
vcclose = "&Chiudi"
vcexit = "&Esci"

# voci messaggi predefiniti
msgselfl = "Seleziona il file"
msgselflimp = "ATTENZIONE file gia' importato !"
msgint = "ATTENZIONE Dati presenti Vuoi proseguire ? "
msgass = "ATTENZIONE Dati assenti "
msgesci = "Vuoi Uscire Adesso ? "
msgdatonull = "Nessun dato trovato "
msgdatonocons = "Nessun dato da consolidare "
msgordicons = "ATTENZIONE ordine gia' consolidato "
msgstampanull = "Nessun dato da stampare "
msgdelrow = "Vuoi eliminare la riga ? "
msgnocod = "Codice non valido "
msgmodi_doc = "Vuoi modificare il Documento ?"
msgmodi_anag = "Vuoi modificare l'Anagrafica ?"
msgdele_anag = "Vuoi eliminare l'Anagrafica ?"
msgmodi_tbl = "Vuoi modificare la tabella ?"
msgnodele_valtbl = "ATTENZIONE volete cancellare il valore della tabella"
msgdele_valtbl = "Vuoi eliminare il valore della tabella ?"
msgdele_tbl = "Vuoi eliminare la tabella ?"
msgprezno = "ATTENZIONE Prezzo non valido "
msgimportono = "ATTENZIONE Importo non valido "
msgdiffno = "ATTENZIONE Differenza non valida \rProseguire ugualmente ?  "
msgcostono = "ATTENZIONE Costo non valido "
msgscno = "ATTENZIONE Sconto non valido "
msgqtno = "ATTENZIONE Quantita' non valida "
msgfnd = "ATTENZIONE Raffinare la ricerca record trovati --> "
msgdatault = "Data inferiore all'ultima registrazione \rProseguire ugualmente ? "
msgdatacont = "Data non compresa nell'esercizio contabile !"
msgdatra = "Data inferiore alla data del documento \rProseguire ugualmente ? "
msgdataes = "Data non compresa nell'esercizio "
msgdatano = "Data non valida "
msgdatono = "Valore non valido "
msgdatosi = "ATTENZIONE dato gia' presente "
msgcmp_null = "ATTENZIONE Campo vuoto"
msgnodele_anag ="""ATTENZIONE impossibile cancellare l'Anagrafica perche'
\rpresenta progressivi nell'esercizio contabile """
msgpwdno = "ATTENZIONE Password Errata "
msgnomodulo = "ATTENZIONE modulo non abilitato "
msgnoaz = "ATTENZIONE non e' stata selezionata l'azienda di lavoro "
msgimpend=" Importazione dei dati terminata  "
msgfileno = "ATTENZIONE impossibile trovare il file : \n "
msgazzarchivi = """ATTENZIONE con questa funzione si azzera il contenuto esistente
\n per poi importare i dati nuovi. """
msgconsdoc = "ATTENZIONE si vuole consolidare i documenti selezionati ? "
msgnodele_doc = "ATTENZIONE con questa funzione elimina il Documento "
msgdele_doc = "Vuoi eliminare il Documento ?"
msgelab = " Elaborazione in corso "
msgconferma = " Confermi l'operazione ? "
msgconfimport = " Confermare l'operazione di importazione"
msgmodstampa = " Controllare se il Modulo di stampa\n e' inserito corettamente: "
msgstpno = "ATTENZIONE Stampa Annullata"
msgstpnull = 'Annullare la Stampa?'
msgopeno = "ATTENZIONE Errore nell'operazione eseguita  "
msgclose = "Per terminare la sessione devi prima chiudere tutte le finestre attive"

#voci documenti
vcCFM=['Cliente','Fornitore','Magazzino']
vcCF=['Cliente','Fornitore']
vcwstp="Anteprima di stampa"
vcpreve="PREVENTIVO"
vcpreven="Preventivo n. "
vcordine="ORDINE"
vcordinen="Ordine n. "

