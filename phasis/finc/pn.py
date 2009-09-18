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

def corpo (c,row,Y):
    c.setLineWidth(1)
    c.setFont('Helvetica',10)
    ##c.drawString(190,Y,str(row['NUM_MOV']))
    c.drawString(42,Y,str(row['RAG_SOC']))
    c.drawString(198,Y,str(row['DESCRIZ']))
    c.drawString(390,Y,str(row['IMP_DARE']))
    c.drawRightString(480,Y,str(row['IMP_AVERE']))
    c.drawRightString(548,Y,str(row['IMP_SALDO']))

def struttura (c):
    c.rect(36,760,525,-700,1,0)
    c.setFont('Helvetica-Bold',12)
    c.drawString(463.193,781.186,_("del  "))
    c.setFont('Helvetica-Bold',14)
    c.drawString(210,783,_("LISTA DI CASSA"))
    c.rect(36,720,525,0,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(45,734,_("CLIENTE"))
    c.rect(194,759,0,-700,1,0)
    c.drawString(198,734,_("Descrizione"))
    c.rect(381,759,0,-700,1,0)
    c.drawString(388,734,_("Avere"))
    c.rect(435,759,0,-700,1,0)
    c.drawString(450,734,_("Dare"))
    c.rect(494,759,0,-700,1,0)
    c.drawString(515,734,_("Saldo"))

def testata (c,row):
    c.setFont('Helvetica',10)
    c.drawString(41,821,str(row['rsaz']))
    c.rect(36,809,525,-40,1,0)
    c.setFont('Helvetica',12)
    c.drawString(495,781,str(row['datacon']))

def querycorpo ():
     return '''
SELECT substr((COD||"-"||RAG_SOC1||" "||RAG_SOC2),0,28) as RAG_SOC, NUM_MOV, 
substr((DESCRIZ||" "||NUMDOC||" - del "||DATADOC),0,42) as DESCRIZ, 
IFNULL(ROUND(IMPORTO,6),0) AS IMP_DARE, 
IFNULL(ROUND(IMPORVAL,6),0) AS IMP_AVERE, IFNULL(ROUND((IMPORTO-IMPORVAL),6),0) as IMP_SALDO,
 COD_CF 
FROM movcon LEFT JOIN anag ON movcon.ANNO="%s" AND COD_CF=COD AND ANAG.T_CPART="C"  
ORDER BY NUM_MOV '''

def fontcorpo ():
     return 10

def Ycorpo ():
     return 705

def fineSeq ():
     return 71
