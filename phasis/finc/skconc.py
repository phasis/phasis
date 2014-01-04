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
    ##c.drawString(42,Y,str(row['RAG_SOC']))
    ##c.drawString(192,Y,str(row['NUM_MOV']))
    c.drawString(45,Y,str(row['DESCRIZ']))
    if str(row['SEGNO'])=="D":
        c.drawRightString(446,Y,str(row['IMPORVAL']))
    else:
        c.drawRightString(500,Y,str(row['IMPORVAL']))


def struttura (c):
    c.rect(36,745,525,-550,1,0)
    c.setFont('Helvetica-Bold',12)
    c.drawString(45,780,"del  ")
    c.setFont('Helvetica-Bold',14)
    c.drawString(45,800,"Scheda Contabile")
    c.rect(36,720,525,0,1,0)
    c.setFont('Helvetica-Bold',10)
    #c.drawString(45,734,"CLIENTE")
    #c.rect(184,759,0,-700,1,0)
    c.drawString(46,730,"N°")
    c.drawString(137,730,"Descrizione")
    c.rect(398,745,0,-550,1,0)
    c.drawString(410,730,"Dare")
    c.rect(450,745,0,-550,1,0)
    c.drawString(470,730,"Avere")
    c.rect(505,745,0,-550,1,0)
    c.drawString(520,730,"Saldo")
    c.rect(300,150,200,-60,1,0)
    c.setFont('Helvetica-Bold',14)
    c.drawString(320,130,"TOTALE Avere ")
    c.drawString(320,110,"Euro  ")

def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(41,821,str(row['rsaz']))
    c.rect(36,815,525,-65,1,0)
    c.setFont('Helvetica',12)
    c.drawString(90,780,str(row['datacon']))
    c.setFont('Helvetica',12)
    #c.drawString(143.559,655.378,str(row['PIVA']))
    c.setFont('Helvetica-Bold',12)
    c.drawString(350,800,str(row['RAG_SOC']))
    c.drawString(350,780,str(row['INDI']))
    c.drawString(350,760,str(row['CAP_ZONA_PR']))
    c.setFont('Helvetica',12)
    ##c.drawRightString(536.459,744.716,str(row['COD_CF']))
    #c.drawString(119.101,641.667,str(row['DPAG']))

def calce (c,row):
    c.setFont('Helvetica-Bold',14)
    c.drawString(380,110,str(row['TOT_DOC']))

def querytestata ():
     return '''
SELECT NUM_MOV, CPART, (anag.RAG_SOC1||" "||anag.RAG_SOC2)as RAG_SOC,
(anag.INDIRIZ) as INDI,
(anag.INDIRIZ||" "||anag.CAP||" "||anag.ZONA||" "||anag.LOCALIT)as INDIRIZ_CAP_ZONA,
(anag.CAP||" "||anag.ZONA||" "||anag.LOCALIT||" "||anag.PR )as CAP_ZONA_PR, anag.T_CPART
FROM 
(SELECT NUM_MOV, movcon.CPART as CPART
FROM   movcon WHERE anno= "%s" and CPART="%s" ), anag
WHERE anag.COD = CPART AND T_CPART="C" GROUP BY COD'''
    

def querycorpo ():
     return '''
SELECT CPART, substr(("("||NUM_MOV||")     Cod. cliente " ||CPART||"    "||DESCRIZ||"  ("||D_CONTO||") "),0,100) as DESCRIZ, IMPORVAL, SEGNO, CPART, D_CONTO
FROM movcon WHERE ANNO="%s" and CPART="%s" and T_CPART="C"  ORDER BY NUM_MOV '''

def querycalce ():
     return '''SELECT IFNULL(ROUND(-sum((IMPORVAL)),6),0) as TOT_DOC
FROM movcon
WHERE ANNO = "%s" AND CPART="%s" and T_CPART="C" AND SEGNO = "A" '''

def fontcorpo ():
     return 10

def Ycorpo ():
     return 705

def fineSeq ():
     return 71
