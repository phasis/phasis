
import cfg
import sqlite3 as sqlite
import time

try:
    cn = sqlite.connect(cfg.path_db + 'az001.db' , isolation_level='IMMEDIATE')
    cr = cn.cursor()
    cr.execute(""" create table agenti (
	T_CPART CHAR(1), 
	COD INTEGER, 
	CODBAR VARCHAR(15), 
	RAG_SOC1 VARCHAR(40), 
	RAG_SOC2 VARCHAR(40), 
	NSRIF VARCHAR(11), 
	INDIRIZ VARCHAR(40), 
	CAP VARCHAR(5), 
	ZONA VARCHAR(30), 
	LOCALIT VARCHAR(30),
	PR CHAR(2), 
	STATO VARCHAR(20), 
	INDIRIZ1 VARCHAR(40), 
	CAP1 VARCHAR(5), 
	ZONA1 VARCHAR(30), 
	LOCALIT1 VARCHAR(30), 
	PR1 CHAR(2), 
	STATO1 VARCHAR(20), 
	TEL_ABIT VARCHAR(15), 
	TEL_UFF VARCHAR(15), 
	MOBILE VARCHAR(15), 
	FAX VARCHAR(15), 
	WEB VARCHAR(35), 
	E_MAIL VARCHAR(35), 
	CODFISC VARCHAR(16), 
	PIVA VARCHAR(18), 
	BANCA VARCHAR(40), 
	NUM_CC VARCHAR(15), 
	ABI VARCHAR(6), 
	CAB VARCHAR(6), 
	PROVV DECIMAL(4,2), 
	COD_MA VARCHAR(11), 
	PROVV_MA DECIMAL(4,2), 
	SCAD_DA VARCHAR(10), 
	SCAD_A VARCHAR(10), 
	COD_PDC VARCHAR(5), 
	COD_PAG VARCHAR(5), 
	MASTRO INTEGER, 
	VDIV CHAR(3), 
	RAG_PART CHAR(2), 
	PRECON CHAR(1), 
	NOTE BLOB(80,0), 
	CAMPO1 VARCHAR(15), 
	CAMPO2 VARCHAR(15)) """ )

    cr.execute(""" insert into agenti values('A',1,'','"""+ _("Agente 1")+"""','','','','','','','--','','',
	'','','','--','','','','','','','','','','','',0,0,0,'',0,'','','',
	'PAG23',0,'','','C','','','') """ )

    cr.execute(""" create table anag (
	T_CPART Char(1), 
	COD Integer, 
	CODBAR Varchar(15), 
	RAG_SOC1 Varchar(40), 
	RAG_SOC2 Varchar(40), 
	NSRIF Varchar(30), 
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
	ABI Varchar(6), 
	CAB Varchar(6), 
	SC1 Numeric(3,2), 
	SC2 Numeric(3,2), 
	SC3 Numeric(3,2),
	LST Smallint, 
	SCAD_DA Varchar(10), 
	SCAD_A Varchar(10), 
	CONSEG Varchar(5), 
	TRASP Varchar(5), 
	COD_AGE Varchar(11), 
	COD_DEST Varchar(11), 
	COD_VET Varchar(11), 
	COD_PDC Varchar(5), 
	COD_PAG Varchar(5), 
	MASTRO Integer, 
	VDIV Char(3), 
	FIDO Numeric(15,6), 
	RAG_PART Char(2), 
	PRECON Char(1), 
	NOTE Blob(80,0), 
	CAMPO1 Varchar(15), 
	CAMPO2 Varchar(15), 
        PAESE type varchar(2), 
        COD_C type varchar(2), 
        CIN type varchar(1), 
        FAXD type varchar(20), 
        EMAILD type varchar(35)) """ )

    cr.execute(""" insert into anag values ('V',1,'','Mittente','','','',0,'','','--','','',0,'','','--','','','','',0,'','','','','','',0,0,0,0,0,1,'','','','','','','','','',0,'EU',0,'','C','','','','','','','','') """ )
    cr.execute(""" insert into anag values ('V',2,'','Destinatario','','','',0,'','','--','','',0,'','','--','','','','',0,'','','','','','',0,0,0,0,0,1,'','','','','','','','','',0,'EU',0,'','C','','','','','','','','') """ )

    cr.execute(""" create table articoli (
	COD VARCHAR(15),
	CODBAR VARCHAR(15), 
	DESCRIZ VARCHAR(70), 
	UM CHAR(2), 
	MIS VARCHAR(5), 
	PREZZO_1 NUMERIC(15,6),
	PREZZO_2 NUMERIC(15,6), 
	COSTO NUMERIC(15,6), 
	MERCE VARCHAR(5), 
	COD_FOR INTEGER, 
	DESCRFOR VARCHAR(40), 
	ALIVA VARCHAR(5), 
	QT_MIN NUMERIC(6,2), 
	QT_MAX NUMERIC(6,2), 
	SC1 NUMERIC(3,2), 
	SC2 NUMERIC(3,2), 
	SC3 NUMERIC(3,2), 
	CACQU VARCHAR(10), 
	DIVACQ VARCHAR(3), 
	CVEND VARCHAR(10), 
	DIVVEN VARCHAR(3), 
	PROVV NUMERIC(3,2), 
	IMBAL VARCHAR(5), 
	CONFE VARCHAR(5), 
	PESO DECIMAL(6,2), 
	VOLUME NUMERIC(5,2), 
	DATA_INS VARCHAR(10), 
	DATA_MOD VARCHAR(10), 
	INPROD CHAR(1), 
	NOTE BLOB(80,0)) """ )

    cr.execute(""" insert into articoli values('--','','----------------------------------------',
	'PZ','',0,0,0,01,0,'',20,0,0,0,0,0,'','EU','','EU',0,'IMBVS','CFSF',0,
	0,'','','Y','') """ )

    cr.execute(""" create table docu1 (
	TIPO_DOC CHAR(2), 
	ANNO CHAR(4), 
	NUM_DOC INTEGER, 
	DATA_DOC VARCHAR(10), 
	COD_CF VARCHAR(11), 
	RAG_SOC1 VARCHAR(40), 
	RAG_SOC2 VARCHAR(40), 
	INDIRIZ VARCHAR(40), 
	CAP VARCHAR(5), 
	ZONA VARCHAR(30), 
	LOCALIT VARCHAR(30), 
	PR CHAR(2), 
	STATO VARCHAR(20), 
	COD_DEST VARCHAR(5), 
	RAG_SOC3 VARCHAR(40), 
	RAG_SOC4 VARCHAR(40), 
	INDIRIZ1 VARCHAR(40), 
	CAP1 VARCHAR(5), 
	ZONA1 VARCHAR(30),
	LOCALIT1 VARCHAR(30), 
	PR1 CHAR(2), 
	STATO1 VARCHAR(20), 
	CAMBIO NUMERIC(15,6), 
	LST SMALLINT, 
	VSORD VARCHAR(10), 
	VSDATA VARCHAR(10),
	VDIV VARCHAR(3), 
	COD_AGE VARCHAR(11), 
	PAGAM VARCHAR(5), 
	CONSE VARCHAR(5), 
	TRASP VARCHAR(5), 
	COD_VET VARCHAR(11), 
	VSRIF VARCHAR(15), 
	NSRIF VARCHAR(15), 
	RAG_DOC CHAR(2), 
	CAMPO1 VARCHAR(15), 
	CAMPO2 VARCHAR(15), 
	NOTE BLOB(80,0), 
	IMBAL VARCHAR(5), 
	ASPET VARCHAR(5), 
	COLLI NUMERIC(6,2), 
	PESO NUMERIC(6,2), 
	SC1 NUMERIC(3,2), 
	SC2 NUMERIC(3,2), 
	SC3 NUMERIC(3,2), 
	PDC_SC VARCHAR(5), 
	COD_IMB VARCHAR(5), 
	IVA_IMB VARCHAR(5), 
	PREZ_IMB NUMERIC(15,6), 
	COD_SPE VARCHAR(5), 
	IVA_SPE VARCHAR(5), 
	PREZ_SPE NUMERIC(15,6), 
	COD_RIV VARCHAR(5), 
	IVA_RIV VARCHAR(5), 
	PREZ_RIV NUMERIC(15,6), 
	COD_BOL VARCHAR(5), 
	IVA_BOL VARCHAR(5), 
	PREZ_BOL NUMERIC(15,6), 
	COD_TRA VARCHAR(5), 
	IVA_TRA VARCHAR(5), 
	PREZ_TRA NUMERIC(15,6), 
	DATA_TRA VARCHAR(10), 
	ORA_TRA VARCHAR(8), 
	CAMPO3 SMALLINT, 
	CAMPO4 NUMERIC(15,6), 
	NOTE1 BLOB(80,0), 
	STT_DOC CHAR(1)) """ )

    cr.execute(""" create table docu2 (
	TIPO_DOC CHAR(2), 
	ANNO VARCHAR(4), 
	NUM_DOC INTEGER, 
	COD_MAG SMALLINT, 
	NUM_RIG SMALLINT, 
	COD VARCHAR(15), 
	CODBAR VARCHAR(15), 
	CODMERC VARCHAR(5), 
	DESCRIZ VARCHAR(70), 
	UM CHAR(2), 
	MIS VARCHAR(5), 
	QT_1 NUMERIC(6,2), 
	QT_2 NUMERIC(6,2),
	QT_3 NUMERIC(6,2), 
	PREZ_UN NUMERIC(15,6), 
	PREZ_AG NUMERIC(15,6), 
	TOT_RIGA NUMERIC(15,6), 
	ALIVA VARCHAR(5), 
	SC1 NUMERIC(3,2), 
	SC2 NUMERIC(3,2), 
	SC3 NUMERIC(3,2), 
	PROVV NUMERIC(3,2), 
	CAMBIO NUMERIC(15,6), 
	COLLI NUMERIC(6,2), 
	PESO NUMERIC(6,2), 
	LST SMALLINT, 
	PDC VARCHAR(5), 
	ANNODOC CHAR(4),
	TIPODOC CHAR(2), 
	DATADOC VARCHAR(10), 
	NUMDOC VARCHAR(15), 
	RIGAORD SMALLINT, 
	RIGAMAG SMALLINT, 
	RAG_DOC CHAR(2), 
	CAMPO1 VARCHAR(15), 
	CAMPO2 VARCHAR(15), 
	STT_DOC CHAR(1)) """ )

    cr.execute(""" create table giacen(
	ANNO CHAR (4) not null,
	CODMAG SMALLINT,
	COD VARCHAR (15) not null,
 	LRIORD CHAR (1),
 	QTMIN NUMERIC (6, 2),
 	QTMAX NUMERIC (6, 2),
 	GIAINIZ NUMERIC (6, 2),
 	VALINIZ NUMERIC (6, 2),
 	PROCAR NUMERIC (6, 2),
 	PROSCA NUMERIC (6, 2),
 	CARVAL NUMERIC (15,6),
 	SCAVAL NUMERIC (15,6),
 	VALCAR NUMERIC (15,6),
 	VALSCA NUMERIC (15,6),
 	QTAVIS NUMERIC (6, 2),
 	QTAENT NUMERIC (6, 2),
 	QTAORD NUMERIC (6, 2),
 	QTAIMP NUMERIC (6, 2),
 	UCOSTO NUMERIC (15,6),
 	UDATCAR VARCHAR (10),
 	UDATSCA VARCHAR (10),
 	CFM CHAR (1),
 	COD_CFM VARCHAR (11),
 	CF_SCA CHAR (1),
 	CODCFSCA VARCHAR (11),
	PRIMARY KEY (ANNO,COD)) """ )

    cr.execute(""" create table libriaz (
	CHIAVE VARCHAR(5), 
	ANNO VARCHAR(10), 
	REGISTRO CHAR(2), 
	ULTNUM INTEGER, 
	ULTPAG NUMERIC(15,6), 
	ULTIMP NUMERIC(15,6), 
	TOTDARE NUMERIC(15,6), 
	TOTAVERE NUMERIC(15,6), 
	TIPOREG CHAR(1), 
	LIQUIDA NUMERIC(15,6), 
	RAG_LIQ CHAR(1), 
	DEBCRE CHAR(1), 
	CONTO VARCHAR(5), 
	DESCRIZ VARCHAR(40), 
	DESCRIZ1 VARCHAR(40), 
	UDATST VARCHAR(10), 
	UDATREG VARCHAR(10), 
	LIQANN NUMERIC(15,6), 
	INTESTA VARCHAR(20)) """ )

    cr.execute(""" insert into libriaz values('REFF1',2009,'R1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('REFF2',2009,'R2',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RIMP',2009,'R1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RIMP',2009,'S',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RINT',2009,'S',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RIVA1',2009,'R1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RIVA2',2009,'R2',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RIVA3',2009,'R3',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RIVAL',2009,'R0',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RMAG',2009,'R1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RMOV',2009,'R1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RORD',2009,'OC',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RORD',2009,'OF',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RVEN',2009,'B1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RVEN',2009,'B2',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RVEN',2009,'B3',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RVEN',2009,'C1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RVEN',2009,'F1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RVEN',2009,'F2',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RVEN',2009,'I1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RVEN',2009,'R1',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RORD',2009,'PC',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values('RORD',2009,'PF',0,'','','','','','','','','','','','','','','') """ )

    cr.execute(""" create table lisart(
 	CHIAVE VARCHAR (5) not null,
 	LISART SMALLINT,
 	COD VARCHAR (15),
 	MIS VARCHAR (5),
 	COD_CF VARCHAR (11) not null,
 	QT NUMERIC (6, 2),
 	PREZCOR NUMERIC (15,6),
 	DATCOR VARCHAR (10),
 	SC1COR NUMERIC (3, 2),
 	SC2COR NUMERIC (3, 2),
 	SC3COR NUMERIC (3, 2),
 	PROVCOR NUMERIC (3, 2),
 	PREZFUT NUMERIC (15,6),
 	DATFUT VARCHAR (10),
 	SC1FUT NUMERIC (3, 2),
 	SC2FUT NUMERIC (3, 2),
 	SC3FUT NUMERIC (3, 2),
 	PROVFUT NUMERIC (3, 2),
 	PREZPRE NUMERIC (15,6),
 	DATPRE VARCHAR (10),
 	SC1PRE NUMERIC (3, 2),
 	SC2PRE NUMERIC (3, 2),
 	SC3PRE NUMERIC (3, 2),
 	PROVPRE NUMERIC (3, 2),
 	TIPSC VARCHAR (5),
 	PRIMARY KEY (CHIAVE,COD_CF)) """ )

    cr.execute(""" create table movcon(
 	ANNO CHAR (4) not null,
 	NUM_MOV INTEGER not null,
 	DATAMOV VARCHAR (10),
 	NUM_RIG SMALLINT not null,
 	ANNOIVA CHAR (4),
 	VDIV CHAR (3),
	CAUSA VARCHAR (5),
 	DESCRIZ VARCHAR (40),
 	IMPORVAL NUMERIC (15,6),
 	IMPONVAL NUMERIC (15,6),
 	ANNODOC CHAR (4),
 	TIPODOC CHAR (2),
 	DATADOC VARCHAR (10),
 	NUMDOC VARCHAR (15),
 	NUMDOC1 VARCHAR (15),
 	CONTO VARCHAR (5),
 	IMPORTO NUMERIC (15,6),
 	SEGNO CHAR (1),
 	CPART VARCHAR (5),
 	CAMBIO NUMERIC (15,6),
 	TIPOIVA VARCHAR (5),
 	TIPOIVA1 VARCHAR (5),
 	ALIVA VARCHAR (5),
 	REGISTRO CHAR (1),
 	IMPONIB NUMERIC (15,6),
 	RIGAGIOR SMALLINT,
 	PAGGIOR SMALLINT,
	NOTE Blob(80,0), 
        STT_MOV CHAR(1),
 	PRIMARY KEY (ANNO,NUM_MOV,NUM_RIG)) """ )

    cr.execute(""" create table movmag (
 	ANNO VARCHAR (4) not null,
 	NUM_MOV INTEGER not null,
 	DATAMOV VARCHAR (10),
 	CAUMA VARCHAR (5) not null,
 	COD_MAG SMALLINT,
 	CFM CHAR (1) not null,
 	COD_CF VARCHAR (11),
 	NUM_RIG SMALLINT not null,
 	COD VARCHAR (15),
 	CODBAR VARCHAR (15),
 	CODMERC VARCHAR (5),
 	DESCRIZ VARCHAR (70),
 	UM CHAR (2),
 	MIS VARCHAR (5),
 	QT NUMERIC (6, 2),
 	COSTO_UN NUMERIC (15,6),
 	COSTO_AG NUMERIC (15,6),
 	TOT_RIGA NUMERIC (15,6),
 	ALIVA VARCHAR (5),
 	VDIV VARCHAR (3),
 	CAMBIO NUMERIC (15,6),
 	SC1 NUMERIC (3, 2),
 	SC2 NUMERIC (3, 2),
 	SC3 NUMERIC (3, 2),
 	LST SMALLINT,
 	ANNODOC VARCHAR (4),
 	TIPODOC CHAR (2),
 	DATADOC VARCHAR (10),
 	NUMDOC VARCHAR (15),
 	RIGADOC SMALLINT,
 	CAMPO1 VARCHAR (15),
 	CAMPO2 VARCHAR (15),
 	PRIMARY KEY (ANNO,CAUMA,NUM_MOV,CFM,NUM_RIG)) """ )

    cr.execute(""" create table movsta(
 	CFM CHAR (1) not null,
 	COD_CF VARCHAR (11),
 	COD VARCHAR (15) not null,
 	CODMERC VARCHAR (5),
 	MIS VARCHAR (5),
 	QT NUMERIC (6, 2),
 	VALORE NUMERIC (15,6),
 	PRIMARY KEY (CFM,COD)) """ )

    cr.execute(""" create table ordi1 (
	TIPO_ORD CHAR(2), 
	ANNO CHAR(4), 
	NUM_ORD INTEGER, 
	DATA_ORD VARCHAR(10), 
	COD_CF VARCHAR(11), 
	RAG_SOC1 VARCHAR(40), 
	RAG_SOC2 VARCHAR(40), 
	INDIRIZ VARCHAR(40),
	CAP VARCHAR(5),
	ZONA VARCHAR(30), 
	LOCALIT VARCHAR(30), 
	PR CHAR(2), 
	STATO VARCHAR(20), 
	COD_DEST VARCHAR(5), 
	RAG_SOC3 VARCHAR(40), 
	RAG_SOC4 VARCHAR(40), 
	INDIRIZ1 VARCHAR(40), 
	CAP1 VARCHAR(5), 
	ZONA1 VARCHAR(30), 
	LOCALIT1 VARCHAR(30), 
	PR1 CHAR(2), 
	STATO1 VARCHAR(20), 
	STT_ORD CHAR(1),
	LST SMALLINT, 
	VSORD VARCHAR(10), 
	VSDATA VARCHAR(10),
	VDIV VARCHAR(3), 
	COD_AGE VARCHAR(11), 
	PRIO SMALLINT, 
	PAGAM VARCHAR(5), 
	CONSE VARCHAR(5), 
	TRASP VARCHAR(5), 
	COD_VET VARCHAR(11), 
	VSRIF VARCHAR(15), 
	NSRIF VARCHAR(15),
	RAG_ORD CHAR(2), 
	CAMPO1 VARCHAR(15), 
	CAMPO2 VARCHAR(15), 
	NOTE BLOB(80,0), 
	ASPET VARCHAR(5), 
	COLLI NUMERIC(6,2), 
	PESO NUMERIC(6,2), 
	SC1 NUMERIC(3,2), 
	SC2 NUMERIC(3,2), 
	SC3 NUMERIC(3,2), 
	PDC_SC VARCHAR(5), 
	PREZ_AC NUMERIC(15,6), 
	PREZ_AC1 NUMERIC(15,6), 
	CAMPO3 SMALLINT,
	CAMPO4 NUMERIC(15,6), 
	NOTE1 BLOB(80,0)) """ )

    cr.execute(""" create table ordi2(
	TIPO_ORD CHAR (2) not null,
 	ANNO VARCHAR (4) not null,
 	NUM_ORD INTEGER not null,
 	COD_MAG SMALLINT,
 	NUM_RIG SMALLINT not null,
 	COD VARCHAR (15),
 	CODBAR VARCHAR (15),
 	CODMERC VARCHAR (5),
 	DESCRIZ VARCHAR (70),
 	UM CHAR (2),
 	MIS VARCHAR (5),
 	QT_ORD NUMERIC (6, 2),
 	QT_CON NUMERIC (6, 2),
 	QT_EVA NUMERIC (6, 2),
 	PREZ_UN NUMERIC (15,6),
 	PREZ_AG NUMERIC (15,6),
 	TOT_RIGA NUMERIC (15,6),
 	ALIVA VARCHAR (5),
 	SC1 NUMERIC (3, 2),
 	SC2 NUMERIC (3, 2),
 	SC3 NUMERIC (3, 2),
 	PROVV NUMERIC (3, 2),
 	DATACONS VARCHAR (10),
 	COLLI NUMERIC (6, 2),
 	PESO NUMERIC (6, 2),
 	LST SMALLINT,
 	PDC VARCHAR (5),
 	STT_ORD CHAR (1),
 	ANNODOC CHAR (4),
 	TIPODOC CHAR (2),
 	DATADOC VARCHAR (10),
 	NUMDOC VARCHAR (15),
 	CAMPO1 VARCHAR (15),
	CAMPO2 VARCHAR (15),
 	PRIMARY KEY (ANNO,TIPO_ORD,NUM_ORD,NUM_RIG)) """ )

    cr.execute(""" create table provage(
 	NUM_PRV INTEGER not null,
 	COD_AGE VARCHAR (11),
 	ANNODOC CHAR (4),
 	TIPODOC CHAR (2),
 	DATADOC VARCHAR (10),
 	NUMDOC VARCHAR (15),
 	COD_CF VARCHAR (11),
 	COD VARCHAR (15),
 	DESCRIZ VARCHAR (70),
 	QT NUMERIC (6, 2),
 	IMPORTO NUMERIC (15,6),
 	SC1 NUMERIC (3, 2),
 	PROVV NUMERIC (3, 2),
 	VSORD VARCHAR (5),
 	VSDATA VARCHAR (5),
 	VALORE1 NUMERIC (15,6),
 	VALORE2 NUMERIC (15,6),
 	STT_PRV VARCHAR (1),
 	PRIMARY KEY (NUM_PRV)) """ )


    cr.execute(""" create table tabgen (
       COD Varchar(11) ,
       VALORE Varchar(15) not null ,
       DESCRIZ Varchar(50) ,
       VAL1 Varchar(2), 
       VAL2 Varchar(4),
       PRIMARY KEY (VALORE)) """ )

    cr.execute(""" insert into tabgen values('ALIVA',10,'Aliquota 10%','LG','') """ )
    cr.execute(""" insert into tabgen values('ALIVA',100,'Esente a.10','LG','') """ )
    cr.execute(""" insert into tabgen values('ALIVA',101,'Esente a.10  6/10/11','LG','') """ )
    cr.execute(""" insert into tabgen values('ALIVA',102,'Esente a.10 da 1 a 9','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',110,'Fattura di vendita','RI','D2FT') """ )
    cr.execute(""" insert into tabgen values('CAUSA',111,'Nota credito emessa','RI','A2NC') """ )
    cr.execute(""" insert into tabgen values('CAUSA',120,'Fattura di acquisto','RI','D1FT') """ )
    cr.execute(""" insert into tabgen values('CAUSA',121,'Nota credito ricevuta','RI','A1NC') """ )
    cr.execute(""" insert into tabgen values('CAUSA',131,'Corrispettivi a scorporo','RI','N3SC') """ )
    cr.execute(""" insert into tabgen values('CAUSA',132,'Corrispettivi ventilazione','RI','N3VE') """ )
    cr.execute(""" insert into tabgen values('CAUSA',140,'Incassato fattura n.','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',141,'Pagato n/c a cliente','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',145,'Ricevuto acconto da cliente','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',170,'Ricevuto assegno n.','LG','') """ )
    cr.execute(""" insert into tabgen values('ALIVA',20,'Aliquota 20%','LG','') """ )
    cr.execute(""" insert into tabgen values('ALIVA','20C','Aliq. 20% Intra-CEE','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',240,'Pagato fattura n.','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',241,'Incassato n/c da fornitore','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',245,'Pagato acconto a fornitore','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',270,'Emesso assegno n.','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',300,'Compensazione partite','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',301,'Rimanenze inizio anno','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',302,'Rimanenze c/visione carico','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',303,'Rimanenze c/visione scarico','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',304,'Rimanenze ordini da clienti','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',305,'Rimanenze ordini a fornitori','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',310,'Entrata di cassa','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',320,'Uscita di cassa','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',330,'Versamento contanti','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',340,'Prelevamento contanti','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',350,'Giroconto omaggi','LG','') """ )
    cr.execute(""" insert into tabgen values('ALIVA',4,'Aliquota 4%','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',410,'Pagato salari mese di','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',412,'Pagato ritenute sociali mese di','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',414,'Pagato ritenute fiscali mese di','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',416,'Salari lordi mese di','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',418,'Contributi a carico ditta mese di','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',420,'Assegni familiari mese di','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',422,'Malattia c/INPS mese di','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',430,'Uscita conto visione','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',434,'Ordini a fornitori','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',438,'Ordini da clienti','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',440,'Pagato debito I.V.A.','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',445,'Entrata conto visione','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',450,'Addebito spese bancarie','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',452,'Liquidazione competenze c/c','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',510,'Rilevata quota ammortamento','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',520,'Risconti attivi','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',521,'Risconti passivi','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',522,'Ratei attivi','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',523,'Ratei passivi','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',601,'Chiusura conto economico','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',602,'Chiusura stato patrimoniale','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',603,'Apertura stato patrimoniale','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',604,'Apertura patrimoniale clienti','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUSA',605,'Apertura patrimoniale fornitori','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',801,'Carico (quantita` e valore)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',802,'Carico (quantita`)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',803,'Carico (valore)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',804,'Reso da cliente','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',805,'Carico (prodotto finito)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',807,'Entrate varie','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',821,'Passaggio tra magazzini (car)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',900,'Riparazione','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',901,'Scarico (quantita` e valore)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',902,'Scarico (quantita`)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',903,'Scarico (valore)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',904,'Reso a fornitore','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',905,'Scarico lavorazione','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',907,'Uscite varie','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',910,'Omaggi','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',921,'Passaggio tra magazzini (sca)','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',950,'Vendita reg.di cassa','LG','') """ )
    cr.execute(""" insert into tabgen values('CAUMA',981,'Vendita al banc','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','AT','Austria','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPODOC','B1','Documento di trasporto (DDT)','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPODOC','B2','Doc.trasporto da non fatturare','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPODOC','B3','Doc.trasporto - Reso fornitore','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','BE','Belgio','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPODOC','C1','Nota di accredito','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF1','Cartoni da 1','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF10','Cartoni da 10','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF12','Cartoni da 12','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF2','Cartoni da 2','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF20','Cartoni da 20','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF24','Cartoni da 24','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF4','Cartoni da 4','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF48','Cartoni da 48','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF6','Cartoni da 6','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CF8','Cartoni da 8','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CFCR','Cartoni','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CFSC','Sacchi','LG','') """ )
    cr.execute(""" insert into tabgen values('CONFE','CFSF','Sfusi','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','CM','Centimetri','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','DE','Germania','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','DK','Danimarca','LG','') """ )
    cr.execute(""" insert into tabgen values('DIVIS','DO','Dollaro','LG','') """ )
    cr.execute(""" insert into tabgen values('ALIVA','E74','Esente art.74','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','EL','Greci','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','ES','Spagna','LG','') """ )
    cr.execute(""" insert into tabgen values('DIVIS','EU','Euro','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPODOC','F1','Fattura differita (da DDT)','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPODOC','F2','Fattura senza doc.trasporto','LG','') """ )
    cr.execute(""" insert into tabgen values('ALIVA','FC','Fuori campo IVA','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','FI','Finlandia','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','FR','Francia','LG','') """ )
    cr.execute(""" insert into tabgen values('DIVIS','FS','Franco svizzero','LG','') """ )
    cr.execute(""" insert into tabgen values('FAT02','FT21','Spese di trasporto','LG','') """ )
    cr.execute(""" insert into tabgen values('FAT02','FT22','Spese di imballo','LG','') """ )
    cr.execute(""" insert into tabgen values('FAT02','FT23','Spese varie','LG','') """ )
    cr.execute(""" insert into tabgen values('FAT02','FT24','Spese bolli','LG','') """ )
    cr.execute(""" insert into tabgen values('FAT02','FT25','Spese bancarie','LG','') """ )
    cr.execute(""" insert into tabgen values('FAT02','FT26','Arrotondamento','LG','') """ )
    cr.execute(""" insert into tabgen values('FAT02','FT31','Sconto su totale imponibile','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','GB','Gran Bretagna','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','GR','Grammi','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPODOC','I1','Fattura accompagnatoria','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','IE','Irlanda','LG','') """ )
    cr.execute(""" insert into tabgen values('IMBAL','IMBCR','Cartoni','LG','') """ )
    cr.execute(""" insert into tabgen values('IMBAL','IMBPL','Pallets','LG','') """ )
    cr.execute(""" insert into tabgen values('IMBAL','IMBSA','Sacchi','LG','') """ )
    cr.execute(""" insert into tabgen values('IMBAL','IMBSC','Scatole','LG','') """ )
    cr.execute(""" insert into tabgen values('IMBAL','IMBSF','Sfusi','LG','') """ )
    cr.execute(""" insert into tabgen values('IMBAL','IMBVS','A vista','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','IT','Italia','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','KG','Kilogrammi','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','KM','Kilometri','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','LT','Litri','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','LU','Lussemburgo','LG','') """ )
    cr.execute(""" insert into tabgen values('MAGAZ','MAG01','Magazzino Centrale','LG','') """ )
    cr.execute(""" insert into tabgen values('MAGAZ','MAG02','Magazzino Periferico','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','MG','Milligrammi','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','MM','Millimetri','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','MT','Metri','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','NL','Olanda','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','NR','Numero','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPOORD','OC','Ordine Clienti','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPOORD','OF','Ordine Fornitori','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','PAG00','Pagamento non standard','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','PAG01','Pagamento con assegno','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','PAG02','Pagamento  Contanti','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','PAG22','Contrassegno','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','PAG23','Finanziamento','LG','') """ )
    cr.execute(""" insert into tabgen values('PORTO','POR1','Porto franco','LG','') """ )
    cr.execute(""" insert into tabgen values('PORTO','POR2','Franco ns.magazzino','LG','') """ )
    cr.execute(""" insert into tabgen values('PORTO','POR3','Franco vs.magazzino','LG','') """ )
    cr.execute(""" insert into tabgen values('PORTO','POR4','Porto assegnato','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','PT','Portogallo','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','PZ','Pezzi','LG','') """ )
    cr.execute(""" insert into tabgen values('UNMIS','QL','Quintali','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPODOC','R1','Ricevuta fiscale','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','RD01','Rimessa diretta v.f.','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','RD03','Rimessa diretta 30 gg. d.f.','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','RD05','Rimessa diretta 60 gg. d.f.','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','RD06','Rimessa diretta 90 gg. d.f.','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','RD07','Rimessa diretta 30/60 gg. d.f.','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','RD08','Rimessa diretta 30/60/90 gg. d.f.','LG','') """ )
    cr.execute(""" insert into tabgen values('PAGAM','RD09','Rimessa diretta 30/60/90/120 gg. d.f.','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','SE','Svezia','LG','') """ )
    cr.execute(""" insert into tabgen values('NAZIO','SM','San Marino','LG','') """ )
    cr.execute(""" insert into tabgen values('DIVIS','ST','Sterlina','LG','') """ )
    cr.execute(""" insert into tabgen values('TRASP','TRA1','Vendita','LG','') """ )
    cr.execute(""" insert into tabgen values('TRASP','TRA2','Reso','LG','') """ )
    cr.execute(""" insert into tabgen values('TRASP','TRA3','Conto visione','LG','') """ )
    cr.execute(""" insert into tabgen values('TRASP','TRA4','Conto lavoro','LG','') """ )
    cr.execute(""" insert into tabgen values('DIVIS','YE','Yen','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPOORD','PC','Offerte Clienti','LG','') """ )
    cr.execute(""" insert into tabgen values('TIPOORD','PF','Offerte Fornitori','LG','') """ )

    cr.execute(""" create table tabmag(
	COD VARCHAR (11),
 	VALORE VARCHAR (15) not null,
 	DESCRIZ VARCHAR (50),
 	PRIMARY KEY (VALORE)) """ )

    cr.execute(""" create table tblcf (
	T_CPART CHAR(1), 
	COD INTEGER, 
	CODCF INTEGER, 
	RAG_SOC1 VARCHAR(40), 
	RAG_SOC2 VARCHAR(40), 
	NSRIF VARCHAR(11),
	INDIRIZ VARCHAR(40), 
	CAP VARCHAR(5), 
	ZONA VARCHAR(30), 
	LOCALIT VARCHAR(30), 
	PR CHAR(2), 
	STATO VARCHAR(20), 
	TEL_ABIT VARCHAR(15), 
	TEL_UFF VARCHAR(15), 
	FAX VARCHAR(15), 
	NOTE BLOB(80,0), 
	CAMPO1 VARCHAR(15),
	CAMPO2 VARCHAR(15)) """ )

    cr.execute(""" create table veriva(
	ANNO VARCHAR (4) not null,
 	PERIODO VARCHAR (2),
 	IMPORTO NUMERIC (15,6),
	IMPINT NUMERIC (15,6),
 	DATVERSA VARCHAR (4),
 	CODBANCA VARCHAR (5),
 	VERSATO NUMERIC (15,6),
	PRIMARY KEY (ANNO)) """ )


    cr.execute(""" create table scad (
            COD INTEGER not null,
            ANNO VARCHAR (10), 
    	    DATA_SCAD VARCHAR (10),
	    TIPO_SCAD VARCHAR (40), 
            PAGAM VARCHAR (5),
            T_CPART CHAR (1),
            COD_CF INTEGER,
            RAG_SOC1 VARCHAR (40), 
            RAG_SOC2 VARCHAR (40), 
            DATA_DOC VARCHAR (10), 
            TIPO_DOC VARCHAR (2),
            NUM_DOC INTEGER,
            DA CHAR (1),
            TOTALE NUMERIC (15,6),
            STT_SCAD CHAR(1),
    	    DATA_SCAD_INT INTEGER ,
            PRIMARY KEY (COD, ANNO)) """ )
 
    cr.execute(""" create table scadenze (
            COD Varchar (11) ,
            VALORE Varchar (15) NOT NULL ,
            DESCRIZ Varchar (50) ,
            VAL1 Varchar (2) , 
            VAL2 Varchar (4) , 
            PRIMARY KEY (VALORE)) """ )

    cr.execute(""" insert into scadenze values('SCAD','S01','"""+ _("Bollette")+"""','F','S') """ )
    cr.execute(""" insert into scadenze values('SCAD','S02','"""+ _("Debiti verso fornitori")+"""','F','S') """ )
    cr.execute(""" insert into scadenze values('SCAD','S04','"""+ _("Debiti verso clienti")+"""','C','S') """ )
    cr.execute(""" insert into scadenze values('SCAD','S05','"""+ _("Debiti verso agenti")+"""','A','S') """ )
    cr.execute(""" insert into scadenze values('SCAD','S06','"""+ _("Crediti verso fornitori")+"""','F','S') """ )
    cr.execute(""" insert into scadenze values('SCAD','S07','"""+ _("Crediti verso clienti")+"""','C','S') """ )
    cr.execute(""" insert into scadenze values('SCAD','S08','"""+ _("Crediti verso agenti")+"""','A','S') """ )
    cr.execute(""" insert into scadenze values('SCAD','S03','"""+ _("Documenti Phasis")+"""','T','N') """ )


    #
    cr.execute(""" alter table movcon add column D_CONTO varchar(150) """ )  

    #
    cr.execute(""" create table piacon(
	COD VARCHAR (6) not null,
 	DESCRIZ VARCHAR (50),
 	NATCON VARCHAR (1),
 	GRADO SMALLINT,
 	CFR VARCHAR (1),
 	PRIMARY KEY (COD)) """ )

    cr.execute(""" insert into piacon values('1','"""+ _("Immobilizzi attivi")+"""','A','1','R') """ )
    cr.execute(""" insert into piacon values('2','"""+ _("Costi pluriennali")+"""','A','1','R') """ )
    cr.execute(""" insert into piacon values('3','"""+ _("Rimanenze")+"""','A','1','R') """ )
    cr.execute(""" insert into piacon values('5','"""+ _("Cassa e portafoglio")+"""','A','1','R') """ )
    cr.execute(""" insert into piacon values('6','"""+ _("Banche")+"""','A','1','R') """ )
    cr.execute(""" insert into piacon values('10','"""+ _("Clienti")+"""','A','1','C') """ )
    cr.execute(""" insert into piacon values('12','"""+ _("Erario c/I.V.A.")+"""','A','1','R') """ )
    cr.execute(""" insert into piacon values('15','"""+ _("Crediti diversi")+"""','A','1','R') """ )
    cr.execute(""" insert into piacon values('16','"""+ _("Effetti in portafoglio")+"""','A','1','R') """ )
    cr.execute(""" insert into piacon values('26','"""+ _("Fondi di ammortamento")+"""','P','1','R') """ )
    cr.execute(""" insert into piacon values('27','"""+ _("Fondi vari")+"""','P','1','R') """ )
    cr.execute(""" insert into piacon values('30','"""+ _("Fornitori")+"""','P','1','F') """ )
    cr.execute(""" insert into piacon values('32','"""+ _("Debiti a medio/lungo termine")+"""','P','1','R') """ )
    cr.execute(""" insert into piacon values('35','"""+ _("Debiti diversi")+"""','P','1','R') """ )
    cr.execute(""" insert into piacon values('50','"""+ _("Acquisti")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('51','"""+ _("Altri costi di produzione")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('53','"""+ _("Rimanenze iniziali")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('55','"""+ _("Oneri del personale")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('60','"""+ _("Spese amministrazione")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('61','"""+ _("Altri costi e spese")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('65','"""+ _("Oneri tributari")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('70','"""+ _("Oneri finanziari")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('72','"""+ _("Ammortamenti")+"""','C','1','R') """ )
    cr.execute(""" insert into piacon values('73','"""+ _("Rimanenze finali")+"""','R','1','R') """ )
    cr.execute(""" insert into piacon values('75','"""+ _("Ricavi di vendita")+"""','R','1','R') """ )
    cr.execute(""" insert into piacon values('76','"""+ _("Recupero spese")+"""','R','1','R') """ )
    cr.execute(""" insert into piacon values('77','"""+ _("Altri ricavi")+"""','R','1','R') """ )
    cr.execute(""" insert into piacon values('90','"""+ _("Proventi finanziari")+"""','R','1','R') """ )
    cr.execute(""" insert into piacon values('98','"""+ _("Conti transitori")+"""','O','1','R') """ )
    cr.execute(""" insert into piacon values('99','"""+ _("Capitale netto")+"""','P','1','R') """ )
    cr.execute(""" insert into piacon values('101','"""+ _("Terreni")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('102','"""+ _("Fabbricati civili")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('103','"""+ _("Fabbricati destinati alla industria")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('104','"""+ _("Costruzioni leggere")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('105','"""+ _("Impianti generici")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('106','"""+ _("Impianti specifici")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('107','"""+ _("Macchinari")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('108','"""+ _("Attrezzature")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('109','"""+ _("Mobili e macchine da ufficio")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('110','"""+ _("Macchine da ufficio elettrom. ed elettr.")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('111','"""+ _("Autovetture")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('112','"""+ _("Mezzi di trasporto interno")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('113','"""+ _("Autocarri")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('201','"""+ _("Spese costituzione e modifica")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('202','"""+ _("Avviamento")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('203','"""+ _("Riparazioni e Manutenz. capitalizzate")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('204','"""+ _("Spese di impianto")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('205','"""+ _("Oneri di pubblicita`")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('301','"""+ _("Rimanenze finali materie prime")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('302','"""+ _("Rimanenze finali semilavorati")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('303','"""+ _("Rimanenze finali prodotti finiti")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('304','"""+ _("Rimanenze finali merci")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('305','"""+ _("Rimanenze finali materiali di consumo")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('501','"""+ _("Cassa contanti")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('502','"""+ _("Cassa effetti")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('503','"""+ _("Cassa valori bollati")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('601','"""+ _("Banca Nazionale del Lavoro")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('602','"""+ _("COMIT")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1201','"""+ _("I.V.A. su acquisti")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1202','"""+ _("I.V.A. su vendite")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1203','"""+ _("Erario c/I.V.A.")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1204','"""+ _("I.V.A. su acquisti in sospensione")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1205','"""+ _("I.V.A. su vendite in sospensione")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1501','"""+ _("Clienti per fatture da emettere")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1502','"""+ _("Prelevamenti c/titolare")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1503','"""+ _("Prelevamenti c/soci")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1504','"""+ _("Caparre a fornitori")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1505','"""+ _("Ratei attivi")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1506','"""+ _("Risconti attivi")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1507','"""+ _("Depositi cauzionali")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1601','"""+ _("Effetti attivi")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1602','"""+ _("Effetti allo incasso")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1603','"""+ _("Effetti allo sconto")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1604','"""+ _("Effetti insoluti")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('1605','"""+ _("Cambiali attive")+"""','A','2','R') """ )
    cr.execute(""" insert into piacon values('2601','"""+ _("Fondo amm.terreni")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2602','"""+ _("Fondo amm.fabbricati civili")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2603','"""+ _("Fondo amm.fabbricati dest.alla industria")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2604','"""+ _("Fondo amm.costruzioni leggere")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2605','"""+ _("Fondo amm.impianti generici")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2606','"""+ _("Fondo amm.impianti specifici")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2607','"""+ _("Fondo amm.macchimari")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2608','"""+ _("Fondo amm.attrezzature")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2609','"""+ _("Fondo amm.mobili e macchine da ufficio")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2610','"""+ _("Fondo amm.macch. uff.elettrom. ed elettr")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2611','"""+ _("Fondo amm.autovetture")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2612','"""+ _("Fondo amm.mezzi trasporto interno")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2613','"""+ _("Fondo amm.autocarri")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2701','"""+ _("Fondo T.F.R.")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2702','"""+ _("Fondo imposte e tasse")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2703','"""+ _("Fondo oscillazione cambio")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('2704','"""+ _("Fondo svalutazione crediti")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3201','"""+ _("Mutui passivi")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3501','"""+ _("Fornitori per fatture da ricevere")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3502','"""+ _("Enti previdenziali")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3503','"""+ _("Erario c/ritenute fiscali")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3504','"""+ _("Dipendenti c/retribuzioni")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3505','"""+ _("Ratei passivi")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3506','"""+ _("Risconti passivi")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3507','"""+ _("Cambiali passive")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('3508','"""+ _("Erario c/ritenute di acconto")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('5001','"""+ _("Acquisti di merce soggetta a rivendita")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5002','"""+ _("Acquisti di materie prime e semilavorati")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5101','"""+ _("Lavorazioni da terzi")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5301','"""+ _("Rimanenze iniziali materie prime")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5302','"""+ _("Rimanenze iniziali semilavorati")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5303','"""+ _("Rimanenze iniziali prodotti finiti")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5304','"""+ _("Rimanenze iniziali merci")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5305','"""+ _("Rimanenze iniziali materiali di consumo")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5501','"""+ _("Salari lordi")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5502','"""+ _("Stipendi lordi")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5503','"""+ _("Contributi")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('5504','"""+ _("I.N.A.I.L.")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6001','"""+ _("Spese telefoniche")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6002','"""+ _("Cancelleria")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6003','"""+ _("Valori bollati")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6101','"""+ _("Spese energia elettrica")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6102','"""+ _("Spese di viaggio")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6103','"""+ _("Carburanti e lubrificanti")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6104','"""+ _("Riscaldamento")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6105','"""+ _("Sconti e abbuoni passivi")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6106','"""+ _("Costi inerenti agli automezzi")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6107','"""+ _("Riparazioni e manutenzioni")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6108','"""+ _("Leasing e locazioni")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6109','"""+ _("Affitti passivi")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6110','"""+ _("Trasporti")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6111','"""+ _("Omaggi su vendite")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6501','"""+ _("Imposte e tasse")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('6502','"""+ _("Imposte e tasse non deducib.fiscalmente")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7001','"""+ _("Interessi passivi di c/c")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7002','"""+ _("Interessi passivi su mutui")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7003','"""+ _("Interessi passivi da fornitori")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7201','"""+ _("Amm.terreni")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7202','"""+ _("Amm.fabbricati civili")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7203','"""+ _("Amm.fabbricati destinati alla industria")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7204','"""+ _("Amm.costruzioni leggere")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7205','"""+ _("Amm.impianti generici")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7206','"""+ _("Amm.impianti specifici")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7207','"""+ _("Amm.macchinari")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7208','"""+ _("Amm.attrezzature")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7209','"""+ _("Amm.mobili e macchine da ufficio")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7210','"""+ _("Amm.macch. uff.elettrom. ed elettr.")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7211','"""+ _("Amm.autovetture")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7212','"""+ _("Amm.mezzi di trasporto interni")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7213','"""+ _("Amm.autocarri")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7214','"""+ _("Amm.costi pluriennali")+"""','C','2','R') """ )
    cr.execute(""" insert into piacon values('7301','"""+ _("Rimanenze finali materie prime")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7302','"""+ _("Rimanenze finali semilavorati")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7303','"""+ _("Rimanenze finali prodotti finitti")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7304','"""+ _("Rimanenze finali merci")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7305','"""+ _("Rimanenze finali materiali di consumo")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7501','"""+ _("Vendita prodotti finiti")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7502','"""+ _("Vendite da corrispettivi")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7503','"""+ _("Vendita merci")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7601','"""+ _("Recupero spese trasporto")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7602','"""+ _("Recupero spese imballlo")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7603','"""+ _("Recupero spese varie")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7604','"""+ _("Recupero spese bolli")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7605','"""+ _("Recupero spese bancarie")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7701','"""+ _("Proventi diversi")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7702','"""+ _("Provvigioni attive")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('7703','"""+ _("Sconti ed abbuoni attivi")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('9001','"""+ _("Interessi attivi di c/c")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('9002','"""+ _("Interessi attivi su crediti")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('9003','"""+ _("Utili su titoli")+"""','R','2','R') """ )
    cr.execute(""" insert into piacon values('9801','"""+ _("Bilancio di apertura")+"""','O','2','R') """ )
    cr.execute(""" insert into piacon values('9802','"""+ _("Bilancio di chiusura")+"""','O','2','R') """ )
    cr.execute(""" insert into piacon values('9803','"""+ _("Profitti e perdite")+"""','O','2','R') """ )
    cr.execute(""" insert into piacon values('9901','"""+ _("Capitale netto")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('9902','"""+ _("Capitale sociale")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('9903','"""+ _("Utili non distribuiti")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('9904','"""+ _("Fondo riserva legale")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('9905','"""+ _("Utile di esercizio")+"""','P','2','R') """ )
    cr.execute(""" insert into piacon values('9906','"""+ _("Perdita di esercizio")+"""','P','2','R') """ )

    #
    #cr.execute(""" drop table movcon """ )    
    cr.execute(""" create table movcon(
 	ANNO CHAR (4) not null,
 	NUM_MOV INTEGER not null,
 	DATAMOV VARCHAR (10),
 	NUM_RIG SMALLINT not null,
 	ANNOIVA CHAR (4),
 	VDIV CHAR (3),
	CAUSA VARCHAR (5),
 	DESCRIZ VARCHAR (40),
 	IMPORVAL NUMERIC (15,6),
 	IMPONVAL NUMERIC (15,6),
 	ANNODOC CHAR (4),
 	TIPODOC CHAR (2),
 	DATADOC VARCHAR (10),
 	NUMDOC VARCHAR (15),
 	NUMDOC1 VARCHAR (15),
 	CONTO VARCHAR (5),
 	IMPORTO NUMERIC (15,6),
 	SEGNO CHAR (1),
 	CPART VARCHAR (5),
 	CAMBIO NUMERIC (15,6),
 	TIPOIVA VARCHAR (5),
 	TIPOIVA1 VARCHAR (5),
 	ALIVA VARCHAR (5),
 	REGISTRO CHAR (1),
 	IMPONIB NUMERIC (15,6),
 	RIGAGIOR SMALLINT,
 	PAGGIOR SMALLINT,
	NOTE Blob(80,0), 
        STT_MOV CHAR(1),
 	PRIMARY KEY (ANNO,NUM_MOV,NUM_RIG)) """ )

    #
    ##cr.execute(""" alter table movcon add column DATA_INT INTEGER """ )
    ##cr.execute(""" alter table movcon add column T_CPART CHAR (1) """ )

    #

    #cr.execute(""" alter table tabgen add column VAL1 varchar(2) """ )      
    #cr.execute(""" alter table tabgen add column VAL2 varchar(4) """ )     
    #cr.execute(""" update tabgen set VAL1 = "LG", VAL2 = "" """ )
    #cr.execute(""" update tabgen set VAL1 = "RI",  VAL2 = "D2FT" where VALORE=110 """ )
    #cr.execute(""" update tabgen set VAL1 = "RI",  VAL2 = "A2NC" where VALORE=111 """ )
    #cr.execute(""" update tabgen set VAL1 = "RI",  VAL2 = "D1FT" where VALORE=120 """ )
    #cr.execute(""" update tabgen set VAL1 = "RI",  VAL2 = "A1NC" where VALORE=121 """ )
    #cr.execute(""" update tabgen set VAL1 = "RI",  VAL2 = "N3SC" where VALORE=131 """ )
    #cr.execute(""" update tabgen set VAL1 = "RI",  VAL2 = "N3VE" where VALORE=132 """ )

    #
    #cr.execute(""" alter table anag add column PAESE varchar(2) """ )    
    #cr.execute(""" alter table anag add column COD_C varchar(2) """ )
    #cr.execute(""" alter table anag add column CIN varchar(1) """ )
    #cr.execute(""" update anag set PAESE = "", COD_C = "", CIN = "" """ )

    #
    #cr.execute(""" alter table anag add column FAXD varchar(20) """ )    
    #cr.execute(""" alter table anag add column EMAILD varchar(35) """ )
    #cr.execute(""" update anag set FAXD = "", EMAILD = "" """ )
 
except StandardError, msg:
    evt = 'Error %s' % (msg)
    t = time.localtime(time.time())	    
    st = time.strftime(" %d/%m/%Y  %H:%M", t)
    ferr = open (cfg.path_logs + "err_creaaz.log","a")
    err = st + "  " + evt
    print err            
    ferr.write(err+'\n')
    ferr.close()
cn.commit()

