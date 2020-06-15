# -*- coding: iso-8859-1 -*-
#
#  Copyright (C) 2001 - 2020 Massimo Gerardi all rights reserved.
#
#  Author: Massimo Gerardi massimo.gerardi@gmail.com
#
#  Copyright (c) 2020 Qsistemi.com.  All rights reserved.
#
#  Viale Giorgio Ribotta, 11 (Roma)
#  00144 Roma (RM) - Italy
#  Phone: (+39) 06.87.163
#  
#
#  Si veda file COPYING per le condizioni di software.
#
#   www.qsistemi.com - italy@qsistemi.com


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

