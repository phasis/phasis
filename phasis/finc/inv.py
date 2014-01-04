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
    c.setFont('Helvetica',10)
    c.drawString(42,Y,row['COD'])
    c.drawString(128,Y,row['DESCRIZ'])
    c.drawString(350,Y,str(row['UM'])) # (390,Y,str(row['UM'])) originale
    c.drawRightString(555,Y,str(row['QT'])) # (480,Y,str(row['QT']))  originale
    c.setFont('Helvetica',10)
    ##c.drawRightString(548,Y,str(row['VALORE'])) # originale
    c.drawRightString(440,Y,str(row['QTC'])) # aggiunta
    c.drawRightString(490,Y,str(row['QTS'])) # aggiunta

def struttura (c):
    c.rect(36,760,525,-700,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(45,734,_("Cod.Articolo"))
    c.rect(36,720,525,0,1,0)
    c.drawString(128,734,_("Descrizione Articolo"))
    c.rect(124,759,0,-700,1,0)
    c.drawString(510,734,_("QT Totale")) #originale (515.402,734,"Valore")
    c.drawString(450,734,_("QT Scarico")) # aggiunta
    c.setFont('Helvetica-Bold',12)
    c.drawString(463.193,781.186,_("del  "))
    c.rect(341,759,0,-700,1,0) # (381,759,0,-700,1,0) originale
    c.rect(378,759,0,-700,1,0) # (418,759,0,-700,1,0) originale
    c.rect(444,759,0,-700,1,0) # (494,759,0,-700,1,0) originale
    c.rect(505,759,0,-700,1,0) # aggiunta
    c.setFont('Helvetica-Bold',14)
    c.drawString(210,783,_("INVENTARIO  DI  MAGAZZINO"))
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
SELECT COD, substr(DESCRIZ,0,40) as DESCRIZ, UM, IFNULL(ROUND(SUM(qtc),6),0) as QTC, IFNULL(ROUND(SUM(qts),6),0) as QTS, IFNULL(ROUND(SUM(qt),6),0) AS QT, IFNULL(ROUND(SUM(costo),6),0) AS VALORE FROM
(SELECT COD, DESCRIZ, UM, SUM(qt) as qtc , "0" as qts, SUM(qt) as qt, SUM(costo_un) as costo FROM movmag WHERE (cauma="%s" OR cauma="%s") AND anno="%s" GROUP BY COD 
UNION
SELECT COD, DESCRIZ, UM, "0" as qtc, SUM(qt) as qts, (-(SUM(qt))) as qt,  SUM(costo_un) as COSTO FROM movmag  WHERE ( cauma="%s" OR cauma="%s") AND anno="%s" GROUP BY COD )
GROUP BY COD ORDER BY COD """

def fontcorpo ():
     return 10

def Ycorpo ():
     return 705

def fineSeq ():
     return 71
