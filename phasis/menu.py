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



########################################################################
#
# Questo file di configurazione del menu a breve verra' eliminato
# ed inserito nel database azienda
#
########################################################################

import string
import sys
import os.path
import wx

path_work = os.path.abspath(os.path.dirname(sys.argv[0]))

import ConfigParser
cfg = ConfigParser.ConfigParser()

if os.path.isfile(os.path.join(path_work,"defaultset.cfg")):
    cfg.read(os.path.join(path_work,"defaultset.cfg"))
else: cfg.read(os.path.join(path_work,"default.cfg"))


#cfg.read(os.path.join(path_work,"default.cfg"))


MENUbar = ("base",_("&Base")), ("cont",_("&Contabilita`")), ("vend",_("&Vendite")),\
                        ("maga",_("&Magazzino")), ("ordi",_("&Ordini")),\
                        ("stru",_("&Utilita`")), ("help",_("&Help"))


#******************************************************************************
# 0 modulo ggestito da MDI sia a tab che frame
# 3 module gestito da MDI ma gestito da solo (si autocostruisce il frame)
# 4 modulo autonomo solo eseguito da MDI ma non gestito dallo stesso (in modalita' modal)
#******************************************************************************
# Imposta Voci menu

MENU = {
"base": (
(1001,_("Anagrafica &Articoli\tF11"),
      _("Inserimento e Modifica Anagrafica Articoli"),"base", 
      "articoli", _("Anagrafica Articoli"), "1", "A","","0"),
(1002,_("Anagrafica &Clienti\tF12"),
      _("Inserimento e Modifica Anagrafica Clienti"), "base", 
      "anag", _("Anagrafica Clienti"), "0", "C","","0"),
(1003,_("Anagrafica &Fornitori\tCtrl+F"),
      _("Inserimento e Modifica Anagrafica Fornitori"),"base",
      "anag", _("Anagrafica Fornitori"),"1","F","","0"),
(1020,"","","","","","0","","-","3"),
(1021,_("Lista Articoli"), _("Lista Articoli"),"base", 
      "lstart", _("Lista Articoli"), "1", "A","","0"),
(1022,_("Lista Clienti"),_("Lista Clienti"), "base", 
      "lstanag", _("Lista Clienti"), "0", "C","","0"),
(1023,_("Lista Fornitori"), _("Lista Fornitori"), "base",
      "lstanag", _("Lista Fornitori"), "2", "F","","0"),
(1030,"","","","","","0","","-","3"),
#(1031,"Seleziona A&zienda\tCtrl+Z", "Seleziona Azienda","",
#      "selaz","Seleziona Azienda","3","Z","","3"),
(1032,_("Anagrafica Azienda"), _("Inserimento e Modifica Anagrafica Azienda"), "base",
      "azienda", _("Anagrafica Azienda"), "1", "Z","","0"),

(1040,_("Archivi Contabili"), _("Archivi Contabili"),"", 
      "", _("Archivi Contabili"), "1","", "+","0"),
(1041,_("Codici I.V.A."), _("Codici I.V.A."), "base", 
      "tabgen", _("Codici I.V.A."), "1", "ALIVA", "sub","0"),
(1042,_("Condizioni Pagamento"), _("Condizioni Pagamento"), "base",
      "tabgen", _("Condizioni Pagamento"), "1", "PAGAM", "sub","0"),
(1043,_("Causali Contabili"), _("Causali Contabili"), "base",
      "tabgen", _("Causali Contabili"), "9", "CONTAB", "sub","0"),
(1050,_("Categoria Merceologica"), _("Categoria Merceologica"), "base",
      "tabgen", _("Categoria Merceologica"), "1", "MERCE", "sub","0"),      
##(1051,"Gestione Listini","Gestione Listini","base","GestLst","Gestione Listini","3","C"),
(1080,"","","","","","0","","-","3"),
#(1081,"Calcolatrice","Calcolatrice","","","","9","EXEC",""),
(1081,_("Calcolatrice"), _("Calcolatrice"), "base",
      "calcola", _("Calcolatrice"), "1", "","","3"),
(1090,"","","","","","0","","-","3"),
#(9999,"E&sci", "Consente di uscire dalla procedura","","","OnExit","0","CLOSE","","3") ),
(wx.ID_EXIT,_("Te&rmina Sessione"), _("Consente di uscire dalla sessione corrente"),"","","OnExit","0","CLOSE","","3") ),
#(wx.ID_EXIT  5006,"Te&rmina Sessione", "Consente di uscire dalla sessione corrente","","","OnExit","0","CLOSE","","3") ),

"cont": (
(2001,"&Gestione Movimenti", "Inserimento e Modifica Movimenti", "cont",
      "movcon", "Gestione Movimenti", "3","","","0"),
(2002,"&Lista Movimenti", "Lista dei Movimenti", "cont",
      "lstcon", "Lista Movimenti", "0","","","0"),
(2004,"Stampa &Schede", "Stampa delle schede", "cont",
      "stpskcon","Stampa delle schede", "2","","","0"),
(2013,"Stampa &Movimenti", "Stampa dei Movimenti", "cont",
      "rmovcon","Stampa dei Movimenti", "2","","","0"),

(2005,"Inserimento &Fatture Acquisto/Vendita",
      "Inserimento e Modifica Documenti","cont",
      "genmov","Inserimento  Documenti","9","","","0"),

(2003,"","","","","","0","","-","3"),

(2008,"&Scadenzario","Scadenzario",
      "cont","lstscad","Scadenzario","3","","","0"),

(2009,"&Gestione Scadenzario","Gestione Scadenzario",
      "cont","scad","Gestione Scadenzario","3","","","0"),

(2010,"&Aggiungi Scadenze","Agiungi Scadenze",
      "cont","scadenze","Aggiungi Scadenze","3","SCAD","","0"),

(2011,"&Stampa Scadenze","Stampa Scadenze",
      "cont","rscad","Stampa Scadenze","3","","","0"),
   

(2012,"","","","","","0","","-","3"),


#(2005,"Inserimento Prima Nota","Inserimento e Modifica Prima Nota","cont","","Prima Nota","9","",""),
#(2006,"","","","","","0","","-"),
#(2007,"Elaborazioni &Periodiche","Elaborazioni Periodiche","cont","","","9","",""),
(2006,"Chiusura Anno contabile",
      "Procedura Chiusura Anno Contabile","cont",
      "closecon","Chiusura Anno Contabile","0","","","0"),
(2007,"Libro &Giornale", "Stampa del Libro Giornale","cont","","","9","","","0")),

"vend": (
(3001,_("&Gestione Documenti\tF4"),_("Inserimento e Modifica Documenti"),"vend",
      "vendite", _("Gestione Documenti"), "3","","","0"),
(3002,_("&Lista Documenti"), _("Lista dei Documenti"), "vend",
      "lstvend", _("Lista Documenti"), "3","","","0"),
(3003,"","","","","","0","","-","3"),
#(3004,"Genera Fatture", "Generazione delle Fatture", "vend",
#      "gendocb", "Genera Fatture", "3","",""),
(3004,_("Genera Fatture"), _("Generazione delle Fatture"), "vend",
      "gendocf", _("Genera Fatture"), "3","","","0"),
#(3005,"Stampa Documenti", "Stampa dei Documenti", "vend","","", "9","",""),
(3010,"","","","","","0","","-","3"),
(3011,_("Anagrafica &Agenti"), _("Inserimento e Modifica Anagrafica Agenti"),"base",
      "anag", _("Anagrafica Agenti"), "3", "A","","0"),
(3012,_("Lista A&genti"), _("Lista Agenti"), "base", 
      "lstanag", _("Lista Agenti"), "0", "age","","0")),

"maga": (
(5001,_("&Gestione Movimenti\tF5"),_("Inserimento e Modifica Movimenti"),"maga",
      "movmag", _("Gestione Movimenti"), "3", "M","","0"),
(5002,_("&Lista Movimenti"),_("Lista dei Movimenti"),"maga",
      "lstmov", _("Lista Movimenti"), "3", "M","","0"),
# 5006 va lasciata libera perche' predefinita da wx.ID_EXIT per menu mac
(5010,"","","","","","0","","-","3"),
(5011,_("Elaborazioni &Periodiche"), _("Elaborazioni Periodiche"), "maga",
      "","","9","","","0"),
(5012,_("Stampa &Inventario"), _("Stampa Inventario"), "maga",
      "inventa", _("Stampa Inventario"), "3", "M","","0"),
# 5013 va lasciata libera perche' predefinita da wx.ID_ABOUT per menu mac
(5014,_("Chiusura Ma&gazzino"), _("Chiusura Magazzino"), "maga","","","6","","","0"),
(5015,_("Chiusura &Annuale"),_("Chiusura Magazzino"),"maga","","","9","","","0")),

"ordi": (
(6001,_("Ordini &Clienti\tCtrl+O"),_("Inserimento e Modifica Ordini Clienti"),"ordi",
      "ordini", _("Ordini Clienti"), "2","OC","","0"),
(6002,_("&Lista Ordini Clienti"), _("Lista Ordini Clienti"), "ordi",
      "lstord", _("Lista Ordini Clienti"),"2","OC","","0"),
(6003,_("Genera Documenti"), _("Generazione Documenti"), "ordi",
      "gendoc", _("Genera Documenti"),"3","OC","","0"),
(6004,"","","","","","0","","-","3"),
(6005,_("Offerte &Clienti"),_("Inserimento e Modifica Offerte Clienti"),"ordi",
      "ordini", _("Offerte Clienti"), "2","PC","","0"),
(6006,_("&Lista Offerte Clienti"), _("Lista Offerte Clienti"), "ordi",
      "lstord", _("Lista Offerte Clienti"),"2","PC","","0"),
(6011,"","","","","","0","","-","3"),
(6012,_("Ordini Fornitori"),_("Inserimento e Modifica Ordini Fornitori"), "ordi",
      "ordini",_("Ordini Fornitori"),"0","OF","","0"),
(6013,_("Lista Ordini Fornitori"), _("Lista Ordini Fornitori"), "ordi",
      "lstord", _("Lista Ordini Fornitori"),"0","OF","","0"),
(6020,"","","","","","0","","-","3"),
(6021,_("Offerte Fornitori"),_("Inserimento e Modifica Offerte Fornitori"), "ordi",
      "ordini",_("Offerte Fornitori"),"0","PF","","0"),
(6022,_("Lista Offerte Fornitori"), _("Lista Offerte Fornitori"), "ordi",
      "lstord", _("Lista Offerte Fornitori"),"0","PF","","0")), 

"stru": (
(7001,_("Salvataggio Dati"), _("Salvataggio dei Dati"), "utils",
      "backup", _("Salvataggio Dati"),"9","","","3"),
(7010,"","","","","","0","","-","3"),
(7011,_("Importa Listino"),_("Importa listino articoli"),"utils",
      "impart", _("Importa listino articoli"),"9","articoli","","3"),
(7012,_("Esporta Listino"), _("Esporta Listino"), "utils","","","9","","","3"),
(7016,_("Importa Dati"), _("Importa Dati"), "utils",
       "impdati",_("Importa dati"),"9","","","3"),#},
#(7018,"Importa dati (TabGen)","Importa dati (TabGen)","utils","instabgen","Importa dati (TabGen)","1","","")),
#(7017,"Esporta dati (MovMag)","Esporta dati (MovMag)","utils","expmovmag","Esporta dati (MovMag)","1","",""),
#(7018,"Update articoli  (MovMag)","Update articoli (MovMag)","utils","upmagart","Update articoli (MovMag)","1","","")),
(7018,_("Importa dati (MovMag)"),_("Importa dati (MovMag)"),"utils","insmovmag",_("Importa dati (MovMag)"),"9","","","3")),
#(7019,"Importa dati (Articoli)","Importa dati (Articoli)","utils","imparticoli","Importa dati (Articoli)","1","","")),
##(7017,"Riorganizza TabGen ","Riorganizza Tabella Genenerale","Utils","RevTabGen","","9","gen",""),

"help": (
(8001,_("Guida di Phasis"), _("Visualizza la guida dell'applicazione"), "help",
      "","","3","PDF","","3"),
(8020,"","","","","","0","","-","3"),
(8021,_("Supporto sul Web"), _("Supporto di Phasis"), "help",
      "http://www.phasis.it/index.php?Supporto","","3","URL","","3"),
(8030,"","","","","","0","","-","3"),
(8031,_("Informazioni su Phasis"),_("Informazioni su Phasis"),"help",
      "about","","0","ABOUT","","3"))
#(wx.ID_ABOUT  5013,"Informazioni su Phasis","Informazioni su Phasis","help",
#      "info","","0","Z","","3"),   
#(8020,"","","","","","0","","-","3"))  
        }  

           
TOOLBAR = (
(1001,"articoli.png|"+ _("Articoli")+"|||title|1|"),
(1002,"clienti.png|"+ _("Clienti")+"|||title|1|"),
(1003,"fornitori.png|"+ _("Fornitori")+"|||title|1|"),
(0,"-|||||0|"),
(2001,"cassa.png|"+ _("Gestione Movimeti")+"|||title|1|"),
(3001,"documenti.png|"+ _("Gestione Documenti")+"|||title|1|"),
(5001,"magazzino.png|"+ _("Gestione Magazzino")+"|||title|1|"),
(6001,"ordini.png|"+ _("Gestione Ordini")+"|||title|1|"),
(0,"-|||||0|"),
(1081,"calcola.png|"+ _("Calcolatrice")+"|||title|1|"),
(0,"-|||||0|"),
(8001,"aiuto.png|"+ _("Guida di Phasis")+"|||title|1|"),
(8031,"info.png|"+ _("Informazioni su Phasis")+"|||title|1|"),
(0,"-|||||0|"),
(wx.ID_EXIT,"uscita.png|"+ _("Termina sessione")+"|||title|1|") #sistemare l'ordine in base all'inserimento
#10020:("-|||||0|"),
#10021:("filenew.png|File|||title|1|"),
#10022:("editdelete.png|Taglia|||title|1|"),
#10023:("editcopy.png|Copia|||title|1|"),
#10024:("editpaste.png|Incolla|||title|1|"),
#10030:("-|||||0|"),
#10031:("filefind.png|Cerca|||title|2|"),
#10032:("fileprint.png|Stampa|||title|2|"),
#10033:("list.png|Preferenze|||title|4|"),
#10034:("help.png|Aiuto|help|info|Informazioni su :|2|azi"),
        ) 



# barra dei pulsante in basso
# (idmenu,"Label Pulsanet|Tooltip|")  N.B. Nella Label va indicato lo stesso tasto di accerelazione indicato nel menu.

BUTTONSBAR = (
(1001,_("F11 Articoli") +"|"+ _("Archivio articoli")+"|"),
(1002,_("F12 Clienti")+"|" + _("Archivio Clienti")+"|"),
(2001,_("F4 Fatture")+"|" + _("Gestione Fatture")+"|"),
(5001,_("F5 Magazzino")+"|" + _("Gestione Magazzino")+"|"),
        ) 




