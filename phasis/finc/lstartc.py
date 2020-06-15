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
    return landscape(A4)

def corpo (c,row,Y):
    c.setLineWidth(1)
    c.setFont('Helvetica',10)
    c.drawString(44,Y,str(row['COD']))
    c.drawString(139,Y,str(row['DESCRIZ']))
    c.drawRightString(548,Y,str(row['PREZZO_1']))
    c.drawRightString(490,Y,str(row['ALIVA']))
    c.setFont('Times-Roman',12)
    c.setFont('Helvetica',10)
    c.drawRightString(466,Y,str(row['COSTO']))
    c.drawString(691,Y,str(row['PROVV']))
    c.drawString(789,Y,str(row['INPROD']))
    c.drawString(730,Y,str(row['COD_FOR']))
    c.drawString(631,Y,str(row['MERCE']))
    c.drawRightString(610,Y,str(row['PREZZO_2']))

def struttura (c):
    c.rect(36,510,782,-494,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(46,485,_("Cod.Articolo"))
    c.drawString(138,485,_("Descrizione Articolo"))
    c.drawString(503,485,_("Imponibile"))
    c.drawString(478,485,_("Iva "))
    c.drawString(423,485,_("Costo Un."))
    c.rect(36,470,783,0,1,0)
    c.rect(134.57,509.967,0,-493.75,1,0)
    c.setFont('Helvetica-Bold',12)
    c.drawString(676.91,531.567,_("del  "))
    c.setFont('Helvetica-Bold',14)
    c.drawString(234,531,_("LISTINO ARTICOLI  COMPLETO  "))
    c.rect(415,510,0,-493,1,0)
    c.rect(476,510,0,-493,1,0)
    c.rect(499,509,0,-493,1,0)
    c.rect(557,510,0,-497,1,0)
    c.rect(620,510,0,-493,1,0)
    c.rect(676,510,0,-493,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(684.874,485.16,_("Provv. "))
    c.rect(724,510,0,-493,1,0)
    c.drawString(726,485,_("Cod.For. "))
    c.rect(773,510,0,-493,1,0)
    c.drawString(775,485,_(" In Prod. "))
    c.drawString(623,485,_("Cat. Merce "))
    c.drawString(569,485,_("Prezzo"))

def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(42.8833,571,str(row['rsaz']))
    c.rect(36,559,782,-40,1,0)
    c.setFont('Helvetica',12)
    c.drawString(709,531,str(row['datacon']))

def querycorpo ():
     return '''SELECT COD, DESCRIZ, round(PREZZO_1, 6) as PREZZO_1 , ALIVA, round(COSTO, 6) as COSTO, PROVV, 
INPROD, COD_FOR, MERCE, round(PREZZO_2, 6) as PREZZO_2 FROM articoli'''

def fontcorpo ():
     return 10

def Ycorpo ():
     return 452

def fineSeq ():
     return 25
