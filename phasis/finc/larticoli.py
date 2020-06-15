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
