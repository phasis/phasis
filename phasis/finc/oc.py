# -*- coding: iso-8859-1 -*-
# Copyright (C) 2003 - 2008  SeeOpen - http://www.seeopen.it/
#
# Developer:
# Massimo Gerardi <massimog@seeopen.it>
# Daniele Cicchinelli <danielec@seeopen.it>
#
#
# Released under the terms of the GNU General Public License
# (version 2 or above)
#
# See COPYING for details.
#
#   www.phasis.it - info@phasis.it 
#

import cfg
from reportlab.lib.pagesizes import *

def layout():
    return portrait(A4)

def testata (c,row):
    c.setFont('Helvetica-Bold',12)
    if str(row['tipo_ord'])=='PC'  : 
        c.drawString(308,646,_("OFFERTA CLIENTE"))    
    if str(row['tipo_ord'])=='OC' : 
        c.drawString(308,646,_("ORDINE CLIENTE"))    
    c.setFont('Helvetica',12)
    c.drawString(466,617,str(row['data_ord']))
    c.drawString(360,617,str(row['num_ord']))
    c.drawString(143,655,str(row['piva']))
    c.setFont('Helvetica-Bold',12)
    c.drawString(313,723,str(row['rag_soc']))
    c.drawString(313,706,str(row['indi']))
    c.drawString(313,690,str(row['cap_zona_pr']))
    c.setFont('Helvetica',12)
    c.drawRightString(536,744,str(row['cod_cf']))
    c.drawString(119,641,str(row['dpag']))

    if cfg.logofinc=='1':
        c.drawImage(cfg.path_img+'/logo1.jpg',25,740,180,85)
        if str(row['banca'])!='':
            c.setFont('Helvetica-Bold',10)
            c.drawString(40,622,"Banca: ")
            #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
            c.drawString(40,610,"IBAN: ")
            c.setFont('Helvetica',10)
            c.drawString(80,622,str(row['banca']))
            c.drawString(80,610,str(row['iban'])) 
 
    elif cfg.logofinc=='2':
        c.drawImage(cfg.path_img+'/logo2.jpg',25,745,80,70)
        c.setFont('Helvetica-Bold',14)
        c.drawString(110,780,str(row['rsaz'])) 
        c.setFont('Helvetica',10)
        if str(row['ind1'])!="":
           c.drawString(39,720,"Sede Legale: " + str(row['ind_cap_loc_pr']))
           c.drawString(39,710,"Sede Amm.: " + str(row['ind_cap_loc_pr1']))
	   c.drawString(39,700,str(row['tel_faxaz']))
           c.drawString(39,690,str(row['emailaz'])) 
           c.drawString(39,680,str(row['piva_cfaz']))
        else:
           c.drawString(39,720,str(row['ind_cap_loc_pr']))
           c.drawString(39,710,str(row['tel_faxaz']))
           c.drawString(39,700,str(row['emailaz'])) 
           c.drawString(39,690,str(row['piva_cfaz']))
        if str(row['banca'])!='':
            c.setFont('Helvetica-Bold',10)
            c.drawString(40,622,"Banca: ")
            #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
            c.drawString(40,610,"IBAN: ")
            c.setFont('Helvetica',10)
            c.drawString(80,622,str(row['banca']))
            c.drawString(80,610,str(row['iban']))  

    elif cfg.logofinc=='3':
        c.drawImage(cfg.path_img+'/logo3.jpg',39,740,180,85)
        #c.setFont('Helvetica-Bold',14)
        #c.drawString(110,800,str(row['rsaz'])) 
        c.setFont('Helvetica',10)
        if str(row['ind1'])!="":
           c.drawString(39,725,"Sede Legale: " + str(row['ind_cap_loc_pr']))
           c.drawString(39,715,"Sede Amm.: " + str(row['ind_cap_loc_pr1']))
	   c.drawString(39,705,str(row['tel_faxaz']))
           c.drawString(39,695,str(row['emailaz'])) 
           c.drawString(39,685,str(row['piva_cfaz']))
        else:
           c.drawString(39,725,str(row['ind_cap_loc_pr']))
           c.drawString(39,715,str(row['tel_faxaz']))
           c.drawString(39,705,str(row['emailaz'])) 
           c.drawString(39,695,str(row['piva_cfaz']))
        if str(row['banca'])!='':
            c.setFont('Helvetica-Bold',10)
            c.drawString(40,622,"Banca: ")
            #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
            c.drawString(40,610,"IBAN: ")
            c.setFont('Helvetica',10)
            c.drawString(80,622,str(row['banca']))
            c.drawString(80,610,str(row['iban']))
    elif cfg.logofinc=='4':
        #c.drawImage(cfg.path_img+'/logo4.jpg',39,740,180,85)
        ##c.drawImage(cfg.path_img+'/logo4.jpg',39,740,260,85)
        c.drawImage(cfg.path_img+'/logo4.jpg',39,740,260,75)
        c.setFont('Helvetica-Bold',14)
        c.drawString(39,730,str(row['rsaz'])) 
        c.setFont('Helvetica',10)
        if str(row['ind1'])!="":
           c.drawString(39,715,"Sede Legale: " + str(row['ind_cap_loc_pr']))
           c.drawString(39,705,"Sede Amm.: " + str(row['ind_cap_loc_pr1']))
	   c.drawString(39,695,str(row['tel_faxaz']))
           c.drawString(39,685,str(row['emailaz'])) 
           c.drawString(39,675,str(row['piva_cfaz']))
        else:
           c.drawString(39,715,str(row['ind_cap_loc_pr']))
           c.drawString(39,703,"Telefono: " + str(row['telaz']))
           c.drawString(39,691,str(row['emailaz'])) 
           c.drawString(39,678,str(row['piva_cfaz']))
        if str(row['banca'])!='':
            c.setFont('Helvetica-Bold',10)
            c.drawString(40,622,"Banca: ")
            #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
            c.drawString(40,610,"IBAN: ")
            c.setFont('Helvetica',10)
            c.drawString(80,622,str(row['banca']))
            c.drawString(80,610,str(row['iban'])) 
 
    else:
        c.setFont('Helvetica-Bold',14)
        c.drawString(39,800,str(row['rsaz']))
        c.setFont('Helvetica',10)
        if str(row['ind1'])!="":
           c.drawString(39,785,"Sede Legale: " + str(row['ind_cap_loc_pr']))
           c.drawString(39,770,"Sede Amm.: " + str(row['ind_cap_loc_pr1']))
	   c.drawString(39,755,str(row['tel_faxaz']))
           c.drawString(39,740,str(row['emailaz'])) 
           c.drawString(39,725,str(row['piva_cfaz']))
        else:
           c.drawString(39,785,str(row['ind_cap_loc_pr']))
           c.drawString(39,770,str(row['tel_faxaz']))
           c.drawString(39,755,str(row['emailaz'])) 
           c.drawString(39,740,str(row['piva_cfaz']))
        if str(row['banca'])!='':
            c.setFont('Helvetica-Bold',10)
            c.drawString(40,622,"Banca: ")
            #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
            c.drawString(40,610,"IBAN: ")
            c.setFont('Helvetica',10)
            c.drawString(80,622,str(row['banca']))
            c.drawString(80,610,str(row['iban']))  

def struttura (c):
    c.rect(307,761,254,-92,1,0)
    c.rect(36,600,525,-415,1,0)
    c.rect(110,600,0,-415,1,0)
    c.rect(330,600,0,-415,1,0)
    c.rect(370,600,0,-415,1,0)
    c.rect(460,600,0,-415,1,0)
    c.rect(504,600,0,-415,1,0)
    c.rect(37,575,525,0,1,0)
    c.setFont('Helvetica-Bold',10)
    c.drawString(41,583,_("Cod.Articolo"))
    c.drawString(115,583,_("Descrizione Articolo"))
    c.setFont('Helvetica-Bold',12)
    c.drawString(319,616,_("Num.  "))
    c.drawString(39,655,_("P.Iva/Cod. Fisc. :"))
    c.setFont('Helvetica-Bold',10)
    c.drawString(342,583,_("Q.ta`"))
    c.drawString(376,583,_("Prezzo Unitario"))
    c.drawString(477,584,_("Iva"))
    c.drawString(515,583,_("Importo"))
    c.drawString(52,156,_("Totale merce"))
    c.drawString(413,156,_("Valuta"))
    c.drawString(136,156,_("Imponibile"))
    c.drawString(204,156,_("Iva"))
    c.drawString(320,156,_("Importo Iva"))
    c.drawString(231,156,_("Descrizione"))
    c.rect(36,177,526,-95,1,0)
    c.setFont('Helvetica',11)
    c.drawString(313,744,_("Spett.le Ditta"))
    c.rect(307,634,254,-26,1,0)
    c.setFont('Helvetica-Bold',12)
    c.drawString(436,616,_("del  "))
    #c.drawString(308,646,"PREVISIONE DI ORDINE")
    c.setFont('Helvetica-Bold',10)
    c.drawString(51,118,_("Scadenze    :"))
    c.drawString(52,105,_("Importi        :"))
    c.drawString(470,156,_("Totale Documento"))
    c.setFont('Helvetica-Bold',12)
    c.drawString(39,641,_("Pagamento :"))
    c.drawString(39,618,_("Banca :"))
    c.setFont('Helvetica',12)
    c.drawString(418,139,_("Euro"))



def corpo (c,row,Y):
    c.setFont('Helvetica',10)
    c.drawString(41,Y,str(row['codart']))
    c.drawString(115,Y,str(row['descriz']))
    c.drawRightString(364,Y,str(row['qt_ord']))
    c.drawRightString(453,Y,str(row['prez_un']))
    c.drawString(480,Y,str(row['alivaart']))
    c.drawRightString(554,Y,str(row['tot_riga']))


def dettaglioiva (c,row,Y):
    c.setLineWidth(1)
    c.setFont('Times-Roman',12)
    c.setFont('Helvetica',12)
    c.drawString(235,Y,str(row['d_des']))
    c.drawString(141,Y,str(row['d_imp']))
    c.drawString(203,Y,str(row['d_iva']))

def calce (c,row):
    c.drawString(68,140,str(row['tot_merce']))
    c.drawRightString(532,140,str(row['tot_ord']))
    c.drawString(325,140,str(row['tot_iva']))

def querycorpo ():
     return ''' select round(prez_un, 6) as prez_un , 
                round(qt_ord, 6) as qt_ord, round(sc1,6) as sc1, 
		(substr(descriz,0,35)) as descriz, cod as codart, aliva as alivaart, 
		(round((prez_un * qt_ord),6) - round((prez_un * qt_ord * (round(sc1,6)/100)),6)) as tot_riga
		from ordi2 where anno = "%s"  and tipo_ord = "%s"  
		and num_ord = %s '''


def querytestata ():
     return ''' select tipo_ord, stt_ord,rag_soc, piva, data_ord, num_ord, cod_cf, tpag, 
                cap_zona_pr, indi, tabgen.descriz as dpag
		from
                (select stt_ord, rag_soc, indiriz_cap_zona, cap_zona_pr, indi, 
		data_ord, num_ord, cod_cf, tpag, anag.piva as piva, tipo_ord
		from
                (select(rag_soc1||" "||rag_soc2) as rag_soc, (indiriz) as indi,
		(indiriz||" "||cap||" "||zona||" "||localit)as indiriz_cap_zona,
		(cap||" "||zona||" "||localit||" "||pr )as cap_zona_pr, 
		ordi1.pagam as tpag, data_ord, num_ord, cod_age, cod_cf, stt_ord,
		ordi1.cod_cf as codcf, tipo_ord
		from ordi1 where anno = "%s" and tipo_ord = "%s" 
		and num_ord = %s),anag
		where anag.cod = codcf), tabgen
		where tabgen.cod = "PAGAM" and tabgen.valore = tpag'''

def querydettaglioiva ():
     return ''' select d_imp, d_iva, imp_iva, tabgen.descriz as d_des
                from
		(select  sum(ordi2.tot_riga) as d_imp, ordi2.aliva as d_iva,
		(sum(ordi2.tot_riga) * round(ordi2.aliva,2)/100) as imp_iva
		from ordi2 where anno = "%s" and tipo_ord = "%s" 
		and num_ord = %s group by aliva) as ordi, tabgen
		where tabgen.cod = "ALIVA" and tabgen.valore = d_iva '''

def querycalce ():
     return ''' select sum(ordi.d_imp) as tot_merce, 
                sum(ordi.imp_iva) as tot_iva, 
		sum(ordi.d_imp) + sum(ordi.imp_iva) as tot_ord
		from
		(select  sum(ordi2.tot_riga) as d_imp,
		(sum(ordi2.tot_riga) * round(ordi2.aliva,2)/100) as imp_iva
		from ordi2 
		where anno = "%s"  and tipo_ord = "%s"  and num_ord = %s 
		group by aliva)  as ordi '''

def fontcorpo ():
     return 12

def Ycorpo ():
     return 553

def fontdettaglioiva ():
     return 12

def Ydettaglioiva ():
     return 140

def fineSeq ():
     return 195
