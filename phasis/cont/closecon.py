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




import  wx
import cfg
import fdb
from time import strftime
vanno= strftime("%Y")
vdata = strftime("%d/%m/%Y")

def create(parent,cnt):
    return CloseCont(parent,cnt)

class CloseCont(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######

        #wx.Dialog.__init__(self, id=wx.NewId(), name='',
        #      parent=prnt, pos=wx.Point(0, 0), size=wx.DefaultSize,  
        #      style=wx.DEFAULT_FRAME_STYLE, title=cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.SetClientSize(wx.Size(400, 200))
        #self.Center(wx.BOTH)
        self.rec=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        self.ttl = cnt[0]
        Nid = wx.NewId()
        self.__MDI__ = wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz = self.__MDI__.GetConnAZ() 
        self.annoc = self.__MDI__.GetAnnoC() 
        self.datacon = self.__MDI__.GetDataC()
        self.dzDatiAzienda = self.__MDI__.dzDatiAzienda
        
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0), size = wx.DLG_SZE(self,680/2,370/2), #size=wx.Size(680, 370),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        #self.font=self.GetFont()
        self.pnl.SetFont(self.font)
        
        self.label1 = wx.StaticText(self.pnl,-1,'', 
              wx.DLG_PNT(self.pnl,20,15))
        self.label2 = wx.StaticText(self.pnl,-1,'', 
              wx.DLG_PNT(self.pnl,20,25))
        self.label3 = wx.StaticText(self.pnl,-1,'', 
              wx.DLG_PNT(self.pnl,20,35))
        self.label4 = wx.StaticText(self.pnl,-1,'', 
              wx.DLG_PNT(self.pnl,20,45))
        self.label5 = wx.StaticText(self.pnl,-1,'', 
              wx.DLG_PNT(self.pnl,20,55))
        wx.StaticLine(self.pnl , -1, wx.DLG_PNT(self.pnl , 5,80), 
              wx.DLG_SZE(self.pnl , 150,-1))

        self.conf = wx.Button(self.pnl, -1, cfg.vcconf, 
              wx.DLG_PNT(self, 15,90), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self.pnl, -1, cfg.vccanc, 
              wx.DLG_PNT(self, 85,90),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))    
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        #self.SetFont(self.font)
        
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)
        
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.conf.Bind(wx.EVT_BUTTON, self.Conferma)
        self.Start(self)

    def Start(self, evt):
        self.label1.SetLabel("")
        self.label2.SetLabel("")
        self.label3.SetLabel("")
        self.label4.SetLabel("")
        self.label5.SetLabel("")
        self.conf.Enable(False)
        self.canc.Enable(True)
        self.canc.SetFocus()
        self.SelAnnoC(self)

    def Close(self, evt):
        self.AggMenu(True,self.IDMENU )
        wx.GetApp().GetPhasisMdi().CloseTabObj(self)
        #self.Destroy() 
                             
    def SelAnnoC (self, evt):
        annoc = self.annoc
        sql = " SELECT cod, valore, var2, var3 from parcon "   
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql)  
            while (1):
                row = cr.fetchone ()
                if row == None: 
                    break
                if (row[0]=="ANNOA"):sANNOA = row[1]
        except StandardError, msg:
            self.__MDI__.MsgErr("closecon","SelAnnoC parcon Error %s " % (msg)) 
        fdb.CnDBAZ.commit()
        sql = " SELECT chiave, anno from libriaz "   
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            while (1):
                row = cr.fetchone ()
                if row == None: 
                    break
                if (row[0]=="RVEN"):sANNO = row[1]
        except StandardError, msg:
            self.__MDI__.MsgErr("closecon"," SelAnnoC libriaz Error %s " % (msg)) 
        self.CnAz.commit()
        if sANNOA==vanno or sANNO==vanno:
            self.conf.Enable(False)
            self.canc.SetFocus()
            self.label1.SetLabel(_("ATTENZIONE !!!!!!!!! La procedura di chiusura "))
            self.label2.SetLabel(_("dell'anno contabile --> ") + self.annoc + " <--")
            self.label3.SetLabel(_("risulta gia` essere effettuata"))
            self.label4.SetLabel("")
            self.label5.SetLabel("")
        else:
            self.label1.SetLabel(_("ATTENZIONE !!!!!!!!!"))
            self.label2.SetLabel(_("E` stata selezionata la procedura di chiusura"))
            self.label3.SetLabel(_("dell'anno contabile --> ") + self.annoc + " <--")
            self.label4.SetLabel(_("Siete sicuri di confermare l'operazione ?"))
            self.label5.SetLabel("")
            self.conf.Enable(True)
            self.canc.Enable(True)
            self.canc.SetFocus()

    def Conferma(self, evt):
        dlg = wx.MessageDialog(self, _("Confermi l'operazione ?"), self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.closecon(self)
            dlg.Destroy()


    def closecon(self, evt):
        cnt = 0
        val_parcon = vanno, vdata
        val_libriaz = vanno, int('0'), '' 
        sql_post = " UPDATE parcon SET var2='%s', var3='%s' where cod = 'POSL1' "
        sql_annoa = " UPDATE parcon SET valore='%s' where cod = 'ANNOA' "
        sql_anno = " UPDATE libriaz SET anno='%s', ultnum = %s, udatreg ='%s' "
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql_post % val_parcon)
            cnt+=1    
        except StandardError, msg:
            self.__MDI__.MsgErr("closecon"," sql_post Error %s " % (msg)) 
        fdb.CnDBAZ.commit()
        
        try:
            cr = fdb.CnDBAZ.cursor ()
            cr.execute(sql_annoa % vanno) 
            cnt+=1  
        except StandardError, msg:
            self.__MDI__.MsgErr("closecon"," sql_annoa Error %s " % (msg)) 
        fdb.CnDBAZ.commit()
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql_anno % val_libriaz) 
            cnt+=1  
        except StandardError, msg:
            self.__MDI__.MsgErr("closecon"," sql_anno Error %s " % (msg)) 
        self.CnAz.commit()
        if cnt==3 :
            self.label1.SetLabel(_("Operazione eseguita con successo"))
            self.label2.SetLabel('')
            self.label3.SetLabel('')
            self.label4.SetLabel('')
            self.label5.SetLabel('')
        else:
            self.label1.SetLabel(_("ATTENZIONE !!!!!!!!! La procedura di chiusura "))
            self.label2.SetLabel(_("dell'anno contabile --> ") + vanno + " <--")
            self.label3.SetLabel(_("ha riportato un errore"))
            self.label4.SetLabel("")
            self.label5.SetLabel("")
        self.conf.Enable(False)
        self.canc.SetFocus()



