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
    return landscape(A4)

def corpo (c,row,Y):
    c.setLineWidth(1)
    c.setFont('Helvetica',10)
    c.drawRightString(94,Y,str(row['NUM_MOV']))
    if str(row['DATADOC'])=="":
         c.drawString(111,Y,str(row['DATAMOV']))
    else:
         c.drawString(111,Y,str(row['DATADOC']))
    c.drawString(188,Y,str(row['CPART'] + ' - ' + row['RAGSOC']))
    c.drawString(368,Y,str(row['DESCRIZ'] + ' - ' + row['D_CONTO']))
    c.setFont('Times-Roman',12)
    c.setFont('Helvetica',10)
    c.drawString(695,Y,str(row['SEGNO']))
    c.drawRightString(804,Y,str(row['IMPORVAL']))


def struttura (c):
    c.rect(36,510,782,-494,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(46,485,_("Num. Doc."))
    c.drawString(111,485,_("Data Scad."))
    c.drawString(188,485,_("Ragione Sociale"))
    c.drawString(368,485,_("Causale - Operazione"))
    c.drawString(670,485,_("Dare/Avere"))
    c.drawString(774,485,_("Totale"))

    c.rect(36,470,783,0,1,0)
    c.rect(104.57,509.967,0,-493.75,1,0)
    c.rect(178,510,0,-493,1,0)
    c.rect(363,510,0,-493,1,0)
    c.rect(665,510,0,-493,1,0)
    c.rect(730,510,0,-493,1,0)
    c.setFont('Helvetica-Bold',10)

    c.setFont('Helvetica-Bold',12)
    c.drawString(676.91,531.567,_("Al  "))
    c.setFont('Helvetica-Bold',14)
    c.drawString(234,531,_("LISTA MOVIMENTI AGGIORNATO  "))




def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(42.8833,571,str(row['rsaz']))
    c.rect(36,559,782,-40,1,0)
    c.setFont('Helvetica',12)
    c.drawString(709,531,str(row['datacon']))

def querycorpo ():
     return '''SELECT *,anag.rag_soc1 as RAGSOC FROM movcon,anag WHERE movcon.T_CPART = "%s" AND movcon.DATA_INT>="%s" 
AND movcon.DATA_INT<= "%s" AND anag.T_CPART=movcon.T_CPART AND anag.COD=movcon.CPART 
 ORDER BY movcon.DATA_INT ASC'''


def fontcorpo ():
     return 10

def Ycorpo ():
     return 452

def fineSeq ():
     return 25
