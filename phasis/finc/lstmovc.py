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
    return portrait(A4)

def corpo (c,row,Y):
    c.setLineWidth(1)
    c.setFont('Helvetica',8)
    c.drawString(42,Y,str(row['RAG_SOC']))
    ##c.drawString(192,Y,str(row['NUM_MOV']))
    c.drawString(186,Y,str(row['DESCRIZ'] + " " + row['D_CONTO']))
    if str(row['SEGNO'])=="D":
        c.drawRightString(446,Y,str(row['IMPORVAL']))
    else:
        c.drawRightString(486,Y,str(row['IMPORVAL']))

def struttura (c):
    c.rect(36,760,525,-700,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(463.193,781.186,"del  ")
    c.setFont('Helvetica-Bold',12)
    c.drawString(210,783,"LISTA MOVIMENTI")
    c.rect(36,720,525,0,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(45,734,"CLIENTE / FORNITORE")
    c.rect(184,759,0,-700,1,0)
    c.drawString(189,734,"Descrizione")
    c.rect(398,759,0,-700,1,0)
    c.drawString(410,734,"Dare")
    c.rect(450,759,0,-700,1,0)
    c.drawString(470,734,"Avere")


    c.rect(505,759,0,-700,1,0)
    c.drawString(520,734,"Saldo")

def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(41,821,str(row['rsaz']))
    c.rect(36,809,525,-40,1,0)
    c.setFont('Helvetica',12)
    c.drawString(495,781,str(row['datacon']))

def querycorpo ():
     return '''
SELECT substr((COD||"-"||RAG_SOC1||" "||RAG_SOC2),0,28) as RAG_SOC, 
DESCRIZ, D_CONTO, IMPORVAL, SEGNO, CPART as CODCF FROM movcon LEFT JOIN anag ON movcon.ANNO="%s" AND CPART=COD 
AND ANAG.COD=movcon.CPART  ORDER BY DATA_INT '''

def fontcorpo ():
     return 10

def Ycorpo ():
     return 705

def fineSeq ():
     return 71
