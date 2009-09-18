#!/usr/bin/env python
#
# Project       Phasis
#
# Description
# Gestionale Aziendale Open Source Phasis (R)
#
#*  Copyright (C) 2003 - 2007  Phasis - http://www.phasis.it/
#   Author: Massimo Gerardi <m.gerardi@mgsoft.it>
#   Via Michele Rosi 184 - Aranova (RM)
#   00050 Aranova (Roma) - Italy
#   tel. +39 06 6674756 - fax +39 06 6674756
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
