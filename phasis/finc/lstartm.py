# -*- coding: iso-8859-1 -*-
# Copyright (C) 2003 - 2008  SeeOpen - http://www.seeopen.it/
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
    return portrait(A4)

def corpo (c,row,Y):
    c.setLineWidth(1)
    c.setFont('Helvetica',11)
    c.drawString(42,Y,str(row['coda']))
    c.drawString(137,Y,str(row['descriza']))
    c.drawRightString(468,Y,str(row['prezzo_1a']))
    c.drawRightString(490,Y,str(row['alivaa']))
    c.setFont('Helvetica',11)
    c.drawRightString(550,Y,str(row['prezzo_2a']))
    c.setStrokeColor((0.68, 0.68, 0.68))
    c.rect(36, Y-3,525,0,1,0)
    c.setStrokeColor((0, 0, 0))

def struttura (c):
    c.setFont('Helvetica-Bold',12)
    c.drawString(398,822,_("del  "))
    c.drawString(226,822,_("LISTINO ARTICOLI  "))
    c.rect(36,814,525,-754,1,0) #cornice corpo
    c.rect(36,787,525,0,1,0)
    c.setFont('Helvetica-Bold',11)
    c.drawString(45,798,_("Cod.Articolo"))
    c.drawString(137,798,_("Descrizione Articolo"))
    c.drawString(418,798,_("Imponibile"))
    c.drawString(477,798,_("Iva "))
    c.drawString(503,798,_("Prezzo I/C"))
    c.setLineWidth(0.3) 
    c.rect(133,814,0,-755,1,0)
    c.rect(414,814,0,-755,1,0)
    c.rect(474,814,0,-754,1,0)
    c.rect(494,814,0,-754,1,0)

def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(40,822,str(row['rsaz']))
    c.setFont('Helvetica',12)
    c.drawString(430,822,str(row['datacon']))
    c.setFont('Helvetica-Bold',12)
    c.drawString(510,822,str(row['##npag']))

def querycorpo ():
     return """ select cod as coda, substr(descriz, 0, 40) as descriza, um, 
                aliva as alivaa, round(prezzo_1, 6) as prezzo_1a, 
                round(prezzo_2, 6) as prezzo_2a
                from
                articoli where merce = "%s" order by descriz asc """

def fontcorpo ():
     return 18

def Ycorpo ():
     return 769

def fineSeq ():
     return 71
