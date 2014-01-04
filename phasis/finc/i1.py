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


import cfg
from reportlab.lib.pagesizes import *

def layout():
    return portrait(A4)

def testata (c,row):
    c.setFont('Helvetica',12)
    c.drawString(466,617,str(row['data_doc']))
    c.drawString(360,617,str(row['num_doc']))
    c.setFont('Helvetica',10)
    c.drawString(143,660,str(row['codfisc']))
    c.drawString(143,648,str(row['piva']))
    c.drawString(119,636,str(row['dpag']))
    c.setFont('Helvetica-Bold',12)
    c.drawString(313,723,str(row['rag_soc']))
    c.drawString(313,706,str(row['indi']))
    c.drawString(313,690,str(row['cap_zona_pr']))
    c.setFont('Helvetica',12)
    c.drawRightString(536,744,str(row['cod_cf']))




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
        #c.drawImage(cfg.path_img+'/logo4.jpg',39,740,260,85)
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
    ##c.rect(307,700,254,-92,1,0)
    ##c.drawString(315,650,"Luogo di destinazione (se diverso)  ")
    c.rect(307,761,254,-92,1,0) # corn testata
    c.rect(36,600,525,-376,1,0) # corn corpo
    c.rect(110,600,0,-376,1,0) # riga vert codart
    c.rect(330,600,0,-376,1,0) # riga vert descriz
    c.rect(360,600,0,-376,1,0) # riga vert um
    c.rect(415,600,0,-376,1,0) # riga vert qt
    c.rect(480,600,0,-376,1,0) # riga vert prezzo un
    c.rect(504,600,0,-376,1,0) # riga vert iva 
    c.rect(36,219,525,-69,1,0) # corn calce
    c.rect(36,145,525,-124,1,0) # corn calceb
    c.rect(307,634,254,-26,1,0) # corn num data docu
    c.rect(36,575,525,0,1,0) # riga oriz testata copro

    c.setFont('Helvetica',11)
    c.drawString(313,744,_("Spett.le")) #### Ditta")
    c.setFont('Helvetica-Bold',12)
    c.drawString(436,616,_("del  "))
    c.drawString(319,616,_("Num.  "))
    c.drawString(308,646,_("FATTURA  ACCOMPAGNATORIA"))
    ###c.drawString(39,618,"Banca :")
    c.setFont('Helvetica-Bold',10)
    c.drawString(39,660,_("Cod. Fisc. :"))
    c.drawString(39,648,_("P.Iva :"))
    c.drawString(39,636,_("Pagamento :"))
    c.drawString(39,627,_("Banca :"))

    c.setFont('Helvetica-Bold',10)
    c.drawString(41,583,_("Cod.Articolo"))
    c.drawString(115,583,_("Descrizione Articolo"))
    c.drawString(335,583,_("UM"))
    c.drawString(380,583,_("Q.ta`"))
    c.drawString(425,583,_("Prezzo Un."))
    #c.drawString(342,583,_("Q.ta`"))
    #c.drawString(376,583,_("Prezzo Unitario"))
    #c.drawString(477,583,_("Iva"))
    c.drawString(482,583,_("Iva"))
    c.drawString(515,583,_("Importo"))
    c.drawString(51,206,_("Totale merce"))
    c.drawString(412,206,_("Valuta"))
    c.drawString(135,206,_("Imponibile"))
    c.drawString(202,206,_("Iva"))
    c.drawString(319,206,_("Importo Iva"))
    c.drawString(230,206,_("Descrizione"))
    c.setFont('Helvetica-Bold',10)
    c.drawString(475,206,_("Totale Fattura"))
    c.setFont('Helvetica',12)
    c.drawString(416,189,_("Euro"))
    c.setFont('Helvetica-Bold',10)
    c.drawString(42,129,_("Spdedizione merce"))
    c.drawString(314,48,_("Firma del conducente"))
    c.drawString(449,48,_("Firma del destinatario"))
    c.drawString(468,88,_("Firma Vettore"))
    c.drawString(41,88,_("Vettore"))
    c.drawString(163,88,_("Residenza o domicilio"))
    c.drawString(329,88,_("Data e ora ritiro"))
    c.rect(36,59,524,0,1,0)# riga oriz calceb
    c.rect(36,99,524,0,1,0)# riga oriz calceb
    c.drawString(211,129,_("Porto : "))
    c.drawString(337,129,_("Aspetto esteriore dei beni: "))
    c.drawString(42,109,_("Causale"))
    c.drawString(211,109,_("Numero colli:"))
    c.drawString(337,109,_("Peso lordo Kg."))
    c.rect(202,145,0,-46,1,0)# riga vert calceb
    c.rect(328,145,0,-46,1,0)# riga vert calceb
    c.drawString(41,48,_("Data e ora trasporto"))
    c.rect(433,99,0,-78,1,0)# riga vert calceb
    c.rect(299,99,0,-78,1,0)# riga vert calceb
    ##c.rect(135,589,0,-330,1,0)
    ##c.rect(452,589,0,-330,1,0)
	
def corpo (c,row,Y):
    c.setFont('Helvetica',10)
    c.drawString(41,Y,str(row['codart']))
    c.drawString(115,Y,str(row['descriz'].encode('utf_8')))
    c.drawRightString(353,Y,str(row['umart']))
    c.drawRightString(410,Y,str(row['qt_1']))
    c.drawRightString(475,Y,str(row['prez_un']))
    c.drawString(485,Y,str(row['alivaart']))
    #c.drawRightString(364,Y,str(row['qt_1']))
    #c.drawRightString(453,Y,str(row['prez_un']))
    #c.drawString(480,Y,str(row['alivaart']))
    c.drawRightString(554,Y,str(row['tot_riga']))

def calce (c,row):
    c.setFont('Helvetica',12)
    c.drawString(67,190,str(row['tot_merce']))
    c.drawRightString(530,190,str(row['tot_doc']))
    c.drawString(323,190,str(row['tot_iva']))

def dettaglioiva (c,row,Y):
    c.setFont('Helvetica',12)
    c.drawString(234,Y,str(row['d_des']))
    c.drawString(139,Y,str(row['d_imp']))
    c.drawString(202,Y,str(row['d_iva']))

def calceB (c,row):
    c.setLineWidth(1)
    c.setFont('Helvetica',12)
    c.drawString(145,129,str(row['dvett']))
    c.drawString(259,129,str(row['dconse']))
    c.drawString(471,129,str(row['dimbal']))
    c.drawString(97,110,str(row['dtrasp']))
    c.drawString(285,110,str(row['colli']))
    c.drawString(421,110,str(row['peso']))
    c.rect(205,74,0,0,1,0)
    c.drawString(51,32,str(row['data_tra']))
    c.drawString(132,32,str(row['ora_tra']))
    
def querycorpo ():
    return ''' select um as umart, round(prez_un,6) as prez_un, 
               round(qt_1,6) as qt_1, round(sc1,6) as sc1, 
	       (substr(descriz,0,35)) as descriz, 
	       cod as codart, aliva as alivaart, 
	       (round((prez_un * qt_1),6) - round((prez_un * qt_1 * (round(sc1,6)/100)),6)) as tot_riga
	       from docu2 where anno = "%s" and tipo_doc = "%s" 
	       and num_doc = %s '''


def querytestata ():
    return '''select rag_soc, codfisc, piva, data_doc, num_doc, cod_cf, tpag, 
              cap_zona_pr, indi, tabgen.descriz as dpag, vspos, vscom, vsord 
	      from (select rag_soc, indiriz_cap_zona, cap_zona_pr, indi,
	      data_doc, num_doc, cod_cf, tpag,
	      anag.piva as piva,anag.codfisc as codfisc, vspos, vscom, vsord 
	      from (select(rag_soc1||" "||rag_soc2)as rag_soc, 
	      (indiriz) as indi,
	      (indiriz||" "||cap||" "||zona||" "||localit) as indiriz_cap_zona,
	      (cap||" "||zona||" "||localit||" "||pr )as cap_zona_pr,
	      docu1.PAGAM as tpag, data_doc, num_doc, cod_age, cod_cf,
	      docu1.cod_cf as codcf, docu1.nsrif as vspos, docu1.vsrif as vscom, 
	      docu1.vsord as vsord 
	      from docu1 where anno = "%s" and tipo_doc = "%s" 
	      and num_doc = %s),anag
	      where anag.cod =  codcf and t_cpart='C'), tabgen
	      where tabgen.cod = "PAGAM" and tabgen.valore = tpag '''

def querydettaglioiva ():
     return ''' select d_imp, d_iva, imp_iva, tabgen.descriz as d_des
                from
		(select sum(docu2.tot_riga) as d_imp, docu2.aliva as d_iva,
		(sum(docu2.tot_riga) * round(docu2.aliva,2)/100) as imp_iva
		from docu2 where anno = "%s" and tipo_doc = "%s" 
		and num_doc = %s group by aliva)  as docu, tabgen
		where tabgen.cod = "ALIVA" and tabgen.valore = d_iva '''

def querycalce ():
     return ''' select round(sum(docu.d_imp),6) as tot_merce,
                sum(docu.imp_iva) as tot_iva, 
		(sum(docu.d_imp) + sum(docu.imp_iva)) as tot_doc
		from (select sum(docu2.tot_riga) as d_imp, 
		(sum(docu2.tot_riga) * round(docu2.aliva,2)/100) as imp_iva
		from docu2 where anno = "%s"  and tipo_doc = "%s" 
		and num_doc = %s group by aliva)  as docu '''


def querycalceB ():
     return ''' select dimbal, "" as vol, dtrasp, dconfe, dconse, colli, peso,
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
		where t_cpart = "V" and cod = cvet '''
  
def fontcorpo ():
     return 12

def Ycorpo ():
     return 553

def fontdettaglioiva ():
     return 12

def Ydettaglioiva ():
     return 190

def fineSeq ():
     return 231
