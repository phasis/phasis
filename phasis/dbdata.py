#ver 0.0.2
import string
class dbdata:
    def __init__(self):
        self.data=[]
        self.table=[]
    def appendMany(self,rows):
        for r in rows:
            if r[0]:self.append(r)
    def append(self,*args):#table,field,value):
        """append(self,table,field,value)"""
        if len(args)<2:
            for table,field,value in args[0]:
                self._add(table,field,value)
        else:
            self._add(args[0],args[1],args[2])
    def _add(self,table,field,value):
        self.data.append((table,(field,value)))
        if table not in self.table:
            self.table.append(table)
    def dict(self):
        """dict(self) -> {"table1":{"field1":"val","field2":"val"},"table2"...}
           i valori che restituisce rispettano i tipi del database
        """
        #print self.data
        ret1=[]
        for table in self.table:
            ret=[]
            for item  in self.data:
                if item[0] == table:
                    ret.append(item[1])
            ret1.append((table,dict(ret)))        
        return dict(ret1)
        
    def insert(self):
        """restituisce le sql insert per le varie tabelle senza clausola where"""
        table_data = self.dict()
        seq_sql=[]
        sql="INSERT INTO %s  (%s) VALUES (%s)"
        #print "data.insert = %s"%table_data
        for t in table_data.keys():
            field=[]
            value=[]
            
            for f_v in table_data[t]:
                ######print "table_data ,field-value %s"%f_v
                field.append(f_v)
                value.append(table_data[t][f_v])
            #####print 
            seq_sql.append(sql%(t,string.join(field,","),string.join(value,",")))    
            
        return seq_sql
        
    def update(self,where=""):
        """restituisce le sql update per le varie tabelle senza clausola where"""
        table_data = self.dict()
        seq_sql=[]
        sql="UPDATE %s SET %s " 
        for t in table_data.keys():
            value=[]
            for f_v in table_data[t]:
                value.append(" %s = %s " %(f_v,table_data[t][f_v]))
            seq_sql.append(sql%(t,string.join(value,","))+where)    
            
        return seq_sql
        
    def delete(self):
        """restituisce le sql delete per le varie tabelle senza clausola where"""
        return 0