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
import os
__DataC__=''


#-------------------------------------------------------------
# connessione al database con sqlite 
if cfg.cntDB=='sqlite':

    import pysqlite2.dbapi2 as sqlite

    if (os.path.exists (cfg.path_db) == False): os.mkdir(cfg.path_db)
    
    path_dbaz = cfg.path_db + "dbaz.db"
    if not os.path.isfile(path_dbaz):
        sqlite.connect(path_dbaz , isolation_level='IMMEDIATE')
        import crea_dbaz
    CnDBAZ = sqlite.connect(path_dbaz , isolation_level='IMMEDIATE')

    def CnAz (naz):     
        path_az = cfg.path_db + "az00" + naz + ".db"
        if not os.path.isfile(path_az):
            sqlite.connect(path_az , isolation_level='IMMEDIATE')
            import crea_az
        return sqlite.connect(path_az , isolation_level='IMMEDIATE')


#----------------------------------------------------------------------------
## connessione al database con MySQL

elif cfg.cntDB=='mysql':
    import MySQLdb
 
    def CnAz (naz):    
        vaz = "az00"+naz
        #return MySQLdb.connect(host="", user="root", passwd="",db=vaz )
        return MySQLdb.connect(host="localhost", user="root", passwd="",db=vaz )
    ClAz = "cr.commit()"
    BtAz = ""
  
    vdbaz="dbaz"
    #CnDBAZ = MySQLdb.connect(host="", user="root", passwd="",db=vdbaz )
    CnDBAZ = MySQLdb.connect(host="localhost", user="root", passwd="",db=vdbaz )
    ClDBAZ = "cr.commit()"
    BtDBAZ = ""


#-------------------------------------------------------------
# dati azienda
sql = """ select rag_soc1,rag_soc2, indiriz, localit, cap, pr, web, e_mail, 
          codfisc, piva, nsrif, tel_uff, fax, rea, 
          (cap||" "||indiriz||" "||pr ) as cap_ind_pr, zona,
          (indiriz||" "||localit||" - "||cap||" "||pr ) as cap_ind_loc_pr,
          (indiriz1||" "||localit1||" - "||cap1||" "||pr1 ) as cap_ind_loc_pr1, 
          banca,
          (paese||"   "||cod_c||"   "||cin||"   "||abi||"   "||cab||"   "||num_cc ) as iban,
          indiriz1
          from aziende where cod = "%s" """


def dzAz(naz):
    row = None
    cr = CnDBAZ.cursor ()
    cr.execute(sql % int(naz)) 
    row = cr.fetchone()        
    return row 
