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



from reportlab.lib.pagesizes import *

def layout():
    return portrait((600, 799))

def struttura (c):
    c.setLineWidth(1)
    c.setFont('Helvetica',14)
    c.drawString(63,685, _("Codice ......................"))
    c.drawString(63,664, _("Descrizione ..............."))
    c.drawString(63,641, _("UM ............................"))
    c.drawString(63,619, _("Imponibile .................."))
    c.drawString(63,594, _("Prezzo ......................."))
    c.drawString(63,572, _("Costo ........................"))
    c.drawString(63,550, _("Cat. Merce ................"))
    c.drawString(63,529, _("Aliq IVA ....................."))
    c.drawString(63,505, _("In Prod ......................"))
    c.drawString(63,482, _("QT min ......................"))
    c.drawString(63,460, _("QT max ....................."))
    #c.drawString(63,440,"Misura .....................")
    c.setFont('Helvetica',16)
    c.drawString(63,734,_("Scheda  Articolo"))
    c.rect(42,720,503,-450,1,0)
    c.drawString(64,413,_("Note:"))

def testata (c,row):
    c.setFont('Helvetica',14)
    c.drawString(230,685,str(row['codart']))
    c.drawString(230,664,str(row['descrizart']))
    c.drawString(230,641,str(row['umart']))
    c.drawString(230,619,str(row['prezzo_1']))
    c.drawString(230,594,str(row['prezzo_2']))
    c.drawString(230,572,str(row['costo']))
    c.drawString(230,529,str(row['merce']))
    c.drawString(230,505,str(row['alivaart']))
    c.drawString(230,482,str(row['inprod']))
    c.drawString(230,460,str(row['qt_min']))
    c.drawString(230,440,str(row['qt_max']))
    #c.drawString(230,550,str(row['mis']))
    c.rect(42,752,266,-27,1,0)
    c.drawString(65,389,str(row['note']))

def querytestata ():
     return """ select cod as codart, descriz as descrizart, um as umart, 
                round(prezzo_1,6) as prezzo_1,round(prezzo_2,6) as prezzo_2,
                round(costo,6) as costo, merce as merce, aliva as alivaart, 
		inprod as inprod, qt_min as qt_min, 
		qt_max as qt_max, note as note from articoli where  cod = '%s' """

def Ycorpo ():
     return 1
