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
    ###c.drawString(150,118,str(row['vsord']))
    ###c.drawString(150,105,str(row['vscom']))
    ###c.drawString(150,93,str(row['vspos']))

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
    c.rect(36,600,525,-415,1,0) # corn corpo
    c.rect(36,575,525,0,1,0) # riga oriz testata corpo
    c.rect(36,177,526,-95,1,0) # corn calce
    c.rect(110,600,0,-415,1,0) # riga vert codart
    c.rect(330,600,0,-415,1,0) # riga vert descriz
    c.rect(360,600,0,-415,1,0) # riga vert um
    c.rect(415,600,0,-415,1,0) # riga vert qt
    c.rect(480,600,0,-415,1,0) # riga vert prezzo un
    c.rect(504,600,0,-415,1,0) # riga vert iva 
    c.rect(307,761,254,-92,1,0) # corn testata documento 
    c.rect(307,634,254,-26,1,0) # corn num data documento 
    #c.setFillColor((0, 0, 0))

    c.setFont('Helvetica',11)
    c.drawString(313,744,_("Spett.le")) #### Ditta")
    c.setFont('Helvetica-Bold',12)
    c.drawString(436,616,_("del  "))
    c.drawString(319,616,_("Num.  "))
    c.drawString(308,646,_("NOTA DI ACCREDITO"))
    ###c.drawString(39,618,"Banca :")
    c.setFont('Helvetica-Bold',10)
    c.drawString(39,660,_("Cod. Fisc. :"))
    c.drawString(39,648,_("P.Iva :"))
    c.drawString(39,636,_("Pagamento :"))
    c.setFont('Helvetica-Bold',10)
    c.drawString(41,583,_("Cod. Articolo"))
    c.drawString(115,583,_("Descrizione Articolo"))
    c.drawString(335,583,_("UM"))
    c.drawString(380,583,_("Q.ta`"))
    c.drawString(425,583,_("Prezzo Un."))
    ###c.drawString(52,118,"Ordine N.           :") ##gia` Scadenze
    ###c.drawString(52,105,"Commessa N.    :") ##gia` Importi
    ###c.drawString(52,92,"Posizione N.       :") ## news
    c.drawString(470,156,_("Totale Documento"))
    ####c.drawString(475,583,"Sc.")
    c.drawString(482,583,_("Iva"))
    c.drawString(515,583,_("Importo"))
    c.drawString(52,156,_("Totale merce"))
    c.drawString(413,156,_("Valuta"))
    c.drawString(136,156,_("Imponibile"))
    c.drawString(204,156,_("Iva"))
    c.drawString(320,156,_("Importo Iva"))
    c.drawString(231,156,_("descrizione"))
    c.setFont('Helvetica',12)
    c.drawString(418,139,_("Euro"))
    #c.setFont('Helvetica',9)
    #c.drawString(115,192,"Contributo Ambientale CONAI Assolto (ove dovuto)")

def corpo (c,row,Y):
    c.setFont('Helvetica',10)
    c.drawString(45,Y,str(row['codart']))
    c.drawString(115,Y,str(row['descriz']))
    c.drawRightString(353,Y,str(row['umart']))
    c.drawRightString(410,Y,str(row['qt_1']))
    c.drawRightString(475,Y,str(row['prez_un']))
    ####c.drawRightString(460,Y,str(row['SC1']))
    c.drawString(485,Y,str(row['alivaart']))
    c.drawRightString(554,Y,str(row['tot_riga']))

def dettaglioiva (c,row,Y):
    c.setLineWidth(1)
    c.setFont('Helvetica',12)
    c.drawString(235,Y,str(row['d_des']))
    c.drawString(141,Y,str(row['d_imp']))
    c.drawString(203,Y,str(row['d_iva']))

def calce (c,row):
    c.drawString(68,140,str(row['tot_merce']))
    c.drawRightString(532,140,str(row['tot_doc']))
    c.drawString(325,140,str(row['tot_iva']))

def querycorpo ():
    return ''' select um as umart, round(prez_un,6) as prez_un , round(qt_1,6) as qt_1, 
               round(sc1,6) as sc1, (substr(descriz,0,35)) as descriz, 
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
