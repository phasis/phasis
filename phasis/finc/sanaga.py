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

from reportlab.lib.pagesizes import *

def layout():
    return portrait((600, 799))

def struttura (c):
    c.setLineWidth(1)
    c.setFont('Helvetica',14)
    c.drawString(63,685,_("Cod. agente ..................................."))
    c.drawString(63,664,_("Ragione soc. (Cognome) ..............."))
    c.drawString(63,641,_("Ragione soc.  (Nome) ...................."))
    c.drawString(63,619,_("Indirizzo .........................................."))
    c.drawString(63,594,_("Localita` .........................................."))
    c.drawString(63,572,_("Zona ..............................................."))
    c.drawString(63,550,_("Cap ................................................."))
    c.drawString(63,529,_("Telefono ........................................."))
    c.drawString(63,505,_("Fax ................................................."))
    c.drawString(63,482,_("Mobile ............................................"))
    c.drawString(63,460,_("P. Iva .............................................."))
    c.drawString(63,440,_("Cod. Fisc ........................................"))
    c.setFont('Helvetica',16)
    c.drawString(63,734,_("Scheda  Agente"))
    c.rect(42,720,503,-450,1,0)
    c.drawString(64,413,_("Note:"))

def testata (c,row):
    c.setFont('Helvetica',14)
    c.drawString(285,685,str(row['COD']))
    c.drawString(285,664,str(row['RAG_SOC1']))
    c.drawString(285,641,str(row['RAG_SOC2']))
    c.drawString(285,619,str(row['INDIRIZ']))
    c.drawString(285,594,str(row['LOCALIT']))
    c.drawString(285,572,str(row['ZONA']))
    c.drawString(285,529,str(row['TEL_ABIT']))
    c.drawString(285,505,str(row['FAX']))
    c.drawString(285,482,str(row['MOBILE']))
    c.drawString(285,460,str(row['PIVA']))
    c.drawString(285,440,str(row['CODFISC']))
    c.drawString(285,550,str(row['CAP']))
    c.rect(42,752,266,-27,1,0)
    c.drawString(65,389,str(row['NOTE']))

def querytestata ():
     return '''SELECT * FROM agenti WHERE T_CPART = "%s" and  COD = %s'''

def Ycorpo ():
     return 1
