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

def struttura (c):
    c.setLineWidth(1)
    c.setFont('Helvetica',14)
    c.drawString(26.439,779.669,_("Cliente: "))
    c.rect(14.5299,800.389,558.02,-30.2045,1,0)
    c.rect(14.5299,767.54,558.932,-110.622,1,0)
    c.drawString(26.439,718.501,_("Telefono:"))
    c.drawString(297.182,718.501,_("Mobile:"))
    c.drawString(26.439,745.864,_("Indirizzo:"))
    c.drawString(266.17,695.697,_("Rifer.:"))
    c.drawString(26.439,696.61,_("Note:"))

def testata (c,row):
    c.setFont('Helvetica',18)
    c.drawString(100.77,780.497,str(row['RAG_SOC']))
    c.drawString(97.518,747.106,str(row['IND_CAP_ZONA_PR']))
    c.drawString(26.3724,672.033,str(row['NOTE']))
    c.drawString(93.8695,719.329,str(row['TEL_ABIT']))
    c.setFont('Helvetica',14)
    c.drawString(496.024,779.255,str(row['COD_AGE']))
    c.setFont('Helvetica',14)
    c.drawString(324.545,695.698,str(row['NSRIF']))
    c.setFont('Helvetica',18)
    c.drawString(355.558,719.329,str(row['MOBILE']))

def querytestata ():
     return '''SELECT (RAG_SOC1||" "||RAG_SOC2) as RAG_SOC, (INDIRIZ||" "||CAP||" "||ZONA||" "||PR ) as IND_CAP_ZONA_PR,
COD_AGE,NSRIF,NOTE,TEL_ABIT,MOBILE
FROM anag WHERE T_CPART = "%s" AND PRECON ="%s"
AND NSRIF LIKE "%s" AND RAG_SOC1 LIKE "%s" AND NOTE LIKE "%s" AND COD_AGE= "%s" ORDER BY RAG_SOC1'''

def Ycorpo ():
     return 1

def blocchi():
     return [(0, -175), (0, -175), (0, -175)]
