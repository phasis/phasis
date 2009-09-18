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
    return portrait(A4)

def struttura (c):
    c.setFillColor((0.349, 0.349, 0.349))
    c.setLineWidth(1)
    c.rect(20,773,326,-102,1,1)
    c.setFillColor((1, 1, 1))
    c.rect(10,783,326,-103,1,1)
def testata (c,row):
    c.setFillColor((0, 0, 0))
    c.setFont('Times-Roman',14)
    c.drawString(67,760,str(row['COD']))
    c.drawString(46,721,str(row['DESCRIZ']))
    c.drawString(77,690,str(row['PREZZO_1']))
    c.setFont('Times-Roman',12)

def Ycorpo ():
     return 1

def blocchi():
     return [(178, -240), (133, -334), (182, -513)]
