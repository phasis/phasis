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
    c.setFont('Helvetica',12)
    c.drawString(174,609,str(row['data_doc']))
    c.drawString(83,609,str(row['num_doc']))
    c.drawString(417,698,str(row['codfisc']))
    c.drawString(417,682,str(row['piva']))
    c.drawString(314,749,str(row['rag_soc']))
    c.drawString(314,732,str(row['indi']))
    c.drawString(314,716,str(row['cap_zona_pr']))
    c.drawRightString(536,764,str(row['cod_cf']))
    #c.drawRightString(450,630,str(row['rag_soc3']))
    #c.drawRightString(450,610,str(row['rag_soc4']))
    if cfg.logofinc=='1':
        c.drawImage(cfg.path_img+'/logo1.jpg',25,740,180,85)
        ##if str(row['banca'])!='':
        ##    c.setFont('Helvetica-Bold',10)
        ##    c.drawString(40,622,"Banca: ")
        ##    #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
        ##    c.drawString(40,610,"IBAN: ")
        ##    c.setFont('Helvetica',10)
        ##    c.drawString(80,622,str(row['banca']))
        ##    c.drawString(80,610,str(row['iban'])) 
 
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
        ##if str(row['banca'])!='':
        ##    c.setFont('Helvetica-Bold',10)
        ##    c.drawString(40,622,"Banca: ")
        ##    #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
        ##    c.drawString(40,610,"IBAN: ")
        ##    c.setFont('Helvetica',10)
        ##    c.drawString(80,622,str(row['banca']))
        ##    c.drawString(80,610,str(row['iban']))  

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
        ##if str(row['banca'])!='':
        ##    c.setFont('Helvetica-Bold',10)
        ##    c.drawString(40,622,"Banca: ")
        ##    #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
        ##    c.drawString(40,610,"IBAN: ")
        ##    c.setFont('Helvetica',10)
        ##    c.drawString(80,622,str(row['banca']))
        ##    c.drawString(80,610,str(row['iban']))
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
        ##if str(row['banca'])!='':
        ##    c.setFont('Helvetica-Bold',10)
        ##    c.drawString(40,622,"Banca: ")
        ##    #c.drawString(40,620,"      Check   Cin   Abi     Cab        Conto")
        ##    c.drawString(40,610,"IBAN: ")
        ##    c.setFont('Helvetica',10)
        ##    c.drawString(80,622,str(row['banca']))
        ##    c.drawString(80,610,str(row['iban']))  


def struttura (c):
    #c.setLineWidth(1)
    ##c.rect(307,254,-92,1,0)
    c.rect(307,781,254,-112,1,0) # corn testata bolla 
    c.rect(307,664,254,-65,1,0) # corn destinazione 
    c.rect(135,589,0,-330,1,0) # riga vert cod articolo
    c.rect(452,589,0,-330,1,0) # riga vert descrizione
    c.rect(36,589,525,-330,1,0) # corn corpo
    c.rect(36,254,525,-98,1,0) # corn calce
    c.rect(36,563,525,0,1,0) # corn destinazione 
    c.rect(38,622,254,-23,1,0) # corn num data ord bolla  
    c.setFont('Helvetica',11)
    c.drawString(313,764,_("Spett.le Ditta"))
    c.setFont('Helvetica-Bold',12)
    c.drawString(314,698,_("Cod. Fisc. :"))
    c.drawString(314,682,_("P.Iva :"))
    c.drawString(315,650,_("Luogo di destinazione (se diverso)  "))
    c.setFont('Helvetica-Bold',10)
    c.drawString(41,572,_("Cod.Articolo"))
    c.drawString(201,572,_("Descrizione dei beni (Natura - Qualita`)"))
    c.drawString(479,572,_("Quantita`"))
    c.setFont('Helvetica-Bold',12)
    c.drawString(47,608,_("Num.  "))
    c.drawString(147,608,_("del  "))
    c.drawString(44,634,_("Doc.trasporto DDT - Reso fornitore"))
    c.setFont('Helvetica-Bold',10)
    c.drawString(401,134,_("Firma Destinatario"))
    c.drawString(57,134,_("Firma Vettore"))
    c.drawString(226,134,_("Firma Conducente"))
    c.drawString(57,99,"...................................................")
    c.drawString(226,99,"...................................................")
    c.drawString(401,99,"...................................................")
    c.drawString(53,219,_("Aspetto esteriore dei  beni: "))
    c.drawString(53,238,_("Spedizione a mezzo: "))
    c.drawString(247,238,_("Porto: "))
    c.drawString(53,198,_("Causale: "))
    c.drawString(172,198,_("Numero Colli: "))
    c.drawString(325,198,_("Volume: "))
    c.drawString(436,198,_("Peso lordo Kg. :"))
    c.drawString(53,174,_("Vettore incaricato del trasporto: "))
    c.setFont('Helvetica',9)
    #c.drawString(117,66,_("I beni in oggetto della presente nota di spedizione sono soggetti al regime di fatturazione immediata"))

def corpo (c,row,Y):
    c.setFont('Helvetica',12)
    c.drawString(43,Y,str(row['codart']))
    c.drawString(148,Y,str(row['descrizart']))
    c.drawRightString(487,Y,str(row['qtart']))

def calce (c,row):
    c.rect(29.5484,248.266,0,0,1,0)

def calceB (c,row):
    c.setFont('Helvetica',10)
    c.drawString(174,238,str(row['dvett']))
    c.drawString(289,238,str(row['dconse']))
    c.drawString(199,219,str(row['dconfe']))
    c.drawString(105,198,str(row['dtrasp']))
    c.drawString(249,198,str(row['colli']))
    c.drawString(519,198,str(row['peso']))
    c.drawString(372,198,str(row['vol']))

def querycorpo ():
     return """ select round((prez_un), 6) as prez_un, qt_1 as qtart, sc1, 
                descriz as descrizart, cod as codart, aliva,
                round(((prez_un * qt_1)- (prez_un * qt_1 * (sc1/100))) ,6) as tot_riga
                from docu2 where anno = "%s"  and tipo_doc = "%s"  
		and num_doc = %s """

def querytestata ():
     return """ select rag_soc,codfisc, piva, data_doc, num_doc, cod_cf, tpag, 
                cap_zona_pr,indi,tabgen.descriz as dpag
		from
		(select rag_soc,indiriz_cap_zona,cap_zona_pr, 
		indi, data_doc, num_doc, cod_cf, tpag, 
		anag.piva as piva,anag.codfisc as codfisc
		from
		(select(rag_soc1||" "||rag_soc2)as rag_soc,
		(indiriz) as indi, 
		(indiriz||" "||cap||" "||zona||" "||localit) as indiriz_cap_zona,
		(cap||" "||zona||" "||localit||" "||PR )as cap_zona_pr, 
		docu1.pagam as tpag, data_doc, num_doc, cod_age, cod_cf,
		docu1.cod_cf as codcf
		from docu1 where anno = "%s" and tipo_doc = "%s" and num_doc = %s),anag
		where anag.cod =  codcf and t_cpart='F'), tabgen
		where tabgen.cod = "PAGAM" and tabgen.valore = tpag """

def querycalce ():
     return """ select sum(docu.d_imp) as tot_merce, sum(docu.imp_iva) as tot_iva,
                (sum(docu.d_imp)+sum(docu.imp_iva)) as tot_doc
		from
		(select sum(docu2.tot_riga) as d_imp, 
		(sum(docu2.tot_riga) * docu2.aliva /100) as imp_iva
		from docu2 where anno = "%s"  and tipo_doc = "%s"  and num_doc = %s
		group by aliva) as docu """

def querycalceB ():
     return """ select dimbal, "" as vol, dtrasp, dconfe, dconse, colli, peso,
                data_tra, ora_tra, rag_soc1 as dvett
		from
		(select descriz as dimbal, dconfe, dtrasp, dconse, colli, 
		peso, data_tra, ora_tra, cvet
		from
		(select descriz as dconfe, dtrasp, dconse, vimbal, colli,
		peso, data_tra, ora_tra, cvet
 		from
		(select descriz as dconse, dtrasp, vconfe, vimbal, colli,
		peso, data_tra, ora_tra, cvet
 		from
		(select descriz as dtrasp, vtrasp, vconfe, vconse, vimbal, 
		colli, peso, data_tra, ora_tra, cvet
 		from
		(select trasp as vtrasp, conse as vconse, aspet as vconfe,
		imbal as vimbal, colli, peso, data_tra, ora_tra,
		cod_vet as cvet
		from docu1 where anno = "%s" and tipo_doc = "%s" 
		and num_doc = %s ), tabgen
		where cod = "TRASP" and valore = vtrasp),tabgen
		where cod = "PORTO" and valore = vconse),tabgen
		where cod = "CONFE" and valore = vconfe),tabgen
		where cod = "IMBAL" and valore = vimbal),anag
		where t_cpart = "V" and cod = cvet """

def fontcorpo ():
     return 12

def Ycorpo ():
     return 546

def fineSeq ():
     return 266
