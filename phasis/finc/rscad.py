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
    c.drawRightString(94,Y,str(row['COD']))
    c.drawString(111,Y,str(row['DATA_SCAD']))

    c.drawString(188,Y,str(row['RAG_SOC1']))
    c.setFont('Times-Roman',12)
    c.setFont('Helvetica',10)
    c.drawString(695,Y,str(row['DA']))
    c.drawRightString(804,Y,str(row['TOTALE']))

# BO
    #c.drawString(691,Y,str(row['PROVV']))
    #c.drawString(789,Y,str(row['INPROD']))
    #c.drawString(730,Y,str(row['COD_FOR']))
    #c.drawString(631,Y,str(row['MERCE']))
    #c.drawRightString(610,Y,str(row['PREZZO_2']))

def struttura (c):
    c.rect(36,510,782,-494,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(46,485,_("Num. Doc."))
    c.drawString(111,485,_("Data Scad."))
    c.drawString(188,485,_("Ragione Sociale "))
    c.drawString(670,485,_("Dare/Avere"))
    c.drawString(774,485,_("Totale"))

    c.rect(36,470,783,0,1,0)
    c.rect(104.57,509.967,0,-493.75,1,0)
    c.rect(178,510,0,-493,1,0)
    c.rect(665,510,0,-493,1,0)
    c.rect(730,510,0,-493,1,0)
    c.setFont('Helvetica-Bold',10)

    c.setFont('Helvetica-Bold',12)
    c.drawString(676.91,531.567,_("Al  "))
    c.setFont('Helvetica-Bold',14)
    c.drawString(234,531,_("LISTA SCADENZE AGGIORNATO  "))




def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(42.8833,571,str(row['rsaz']))
    c.rect(36,559,782,-40,1,0)
    c.setFont('Helvetica',12)
    c.drawString(709,531,str(row['datacon']))

def querycorpo ():
     return '''SELECT * FROM scad WHERE T_CPART = "%s" AND DATA_SCAD_INT>="%s" AND DATA_SCAD_INT<= "%s" 
AND TIPO_SCAD = "%s" ORDER BY DATA_SCAD_INT '''


def fontcorpo ():
     return 10

def Ycorpo ():
     return 452

def fineSeq ():
     return 25
