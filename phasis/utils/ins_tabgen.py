
import cfg
import sqlite3 as sqlite
import time

try:
    cn = sqlite.connect(cfg.path_db + 'az001.db' , isolation_level='IMMEDIATE')
    cr = cn.cursor()
    cr.execute(""" insert into tabgen values("TIPOORD","PC","Offerte Clienti","LG","") """ )
    cr.execute(""" insert into tabgen values('TIPOORD',"PF","Offerte Fornitori","LG","") """ )

except StandardError, msg:
    evt = 'Error %s' % (msg)
    t = time.localtime(time.time())	    
    st = time.strftime(" %d/%m/%Y  %H:%M", t)
    ferr = open (cfg.path_logs + "err_ins_tabgen.log","a")
    err = st + "  " + evt
    #print err            
    ferr.write(err+'\n')
    ferr.close()
cn.commit()

