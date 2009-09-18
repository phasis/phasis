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
import string 
from cfg import *
import cfg

def create(parent,cnt):
    return Tblcf(parent,cnt)
 
class Tblcf(wx.Dialog):
    def __init__(self, prnt, cnt):
        wx.Dialog.__init__(self, id=wx.NewId(), name='',
              parent=prnt, pos=wx.Point(10, 50), size=wx.DefaultSize,
              style=wx.DEFAULT_FRAME_STYLE, title=cnt[0])
        self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        
        self.cnt = cnt
        self.ttl = cnt[0]
        self.ttldest = _(" Anagrafica spedizioni ") 
        tcpart = cnt[1].upper()
        self.cod = str(cnt[4])
        self.rec = cnt[2]
        self.tcpart = tcpart
        self.tbl = "tblcf"
        Nid = wx.NewId()
        #self.font=self.GetFont()
        self.CnAz = prnt.CnAz
        #self.font = self.GetFont()
        self.__FRM__ = prnt.__MDI__
        
        self.__MDI__= wx.GetApp().GetPhasisMdi()
       
        self.font=self.__MDI__.font
        self.SetFont(self.font)

        
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0)) #, size=wx.Size(680, 270))
        self.pnl.SetFont(self.font)
        
        self.t_cpart = wx.TextCtrl(self.pnl,-1, "", wx.DLG_PNT(self.pnl, 275,37))
        
        self.lcod = wx.StaticText(self.pnl, -1, _("Codice :"), 
              wx.DLG_PNT(self.pnl, 5,7))
        self.lcod.SetFont(self.font)
        
        self.codcf1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,5), wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT))
        self.codcf1.SetFont(self.font)
        
        self.ccodcf1 = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 110,5),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        self.lcodcf=wx.StaticText(self.pnl, -1, _("Cod. Cliente :"), 
              wx.DLG_PNT(self.pnl, 140,7))
        self.lcodcf.SetFont(self.font)
        
        self.codcf = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 185,5), wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT))
        self.codcf.SetFont(self.font)
        
        #self.ccodcf=wx.Button(self.pnl, Nid, "...", 
        #      wx.DLG_PNT(self.pnl, 240,5),
        #      wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lragsoc1= wx.StaticText(self.pnl, -1, _("Rag. Sociale ( Cognome ) :"), 
              wx.DLG_PNT(self.pnl, 5,20))
        self.lragsoc1.SetFont(self.font)
        
        self.ragsoc1 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 5,30), 
              wx.DLG_SZE(self.pnl, 120,cfg.DIMFONTDEFAULT))    
        self.ragsoc1.SetFont(self.font)
        
        self.cragsoc1=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
              wx.DLG_PNT(self.pnl, 130,30),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        wx.StaticText(self.pnl, -1, _("( Nome ) :"), 
              wx.DLG_PNT(self.pnl, 150,20)).SetFont(self.font)
        
        self.ragsoc2 = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 150, 30), wx.DLG_SZE(self.pnl, 105,cfg.DIMFONTDEFAULT))          
        self.ragsoc2.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Indirizzo :"), wx.DLG_PNT(self.pnl, 5,47)).SetFont(self.font)
        
        self.indiriz = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,45), wx.DLG_SZE(self.pnl, 210,cfg.DIMFONTDEFAULT))                    
        self.indiriz.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Citta' :"), wx.DLG_PNT(self.pnl, 5,62)).SetFont(self.font)
        
        self.zona = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,60), wx.DLG_SZE(self.pnl, 100,cfg.DIMFONTDEFAULT))          
        self.zona.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("CAP :"), wx.DLG_PNT(self.pnl, 150,62)).SetFont(self.font)
        
        self.cap = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 175, 60), wx.DLG_SZE(self.pnl, 35,cfg.DIMFONTDEFAULT))                     
        self.cap.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("PR :"), wx.DLG_PNT(self.pnl, 215,62)).SetFont(self.font)
        
        self.pr = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 235, 60), wx.DLG_SZE(self.pnl, 20,cfg.DIMFONTDEFAULT))
        self.pr.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Localita' :"), wx.DLG_PNT(self.pnl, 5,77)).SetFont(self.font)
        
        self.localit = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,75), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))          
        self.localit.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Stato :"), wx.DLG_PNT(self.pnl, 140,77)).SetFont(self.font)
        
        self.stato = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 170, 75), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))
        self.stato.SetFont(self.font)
        
        self.ltabi = wx.StaticText(self.pnl, -1, _("Telefono :"), 
              wx.DLG_PNT(self.pnl, 5,92))
        self.ltabi.SetFont(self.font)
        
        self.tabi = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,90), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))
        self.tabi.SetFont(self.font)
        
        self.ltuff = wx.StaticText(self.pnl, -1, _("Telefono :"), 
              wx.DLG_PNT(self.pnl, 5,107))
        self.ltuff.SetFont(self.font)
        
        self.tuff = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 45,105), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))          
        self.tuff.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Fax :"), wx.DLG_PNT(self.pnl, 140,107)).SetFont(self.font)
        
        self.fax = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 170, 105), wx.DLG_SZE(self.pnl, 85,cfg.DIMFONTDEFAULT))
        self.fax.SetFont(self.font)
        
        self.new = wx.Button(self.pnl, Nid, cfg.vcnew, 
              wx.DLG_PNT(self.pnl, 285,20), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.new.SetFont(self.font)
        
        self.ok = wx.Button(self.pnl, Nid, cfg.vcok, 
              wx.DLG_PNT(self.pnl, 285,20), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))               
        self.ok.SetFont(self.font)
        
        self.int = wx.Button(self.pnl, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 285,35), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV)) 
        self.int.SetFont(self.font)
        
        self.canc = wx.Button(self.pnl, Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 285,35), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFont(self.font)
        
        self.modi = wx.Button(self.pnl, Nid, cfg.vcmodi, 
              wx.DLG_PNT(self.pnl, 285,50), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))      
        self.modi.SetFont(self.font)
        
        self.dele = wx.Button(self.pnl, Nid, cfg.vcdele, 
              wx.DLG_PNT(self.pnl, 285,50), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.dele.SetFont(self.font)
        
        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 285,65), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa.SetFont(self.font)
        
        self.selez = wx.Button(self.pnl, Nid, cfg.vcselez, 
              wx.DLG_PNT(self.pnl, 285,65), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.selez.SetFont(self.font)
        
        
        #self.SetFont(self.font)
        box_sizer = wx.BoxSizer(wx.VERTICAL)
       	box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        self.SetAutoLayout(1)
        self.SetSizer(box_sizer)
        box_sizer.Fit(self)
        
        self.ok.Bind(wx.EVT_BUTTON, self.Save)
        self.new.Bind(wx.EVT_BUTTON, self.New)  
        self.int.Bind(wx.EVT_BUTTON, self.IntTblcf) 
        self.modi.Bind(wx.EVT_BUTTON, self.Modi)      
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.dele.Bind(wx.EVT_BUTTON, self.CntrDele)
        self.selez.Bind(wx.EVT_BUTTON, self.Selez)
        self.ccodcf1.Bind(wx.EVT_BUTTON, self.FndCodCF1)
        self.codcf1.Bind(wx.EVT_TEXT_ENTER, self.FndCodCF1)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnagDest)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnagDest)
        self.ragsoc1.Bind(wx.EVT_CHAR, self.EvtChar)
        self.indiriz.Bind(wx.EVT_TEXT_ENTER, self.zonaSF)
        self.zona.Bind(wx.EVT_TEXT_ENTER, self.capSF)
        self.cap.Bind(wx.EVT_TEXT_ENTER, self.prSF)
        self.pr.Bind(wx.EVT_TEXT_ENTER, self.localitSF)
        self.localit.Bind(wx.EVT_TEXT_ENTER, self.tabiSF)
        self.Bind(wx.EVT_CLOSE, self.Close)    
        
        self.Start(self)
        
    def Start(self, evt):
        self.DelTxt(self)
        self.OffTxt(self)
        self.stampa.Enable(False)
        self.modi.Enable(False)
        self.new.Show(True)
        self.ok.Show(False)
        self.int.Show(False)
        self.codcf1.Enable(True)
        self.ccodcf1.Enable(True)
        self.codcf.Enable(False)
        self.ragsoc1.Enable(True)
        self.ragsoc1.SetFocus()
        self.cragsoc1.Enable(True)
        self.t_cpart.Enable(False)
        self.t_cpart.Show(False)
        self.stampa.Show(False)
        self.cntr=""
        self.codcf.SetValue(self.cod)

    def indirizSF(self, evt):
        self.indiriz.SetFocus()
    def zonaSF(self, evt):
        self.zona.SetFocus()
    def capSF(self, evt):
        self.cap.SetFocus()
    def prSF(self, evt):
        self.pr.SetFocus()
    def localitSF(self, evt):
        self.localit.SetFocus()
    def tabiSF(self, evt):
        self.tabi.SetFocus()
            
    def IntTblcf(self, evt):
        self.rec=""
        self.Start(self)
        self.canc.Show(True)
        self.new.Show(True)
        self.ok.Show(False)
        self.dele.Show(False)
        self.stampa.Enable(False)
        
    def FndSel(self, evt):
        row=evt
        self.t_cpart.SetValue(str(row[0]))
        self.codcf1.SetValue(str(row[1]))
        self.codcf.SetValue(str(row[2]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.indiriz.SetValue(str(row[6]).title())         
        self.zona.SetValue(str(row[8]).title())
        self.localit.SetValue(str(row[9]).title())
        cap='%05d' % row[7]
        if cap == "00000" : cap =""
        self.cap.SetValue(cap)
        self.pr.SetValue(str(row[10]).strip().upper())
        self.stato.SetValue(str(row[11]).title())
        self.tabi.SetValue(str(row[12]))
        self.tuff.SetValue(str(row[13]))
        self.fax.SetValue(str(row[14]))
        self.OffTxt(self)
        self.modi.Enable(True)
        self.modi.SetFocus()
        self.canc.Show(False)
        self.int.Show(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(False)
        self.dele.Show(False)
        self.stampa.Enable(True)

    def NewTxt(self, evt):
        self.OnTxt(self) 
        self.codcf1.Enable(False)
        self.ccodcf1.Enable(False)
        self.ragsoc1.SetFocus()
        self.cragsoc1.Enable(False)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(True)
        self.canc.Show(False)
        self.int.Show(True)
        self.dele.Show(False)
        
    def ModiTxt(self, evt):
        self.OnTxt(self)
        self.modi.Enable(False)
        self.int.SetFocus()
        self.ok.Enable(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.dele.Show(True)
        
    def SaveTxt(self, evt):
        self.OffTxt(self)
        self.int.SetFocus()
        self.ok.Show(False)
        self.new.Show(True)
        self.dele.Show(False)

    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.int.SetFocus()
        evt.Skip()
        
    def OffTxt(self, evt):
        self.codcf1.Enable(False)
        self.ccodcf1.Enable(False)
        self.ragsoc1.Enable(False)
        self.ragsoc2.Enable(False)
        self.cragsoc1.Enable(False)
        self.indiriz.Enable(False)
        self.zona.Enable(False)
        self.pr.Enable(False)
        self.cap.Enable(False)
        self.localit.Enable(False)
        self.stato.Enable(False)
        self.tabi.Enable(False)
        self.tuff.Enable(False)
        self.fax.Enable(False)
        self.cntr=""

    def OnTxt(self ,evt):
        self.codcf1.Enable(True)
        self.ccodcf1.Enable(True)
        self.ragsoc1.Enable(True)
        self.ragsoc2.Enable(True)
        self.cragsoc1.Enable(True)
        self.zona.Enable(True)
        self.pr.Enable(True)
        self.cap.Enable(True)
        self.localit.Enable(False)
        self.stato.Enable(False)
        self.indiriz.Enable(True)
        self.tabi.Enable(True)
        self.tuff.Enable(True)
        self.fax.Enable(True)
        
    def DelTxt(self, evt):
        self.codcf1.SetValue('')
        #self.codcf.SetValue('')
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.indiriz.SetValue('')
        self.zona.SetValue('')
        self.cap.SetValue('')
        self.pr.SetValue('')
        self.localit.SetValue('')
        self.stato.SetValue('')
        self.tabi.SetValue('')
        self.tuff.SetValue('')
        self.fax.SetValue('')
        self.t_cpart.SetValue(self.tcpart)
        
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_OK:
            dlg.Destroy()
            
    def SetFcs(self, evt):
        evt.Skip()
        
    def KillFcs_cap(self, evt):            
        vcap=self.cap.GetValue()
        if (vcap!=""):
            if (vcap.isdigit()!= True):
                self.Message(_("CAP ") + cfg.msgdatono,self.ttl)
                self.cap.SetFocus()
            else:self.pr.SetFocus()

    def KillFcs_tabi(self, evt):
        vtabi=self.tabi.GetValue()
        if (vtabi!=""):
            if (vtabi.isdigit()!= True ):
                self.Message(_("Tel. ") + cfg.msgdatono,self.ttl)
                self.tabi.SetFocus()
                
    def KillFcs_codcf1(self, evt):
        vcodcf1=self.codcf1.GetValue()
        if (vcodcf1==""):
            self.Message(cfg.msgnocod,self.ttl)
            self.codcf1.SetFocus()
                       
    def KillFcs_fax(self, evt):
        vfax=self.fax.GetValue()
        if (vfax!=""):
            if (vfax.isdigit()!= True):
                self.Message(_("Fax ") + cfg.msgdatono,self.ttl)
                self.fax.SetFocus()
            
    def KillFcs_tuff(self, evt):
        vtuff=self.tuff.GetValue()
        if (vtuff!=""):
            if (vtuff.isdigit()!= True):
                self.Message(_("Tel. ") + cfg.msgdatono,self.ttl)
                self.tuff.SetFocus()

    def KillFcs_pr(self, evt):
        vpr=self.pr.GetValue()
        if (vpr!=""): 
            if (vpr.isalpha()!= True):
                self.Message(_("PR ") + cfg.msgdatono,self.ttl)
                self.pr.SetFocus()
            
    ##Funzioni tasti            
    def Close(self, evt):
        #print self.IDMENU 
        if (self.ragsoc1.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgesci, self.ttl,
                  wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
                self.Destroy()   
            else:
                dlg.Destroy() 
        else:
            self.Destroy() 
                 
    def Modi(self, evt):
        dlg = wx.MessageDialog(self, msgmodi_anag, self.ttl,
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
        tcpart = self.t_cpart.GetValue().upper()
        sql = " SELECT MAX(cod) FROM  tblcf WHERE T_CPART = '%s' "
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % tcpart)
            while (1):
                row=cr.fetchone()
                if row == None:
                    break
                if (row[0] == None) : self.codcf1.SetValue('1')
                if (row[0] != None) : self.codcf1.SetValue(str(int(row[0])+1))
        except StandardError, msg:
            self.__FRM__.MsgErr("tblcf"," New Error %s"  % (msg))
        self.CnAz.commit()
           
    def Save(self, evt):
        vcntr=self.cntr
        vtabi=self.tabi.GetValue()
        vfax=self.fax.GetValue()
        vtuff=self.tuff.GetValue()
        vpr=self.pr.GetValue()
        if vpr=="":vpr="--"
        vcodcf1=self.codcf1.GetValue()
        vcodcf=self.codcf.GetValue()
        vragsoc1=self.ragsoc1.GetValue().strip().title() 
        if (vcodcf.isdigit()!= True ):
            self.Message(cfg.msgdatono,self.ttl)
        if (vragsoc1==""):
            self.Message(cfg.msgcmp_null,self.ttl)
            self.ragsoc1.SetFocus()
        else:
            self.SaveTxt(self)
            vtcpart=self.t_cpart.GetValue().strip().upper()        
            vcodcf1=self.codcf1.GetValue().strip()
            vcodcf=self.codcf.GetValue()
            vragsoc2=self.ragsoc2.GetValue().strip().title() 
            vragsoc1=self.ragsoc1.GetValue().strip().title()  
            vindiriz=self.indiriz.GetValue().strip().title()
            vzona=self.zona.GetValue().strip().title()
            vlocalit=self.localit.GetValue().strip().title()
            vcap=self.cap.GetValue().strip()
            if vcap == "" : vcap=0                   
            vpr=self.pr.GetValue().strip().upper()
            if vpr=="":vpr="--"
            vstato=self.stato.GetValue().title()
            vtabi=self.tabi.GetValue().strip()        
            vfax=self.fax.GetValue().strip()      
            vtuff=self.tuff.GetValue().strip()       
            vnote=''
            vnsrif="" 
            vcampo1=""
            vcampo2=""
            vfrm1modi = int(vcodcf),vragsoc1,vragsoc2,vnsrif
            vfrm1 = vtcpart,int(vcodcf1),int(vcodcf),vragsoc1,vragsoc2,vnsrif
            vfrm2 = vindiriz,int(vcap),vzona,vlocalit,vpr,vstato 
            vfrm3 = vtabi,vtuff,vfax
            vfrm4 = vnote,vcampo1,vcampo2
            vfrm4modi = vnote,vcampo1,vcampo2,int(vcodcf1),vtcpart 
            valueSql_cf = vfrm1+vfrm2+vfrm3+vfrm4
            valueSql_modi_cf = vfrm1modi+vfrm2+vfrm3+vfrm4modi
            if(vcntr=="new"):
                try:
                    cr = self.CnAz.cursor()
                    sql = """ INSERT INTO tblcf 
                              VALUES('%s','%s','%s','%s','%s','%s','%s','%s',
                                     '%s','%s','%s','%s','%s','%s','%s','%s',
                                     '%s','%s') """
                    cr.execute(sql % valueSql_cf)  
                except StandardError, msg:
                    self.__FRM__.MsgErr("tblcf"," Save new Error %s"  % (msg))
                self.CnAz.commit()
            if(vcntr=="modi"):
                try:
                    cr = self.CnAz.cursor()
                    sql = """ UPDATE tblcf SET
                              CODCF = '%s', RAG_SOC1 = '%s', RAG_SOC2 = '%s', 
                              NSRIF = '%s', INDIRIZ = '%s', CAP = '%s', ZONA = '%s', 
                              LOCALIT = '%s', PR = '%s', STATO = '%s' , TEL_ABIT = '%s',
                              TEL_UFF = '%s', FAX = '%s', NOTE = '%s', CAMPO1 = '%s', 
                              CAMPO2 = '%s'
                              WHERE COD = '%s' AND T_CPART = '%s' """
                    cr.execute(sql % valueSql_modi_cf)  
                except StandardError, msg:
                    self.__FRM__.MsgErr("tblcf"," Save modi Error %s"  % (msg))
                self.CnAz.commit()

    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgnodele_anag, self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr=""
            dlg.Destroy()
            
    def Dele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdele_anag,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.cntr="dele"
            cod=self.codcf1.GetValue()
            sql = " DELETE FROM tblcf WHERE cod = '%s' AND t_cpart = '%s' "
            valueSql = int(cod), self.tcpart
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
            except StandardError, msg:
                self.__FRM__.MsgErr("tblcf"," Dele Error %s"  % (msg))
            self.CnAz.commit()
                  
            self.IntTblcf(self)
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()
    
    def FndCodCF1(self, evt):
        pass

    def FndCodCFDest(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        cod = self.codcf1.GetValue()
        sql = " SELECT * FROM tblcf WHERE cod = '%s' AND t_cpart = '%s' "
        valueSql = int(cod), self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1   
        except StandardError, msg:
            self.__FRM__.MsgErr("tblcf"," FndCodCFDest Error %s"  % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttldest)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnagDest(row)

    def FndAnagDest(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue()
        cod = self.codcf1.GetValue()
        sql = " SELECT * FROM tblcf WHERE rag_soc1 like '%s' AND t_cpart = '%s' "
        valueSql = '%'+val.title()+'%', self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__FRM__.MsgErr("tblcf"," FndAnagDest Error %s"  % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttldest)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnagDest(row)
        elif (cnt_rec>1):
            import srctblcf
            control = [self.tcpart,self.codcf1,self.ragsoc1,self.FndCodCFDest,self.codcf]               
            win = srctblcf.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else:
            self.ragsoc1.SetFocus()

    def FndSelAnagDest(self, evt):
        row=evt
        self.codcf1.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.indiriz.SetValue(str(row[6]).title())
        cap=string.zfill(str(row[7]).strip(),5)
        if cap == "00000" : cap =""
        self.cap.SetValue(cap)
        self.__FRM__.CnvNone(row[8])
        self.zona.SetValue(self.__FRM__.val)
        self.__FRM__.CnvNone(row[9])
        self.localit.SetValue(self.__FRM__.val)
        self.__FRM__.CnvNone(row[10])
        self.pr.SetValue(self.__FRM__.val)
        self.__FRM__.CnvNone(row[11])
        self.stato.SetValue(self.__FRM__.val)

    def Selez(self, event):
        self.cnt[2].SetValue(self.codcf1.GetValue())
        self.cnt[3].SetValue(self.ragsoc1.GetValue())      
        self.Destroy() 
