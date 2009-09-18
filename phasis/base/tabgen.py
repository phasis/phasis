# Copyright (C) 2003 - 2007  See Open - http://www.seeopen.it/
# Author: Massimo Gerardi <m.gerardi@mgsoft.it>
#
# Released under the terms of the GNU General Public License
# (version 2 or above)
#
# See COPYING for details.
#
# www.phasis.it - info@phasis.it 

import wx
#from wxPython.wx import *
from cfg import *
import cfg

def create(parent,cnt):
    return tabgen(parent,cnt)
 
class tabgen(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        #wx.Dialog.__init__(self, id=wx.NewId(), name='',
        #      parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
        #      style=wx.DEFAULT_FRAME_STYLE, title=cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.cnt = cnt
        self.ttl=cnt[0]
        self.rec=cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
         
        #self.font=self.GetFont()
        self.vCodTblG= cnt[1]
        titolo_tab=""
        if self.vCodTblG =="ALIVA": titolo_tab="Codici Iva"
        elif self.vCodTblG =="PAGAM": titolo_tab="Condizioni di Pagamento"
        elif self.vCodTblG =="MERCE": titolo_tab="Categoria Merceologica"
        elif self.vCodTblG =="CATCOM": titolo_tab="Categoria Commerciale"
        elif self.vCodTblG =="PRCONT": titolo_tab="Primo Contatto"


        self.__MDI__= wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz=self.__MDI__.GetConnAZ()
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL) 
        self.pnl.SetFont(self.font)

        self.ltitolo=wx.StaticText(self.pnl, -1, _(titolo_tab), 
              wx.DLG_PNT(self.pnl, 5,5))
        self.ltitolo.SetFont(self.font)

        
        self.lvalore=wx.StaticText(self.pnl, -1, _("Valore :"), 
              wx.DLG_PNT(self.pnl, 5,27))
        self.lvalore.SetFont(self.font)
              
        self.valore = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 50,25), wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT))
        self.valore.SetFont(self.font)      
              
        self.cvalore=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, -1, "...", 
              wx.DLG_PNT(self.pnl, 115,25),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
              
        self.lcodgen=wx.StaticText(self.pnl, -1, _("Codic :"), 
              wx.DLG_PNT(self.pnl, 140,17))
        self.lcodgen.SetFont(self.font)
              
        self.codgen = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 185,15), wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT))
        self.codgen.SetFont(self.font)
              
        self.ldescriz= wx.StaticText(self.pnl, -1, _("Descrizione :"), 
              wx.DLG_PNT(self.pnl, 5,47))
        self.ldescriz.SetFont(self.font)
              
        self.descriz = wx.TextCtrl(self.pnl, -1, "",
              wx.DLG_PNT(self.pnl, 50,45), 
              wx.DLG_SZE(self.pnl, 180,cfg.DIMFONTDEFAULT))
        self.descriz.SetFont(self.font)
              
        self.cdescriz=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, -1, "...", 
              wx.DLG_PNT(self.pnl, 233,45),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
              
        self.new = wx.Button(self.pnl, -1, cfg.vcnew, 
              wx.DLG_PNT(self.pnl, 285,20), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.new.SetFont(self.font)
              
        self.ok = wx.Button(self.pnl, -1, cfg.vcok, 
              wx.DLG_PNT(self.pnl, 285,20), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))    
        self.ok.SetFont(self.font)
                                    
        self.inte = wx.Button(self.pnl, -1, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 285,35), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.inte.SetFont(self.font)
              
        self.canc = wx.Button(self.pnl, -1, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 285,35), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFont(self.font)
              
        self.modi = wx.Button(self.pnl, -1, cfg.vcmodi, 
              wx.DLG_PNT(self.pnl, 285,50), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.modi.SetFont(self.font)
                        
        self.dele = wx.Button(self.pnl, -1, cfg.vcdele, 
              wx.DLG_PNT(self.pnl, 285,50), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.dele.SetFont(self.font)
              
        self.stampa = wx.Button(self.pnl, -1, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 285,65), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa.SetFont(self.font)
              
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
        
        self.ok.Bind(wx.EVT_BUTTON, self.Save)
        self.new.Bind(wx.EVT_BUTTON, self.New)  
        self.inte.Bind(wx.EVT_BUTTON, self.Inttabgen) 
        self.modi.Bind(wx.EVT_BUTTON, self.Modi)      
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.dele.Bind(wx.EVT_BUTTON, self.CntrDele)
        self.descriz.Bind(wx.EVT_TEXT_ENTER, self.FndDescriz)
        self.cdescriz.Bind(wx.EVT_BUTTON, self.FndDescriz)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.Bind(wx.EVT_CLOSE, self.Close)    
        self.Start(self)

    def Stampa(self, evt):  # tutto da sistemare modulo non esiste. errori vari. impossibile capitarci
        valore=self.calore.GetValue()
        tbl=self.tbl
        import VPrtTblcf   
        control = [codgen,valore,tbl]
        win = VPrtTblcf.create(self,control)
        win.Centre(wx.BOTH)
        win.Show(True)
        
    def Start(self, evt):
        self.DelTxt(self)
        self.OnTxt(self)
        self.dele.Enable(False)
        self.dele.Show(False) # aggiunto per errore visualizzione mac
        self.stampa.Enable(False)
        self.modi.Enable(False)
        self.modi.Show(True)
        self.new.Show(True)
        self.ok.Show(False)
        self.inte.Show(False)
        self.codgen.Enable(False)
        self.descriz.SetFocus()
        self.cntr=""
        self.codgen.SetValue(self.vCodTblG)
	self.codgen.SetValue(self.vCodTblG)
        self.codgen.Show(False)
	self.lcodgen.Show(False)


            
    def Inttabgen(self, evt):
        self.rec=""
        self.Start(self)
        self.canc.Show(True)
        self.new.Show(True)
        self.ok.Show(False)
        self.dele.Show(False)
        self.dele.Enable(False)
        self.stampa.Enable(False)
        
    def FndSel(self, evt):
        row=evt
        self.valore.SetValue(row[1])
        self.descriz.SetValue(row[2].title())
        self.OffTxt(self)
        self.dele.Show(False)
        self.modi.Show(True)
        self.modi.Enable(True)
        self.modi.SetFocus()
        self.canc.Show(False)
        self.inte.Show(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(False)

            
    def NewTxt(self, evt):
        self.OnTxt(self)
        if (self.vCodTblG=="CATCOM" or self.vCodTblG=="PRCONT") : 
            self.Ins_Cont(self)
        self.descriz.SetFocus()
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.dele.Show(False)
        self.valore.SetFocus()
        
    def ModiTxt(self, evt):
        self.descriz.Enable(True)
        self.valore.Enable(False)
        self.modi.Enable(False)
	self.modi.Show(False)
        self.inte.SetFocus()
        self.ok.Enable(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.dele.Show(True)
        self.dele.Enable(True)
        
        
    def SaveTxt(self, evt):
        self.OffTxt(self)
        self.inte.SetFocus()
        self.ok.Show(False)
        self.new.Show(True)
        self.dele.Show(False)

    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()
        
    def OffTxt(self, evt):
        self.descriz.Enable(False)
        self.cdescriz.Enable(False)
        self.valore.Enable(False)
        self.cvalore.Enable(False)
        self.cntr=""

    def OnTxt(self ,evt):
        self.descriz.Enable(True)
        self.cdescriz.Enable(True)
        self.cvalore.Enable(False)
        if (self.vCodTblG=="CATCOM" or self.vCodTblG=="PRCONT"):
            self.valore.Enable(False)
        else: self.valore.Enable(True) 

        
    def DelTxt(self, evt):
        self.descriz.SetValue('')
        self.valore.SetValue('')

        
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
            
    def SetFcs(self, evt):
        evt.Skip()
        
            
    def Close(self, evt):
        if (self.descriz.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgesci, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
                self.AggMenu(True,self.IDMENU )
                wx.GetApp().GetPhasisMdi().CloseTabObj(self)
                #self.Destroy()   
            else:
                dlg.Destroy() 
        else:
            self.AggMenu(True,self.IDMENU )
            wx.GetApp().GetPhasisMdi().CloseTabObj(self)
            #self.Destroy() 
                 
    def Modi(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgmodi_tbl, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.ModiTxt(self)
            self.cntr="modi"
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()
 
    def New(self, evt):
        self.DelTxt(self)     
        self.cntr="new"
        self.NewTxt(self)
        sql = " SELECT COUNT(cod) FROM tabgen "
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            while (1):
                row=cr.fetchone()
                if row == None:
                    break
                if (row[0] == None) : cnt_rec=1
        except StandardError, msg:
            self.__MDI__.MsgErr("tabgen"," New Error %s " % (msg)) 
        self.CnAz.commit()


    def Ins_Cont(self, evt):
        cnt_rec=0
        sql = " SELECT * FROM tabgen WHERE cod='%s' ORDER BY valore ASC"
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % self.vCodTblG)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec += 1
            val1 = row[1]
            if self.vCodTblG=="CATCOM": val1 = val1.replace("CAT","")
            if self.vCodTblG=="PRCONT": val1 = val1.replace("CON","")
            val1 = int(val1)
            val1+=1
            if val1<10:
                if self.vCodTblG=="CATCOM": self.valore.SetValue("CAT0" + str(val1))
                if self.vCodTblG=="PRCONT": self.valore.SetValue("CON0" + str(val1))
            else:
                if self.vCodTblG=="CATCOM": self.valore.SetValue("CAT" + str(val1))
                if self.vCodTblG=="PRCONT": self.valore.SetValue("CON" + str(val1))
          
        except StandardError, msg:
            self.__MDI__.MsgErr("tabgen"," New Error %s " % (msg)) 
        self.CnAz.commit()

          
        
    def Save(self, evt):
        vcntr=self.cntr
        vcodgen=self.vCodTblG
        vvalore=self.valore.GetValue()
        vdescriz=self.descriz.GetValue().strip().title() 
        if (vvalore=="" ):
            self.Message(cfg.msgcmp_null,self.ttl)
        if (vdescriz==""):
            self.Message(cfg.msgcmp_null,self.ttl)
            self.descriz.SetFocus()
        else:
            self.SaveTxt(self)
            vvalore=self.valore.GetValue().upper()
            vdescriz=self.descriz.GetValue().strip().title()  
            vcodgen=self.vCodTblG
            valueSql_modi =vdescriz,vcodgen,vvalore
            valueSql = vcodgen,vvalore,vdescriz
            if(vcntr=="new"):
                try:
                    cr = self.CnAz.cursor()
                    sql = " INSERT INTO tabgen VALUES('%s','%s','%s','','') "
                    cr.execute(sql % valueSql)  
                except StandardError, msg:
                   self.__MDI__.MsgErr("tabgen"," Save New Error %s " % (msg)) 
                self.CnAz.commit()
            if(vcntr=="modi"):
                try:
                    cr = self.CnAz.cursor()
                    sql = """ UPDATE tabgen SET descriz = '%s' 
                            WHERE cod = '%s' AND valore = '%s' """
                    cr.execute(sql % valueSql_modi)  
                except StandardError, msg:
                  self.__MDI__.MsgErr("tabgen"," Save Modi Error %s " % (msg)) 
                self.CnAz.commit()

    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgnodele_valtbl, self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr=""
            dlg.Destroy()
            
    def Dele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdele_valtbl,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.cntr="dele"
            valore = self.valore.GetValue()
            codgen = self.codgen.GetValue()
            valueSql = valore,codgen 
            sql = " DELETE FROM tabgen WHERE valore = '%s' AND cod = '%s' "
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
            except StandardError, msg:
                self.__MDI__.MsgErr("tabgen"," Dele Error %s " % (msg)) 
            self.CnAz.commit()
            self.Inttabgen(self)
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()

    def FndDescriz(self, evt):
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec=0
            cod = self.codgen.GetValue()
            des = self.descriz.GetValue()
            sql = """ SELECT * FROM tabgen WHERE cod = '%s' 
                      AND descriz like '%s' ORDER BY descriz DESC """
            valueSql = cod,'%'+ des.title()+'%'
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql )
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                self.__MDI__.MsgErr("tabgen"," FndDescriz Error %s " % (msg)) 
            self.CnAz.commit()
            if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
            if (cnt_rec==1 and cnt_rec<2):self.FndSel(row)
            elif (cnt_rec>1):
                import srctabg
                control = ['Ricerca '+ self.ttl,self.valore,self.descriz,self.FndDescriz,cod]
                win = srctabg.create(self,control) 
                win.Centre(wx.BOTH)
                win.Show(True)
            else:
                self.descriz.SetFocus()

