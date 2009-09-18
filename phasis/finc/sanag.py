# -*- coding: iso-8859-1 -*-
# Copyright (C) 2003 - 2007  SeeOpen - http://www.seeopen.it/
#
# Developer:
# Massimo Gerardi <m.gerardi@seeopen.it>
# Daniele Cicchinelli <d.cicchinelli@seeopen.it>
#
#
# Released under the terms of the GNU General Public License
# (version 2 or above)
#
# See COPYING for details.
#
#   www.phasis.it - info@phasis.it 
#


from reportlab.lib.pagesizes import *

def layout():
    return portrait((600, 799))

def struttura (c):
    c.setLineWidth(1)
    c.setFont('Helvetica',14)
    c.drawString(63.2771,685.27,_("Cod. cliente..................................."))
    c.drawString(63.2771,664.715,_("Ragione soc. (Cognome).............. "))
    c.drawString(63.2771,641.91,_("Ragione soc.  (Nome)..................."))
    c.drawString(63.2771,619.106,_("Indirizzo........................................"))
    c.drawString(63.2771,594.053,_("Localita'........................................"))
    c.drawString(63.2771,572.374,_("Zona............................................."))
    c.drawString(63.2771,550.694,_("Cap..............................................."))
    c.drawString(63.2771,529.014,_("Telefono......................................."))
    c.drawString(63.2771,505.734,_("Fax..............................................."))
    c.drawString(63.2771,482.41,_("Mobile..........................................."))
    c.drawString(63.2771,460.384,_("P. Iva............................................"))
    c.drawString(63.2771,440.304,_("Cod. Fisc......................................"))
    c.setFont('Helvetica',16)
    c.drawString(63.2771,734.429,_("Scheda  Cliente"))
    c.rect(42,720,503,-450,1,0)
    c.drawString(64.2562,413.145,_("Note:"))

def testata (c,row):
    c.setFont('Helvetica',14)
    c.drawString(285.704,685.27,str(row['COD']))
    c.drawString(285.704,664.715,str(row['RAG_SOC1']))
    c.drawString(285.704,641.91,str(row['RAG_SOC2']))
    c.drawString(285.704,619.106,str(row['INDIRIZ']))
    c.drawString(285.704,594.053,str(row['LOCALIT']))
    c.drawString(285.704,572.374,str(row['ZONA']))
    c.drawString(285.704,529.014,str(row['TEL_ABIT']))
    c.drawString(285.704,505.734,str(row['FAX']))
    c.drawString(285.704,482.41,str(row['MOBILE']))
    c.drawString(285.704,460.384,str(row['PIVA']))
    c.drawString(285.704,440.304,str(row['CODFISC']))
    c.drawString(285.704,550.694,str(row['CAP']))
    c.rect(42,752,266,-27,1,0)
    c.drawString(65.2812,389.57,str(row['NOTE']))

def querytestata ():
     return '''SELECT * FROM anag WHERE T_CPART = "%s" and  COD = %s'''

def Ycorpo ():
     return 1
