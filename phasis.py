#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
#
#  Copyright (C) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 
#                2008, 2009, 2010, 2011, 2012, 2013
#                2014 Massimo Gerardi all rights reserved.
#
#  Author: Massimo Gerardi massimo.gerardi@gmail.com
#
#  Copyright (c) 2013 Qsistemi.com.  All rights reserved.
#
#  Viale Giorgio Ribotta, 11 (Roma)
#  00144 Roma (RM) - Italy
#  Phone: (+39) 06.87.163
#  
#
#  Si veda file COPYING per le condizioni di software.
#
#   www.qsistemi.com - italy@qsistemi.com
#

#
#  COPYRIGHT
#  I diritti e i copyright relativi a Qsistemi, la documentazione 
#  elettronica e l'eventuale materiale stampato accluso e 
#  qualsiasi copia del Prodotto Software sono di proprieta' del 
#  Produttore. Il titolo e i diritti sulla proprieta' intellettuale
#  relativi a contenuti cui l'Utilizzatore puo' accedere mediante 
#  l'utilizzo di Qsistemi sono di proprieta' dei rispettivi titolari 
#  e possono essere tutelati dal copyright o da altre leggi e 
#  trattati sulla proprieta' intellettuale.
#
#  LIMITAZIONE DELLA RESPONSABILITA'
#  Il software e' fornito "COSI' COM'E'", senza garanzie di ogni sorta.
#  Il Produttore, ed i propri rivenditori o distributori non riconoscono 
#  alcuna garanzia, espressa o implicita, di idoneità del software ad un 
#  fine particolare. 
#  SONO ESCLUSE QUALSIASI RESPONSABILITA' E RIMBORSO DANNI PER PERDITA DI 
#  INFORMAZIONI GESTITE DAL SOFTWARE E/O DA ELABORAZIONI E/O CALCOLI 
#  EFFETTUATI IN MODO IRREGOLARE.
#  IN NESSUN CASO IL PRODUTTORE, I SUOI RIVENDITORI O DISTRIBUTORI, POSSONO 
#  VENIR RITENUTI RESPONSABILI PER LA PERDITA DI PROFITTO O QUALSIASI ALTRA 
#  CONSEGUENZA, SPECIALE, INDIRETTA, INCIDENTALE, PUNITIVA O ALTRI DANNI CHE 
#  POTESSERO INTERVENIRE CON L'USO DEL PRODOTTO.
#
#  Si veda file COPYING per le condizioni di software.
#
#   www.qsistemi.com - info@qsistemi.com
#

import encodings.utf_8 ########da aggiunfere per la 0.9.7-7
#import gettext
#gettext.install('phasis') #, '/usr/share/locale', unicode=1)
import os
import sys

# aggiunge il path della directory di phasis per la ricerca dei moduli
path_work = os.path.abspath(os.path.dirname(sys.argv[0]))
#print path_work
#path_work="/opt/phasis/phasis/phasis/"
sys.path.append(os.path.join(path_work,"phasis"))

import gettext
# imposta la lingua
# valori possibili:
#
# lingua it = italian
# lingua de = german
# lingua en = english
# lingua es = spanish
# lingua fr = french
# lingua pl = polish
# lingua pt = portuguese
# lingua ro = romanian
#
lingua = 'it' # 'it' #codice di poedit
nazione = 'IT' # 'IT' # per il momento la nazione e' uguale alla lingua ma con lettere maiuscole, codice di poedit
file_i18n='phasis'+'-'+lingua+'_'+nazione #+'.mo'
path_i18n=os.path.join(path_work,"i18n")
lang=gettext.translation(file_i18n, path_i18n, languages=[lingua])
lang.install(unicode=True) #file_i18n, path_i18n) #, unicode=True)


#path_work="/opt/phasis/phasis/phasis/"
# esegue l'applicazione principale
import appmain
appmain.main()
