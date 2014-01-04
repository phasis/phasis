
import cfg
import sqlite3 as sqlite
import time

try:
    cn = sqlite.connect(cfg.path_db + 'az001.db' , isolation_level='IMMEDIATE')
    cr = cn.cursor()
    cr.execute(""" insert into libriaz values
                   ('RORD',2009,'PC',0,'','','','','','','','','','','','','','','') """ )
    cr.execute(""" insert into libriaz values
                   ('RORD',2009,'PF',0,'','','','','','','','','','','','','','','') """ )

except StandardError, msg:
    evt = 'Error %s' % (msg)
    t = time.localtime(time.time())	    
    st = time.strftime(" %d/%m/%Y  %H:%M", t)
    ferr = open (cfg.path_logs + "err_ins_libriaz.log","a")
    err = st + "  " + evt
    #print err            
    ferr.write(err+'\n')
    ferr.close()
cn.commit()

