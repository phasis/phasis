# -*- coding: utf-8 -*-
# Copyright (C) 2003 - 2006  Phasis - http://www.phasis.it/
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


from pysqlite2 import dbapi2 as sqlite
import wx
import string
import os
from dbdata import dbdata
import types

def conn (db=None):  # connessione al database
    if db:
        database = db
    else:
        database = wx.GetApp().GetPhasisMdi().GetConnAz()
    return sqlite.connect(database) # da sistemare


def dz(a,b):return(a,b) 

#(connex,sql,tutti= True):    
def eseguiSql(sql, tutti=True, connection=None, where=""):
    dml = False
    row = None
    if connection:
        cn = connection
    else:
        cn = conn()
    cr = cn.cursor ()   
    if type(sql) not in (types.ListType,types.TupleType): sql = [sql]
    for S in sql:
        print "esegui sql: "+S
        try:
            action =  string.split(S)[0].upper()
            if action == "SELECT":
                cr.execute(S)
                if tutti:
                    row = cr.fetchall()
                else:
                    values = cr.fetchone()
                    if values:
                        fieldname=[ n[0] for n in cr.description]
                        row=dict(map(dz,fieldname,values))
                            
            elif  action in ("INSERT","UPDATE","DELETE"):
                dml=True
                row=True
                cr.execute(S)        
        except cn.Error, msg:
            if dml:cn.rollback()
            dml=False
            row=False
            #print " Errore %s" % (msg) 
            alert(wx.GetApp().GetPhasisMdi(),str(msg),_(" Operazione Non Riuscita!"))
    if dml:cn.commit()
    return row 

#classe custom event
class MyEvent(wx.PyCommandEvent):
    def __init__(self, evtType, id):
        wx.PyCommandEvent.__init__(self, evtType, id)
        self.myVal = None


    def SetValue(self, val):
        self.myVal = val


    def GetValue(self):
        return self.myVal   
                 

# utility per la gestione dei panel
def Clear(panel,state):
    for control in panel.controls:
            panel.__dict__[control].Clear(state)  
          
def Enable(panel,enable,state):
    #enable disable all controls
    for control in panel.controls:
            panel.__dict__[control].Enable(enable,state)
            
def LoadRecord(panel,record):
    print record
    if record:
        for field in record.keys():
            if panel.__dict__.has_key(field):
                panel.__dict__[field].SetValue(record[field])
        return 1
    else:
        return 0  
      
def GetData(panel,state=0,controls=None,data=None):
    if not data:data=dbdata()
    if not controls:controls=panel.controls
    for control in controls:
        if panel.__dict__[control].GetValue(state)==False: #  errore
            data= None 
            break 
            # return None
        data.append(panel.__dict__[control].table,
                    control,
                    panel.__dict__[control].GetValue(state)
                    )
    return data

def GetDataOnPanel(panel,state,controls=None):
    """prende i valori nei controlli e li inserisce in una tupla(tabella,campo,valore)"""
    data = []
    if not controls:controls=panel.controls
    for control in controls:
        if panel.__dict__[control].GetValue(state)=="errore":
            data = None 
            break 
            #return None
        data.append((panel.__dict__[control].table,
                    control,
                    panel.__dict__[control].GetValue(state))
                    )
    return data

def FindControl(panel):
    controls = []                                                       
    for k in panel.__dict__.keys():                                         
        if k not in ("this","controls","embedded"):                                   
            if panel.__dict__[k].GetClassName() in ("DTextCtrl","DCombo","DPanel","DGenCtrl"):
                controls.append(k)                                    
    return controls

def compileWhere(panel):
    where="WHERE "
    for field in panel.whereFields:
        where=where+" %s = %s AND"%(field,panel.__dict__[field].GetValue(panel.buttons.GetState()))
    return where[:-3]

def compileWhereIteration(panel):
    where = "WHERE "
    for field in panel.where_iterationFields:
        where = where+" %s = %s AND"%(field,panel.__dict__[field].GetValue(panel.buttons.GetState()))
    return where[:-3]

def saveKey(panel,fields):
    ret = []
    for field in fields:
        ret.append((field,panel.__dict__[field].GetNormalValue()))
    return dict(ret)

def restoreKey(panel,keybackup):
    for k in keybackup.keys():
        panel.__dict__[k].SetValue(keybackup[k])
    return 1

def createSqlLoad(panel):
    sql=panel.sql_load+compileWhere(panel)
    return sql

def ask(parent, msg, title="?",position=None):
    dlg = wx.MessageDialog(parent, msg, title,
                          wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, pos=position)
    ret = False
    if dlg.ShowModal() == wx.ID_YES:
        ret = True
    dlg.Destroy()
    return ret

def alert(parent,msg,title="!"):    
    dlg = wx.MessageDialog(parent, msg,title,wx.ICON_HAND)
    dlg.ShowModal()
    dlg.Destroy()
     
def iterId(panel):
    sql = panel.sql_iteration_code
    if panel.where_iterationFields:sql = sql+compileWhereIteration(panel)
    iterCod = eseguiSql(sql,0).values()[0]
    if not iterCod : iterCod = 0
    panel.__dict__[panel.iterationField].SetValue(str(int(iterCod+1)))
    
def createSqlInsert(records):
    '''cosi funziona soltanto per una tabella per griglia '''
    sql = "INSERT INTO %s  (%s) VALUES (%s)"
    seq_sql = []
    for record in records:
        field = []
        value = []
        for table,field_value in record:
            field.append(field_value[0])
            value.append(field_value[1])
        seq_sql.append(sql%(table,string.join(field,","),string.join(value,",")))        
    return seq_sql

def StoreLastValue(name,value,utente=None):
    #controlla se ci sono dei controlli
    #che devono 'ricordare' l'ultimo dato
    if utente == None:
        utente=wx.GetApp().GetPhasisMdi().GetUtente()[0]
    sql=("DELETE FROM cntrl_val  WHERE cntrl_name= '%s'AND user = %s"% 
        (name,utente),
         '''INSERT INTO cntrl_val  (val,cntrl_name,user)
            VALUES ('%s','%s',%s)'''%(value,name,utente)
        )
    #sql = """ UPDATE cntrl_val SET val = '%s'
    #      WHERE cntrl_name = '%s' AND user = %s """ % (value,name,utente)
        
    eseguiSql(sql,                
        connection=wx.GetApp().GetPhasisMdi().GetConnDbAz())

def LoadLastValue(name,utente=None):
    if utente == None:
        utente = wx.GetApp().GetPhasisMdi().GetUtente()[0]
    value = eseguiSql( """ SELECT val FROM cntrl_val 
          WHERE cntrl_name='%s' AND user = %s """ % (name, utente),                
          connection=wx.GetApp().GetPhasisMdi().GetConnDbAz())
    if value:
        return value[0][0]
    else:
        return '0'
