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

def struttura (c):
    c.setLineWidth(1)
    c.setFont('Helvetica',14)
    c.drawString(26.439,779.669,_("Cliente: "))
    c.rect(14.5299,800.389,558.02,-23.1677,1,0)
    c.rect(14.5299,767.54,558.932,-88.5066,1,0)
    c.drawString(28.4495,727.866,_("Telefono:"))
    c.drawString(28.4495,708.766,_("Mobile:"))
    c.drawString(26.439,745.864,_("Indirizzo:"))
    c.drawString(281.249,725.855,_("Rifer.:"))
    c.drawString(29.4547,688.568,_("Note:"))
    c.drawString(280.549,707.322,_("P.Iva.:"))

def testata (c,row):
    c.drawString(100.77,780.497,str(row['RAG_SOC']))
    c.drawString(97.518,747.106,str(row['IND_CAP_ZONA_PR']))
    c.drawString(97.518,688.117,str(row['NOTE']))
    c.drawString(97.518,728.871,str(row['TEL_ABIT']))
    c.setFont('Helvetica',12)
    c.drawString(496.024,779.255,str(row['COD_AGE']))
    c.setFont('Helvetica',14)
    c.drawString(325.55,725.855,str(row['NSRIF']))
    c.drawString(97.518,708.766,str(row['MOBILE']))
    c.drawString(326.79,708.328,str(row['PIVA']))

def querytestata ():
     return '''SELECT (RAG_SOC1||" "||RAG_SOC2) as RAG_SOC, (INDIRIZ||" "||CAP||" "||ZONA||" "||PR ) as IND_CAP_ZONA_PR,
COD_AGE,NSRIF,NOTE,TEL_ABIT,MOBILE, PIVA
FROM anag WHERE T_CPART = "%s" AND PRECON ="%s"
AND NSRIF LIKE "%s" AND RAG_SOC1 LIKE "%s" AND NOTE LIKE "%s" AND COD_AGE= "%s" ORDER BY RAG_SOC1'''

def Ycorpo ():
     return 1

def blocchi():
     return [(0, -120), (0, -120), (0, -120), (0, -120), (0, -120)]
