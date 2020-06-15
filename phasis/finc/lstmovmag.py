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
def corpo (c,row,Y):
    c.setLineWidth(1)
    c.setFont('Helvetica',10)
    c.drawString(42,Y,row['COD'])
    c.drawString(128,Y,row['DESCRIZ'])
    c.drawString(350,Y,str(row['UM'])) # (390,Y,str(row['UM'])) originale
    c.drawRightString(555,Y,str(row['QT'])) # (480,Y,str(row['QT']))  originale
    c.setFont('Helvetica',10)
    ##c.drawRightString(548,Y,str(row['VALORE'])) # originale
    c.drawRightString(440,Y,str(row['TOT_RIGA'])) # aggiunta
    #c.drawRightString(490,Y,str(row['QTS'])) # aggiunta

def struttura (c):
    c.rect(36,760,525,-700,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(45,734,_("Cod.Articolo"))
    c.rect(36,720,525,0,1,0)
    c.drawString(128,734,_("Descrizione Articolo"))
    c.rect(124,759,0,-700,1,0)
    c.drawString(510,734,_("Importo")) #originale (515.402,734,"Valore")
    #c.drawString(450,734,_("QT Scarico")) # aggiunta
    c.setFont('Helvetica-Bold',12)
    c.drawString(463.193,781.186,_("del  "))
    c.rect(341,759,0,-700,1,0) # (381,759,0,-700,1,0) originale
    c.rect(378,759,0,-700,1,0) # (418,759,0,-700,1,0) originale
    c.rect(444,759,0,-700,1,0) # (494,759,0,-700,1,0) originale
    c.rect(505,759,0,-700,1,0) # aggiunta
    c.setFont('Helvetica-Bold',14)
    c.drawString(210,783,_("MOVIMENTI  MAGAZZINO"))
    c.setFont('Helvetica-Bold',10)
    c.drawString(348,734,_("UM")) # (388,734,"UM") originale 
    c.drawString(390,734,_("QT Carico")) # (450,734,"Q.ta`") originale 

def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(41,821,str(row['rsaz']))
    c.rect(36,809,525,-40,1,0)
    c.setFont('Helvetica',12)
    c.drawString(495,781,str(row['datacon']))

def querycorpo ():
     return """
SELECT COD,DESCRIZ,UM,QT,TOT_RIGA FROM movmag WHERE anno="%s" AND num_mov="%s" """

def fontcorpo ():
     return 10

def Ycorpo ():
     return 705

def fineSeq ():
     return 71
