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
    #c.setLineWidth(1)
    c.setFont('Helvetica',11)
    c.drawString(42,Y,row['codart'])
    c.drawString(137,Y,row['descrizart'])
    c.drawRightString(468,Y,str(row['prezzo_1']))
    c.drawRightString(550,Y,str(row['prezzo_2']))
    c.setFont('Helvetica',9)
    c.drawRightString(493,Y,str(row['alivart']))
    #c.setStrokeColor((0.68, 0.68, 0.68))
    c.setLineWidth(.04) 
    c.rect(36, Y-3,525,0,1,0)
    #c.setStrokeColor((0, 0, 0))

def struttura (c):
    c.setLineWidth(.4) 
    c.rect(36,787,525,0,1,0)    
    c.rect(36,814,525,-754,1,0)
    c.setFont('Helvetica-Bold',11)
    c.drawString(45,798,_("Cod.Articolo"))
    c.drawString(137,798,_("Descrizione Articolo"))
    c.drawString(418,798,_("Imponibile"))
    c.drawString(477,798,_("Iva "))
    c.drawString(503,798,_("Prezzo I/C"))
    c.setLineWidth(.04) 
    #c.rect(36,814,525,-754,1,0)
    c.rect(414,814,0,-755,1,0)
    c.rect(474,814,0,-754,1,0)
    c.rect(494,814,0,-754,1,0)
    c.rect(133,814,0,-755,1,0)
    c.setFont('Helvetica-Bold',12)
    c.drawString(280,822,_("LISTINO ARTICOLI  "))
    #c.setFont('Helvetica',10)
    #c.drawString(398,822,_("del  "))

def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(40,822,str(row['rsaz']))
    ##c.drawString(310,822, str(row['rag_soc']))
    c.setFont('Helvetica',8)
    c.drawString(480,822,str(row['datacon']))
    c.drawString(540,822,str(row['##npag']))

def querycorpo ():
     return ''' select cod as codart, 
                substr(descriz, 0, 40) as descrizart, 
                aliva as alivart, 
                round(prezzo_1, 6) as prezzo_1, round(prezzo_2, 6) as prezzo_2 
                from articoli where cod like "%s" order by descriz'''

def fontcorpo ():
     return 18

def Ycorpo ():
     return 769

def fineSeq ():
     return 71
