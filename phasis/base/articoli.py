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


import wx
from cfg import *
import cfg


def create(parent, cnt):
    return Articoli(parent, cnt)
 
class Articoli(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #wx.Frame.__init__(self, id=wx.NewId(), name='',
        #      parent=prnt, pos=wx.Point(0, 0),size=wx.DefaultSize,  
        #      style=wx.DEFAULT_FRAME_STYLE, title=cnt[0])
        
        #self.SetIcon(wx.Icon(cfg.path_img+"/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.SetClientSize(wx.Size(680, 360))
        #self.Center(wx.BOTH)
        
        #self.SetScrollbars(1,1,100,100) #####
        #self.FitInside()  ######
        
        self.ttl=cnt[0]
        self.tblart="articoli"
        self.rec = cnt[2]
        self.AggMenu=cnt[3]
        self.IDMENU=cnt[4]
        self.sUM=""
        self.sALIVA=""
        self.sMERCE=""
        self.sIMBAL=""
        self.sCONF=""
        self.sDIVacq=""
        self.sFOR=""
        self.cntn="N" #codice numerico
        self.color=self.GetBackgroundColour()
        #self.font=self.GetFont()
        self.cntr=""
        Nid = wx.NewId()   
        
        self.__MDI__= wx.GetApp().GetPhasisMdi()
       
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz=self.__MDI__.GetConnAZ() 
        self.annoc=self.__MDI__.GetAnnoC() 
        self.datacon= self.__MDI__.GetDataC()
        self.dzDatiAzienda= self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id=wx.NewId(), name='panel',
              parent=self, pos=wx.Point(0, 0), size = wx.DLG_SZE(self,680/2,370/2), #size=wx.Size(680, 370), 
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL )
        self.pnl.SetFont(self.font)
        
        self.lbcodart = wx.StaticText(self.pnl, -1, _("Codice :"), 
             wx.DLG_PNT(self.pnl, 5,7))
        self.lbcodart.SetFont(self.font)
        
        self.codart = wx.TextCtrl(self.pnl, Nid, "",
            wx.DLG_PNT(self.pnl, 55,5), 
            wx.DLG_SZE(self.pnl, 60,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.codart.SetFont(self.font)
        
        self.ccodart=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
             wx.DLG_PNT(self.pnl, 120,5),
             wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV),wx.TE_PROCESS_ENTER)
        
        wx.StaticText(self.pnl, -1, _("BarCode :"), wx.DLG_PNT(self.pnl, 140,7)).SetFont(self.font)
        
        self.codbar = wx.TextCtrl(self.pnl, Nid, "",
            wx.DLG_PNT(self.pnl, 180, 5), 
            wx.DLG_SZE(self.pnl, 75,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)
        self.codbar.SetFont(self.font)
        
        self.ccodbar=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
             wx.DLG_PNT(self.pnl, 260,5),
             wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV),wx.TE_PROCESS_ENTER)
        
        wx.StaticText(self.pnl, -1, _("Descrizione :"), wx.DLG_PNT(self.pnl, 5,22)).SetFont(self.font)
        
        self.descriz = wx.TextCtrl(self.pnl, Nid, "",
             wx.DLG_PNT(self.pnl, 55,20), 
             wx.DLG_SZE(self.pnl, 200,cfg.DIMFONTDEFAULT),wx.TE_PROCESS_ENTER)                    
        self.descriz.SetFont(self.font)
        
        self.cdescriz=wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
             wx.DLG_PNT(self.pnl, 260,20),
             wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        
        wx.StaticText(self.pnl, -1, _("UM :"), wx.DLG_PNT(self.pnl, 5,37)).SetFont(self.font)
        
        self.UM = wx.ComboBox(self.pnl, Nid,"",
             wx.DLG_PNT(self.pnl, 55,35), 
             wx.DLG_SZE(self.pnl, 55,-1), [],
             wx.CB_DROPDOWN | wx.CB_SORT | wx.TE_PROCESS_ENTER )
        self.UM.SetFont(self.font)
        
        self.vUM = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,37))                    
        
        wx.StaticText(self.pnl, -1, _("Mis :"), wx.DLG_PNT(self.pnl, 115,37)).SetFont(self.font)
        
        self.mis = wx.TextCtrl(self.pnl, Nid, "",
            wx.DLG_PNT(self.pnl, 135,35), wx.DLG_SZE(self.pnl, 20, cfg.DIMFONTDEFAULT))                    
        self.mis.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Cat. Merc. :"), wx.DLG_PNT(self.pnl, 5,52)).SetFont(self.font)
        
        self.MERCE = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 55,50), 
              wx.DLG_SZE(self.pnl, 100,-1), [],wx.CB_DROPDOWN | wx.CB_SORT )     
        self.MERCE.SetFont(self.font)
        
        self.vMERCE = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,52))                    
        
        wx.StaticText(self.pnl, -1, _("Fornitore :"), wx.DLG_PNT(self.pnl, 5,67)).SetFont(self.font)
        
        self.FOR = wx.ComboBox(self.pnl, Nid,"",
              wx.DLG_PNT(self.pnl, 55,65), 
              wx.DLG_SZE(self.pnl, 100,-1), [],wx.CB_DROPDOWN | wx.CB_SORT )  
        self.FOR.SetFont(self.font)
        
        self.vFOR = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,67))                    
        
        wx.StaticText(self.pnl, -1, _("Aliquota IVA :"), wx.DLG_PNT(self.pnl, 5,82)).SetFont(self.font)
        
        self.ALIVA = wx.ComboBox(self.pnl, Nid,"",
               wx.DLG_PNT(self.pnl, 55,80), 
               wx.DLG_SZE(self.pnl, 100,-1), [],
               wx.CB_DROPDOWN | wx.CB_SORT )                      
        self.ALIVA.SetFont(self.font)
        
        self.vALIVA = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,82))                    
        
        wx.StaticText(self.pnl, -1, _("Divisa CA :"), wx.DLG_PNT(self.pnl, 5,97)).SetFont(self.font)
        
        self.DIVacq = wx.ComboBox(self.pnl, Nid,"",
               wx.DLG_PNT(self.pnl, 55,95), 
               wx.DLG_SZE(self.pnl, 70,-1), [],
               wx.CB_DROPDOWN | wx.CB_SORT )                      
        self.DIVacq.SetFont(self.font)
        
        self.vDIVacq = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,97))                    
        
        self.vDIVven = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 5,97))                    
        
        #self.box = wx.StaticBox(self.pnl, Nid, " ",
        #       wx.DLG_PNT(self.pnl, 165,32), wx.DLG_SZE(self.pnl, 107,60))
        self.box = wx.StaticBox(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 165,35), wx.DLG_SZE(self.pnl, 107,57))
        self.box.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Imponibile :"), wx.DLG_PNT(self.pnl, 169,43)).SetFont(self.font)
        
        self.prezzo1 = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 210, 41), 
               wx.DLG_SZE(self.pnl, 58,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)
        self.prezzo1.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Prezzo :"), wx.DLG_PNT(self.pnl, 169,60)).SetFont(self.font)
        
        self.cprezzo2 = wx.BitmapButton(self.pnl, -1, png,#wx.Button(self.pnl, Nid, "...", 
               wx.DLG_PNT(self.pnl, 195,58),
               wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV),wx.TE_PROCESS_ENTER)
        
        self.prezzo2 = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 210, 58), 
               wx.DLG_SZE(self.pnl, 58,cfg.DIMFONTDEFAULT),  wx.ALIGN_RIGHT)
        self.prezzo2.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Costo :"), wx.DLG_PNT(self.pnl, 169,77)).SetFont(self.font)
        
        self.costo = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 210, 75), 
               wx.DLG_SZE(self.pnl, 58,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)
        self.costo.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Sc1 %"), wx.DLG_PNT(self.pnl, 5,112)).SetFont(self.font)
        
        self.sc1 = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 28,110), 
               wx.DLG_SZE(self.pnl, 26,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)                    
        self.sc1.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Sc2 %"), wx.DLG_PNT(self.pnl, 57,112)).SetFont(self.font)
        
        self.sc2 = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 80,110), 
               wx.DLG_SZE(self.pnl, 26,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)                    
        self.sc2.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Sc3 %"), wx.DLG_PNT(self.pnl, 109,112)).SetFont(self.font)
        
        self.sc3 = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 132,110), 
               wx.DLG_SZE(self.pnl, 26,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)                    
        self.sc3.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("QTmin :"), wx.DLG_PNT(self.pnl, 162,112)).SetFont(self.font)
        
        self.QTmin = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 189,110), 
               wx.DLG_SZE(self.pnl, 26,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.QTmin.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("QTmax :"), wx.DLG_PNT(self.pnl, 218,112)).SetFont(self.font)
        
        self.QTmax = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 247,110), 
               wx.DLG_SZE(self.pnl, 26,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.QTmax.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Imballo :"), wx.DLG_PNT(self.pnl, 5,127)).SetFont(self.font)
        
        self.IMBAL = wx.ComboBox(self.pnl, Nid,"",
               wx.DLG_PNT(self.pnl, 35,125), 
               wx.DLG_SZE(self.pnl, 40,-1), [],wx.CB_DROPDOWN | wx.CB_SORT )
        self.IMBAL.SetFont(self.font)
        
        self.vIMBAL = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 285,127))                    
        
        wx.StaticText(self.pnl, -1, _("Confez :"), wx.DLG_PNT(self.pnl, 80,127)).SetFont(self.font)
        
        self.CONFE = wx.ComboBox(self.pnl, Nid,"",
               wx.DLG_PNT(self.pnl, 110,125), 
               wx.DLG_SZE(self.pnl, 65,-1), [],wx.CB_DROPDOWN | wx.CB_SORT )
        self.CONFE.SetFont(self.font)
        
        self.vCONFE = wx.TextCtrl(self.pnl, -1, "", wx.DLG_PNT(self.pnl, 285,137))                    
        
        wx.StaticText(self.pnl, -1, _("Peso :"), wx.DLG_PNT(self.pnl, 179,127)).SetFont(self.font)
        
        self.peso = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 202,125), 
               wx.DLG_SZE(self.pnl, 26,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)                    
        self.peso.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Vol. :"), wx.DLG_PNT(self.pnl, 230,127)).SetFont(self.font)
        
        self.vol = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 247,125), 
               wx.DLG_SZE(self.pnl, 26,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.vol.SetFont(self.font)
        
        wx.StaticText(self.pnl, -1, _("Note :"), wx.DLG_PNT(self.pnl, 5,142)).SetFont(self.font)
        
        self.note = wx.TextCtrl(self.pnl, Nid, "",
               wx.DLG_PNT(self.pnl, 35,140), wx.DLG_SZE(self.pnl, 238,cfg.DIMFONTDEFAULT))                    
        self.note.SetFont(self.font)
        
        self.lbInP=wx.StaticText(self.pnl, -1, _("InP :"), 
               wx.DLG_PNT(self.pnl, 237,142))
        self.lbInP.SetFont(self.font)
        
        self.InP = wx.TextCtrl(self.pnl, Nid, "",
              wx.DLG_PNT(self.pnl, 253,140), 
              wx.DLG_SZE(self.pnl, 20,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)                    
        self.InP.SetFont(self.font)
        
        self.new = wx.Button(self.pnl, Nid, cfg.vcnew, 
              wx.DLG_PNT(self.pnl, 280,20), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))     
        self.new.SetFont(self.font)
        
        self.ok = wx.Button(self.pnl, Nid, cfg.vcok,
              wx.DLG_PNT(self.pnl, 280,20), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))              
        self.ok.SetFont(self.font)
        
        self.inte = wx.Button(self.pnl, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 280,35), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.inte.SetFont(self.font)
        
        self.canc = wx.Button(self.pnl, Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 280,35), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc.SetFont(self.font)
        
        self.modi = wx.Button(self.pnl, Nid, cfg.vcmodi, 
              wx.DLG_PNT(self.pnl, 280,50), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV)) 
        self.modi.SetFont(self.font)
        
        self.dele = wx.Button(self.pnl, Nid, cfg.vcdele, 
              wx.DLG_PNT(self.pnl, 280,50), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.dele.SetFont(self.font)
        
        self.stampa = wx.Button(self.pnl, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 280,65), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa.SetFont(self.font)
        
        self.scheda = wx.Button(self.pnl, Nid, cfg.vcscheda, 
              wx.DLG_PNT(self.pnl, 280,80), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.scheda.SetFont(self.font)
        
        
        #lscontrolli=self.pnl.GetChildren()
        #for x in self.pnl.GetChildren(): x.SetFont(self.font)
        
        
        
        
        #self.SetFont(self.font)
        
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
        #####self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)
        
        
        self.scheda.Bind(wx.EVT_BUTTON, self.SkArt)      
        #self.descriz.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.dele.Bind(wx.EVT_BUTTON, self.CntrDele)
        self.ok.Bind(wx.EVT_BUTTON, self.Save)
        self.new.Bind(wx.EVT_BUTTON, self.New)  
        self.inte.Bind(wx.EVT_BUTTON, self.Int) 
        self.modi.Bind(wx.EVT_BUTTON, self.Modi)      
        self.canc.Bind(wx.EVT_BUTTON, self.Close)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.ccodbar.Bind(wx.EVT_BUTTON, self.FndCodBar)
        self.ccodart.Bind(wx.EVT_BUTTON, self.FndCodArt)
        self.cdescriz.Bind(wx.EVT_BUTTON, self.FndDesArt)
        self.descriz.Bind(wx.EVT_TEXT_ENTER, self.FndDesArt)
        self.codbar.Bind(wx.EVT_TEXT_ENTER, self.FndCodBar)
        self.codart.Bind(wx.EVT_TEXT_ENTER, self.FndCodArt)
        self.UM.Bind(wx.EVT_TEXT_ENTER, self.UMSF)
        self.mis.Bind(wx.EVT_TEXT_ENTER, self.misSF)
        self.MERCE.Bind(wx.EVT_TEXT_ENTER, self.MERCESF)
        self.FOR.Bind(wx.EVT_TEXT_ENTER, self.FORSF)
        self.ALIVA.Bind(wx.EVT_TEXT_ENTER, self.ALIVASF)
        self.prezzo1.Bind(wx.EVT_TEXT_ENTER, self.prezzo1SF)
        self.cprezzo2.Bind(wx.EVT_BUTTON, self.CalcPrezzo2)
        self.prezzo2.Bind(wx.EVT_TEXT_ENTER, self.prezzo2SF)
        self.costo.Bind(wx.EVT_TEXT_ENTER, self.costoSF)
        self.DIVacq.Bind(wx.EVT_TEXT_ENTER, self.DIVacqSF)
        ##        self.DIVven.Bind(wx.EVT_TEXT_ENTER, self.SetDIVven)
        self.sc1.Bind(wx.EVT_TEXT_ENTER, self.sc1SF)
        self.sc2.Bind(wx.EVT_TEXT_ENTER, self.sc2SF)
        self.sc3.Bind(wx.EVT_TEXT_ENTER, self.sc3SF)
        self.QTmin.Bind(wx.EVT_TEXT_ENTER, self.QTminSF)
        self.QTmax.Bind(wx.EVT_TEXT_ENTER, self.QTmaxSF)
        self.IMBAL.Bind(wx.EVT_TEXT_ENTER, self.IMBALSF)
        self.CONFE.Bind(wx.EVT_TEXT_ENTER, self.CONFESF)
        self.peso.Bind(wx.EVT_TEXT_ENTER, self.pesoSF)
        self.vol.Bind(wx.EVT_TEXT_ENTER, self.volSF)
        ##self.codbar.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_codbar)
        self.codart.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_codart)
        self._locked = False
        self.prezzo1.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_prezzo1)
        self.prezzo2.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_prezzo2)
        self.costo.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_costo)
        self.sc1.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_sc1)
        self.sc2.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_sc2)
        self.sc3.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_sc3)       
        self.QTmin.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_QTmin)
        self.QTmax.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_QTmax)
        self.peso.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_peso)
        self.vol.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_vol)
        self.UM.Bind(wx.EVT_COMBOBOX, self.SelUM)
        self.ALIVA.Bind(wx.EVT_COMBOBOX, self.SelALIVA)
        self.MERCE.Bind(wx.EVT_COMBOBOX, self.SelMERCE)
        self.FOR.Bind(wx.EVT_COMBOBOX, self.SelFOR)
        self.IMBAL.Bind(wx.EVT_COMBOBOX, self.SelIMBAL)
        self.CONFE.Bind(wx.EVT_COMBOBOX, self.SelCONF)
        self.DIVacq.Bind(wx.EVT_COMBOBOX, self.SelDIVacq)
        self.codart.Bind(wx.EVT_CHAR, self.EvtChar)    
        self.Start(self)

    def Start(self, evt):
        self.DelTxt(self)
        self.OffTxt(self)
        self.codbar.Enable(True)
        self.codart.Enable(True)
        self.descriz.Enable(True)
        #self.codart.Show(True)
        #self.codbar.SetFocus()
        self.ccodbar.Enable(True)
        self.ccodart.Enable(True)
        self.cdescriz.Enable(True)
        self.stampa.Enable(False)
        self.scheda.Enable(False)
        self.modi.Enable(False)
        #self.inte.Show(False)
        self.codart.SetFocus()  
        self.vUM.Enable(False)
        self.vUM.Show(False)
        self.vMERCE.Enable(False)
        self.vMERCE.Show(False)
        self.vFOR.Enable(False)
        self.vFOR.Show(False)
        self.vALIVA.Enable(False)
        self.vALIVA.Show(False)
        self.vDIVacq.Enable(False)
        self.vDIVacq.Show(False)
        self.vDIVven.Enable(False)
        self.vDIVven.Show(False)
        self.vIMBAL.Enable(False)
        self.vIMBAL.Show(False)
        self.vCONFE.Enable(False)
        self.vCONFE.Show(False)      
        self.InP.Enable(False)
        self.InP.Show(False)
        self.lbInP.Show(False)
        self.vUM.SetValue("PZ")
        self.vALIVA.SetValue("20")
        self.vMERCE.SetValue("0")
        self.vIMBAL.SetValue("IMBVS")
        self.vCONFE.SetValue("CFSF")
        self.vDIVacq.SetValue("EU")
        self.vDIVven.SetValue("EU")
        self.vFOR.SetValue("0")
        self.InP.SetValue("Y")
        #self.reg_def.SetValue("N")
        self.cntr=""
        if (self.rec!=""):
            self.codart.SetValue(self.rec)
            self.FndCodArt(self)
        self.SelCOMBO(self)

    def CalcPrezzo2(self, evt):
        vALIVA = self.vALIVA.GetValue()
        self.__MDI__.CnvPM(vALIVA)
        vALIVA = self.__MDI__.val
        prezzo1 = self.prezzo1.GetValue()
        self.__MDI__.CnvPM5(prezzo1)
        prezzo1 = self.__MDI__.val
        prezzo2 = prezzo1 + (prezzo1 *  vALIVA / 100 )
        self.__MDI__.CnvVM5(prezzo2)
        prezzo2 = self.__MDI__.val
        self.prezzo2.SetValue(prezzo2)

    def UMSF(self, evt):
        self.mis.SetFocus()
    def misSF(self, evt):
        self.MERCE.SetFocus()      
    def MERCESF(self, evt):
        self.FOR.SetFocus()      
    def FORSF(self, evt):
        self.ALIVA.SetFocus()      
    def ALIVASF(self, evt):
        self.prezzo1.SetFocus()       
    def prezzo1SF(self, evt):
        self.prezzo2.SetFocus()      
    def prezzo2SF(self, evt):
        self.costo.SetFocus()      
    def costoSF(self, evt):
        self.DIVacq.SetFocus()       
    def DIVacqSF(self, evt):
        self.sc1.SetFocus()
    #def DIVvenSF(self, evt):
    #    self.sc1.SetFocus()
    def sc1SF(self, evt):
        self.sc2.SetFocus()        
    def sc2SF(self, evt):
        self.sc3.SetFocus()        
    def sc3SF(self, evt):
        self.QTmin.SetFocus()        
    def QTminSF(self, evt):
        self.IMBAL.SetFocus()        
    def QTmaxSF(self, evt):
        self.QTmax.SetFocus()        
    def IMBALSF(self, evt):
        self.CONFE.SetFocus()        
    def CONFESF(self, evt):
        self.peso.SetFocus()        
    def pesoSF(self, evt):
        self.vol.SetFocus()        
    def volSF(self, evt):
        self.ok.SetFocus()

    def OffTxt(self, evt):
        self.codbar.Enable(False)
        self.ccodbar.Enable(False)
        self.codart.Enable(False)
        self.descriz.Enable(False)
        self.ccodart.Enable(False)
        self.cdescriz.Enable(False)  
        self.UM.Enable(False)
        self.mis.Enable(False)
        self.MERCE.Enable(False)
        self.FOR.Enable(False)
        self.ALIVA.Enable(False)
        self.DIVacq.Enable(False)
        self.prezzo1.Enable(False)
        self.prezzo2.Enable(False)
        self.costo.Enable(False)       
        self.sc1.Enable(False)
        self.sc2.Enable(False)
        self.sc3.Enable(False)
        self.QTmin.Enable(False)
        self.QTmax.Enable(False)
        self.IMBAL.Enable(False)
        self.CONFE.Enable(False)
        self.vol.Enable(False)
        self.peso.Enable(False)
        self.InP.Enable(False)
        self.note.Enable(False)
        self.canc.Show(True) 
        self.canc.Enable(True)
        self.inte.Show(False)
        self.inte.Enable(False)
        self.stampa.Enable(False)
        self.scheda.Enable(False)
        #self.stampa.Show(False)
        self.ok.Show(False)
        self.ok.Enable(False) 
        self.modi.Enable(False)
        self.new.Enable(True)
        self.dele.Enable(False)
        self.dele.Show(False)

    #<daniele> 
    def Stampa(self, evt): 
        codart = self.codart.GetValue()
        valueSql = codart
        import skprint
        skprint.stampaDoc(
            conn = self.CnAz,   #connessione
            tipo = 'sarticoli', #tipo documento e parametro
            parametriSql = valueSql,
            #datiazienda = self.dzDatiAzienda,
            anteprima = True )
    #</daniele>                 

    def OnTxt(self ,evt):
        self.codbar.Enable(True)
        self.ccodbar.Enable(False)
        #self.codbar.SetFocus()
        self.codart.Enable(True)
        self.codart.SetFocus()
        self.ccodart.Enable(False)
        self.descriz.Enable(True)
        self.cdescriz.Enable(False)
        self.UM.Enable(True)
        self.mis.Enable(True)
        self.vUM.Enable(False)
        self.vUM.Show(False)
        self.MERCE.Enable(True)
        self.FOR.Enable(True)
        self.ALIVA.Enable(True)
        self.DIVacq.Enable(True)
        self.prezzo1.Enable(True)
        self.prezzo2.Enable(True)
        self.costo.Enable(True)       
        self.sc1.Enable(True)
        self.sc2.Enable(True)
        self.sc3.Enable(True)
        self.QTmin.Enable(True)
        self.QTmax.Enable(True)
        self.IMBAL.Enable(True)
        self.CONFE.Enable(True)
        self.vol.Enable(True)
        self.peso.Enable(True)
        self.sc1.Enable(True)
        self.sc2.Enable(True)
        self.sc3.Enable(True)
        #self.InP.Enable(False)
        self.note.Enable(True)
        self.canc.Show(False) 
        self.canc.Enable(False)
        self.inte.Show(True)
        self.inte.Enable(True)
        self.ok.Show(True)
        self.ok.Enable(True)
        self.modi.Enable(False)        
        self.stampa.Enable(True)
        self.dele.Enable(True)
        self.dele.Show(True)
        self.new.Enable(False)
        
    def DelTxt(self, evt):
        self.codart.SetValue('')
        self.codbar.SetValue('')
        self.descriz.SetValue('')
        self.mis.SetValue('')
        self.QTmin.SetValue('')
        self.QTmax.SetValue('')
        self.vol.SetValue('')
        self.InP.SetValue('Y')
        self.peso.SetValue('')
        self.note.SetValue('')
        self.prezzo1.SetValue('')
        self.prezzo2.SetValue('')
        self.costo.SetValue('')        
        self.sc1.SetValue('')
        self.sc2.SetValue('')
        self.sc3.SetValue('')
        self.cntr=""

    def SelCOMBO(self, evt):
        # Funzione Cerca TabGen
        vUM=self.vUM.GetValue()
        vALIVA=self.vALIVA.GetValue()
        vMERCE=self.vMERCE.GetValue()
        vFOR=self.vFOR.GetValue()
        vIMBAL=self.vIMBAL.GetValue()
        vCONFE=self.vCONFE.GetValue()
        vDIVacq=self.vDIVacq.GetValue()
        vDIVven=self.vDIVven.GetValue()
        self.UM.Clear()
        self.ALIVA.Clear()
        self.DIVacq.Clear()        
        self.FOR.Clear()
        self.MERCE.Clear()
        self.IMBAL.Clear()
        self.CONFE.Clear()
        sql = """ select cod, valore, descriz from tabgen """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            self.MERCE.Append(' --','0')
                 
            while (1):
                row = cr.fetchone () 
                if row == None: 
                    break          
                if (row[0]=="UNMIS"):
                    if (row[1]==vUM):self.sUM=row[2]
                    self.UM.Append(row[2],row[1])

                if (row[0]=="ALIVA"):
                    if (row[1]==vALIVA):self.sALIVA=row[2]
                    self.ALIVA.Append(row[2],row[1])

                if (row[0]=="MERCE"):
                    if (vMERCE=='0'): self.sMERCE=' --'
                    if (row[1]==vMERCE):self.sMERCE=row[2]
                    self.MERCE.Append(row[2],row[1])

                if (row[0]=="IMBAL"):
                    if (row[1]==vIMBAL): self.sIMBAL=row[2]
                    self.IMBAL.Append(row[2],row[1])
            
                if (row[0]=="CONFE"):
                    if (row[1]==vCONFE):self.sCONF=row[2]
                    self.CONFE.Append(row[2],row[1])
                        
                if (row[0]=="DIVIS"):
                    if (row[1]==vDIVacq):self.sDIVacq=row[2]
                    self.DIVacq.Append(row[2],row[1])

        except StandardError, msg:
            self.__MDI__.MsgErr("Articoli"," Cerca TabGen Error %s"  % (msg))                   
        self.CnAz.commit()
        # Funzione Inserisci Combo CF
        tbl= " anag "
        tcpart="F"
        sql = """ select * from anag where t_cpart = "%s" """
        self.FOR.Append(' --','0')
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % tcpart)                   
            rows = cr.fetchall()
            for row in rows:
                if (vFOR=='0'): self.sFOR=' --'
                if (str(row[1])==vFOR):self.sFOR=str(row[3])+","+str(row[4])
                self.FOR.Append(str(row[3])+","+str(row[4]),str(row[1]))
            #self.FOR.Append(' --','0')
        except StandardError, msg:
            self.__MDI__.MsgErr("Articoli"," FndFOR Error %s"  % (msg))                   
        self.CnAz.commit()
        cntUM=0
        cntALIVA=0
        cntMERCE=0
        cntIMBAL=0
        cntCONF=0
        cntFOR=0
        cntDIVacq=0
        # x mac
        if self.sMERCE=='' : self.sMERCE=' --'
        if self.sFOR=='' : self.sFOR=' --'
        #  --- fine x mac
        cntUM=self.UM.FindString(self.sUM)
        self.UM.Select(cntUM)
        cntALIVA=self.ALIVA.FindString(self.sALIVA)
        self.ALIVA.Select(cntALIVA)
        cntMERCE=self.MERCE.FindString(self.sMERCE)
        self.MERCE.Select(cntMERCE) #se in cat.merceologiche non ci sono valori, da errore, quindi da sistemare
        cntIMBAL=self.IMBAL.FindString(self.sIMBAL)
        self.IMBAL.Select(cntIMBAL)
        cntCONF=self.CONFE.FindString(self.sCONF)
        self.CONFE.Select(cntCONF)
        cntDIVacq=self.DIVacq.FindString(self.sDIVacq)
        self.DIVacq.Select(cntDIVacq)
        cntFOR=self.FOR.FindString(self.sFOR)
        self.FOR.Select(cntFOR)

    def SelDIVacq(self, evt):
        self.Sel(evt)
        self.vDIVacq.SetValue(self.cb_val)

        
    def SelFOR(self, evt):
        self.Sel(evt)
        self.vFOR.SetValue(self.cb_val)


    def SelMERCE(self, evt):
        self.Sel(evt)
        self.vMERCE.SetValue(self.cb_val)

        
    def SelUM(self, evt):
        self.Sel(evt)
        self.vUM.SetValue(self.cb_val)

    def SelALIVA(self, evt):
        self.Sel(evt)
        self.vALIVA.SetValue(self.cb_val)

    def SelIMBAL(self, evt):
        self.Sel(evt)
        self.vIMBAL.SetValue(self.cb_val)

    def SelCONF(self, evt):
        self.Sel(evt)
        self.vCONFE.SetValue(self.cb_val)
        
    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str= evt.GetString()
        evt.Skip()

    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
 	dlg.ShowModal()
        dlg.Destroy()
            
    def SetFcs(self, evt):
        evt.Skip()
        
    #def KillFcs_codbar(self, evt):
        #vcodbar=self.codbar.GetValue()
        #if (vcodbar!=""):
            #if (vcodbar.isalnum()!= True):
                #self.Message(cfg.msgdatono,self.ttl)
                #self.codbar.SetFocus()
            #else: self.descriz.SetFocus()

    def CallAfter(self, func, *args, **kargs):
        def function(args=args, kargs=kargs):
            return func(*args, **kargs)
        wx.CallAfter(function)
        
    def CallLocked(self, evt):
        if self:
            if self._locked:
                self.CallAfter(self.CallLocked, evt)
            else:
                self._locked = True
                wx.BeginBusyCursor()
                try:
                    evt()
                finally:
                    self._locked = False
                    wx.EndBusyCursor()

    def KillFcs_codart(self,evt):
        self.CallAfter(self.CallLocked, self.GetV_codart)
        evt.Skip()

    def GetV_codart(self):
        vcodart=self.codart.GetValue().strip().upper()
        if (self.cntr=="new" and vcodart!=""):
            self.FndDesArtIs(self)
        #self.Refresh()
        

    def KillFcs_mis(self, evt):
        self.MERCE.SetFocus()

    def KillFcs_prezzo1(self,evt):
        self.CallAfter(self.CallLocked, self.GetV_prezzo1)
        evt.Skip()

    def GetV_prezzo1(self):
        vprezzo1=self.prezzo1.GetValue().replace(",","")
        vprezzo1=vprezzo1.replace(".","")
        if (vprezzo1!=""):
            if (vprezzo1.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.prezzo1.SetFocus()
        #self.Refresh()    
            
    def KillFcs_prezzo2(self,evt):
        self.CallAfter(self.CallLocked, self.GetV_prezzo2)
        evt.Skip()

    def GetV_prezzo2(self):
        vprezzo2=self.prezzo2.GetValue().replace(",","")
        vprezzo2=vprezzo2.replace(".","")
        if (vprezzo2!=""):
            if (vprezzo2.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.prezzo2.SetFocus()
        #self.Refresh()    

    def KillFcs_costo(self,evt):
        self.CallAfter(self.CallLocked, self.GetV_costo)
        evt.Skip()

    def GetV_costo(self):
        vcosto=self.costo.GetValue().replace(",","")
        vcosto=vcosto.replace(".","")
        if (vcosto!=""):
            if (vcosto.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.costo.SetFocus()
        #self.Refresh()    


    def KillFcs_QTmin(self, evt):
        self.CallAfter(self.CallLocked, self.GetV_QTmin)
        evt.Skip()

    def GetV_QTmin(self):
        vQTmin=self.QTmin.GetValue().replace(",","")
        vQTmin=vQTmin.replace(".","")
        if (vQTmin!=""):
            if (vQTmin.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.QTmin.SetFocus()


    def KillFcs_QTmax(self, evt):
        self.CallAfter(self.CallLocked, self.GetV_QTmax)
        evt.Skip()

    def GetV_QTmax(self):
        vQTmax=self.QTmax.GetValue().replace(",","")
        vQTmax=vQTmax.replace(".","")
        if (vQTmax!=""):
            if (vQTmax.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.QTmax.SetFocus()

    def KillFcs_sc1(self, evt):
        self.CallAfter(self.CallLocked, self.GetV_sc1)
        evt.Skip()

    def GetV_sc1(self):
        vsc1=self.sc1.GetValue().replace(",","")
        vsc1=vsc1.replace(".","")
        if (vsc1!=""):
            if (vsc1.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.sc1.SetFocus()               

    def KillFcs_sc2(self, evt):
        self.CallAfter(self.CallLocked, self.GetV_sc2)
        evt.Skip()

    def GetV_sc2(self):
        vsc2=self.sc2.GetValue().replace(",","")
        vsc2=vsc2.replace(".","")
        if (vsc2!=""):
            if (vsc2.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.sc2.SetFocus()  
    
    def KillFcs_sc3(self, evt):
        self.CallAfter(self.CallLocked, self.GetV_sc3)
        evt.Skip()

    def GetV_sc3(self):
        vsc3=self.sc3.GetValue().replace(",","")
        vsc3=vsc3.replace(".","")
        if (vsc3!=""):
            if (vsc3.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.sc3.SetFocus()  

    def KillFcs_vol(self, evt):
        self.CallAfter(self.CallLocked, self.GetV_vol)
        evt.Skip()

    def GetV_vol(self):
        vvol=self.vol.GetValue().replace(",","")
        vvol=vvol.replace(".","")
        if (vvol!=""):
            if (vvol.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.vol.SetFocus()  
                
    def KillFcs_peso(self, evt):
        self.CallAfter(self.CallLocked, self.GetV_peso)
        evt.Skip()

    def GetV_peso(self):
        vpeso=self.peso.GetValue().replace(",","")
	vpeso=vpeso.replace(".","")
        if (vpeso!=""):
            if (vpeso.isdigit()!= True):
                self.Message(cfg.msgdatono,self.ttl)
                self.peso.SetFocus()  
                       
            
    def Close(self, evt):
        if (self.codart.GetValue()!="" or self.descriz.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgesci, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
                self.AggMenu(True,self.IDMENU)
                wx.GetApp().GetPhasisMdi().CloseTabObj(self)
                #self.Destroy()
            else:
                dlg.Destroy() 
        else:
            self.AggMenu(True,self.IDMENU)
            wx.GetApp().GetPhasisMdi().CloseTabObj(self)
            #self.Destroy()
        
    def ModiTxt(self, evt):
        self.OnTxt(self)
        self.codart.Enable(False)
        self.descriz.SetFocus()
        self.modi.Enable(False)
        self.inte.SetFocus()
        self.descriz.SetFocus()
        self.ok.Enable(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.stampa.Enable(False)

         
    def SaveTxt(self, evt):
        self.OffTxt(self)
        self.inte.SetFocus()
        self.ok.Show(False)
        self.new.Show(True)
        #self.canc.Show(False)
	self.inte.Enable(True)
        self.inte.Show(True)
        self.dele.Show(False)

    def EvtChar(self, evt):
        evt_char=evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()
           
    def Modi(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgmodi_anag, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.ModiTxt(self)
            self.cntr="modi"
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()
        
    def New(self, evt):
        cnt_rec=0
        sql = " select COUNT(COD) from articoli "
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql)
            while (1):
                row=cr.fetchone()
                if row == None:
                    break
                if (row[0] == None) : cnt_rec=1
        except StandardError, msg:
            self.__MDI__.MsgErr("Articoli"," New Error %s"  % (msg))                   
        self.CnAz.commit()
        self.DelTxt(self)
        self.OnTxt(self) 
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.inte.Enable(True)
        self.dele.Show(False)
        self.cntr="new"
        
    def Int(self, evt):
        self.rec=""
        self.Start(self)
        self.canc.Show(True)
        self.new.Show(True)
        self.ok.Show(False)
        self.dele.Show(False)
              
        
    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self,cfg.msgnodele_anag,self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr=""
            dlg.Destroy()
            
    def Dele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdele_anag, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.cntr = "dele"
            cod = self.codart.GetValue().upper()
            cr = self.CnAz.cursor()
            sql = """ delete from articoli where cod = "%s" """
            cr.execute(sql % cod)
            self.CnAz.commit()
            self.Int(self)
            dlg.Destroy()
        else:
            self.cntr=""
            dlg.Destroy()

    def Save(self, evt):
        vcntr=self.cntr
        vcodart=self.codart.GetValue().upper()
        vcodart=vcodart.strip()
        vcodbar=self.codbar.GetValue().strip()
        vdescriz=self.descriz.GetValue().strip()
        vdescriz=vdescriz.upper()
        vUM=self.vUM.GetValue().strip()
        vmis=self.mis.GetValue().upper().strip()
        self.__MDI__.CnvPM5(self.prezzo1.GetValue().strip())
        vprezzo1=self.__MDI__.val
        self.__MDI__.CnvPM5(self.prezzo2.GetValue().strip())
        vprezzo2=self.__MDI__.val
        self.__MDI__.CnvPM5(self.costo.GetValue().strip())
        vcosto=self.__MDI__.val
        vMERCE=self.vMERCE.GetValue().strip()
        vFOR=self.vFOR.GetValue().strip()
        ##print vFOR
        vALIVA=self.vALIVA.GetValue().strip()
        self.__MDI__.CnvPM(self.QTmin.GetValue().strip())
        vQTmin=self.__MDI__.val
        self.__MDI__.CnvPM(self.QTmax.GetValue())
        vQTmax=self.__MDI__.val
        self.__MDI__.CnvPM(self.sc1.GetValue().strip())
        vsc1=self.__MDI__.val
        self.__MDI__.CnvPM(self.sc2.GetValue().strip())
        vsc2=self.__MDI__.val
        self.__MDI__.CnvPM(self.sc3.GetValue().strip())
        vsc3=self.__MDI__.val
        vCacqu=""
        vDIVacq=self.vDIVacq.GetValue().strip()
        vCvend=""
        vDIVven=self.vDIVven.GetValue().strip()
        vprovv=""
        if vprovv == "" : vprovv=0 
        vIMBAL=self.vIMBAL.GetValue().strip()
        vCONFE=self.vCONFE.GetValue().strip()
        self.__MDI__.CnvPM(self.peso.GetValue().strip())
        vpeso=self.__MDI__.val      
        self.__MDI__.CnvPM(self.vol.GetValue().strip())
        vvol=self.__MDI__.val
        vInP=self.InP.GetValue().upper()
        vInP=vInP.strip()
        vnote=self.note.GetValue().strip()
        vdata_ins=""
        vdata_mod=""
        vdescrfor=""

        if (vcodart==""):
            self.Message(cfg.msgnocod,self.ttl)
            self.codart.SetFocus()
        else:
            self.SaveTxt(self)
            vtbl1 = vcodart,vcodbar,vdescriz,vUM,vmis
            vtbl1modi = vcodbar,vdescriz,vUM,vmis
            vtbl2 = float(vprezzo1),float(vprezzo2),float(vcosto),vMERCE
            vtbl3 = int(vFOR),vdescrfor,vALIVA,float(vQTmin),float(vQTmax)
            vtbl4 = float(vsc1),float(vsc2),float(vsc3),vCacqu,vDIVacq,vCvend,vDIVven,float(vprovv)
            vtbl5 = vIMBAL,vCONFE,float(vpeso),float(vvol),vdata_ins,vdata_mod,vInP,vnote
            vtbl5modi =vIMBAL,vCONFE,float(vpeso),float(vvol),vdata_ins,vdata_mod,vInP,vnote,vcodart
            vfrm=vtbl1 + vtbl2 + vtbl3 + vtbl4 + vtbl5
            vfrm_modi=vtbl1modi + vtbl2 + vtbl3 + vtbl4 + vtbl5modi
            self.cntr=""
            if (vcntr=="new" ):
            # Funzione Salva
                try:
                    cr = self.CnAz.cursor()
                    sql = """ INSERT INTO articoli
                              VALUES("%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s","%s","%s",
                                     "%s","%s","%s","%s","%s","%s")"""                    
                    cr.execute(sql % vfrm)
                except StandardError, msg:
                    self.__MDI__.MsgErr("Articoli"," Ins Articoli Error %s"  % (msg))
		self.CnAz.commit()
            if (vcntr=="modi" ):
                try:
                    cr = self.CnAz.cursor()
                    sql = """ update articoli set codbar = "%s", 
		              descriz = "%s", um = "%s", mis = "%s",
			      prezzo_1 = "%s", prezzo_2 = "%s", costo = "%s",
			      merce = "%s", cod_for = "%s", descrfor = "%s",
			      aliva = "%s", qt_min = "%s", qt_max = "%s", 
			      sc1 = "%s", sc2 = "%s", sc3 = "%s", cacqu = "%s",
			      divacq = "%s", cvend = "%s", divven = "%s", 
			      provv = "%s", imbal = "%s", confe = "%s",
                              peso = "%s", volume = "%s", data_ins = "%s", 
                              data_mod = "%s", inprod = "%s", note = "%s" 
                              where cod = "%s" """
                    cr.execute(sql % vfrm_modi)
                except StandardError, msg:
                    self.__MDI__.MsgErr("Articoli"," Upd Articoli Error %s"  % (msg)) 
		self.CnAz.commit()

            
    def FndSelArt(self, evt):
        row=evt
        self.codart.SetValue(row[0])
        if (row[1]==None or row[1]==0):self.codbar.SetValue("")
        else:self.codbar.SetValue(str(row[1]))    
        self.descriz.SetValue(row[2])
        self.vUM.SetValue(row[3])
        if (row[4]==None):self.mis.SetValue("")
        else: self.mis.SetValue(str(row[4]))
        self.__MDI__.CnvVMPZ(row[5])
        self.prezzo1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVMPZ(row[6])
        self.prezzo2.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVMPZ(row[7])
        self.costo.SetValue(self.__MDI__.val)
        self.vMERCE.SetValue(str(row[8]))
        if (row[9]==None or row[9]==""):self.vFOR.SetValue("0")
        else:self.vFOR.SetValue(str(row[9]))
        self.vALIVA.SetValue(str(row[11]))
        self.__MDI__.CnvVM(row[12])
        self.QTmin.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(row[13])     
        self.QTmax.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(row[14])         
        self.sc1.SetValue(self.__MDI__.val)   
        self.__MDI__.CnvVM(row[15])
        self.sc2.SetValue(self.__MDI__.val) 
        self.__MDI__.CnvVM(row[16])      
        self.sc3.SetValue(self.__MDI__.val)
        vCacqu=""
        self.vDIVacq.SetValue(str(row[18]))
        self.vDIVven.SetValue(str(row[20]))
        self.vIMBAL.SetValue(str(row[22]))
        self.vCONFE.SetValue(str(row[23]))
        self.SelCOMBO(self)
        self.__MDI__.CnvVM(row[24])
        self.peso.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(row[25])
        self.vol.SetValue(self.__MDI__.val)
        self.InP.SetValue(str(row[28]))
        if (row[29]==None):self.note.SetValue("")
        else:self.note.SetValue(str(row[29]))
        self.OffTxt(self)
        self.modi.Enable(True)
        self.modi.SetFocus()
        self.canc.Show(False)
        self.inte.Show(True)
        self.inte.Enable(True)
        self.new.Show(False)
        self.ok.Show(True)
        self.ok.Enable(False)
        self.dele.Show(False)
        self.cntr=""
        self.scheda.Enable(True)
        self.stampa.Enable(True)

    def FndArt(self, evt):
        # Funzione Cerca Codice Articolo
        cnt_rec = 0
	#dml = True
        cod = self.codart.GetValue().upper()           
        sql = """ select * from articoli where cod = "%s" """
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % cod)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("Articoli"," FndArt Error %s"  % (msg))   
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelArt(row)
            
    def FndCodArt(self, evt): 
        # Funzione Cerca Codice Articolo
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec = 0
            cod = self.codart.GetValue().upper()   
	    cod = '%'+cod+'%' 
            sql = """ select * from articoli where cod like "%s" """
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % cod)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                self.__MDI__.MsgErr("Articoli"," FndCodArt Error %s"  % (msg))                   
            self.CnAz.commit()
            if (cnt_rec>=1000): self.Message(cfg.msgfnd + str(cnt_rec) ,self.ttl)
            elif (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
            elif (cnt_rec==1 and cnt_rec<2):self.FndSelArt(row)     
            elif (cnt_rec>1):
                import srcart
                control = [self.tblart,self.codart,self.descriz,self.FndArt]
                win = srcart.create(self,control) 
                win.Centre(wx.BOTH)
                win.ShowModal()#True)
        else: self.codbar.SetFocus()

    def FndCodBar(self, evt):    
        # Funzione Cerca Codice a Barre
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec = 0
            cod = self.codbar.GetValue()
            sql = """ select * from articoli where codbar = "%s" """
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % cod)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                self.__MDI__.MsgErr("Articoli"," FndCodBAr Error %s"  % (msg))                   
            self.CnAz.commit()
            if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttl)
            elif (cnt_rec==1 and cnt_rec<2): self.FndSelArt(row)
        else: self.descriz.SetFocus()
        
    def FndDesArtIs(self, evt):
        # Funzione Cerca Duplicato
        cnt_rec = 0
        val1 = self.codart.GetValue().upper().strip()
        sql = """ select * from articoli where cod = "%s" """  
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % val1)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("Articoli"," FndDescArtIs Error %s"  % (msg))                   
        self.CnAz.commit()
        if (cnt_rec!=0):self.cntr=""
        if (cnt_rec==1 and cnt_rec<2):
            self.Message(cfg.msgdatosi,self.ttl)
            self.FndSelArt(row)     
        elif (cnt_rec>1):
            import srcart
            control = [self.tblart,self.codart,self.descriz,self.FndArt]
            win = srcart.create(self,control) 
            win.Centre(wx.BOTH)
            win.ShowModal()#True)
    
    def FndDesArt(self, evt):
        # Funzione cerca descrizione articolo
        if (self.cntr!="new" and self.cntr!="modi"):
            cnt_rec = 0
            val = self.descriz.GetValue().upper()
	    val = '%'+val+'%'
            sql = """ select * from articoli where descriz like "%s" """
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % val)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                self.__MDI__.MsgErr("Articoli"," FndDescArt Error %s"  % (msg))                   
            self.CnAz.commit()
            if (cnt_rec>=1000): self.Message(cfg.msgfnd + str(cnt_rec) ,self.ttl)
            elif (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
            elif (cnt_rec==1 and cnt_rec<2):self.FndSelArt(row)     
            elif (cnt_rec>1):
                import srcart
                control = [self.tblart,self.codart,self.descriz,self.FndArt]
                win = srcart.create(self,control) 
                win.Centre(wx.BOTH)
                win.ShowModal() #True)
        else: self.UM.SetFocus()

    def SkArt(self, evt):           
        cod=self.codart.GetValue().upper()     
        des=self.descriz.GetValue().upper()   
        costo=self.costo.GetValue()
        prezzo1=self.prezzo1.GetValue()      
        import skart
        control = [cod,des,costo,prezzo1,self.annoc]
        win = skart.create(self,control) 
        win.Centre(wx.BOTH)
        win.ShowModal() #True)
        
    def is_look(self):
        if (self.cntr!="new" and self.cntr!="modi"): return False
        else : return True
        
    def data_reload(self,rec,cntrp):
        self.rec=rec
        #self.tcpart=cntrp
        self.Start(self)


