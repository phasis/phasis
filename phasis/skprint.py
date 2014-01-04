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



from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes 
from reportlab.lib.colors import black,darkgray
import wx
import os
import sys
import string
import cfg
#from wxPython.wx import wxExecute,wxProcess
import types

##import MySQLdb
import pysqlite2.dbapi2 as sqlite

import fpformat
import shutil
import  locale
#locale.setlocale(locale.LC_MONETARY, '')

#<m.gerardi>
LC_M = locale.localeconv()
LC_M['grouping'] = [3,3,0]
LC_M['thousands_sep'] = '.'
LC_M['decimal_point'] = ','
locale.localeconv = lambda: LC_M
#<m.gerardi>


class __stampa__:
    """
    crea un documento pdf              
    """

    def __init__(self, modfinc, conn, outfile, evidenzia, 
                 datiazienda = None, parametri = None):
        self.Cn = conn
        if datiazienda:
            self.DatiAzienda = datiazienda        
        else:
            self.DatiAzienda = {}
        #print self.DatiAzienda 
        modfinc = modfinc.lower()
        self.mfinc = modfinc
        self.outfile = cfg.path_spool + outfile
        if os.path.isfile(cfg.path_finc + modfinc + "set.py"):
            self.TS = __import__( "finc." + modfinc +"set", globals, 
                        locals, modfinc)
        else: 
            self.TS = __import__( "finc." + modfinc, globals, locals, modfinc)
        #print parametri
        self.parametriSql = parametri
        self.cr = None 
        self.pag = 1
        self.record_testata = {}
        self.apriPdf()
        if self.TS.__dict__.has_key("blocchi"):
            self.disegnaBlocchi()
        else:
            if self.TS.__dict__.has_key("testata"):
                self.disegnaTestata()
            if self.TS.__dict__.has_key("corpo"):
                self.disegnaCorpo(evidenzia) 
            if self.TS.__dict__.has_key("dettaglioiva"):
                self.disegnaDettaglioiva()
            if self.TS.__dict__.has_key("calce"):
                self.disegnaCalce()       
            if self.TS.__dict__.has_key("calceB"):
                self.disegnaCalceB()       
         
    
    def npag(self):
        pag = 0
        if self.TS.__dict__.has_key("fontcorpo"):
            fontSize = self.TS.fontcorpo()
        else:
            fontSize=12 #bo!
        if self.TS.__dict__.has_key("querycorpo"):
            #print str("select count() from ("+self.TS.querycorpo()+")") 
            if cfg.cntDB=='mysql': 
                nrighe = str(self.eseguisql("select count(*) from\
                        ("+self.TS.querycorpo()+") as t1")["count(*)"])

            else: 
                nrighe = str(self.eseguisql("select count() from\
                        ("+self.TS.querycorpo()+")")["count()"])

            nrighe = int(string.replace(string.split(nrighe,",")[0],".",""))    
            pag = int(  nrighe  / ((self.TS.Ycorpo() - self.TS.fineSeq())/
                        (fontSize +1)))#righeXpag)
        if self.TS.__dict__.has_key("querytestata") and\
                        self.TS.__dict__.has_key("blocchi"):
            nrighe = self.eseguisql("select count() from\
                        ("+self.TS.querytestata()+")")["count()"]
            nrighe = int(string.replace(string.split(nrighe,",")[0],".",""))
            #print nrighe
            pag = int( nrighe / len(self.TS.blocchi()+1))
        if pag < 1 : pag = 1 
        else : pag+=1
        return pag
        
        
    def apriPdf(self):
        self.pagina = canvas.Canvas(self.outfile)
        self.pagina.setPageSize(self.TS.layout())
      
    
    def disegnaStruttura(self):
        if self.TS.__dict__.has_key("struttura"):
            self.TS.struttura(self.pagina)
    
    def disegnaTestata (self):
        num = ""
        datadoc = ""
        self.disegnaStruttura()
        if self.TS.__dict__.has_key("testata"):
            if  not self.record_testata:
                listaCampi=[]
                if self.TS.__dict__.has_key("querytestata"): 
                    rowTestata = self.eseguisql(self.TS.querytestata())
                    #print rowTestata
                    for k in rowTestata.keys():    
                        listaCampi.append((k,rowTestata[k]))
                        #print k,rowTestata[k]
                        if k=="num_doc" or k=="num_ord" :
                            num = rowTestata[k]
                        if k=="data_doc" or k=="data_ord" :
                            datadoc = str(rowTestata[k]).split('/')
                            datadoc= datadoc[0]+datadoc[1]+datadoc[2]                        
                for k in self.DatiAzienda.keys():            
                    listaCampi.append((k,self.DatiAzienda[k]))
                listaCampi.append(("##npag",""))
                self.record_testata=dict(listaCampi)
                self.totPag=self.npag()
            pag = "%s di %s" % (self.pag, self.totPag)
            #print pag
            self.record_testata["##npag"]=pag
            self.TS.testata(self.pagina,self.record_testata)
            title = self.mfinc.upper() + "-" +\
	          string.zfill(str(num),3) + "-" + str(datadoc)
            self.pagina.setTitle(title) 
            
    def disegnaBlocchi(self):
        #print self.TS.querytestata()
        row=self.eseguisql(self.TS.querytestata())
        coordinate = self.TS.blocchi()
        #print coordinate
        coordinate.insert(0,(0,0))
        while row:
            for coord in coordinate:
                self.pagina.translate(coord[0],coord[1])
                #print coord[0],coord[1]
                if self.TS.__dict__.has_key("struttura"):
                    self.TS.struttura(self.pagina)
                if self.TS.__dict__.has_key("testata"):                    
                    self.TS.testata(self.pagina,row)  
                    #print row              
                row=self.eseguisql(None)
                if not row : 
                    break #sono finiti i record esco dal ciclo  
            self.salta()#salto pagina
            self.pag = self.pag +1      

    def disegnaCorpo(self,evidenzia=False):
        #CORPO DOCUMENTO
        if self.TS.__dict__.has_key("fontcorpo"):
            fontSize = self.TS.fontcorpo()
        else:
            fontSize=12 #bo!
        colore = black
        inizioseq = self.TS.Ycorpo()
        #print self.TS.querycorpo()
        row=self.eseguisql(self.TS.querycorpo())
        right = False
        while row :
            coordinataY = inizioseq
            while 1:
                self.TS.corpo(self.pagina,row,coordinataY)
                #print row
                #qui flip riga
                if evidenzia:
                    if colore == black: colore = black #darkgray
                    else: colore = black
                    self.pagina.setFillColor(colore)
                coordinataY = coordinataY - (fontSize+1)
                row=self.eseguisql(None)
                if coordinataY < self.TS.fineSeq(): #salto paginacoordinataY
                    
                    # controlla che non siano finite le righe 
                    # e che quindi non salti
                    if  row :
                        self.pagina.setFillColor(black)
                        if self.TS.__dict__.has_key("al_salto"):######rivedi
                            self.TS.al_salto()
                        self.salta()#salto pagina
                        self.pag = self.pag +1
                        if self.TS.__dict__.has_key("testata"):######rivedi
                            self.disegnaTestata()#rimette a posto la pagina
                        coordinataY = inizioseq
    
                if not row : 
                    self.pagina.setFillColor(black)
                    break #sono finiti i record esco dal ciclo

    def salta(self):  
        self.pagina.showPage()

    def disegnaDettaglioiva(self,segue=None):
        #Dettaglio iva non ha il salto pagina
        if self.TS.__dict__.has_key("fontdettaglioiva"):
            fontSize = self.TS.fontdettaglioiva()
        else:
            fontSize=12 #bo!
        coordinataY = self.TS.Ydettaglioiva()
        row=self.eseguisql(self.TS.querydettaglioiva())
        while row :
            self.TS.dettaglioiva(self.pagina,row,coordinataY)           
            coordinataY = coordinataY - (fontSize +1) 
            row=self.eseguisql(None)   
    
    def disegnaCalce (self):
        row = self.eseguisql(self.TS.querycalce())
        self.TS.calce(self.pagina,row)

    def disegnaCalceB (self):
        row = self.eseguisql(self.TS.querycalceB())
        self.TS.calceB(self.pagina,row)

    def fine(self):
        self.pagina.save()
        return self.outfile

    def CnvVMPZ(self, evt):
        val=float(evt)
        self.val= locale.format("%."+str(cfg.cdecPZ)+"f",val,1)
        if (self.val=='0,00' or self.val=='0,000'  or self.val=='0,0000'  
                        or self.val=='0,00000') : self.val=''

    def CnvVMQT(self, evt):
        val=float(evt)
        self.val= locale.format("%."+str(cfg.cdecQT)+"f",val,1)
        if (self.val=='0,00' or self.val=='0,000'  or self.val=='0,0000'  
                        or self.val=='0,00000') : self.val=''

    def CnvVM(self, evt):
        if evt!='':
            val = float(evt)
            self.val= locale.format("%."+str(cfg.cdec)+"f",val,1)
            if (self.val=='0,00' or self.val=='0,000'  or self.val=='0,0000'  
                        or self.val=='0,00000') : self.val=''

    def CnvVM0(self, evt):
        val=float(evt)
        self.val= locale.format("%."+str(cfg.cdec)+"f",val,1)
        if (self.val=='0,00' or self.val=='0,000'  or self.val=='0,0000'  
                        or self.val=='0,00000') : self.val='0,00'

    def eseguisql(self,sql):
        #crea il cursore se il parametro sql e' vuoto
        #altrimenti legge da quello aperto
        #locale.localeconv=_temp

        #print sql, self.parametriSql
        try:
            if sql!=None:
                if cfg.cntDB=='mysql':  
                    self.cr = self.Cn.cursor (MySQLdb.cursors.DictCursor)
                else: self.cr = self.Cn.cursor ()
                if self.parametriSql!= None:
                    sql = sql % (self.parametriSql)
                    #print sql
                   # self.cr.execute(sql)#,self.parametriSql)
                #else:
                self.cr.execute(sql)
            values = self.cr.fetchone()
            row = False 
            if values:
                fieldname = [ n[0] for n in self.cr.description]
                row = dict(map(dz,fieldname,values))
            #print "ROW : %s " % row
            if row:   
                listaCampi=[]
                for k in row.keys():
                        listaCampi.append((k, row[k]))
                row = dict(listaCampi)
                #print "ROW : %s " % row
                for k in row.keys():
                    #print type(row[k]),row[k],k
                    if k=='um' and row[k]=='--':
                       row[k] = ''                    
                    if k=='qt_1'  or k=='qt_ord':
                        self.CnvVMQT(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='prez_un'  or k=='prezzo_1'  or k=='prezzo_2' :
                        self.CnvVMPZ(str(row[k]))
                        row[k] = str(self.val)
                    elif type(row[k])==float or k=='d_imp' :
                        self.CnvVM(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='tot_riga' and row[k]=='0,00' :
                        row[k] = ''
                    elif k=='tot_riga' or k=='totcolli' or k=='valore':
                        self.CnvVM(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='tot_merce' or k=='tot_doc' or k=='tot_ord'  or k=='tot_iva' or k=='totale':
                        self.CnvVM(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='imp_dare' or k=='imp_avere'  or k=='imp_saldo':
                        self.CnvVM0(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='peso' or k=='qt' or k=='qts' or k=='qtc' or k=='qtart' :
                        self.CnvVMQT(str(row[k]))
                        row[k] = str(self.val)

                    if k=='QT_1'  or k=='QT_ORD':
                        self.CnvVMQT(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='PREZ_UN'  or k=='PREZZO_1'  or k=='PREZZO_2' :
                        self.CnvVMPZ(str(row[k]))
                        row[k] = str(self.val)
                    elif type(row[k])==float or k=='D_IMP' :
                        self.CnvVM(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='TOT_RIGA' and row[k]=='0,00' :
                        row[k] = ''
                    elif k=='TOT_RIGA' or k=='TOTCOLLI' or k=='VALORE':
                        self.CnvVM(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='TOT_MERCE' or k=='TOT_DOC' or k=='TOT_ORD'  or k=='TOT_IVA' or k=='TOTALE':
                        self.CnvVM(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='imp_dare' or k=='imp_avere'  or k=='imp_saldo':
                        self.CnvVM0(str(row[k]))
                        row[k] = str(self.val)
                    elif k=='PESO' or k=='QT' or k=='QTS' or k=='QTC' or k=='QTART' :
                        self.CnvVMQT(str(row[k]))
                        row[k] = str(self.val)
                    if k=='sc1' :
                        row[k] = str(row[k]).replace(",00","")
        except StandardError, msg:
            print " Error %s " % (msg)                    
        return row 

def dz(a,b):return(a,b) 


def stampaDoc(conn, tipo, datiazienda=None, anteprima=False, 
                        evidenziaCorpo=True,parametriSql=None): # originale
        """
        """

        filename ="doc.pdf"
        f=open(cfg.path_tmp+"pid","r")
        x=f.readline()
        pid = int(x)
        f.close()
        if wx.Process.Exists(pid) and pid != 0 : wx.Process.Kill(pid)
        S = __stampa__(tipo, conn, parametri=parametriSql, outfile=filename, 
                        evidenzia=evidenziaCorpo,datiazienda=datiazienda)
        stampa(S.fine(),anteprima) # originale

def stampa (nomeDoc,anteprima): # origilale
        if sys.platform == 'win32':
            nomeDoc = string.replace(nomeDoc,"/","\\")
            import _winreg
            acrobat =_winreg.QueryValue(_winreg.HKEY_CLASSES_ROOT, 
                        'AcroExch.Document\shell\open\command')[1:-6]
            if anteprima :
                cmd = '"%s" %s'
            else:
                cmd= '"%s" /p /h  %s'
            pid=wx.Execute(cmd % (acrobat,nomeDoc))
        elif wx.Platform == '__WXMAC__':
            if anteprima:
                #os.popen("open " + nomeDoc)
                #pid=wx.Execute("open " + nomeDoc) #da un errore ma funziona
                #wx.Shell("open "+nomeDoc) #ok funziona
                pid=os.system("open " + nomeDoc)
                #os.startfile(nomeDoc) #sembra fuznionare solo su window
            else:
                #wx.Execute("lp " + nomeDoc)
                os.system("lp " + nomeDoc)
                pid=0
        else:
            if anteprima :
                    pid = wx.Execute("evince " + nomeDoc)
            else:
                wx.Execute("lp-cups " + nomeDoc)
                pid=0
        f=open(cfg.path_tmp+"pid","w")
        f.write(str(pid))
        f.close()
