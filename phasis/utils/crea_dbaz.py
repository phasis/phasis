
import cfg
import sqlite3 as sqlite
import time
import gettext

try:
    cn = sqlite.connect(cfg.path_db + 'dbaz.db' , isolation_level='IMMEDIATE')
    cr = cn.cursor()
    cr.execute(""" create table aziende (
        T_CPART Char(1), 
        COD Integer, 
	CODBAR Integer, 
	RAG_SOC1 Varchar(40), 
	RAG_SOC2 Varchar(40), 
	NSRIF Varchar(15), 
	INDIRIZ Varchar(40), 
	CAP Varchar(5), 
	ZONA Varchar(30), 
	LOCALIT Varchar(30), 
	PR Char(2), 
	STATO Varchar(20), 
	INDIRIZ1 Varchar(40), 
	CAP1 Varchar(5), 
	ZONA1 Varchar(30), 
	LOCALIT1 Varchar(30), 
	PR1 Char(2), 
	STATO1 Varchar(20), 
	TEL_ABIT Varchar(15), 
	TEL_UFF Varchar(15), 
	MOBILE Varchar(15), 
	FAX Varchar(15), 
	WEB Varchar(35), 
	E_MAIL Varchar(35), 
	CODFISC Varchar(16), 
	PIVA Varchar(18), 
	BANCA Varchar(40), 
	NUM_CC Varchar(15),
	ABI Varchar(5), 
	CAB Varchar(5), 
	SCAD_DA Varchar(10), 
	SCAD_A Varchar(10), 
	MASTRO Varchar(5), 
	COD_DIV Char(3), 
	REA Varchar(30), 
	CAMPO1 Varchar(25), 
	CAMPO2 Varchar(25),
        PAESE varchar(2),
	COD_C varchar(2),
	CIN varchar(1))	""" )

    cr.execute(""" insert into aziende 
	values('Z',1,'','"""+ _("Azienda da Personalizzare")+"""','',
	'"""+ _("Azienda da Personalizzare")+"""','Via Vattelapesca sns',
	'00050','Aranova','Fiumicino','RM','Italia','','','',
	'','RM','',1234567890,1234567890,'',123456789,'','',
	'',0123456789,'','',0,0,'','',0,'EU','','','','','','') """ )

    cr.execute(""" create table parcon (
       COD Varchar(11) ,
       VALORE Varchar(5) not null  ,
       DESCRIZ Varchar(50) ,
       VAR1 Varchar(4) ,
       VAR2 Varchar(4) ,
       VAR3 Varchar(10) ,
       VAR4 Varchar(10) ,
       VAR5 Varchar(30) ,
       INT1 Smallint,
       INT2 Smallint,
       INT3 Numeric(9,2),
       INT4 Numeric(9,2),
       PRIMARY KEY (VALORE)) """ )

    cr.execute(""" insert into parcon values('POSL',1,'"""+ _("Postazione 001")+"""','','','','','','','','','') """ )
    cr.execute(""" insert into parcon values('ANNODA',2008,'"""+ _("Anno Contabile")+"""','','','','','','','','','') """ )
    cr.execute(""" insert into parcon values('ANNOA',2009,'"""+ _("Anno Contabile")+"""','','','','','','','','','') """ )
    cr.execute(""" insert into parcon values('BACKUP','Y','Phasis','','','','','','','','','') """ )
    cr.execute(""" insert into parcon values('POSL1','','',2008,2009,'01/01/2009','','',1,0,0,0) """ )

    cr.execute(""" create table utenti (
       COD Integer not null,
       UTE Varchar(10) ,
       PWD Varchar(10) ,
       CODAZ Smallint,
       ABL Smallint,
       SCAD Varchar(10) ,
       PRIMARY KEY (COD)) """ )

    cr.execute(""" insert into utenti values(1,'"""+ _("Utente")+"""','Utente','',9,'') """ )

except StandardError, msg:
    evt = 'Error %s' % (msg)
    t = time.localtime(time.time())	    
    st = time.strftime(" %d/%m/%Y  %H:%M", t)
    ferr = open (cfg.path_logs + "err_creadbaz.log","a")
    err = st + "  " + evt
    print err            
    ferr.write(err+'\n')
    ferr.close()
cn.commit()

