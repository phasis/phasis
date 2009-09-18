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
import wx.lib.buttons as buttons #import *
from cfg import *
import cfg

def create(parent,cnt):
    return Movmag(parent,cnt)
  
class Movmag(wx.ScrolledWindow):
    def __init__(self, prnt, cnt):
        self.win=wx.ScrolledWindow.__init__(self, parent=prnt, id=-1,size = wx.DefaultSize)
        self.SetScrollbars(1,1,100,100) #####
        self.FitInside()  ######
        
        png = wx.Image((cfg.path_img + "cerca19x19.png"), 
              wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        #wx.Frame.__init__(self, id = wx.NewId(), name = '',
        #      parent = prnt, pos = wx.Point(0, 0), 
        #      style = wx.DEFAULT_FRAME_STYLE  , title = cnt[0])
        #self.SetIcon(wx.Icon(cfg.path_img + "/null.ico", wx.BITMAP_TYPE_ICO))
        #self.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        #self.SetClientSize(wx.Size(600, 425))
        self.ttl = cnt[0]
        self.tbl = "movmag"
        self.tcpart = "C"        
        self.tblart = "articoli"
        self.rec = cnt[2]
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]   
        #self.font = self.GetFont()
        self.color = self.GetBackgroundColour()
        Nid = wx.NewId()
        self.__MDI__ =  wx.GetApp().GetPhasisMdi()
        
        self.font=self.__MDI__.font
        self.SetFont(self.font)
        
        self.CnAz = self.__MDI__.GetConnAZ()
        self.annoc = self.__MDI__.GetAnnoC()
        self.datacon =  self.__MDI__.GetDataC()
        self.dzDatiAzienda =  self.__MDI__.dzDatiAzienda
        
        self.pnl = wx.Panel(id = wx.NewId(), name = '',
              parent = self, pos = wx.Point(0, 0), 
              size = wx.DLG_SZE(self,600/2,420/2), 
              #size = wx.Size(600, 420),
              style = wx.SIMPLE_BORDER | wx.TAB_TRAVERSAL)
        self.pnl.SetFont(self.font)
        
        self.ntbk = wx.Notebook(id = wx.NewId(), name = 'notebook',
              parent = self.pnl, pos = wx.DLG_PNT(self.pnl, 5/2,5/2), 
              #pos = wx.Point(5, 5), 
              #size = wx.Size(cfg.NTBKH,cfg.NTBKV), style = 0)
              size = wx.DLG_SZE(self.pnl,cfg.NTBKHTUTTI/2,cfg.NTBKVTUTTI/2),style = 0)
        self.ntbk.SetFont(self.font)
        
        self.pnl1 = wx.Panel(id = wx.NewId(), name = 'panel1',
              parent = self.ntbk, pos = wx.Point(0, 0))
        self.pnl1.SetFont(self.font)
        
        self.pnl2 = wx.Panel(id = wx.NewId(), name = 'panel2',
              parent = self.ntbk, pos = wx.Point(0, 0))
        self.pnl2.SetFont(self.font)
        
        self.ntbk.AddPage(imageId = -1, page = self.pnl1, 
              select = True, text = _(' Testata')+' (1) ')
        self.ntbk.AddPage(imageId = -1, page = self.pnl2, 
              select = False, text = _(' Corpo')+' (2) ')
        
        #self.pnl.SetFont(self.font)
        #self.pnl1.SetFont(self.font)
        #self.pnl2.SetFont(self.font)
        #self.ntbk.SetFont(self.font)
        
        self.sbox_cf = wx.StaticBox(self.pnl1, Nid, _(" Registrazione "),
              wx.DLG_PNT(self.pnl1, 5,7), wx.DLG_SZE(self.pnl1, 265,30))
        self.lmov = wx.StaticText(self.pnl1, -1, _("Numero :"), 
              wx.DLG_PNT(self.pnl1, 10,22))
        self.anno = wx.ComboBox(self.pnl1, Nid, self.annoc,
              wx.DLG_PNT(self.pnl1, 45,20), wx.DLG_SZE(self.pnl1, 35,-1),[],
              wx.CB_DROPDOWN | wx.CB_SORT )  
        wx.StaticText(self.pnl1, -1, "/", wx.DLG_PNT(self.pnl1, 85,22))
        self.num_mov = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 90,20), 
              wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER) 
        self.cnum_mov = wx.BitmapButton(self.pnl1, -1, png,
              #wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 135,20),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl1, -1, _("Data :"), 
              wx.DLG_PNT(self.pnl1, 160,22))
        self.datamov = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 185,20), 
              wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT)
        self.cdatamov = wx.BitmapButton(self.pnl1, -1, png,
              #wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 240,20),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.vdatamov = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 280, 135), 
              wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT))
        self.sbox_cf = wx.StaticBox(self.pnl1, Nid, _(" Magazzino "),
              wx.DLG_PNT(self.pnl1, 5,40), 
              wx.DLG_SZE(self.pnl1, 265,45))
        self.lCAUMA = wx.StaticText(self.pnl1, Nid, _("Codice causale :"), 
              wx.DLG_PNT(self.pnl1, 15,52))
        self.vCAUMA = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 85,50), 
              wx.DLG_SZE(self.pnl1, 35, cfg.DIMFONTDEFAULT), 
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER )
        self.cCAUMA = wx.BitmapButton(self.pnl1, -1, png,
              #wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 125,50),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dCAUMA = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 140,50), 
              wx.DLG_SZE(self.pnl1, 120, cfg.DIMFONTDEFAULT))
        self.lcod_mag = wx.StaticText(self.pnl1, Nid, _("Codice magazzino :"), 
              wx.DLG_PNT(self.pnl1, 15,67))
        self.cod_mag = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 85,65), 
              wx.DLG_SZE(self.pnl1, 35, cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT )
        self.ccod_mag = wx.BitmapButton(self.pnl1, -1, png,
              #wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 125,65),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dcod_mag = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 140,65), 
              wx.DLG_SZE(self.pnl1, 120, cfg.DIMFONTDEFAULT))        
        wx.StaticText(self.pnl1, -1, _("Contropartita :"), 
              wx.DLG_PNT(self.pnl1, 10,97))
        self.CFM = wx.ComboBox(self.pnl1, Nid,"",
              wx.DLG_PNT(self.pnl1, 65,95), 
              wx.DLG_SZE(self.pnl1, 60,-1),[], wx.CB_DROPDOWN | wx.CB_SORT )
        self.vCFM = wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 275,90))
        self.lcodcf = wx.StaticText(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 135,97))
        self.codcf = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 185, 95), 
              wx.DLG_SZE(self.pnl1, 60,cfg.DIMFONTDEFAULT))
        self.ccodcf = wx.BitmapButton(self.pnl1, -1, png,
              #wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 250,95),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lragsoc1 = wx.StaticText(self.pnl1, -1,
              _("Rag. Sociale1 ( Cognome ) :"),  wx.DLG_PNT(self.pnl1, 12,110))
        self.ragsoc1 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 10,120), 
              wx.DLG_SZE(self.pnl1, 120,cfg.DIMFONTDEFAULT), wx.TE_PROCESS_ENTER)    
        self.cragsoc1 = wx.BitmapButton(self.pnl1, -1, png,
              #wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 135,120),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lragsoc2 = wx.StaticText(self.pnl1, -1,
              _("Rag. Sociale2 ( Nome ) :"), wx.DLG_PNT(self.pnl1, 155,110))
        self.ragsoc2 = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 153, 120), 
              wx.DLG_SZE(self.pnl1, 110,cfg.DIMFONTDEFAULT))          
        self.sbox_cf = wx.StaticBox(self.pnl1, Nid, _(" Documento "),
              wx.DLG_PNT(self.pnl1, 5,135), wx.DLG_SZE(self.pnl1, 265,30))
        self.ldoc = wx.StaticText(self.pnl1, -1, _("Numero :"), 
              wx.DLG_PNT(self.pnl1, 10,147))
        self.num_doc = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 45,145), 
              wx.DLG_SZE(self.pnl1, 40,cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT | wx.TE_PROCESS_ENTER)        
        wx.StaticText(self.pnl1, -1, _("Data :"), 
              wx.DLG_PNT(self.pnl1, 100,147))
        self.data_doc = wx.TextCtrl(self.pnl1, Nid, "",
              wx.DLG_PNT(self.pnl1, 130,145), 
              wx.DLG_SZE(self.pnl1, 50,cfg.DIMFONTDEFAULT),wx.ALIGN_RIGHT)
        self.cdatadoc = wx.BitmapButton(self.pnl1, -1, png,
              #wx.Button(self.pnl1, Nid, "...", 
              wx.DLG_PNT(self.pnl1, 185,145),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.vDIV =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 280,130))
        self.CAMBIO =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 280,130))
        self.campo1 =  wx.TextCtrl(self.pnl1, -1, "", 
              wx.DLG_PNT(self.pnl1, 280,37))        
        self.campo2 =  wx.TextCtrl(self.pnl1, -1, "",
              wx.DLG_PNT(self.pnl1, 280,37))
        self.lc = wx.ListCtrl(self.pnl2, Nid,
              wx.DLG_PNT(self.pnl2, 5,10), 
              wx.DLG_SZE(self.pnl2, 323,95), 
              wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES)           
        self.lcod = wx.StaticText(self.pnl2, -1, _("Codice :"), 
              wx.DLG_PNT(self.pnl2, 5,112))
        self.codart = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 35,110), 
              wx.DLG_SZE(self.pnl2, 60,cfg.DIMFONTDEFAULT))            
        self.ccodart = wx.BitmapButton(self.pnl2, -1, png,
              #wx.Button(self.pnl2, Nid, " ... ", 
              wx.DLG_PNT(self.pnl2, 100,110),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.codbar = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 35,110), 
              wx.DLG_SZE(self.pnl2, 60,cfg.DIMFONTDEFAULT))            
        self.ccodbar = buttons.GenToggleButton(self.pnl2, Nid, "|''|'|", 
              wx.DLG_PNT(self.pnl2, 112,110), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        wx.StaticText(self.pnl2, -1, _("Descrizione :"), 
              wx.DLG_PNT(self.pnl2, 130,112))
        self.descriz = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 180, 110), 
              wx.DLG_SZE(self.pnl2, 130,cfg.DIMFONTDEFAULT),
              wx.TE_PROCESS_ENTER)                     
        self.cdescriz = wx.BitmapButton(self.pnl2, -1, png,
              #wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 315,110),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))       
        wx.StaticText(self.pnl2, -1, _("UM :"),  wx.DLG_PNT(self.pnl2, 5,127))
        self.UM = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 23,125), 
              wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT))
        self.lmis = wx.StaticText(self.pnl2, -1, _("Mis :"), 
              wx.DLG_PNT(self.pnl2, 50,127))
        self.mis = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 70,125), 
              wx.DLG_SZE(self.pnl2, 20,cfg.DIMFONTDEFAULT))                    
        wx.StaticText(self.pnl2, -1, _("Sc % :"), 
              wx.DLG_PNT(self.pnl2, 95,127))
        self.sc1 = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 120,125), 
              wx.DLG_SZE(self.pnl2, 25, cfg.DIMFONTDEFAULT),wx.ALIGN_RIGHT )
        self.lvALIVA = wx.StaticText(self.pnl2, -1, _("Cod. Iva :"), 
              wx.DLG_PNT(self.pnl2, 155,127))
        self.vALIVA = wx.TextCtrl(self.pnl2, Nid, "20",
              wx.DLG_PNT(self.pnl2, 190,125), 
              wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        self.cALIVA = wx.BitmapButton(self.pnl2, -1, png,
              #wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 215,125),
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.dALIVA = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 230,125), 
              wx.DLG_SZE(self.pnl2, 95, cfg.DIMFONTDEFAULT))   
        self.llst = wx.StaticText(self.pnl2, -1, _("Listino :"), 
              wx.DLG_PNT(self.pnl2, 5,142))
        self.lst = wx.TextCtrl(self.pnl2, Nid, "",
              wx.DLG_PNT(self.pnl2, 33,140), 
              wx.DLG_SZE(self.pnl2, 20, cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT )   
        self.clst = wx.BitmapButton(self.pnl2, -1, png,
              #wx.Button(self.pnl2, Nid, "...", 
              wx.DLG_PNT(self.pnl2, 57,140), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeSH,cfg.btnSzeV))
        self.lcosto_un = wx.StaticText(self.pnl2, Nid, _("Costo Un :"), 
              wx.DLG_PNT(self.pnl2, 75,142))
        self.costo_un = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 105,140), 
              wx.DLG_SZE(self.pnl2, 45, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )      
        wx.StaticText(self.pnl2, -1, _("Q.ta` :"), 
              wx.DLG_PNT(self.pnl2, 160,142))
        self.qt = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 175,140), 
              wx.DLG_SZE(self.pnl2, 30, cfg.DIMFONTDEFAULT),
              wx.ALIGN_RIGHT )
        self.ltotriga = wx.StaticText(self.pnl2, -1, _("Valore totale:"), 
              wx.DLG_PNT(self.pnl2, 215,142))
        #self.ltotriga.SetFont(self.font)
        self.totriga = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 262,140), 
              wx.DLG_SZE(self.pnl2, 65, cfg.DIMFONTDEFAULT), wx.ALIGN_RIGHT )
        #self.totriga.SetFont(self.font)
        self.importo = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))     
        self.ltotale = wx.StaticText(self.pnl2, -1, _("Totale :"), 
              wx.DLG_PNT(self.pnl2, 235,162))
        #self.ltotale.SetFont(self.font)
        self.totale = wx.TextCtrl(self.pnl2, Nid, "0,00",
              wx.DLG_PNT(self.pnl2, 262,160), 
              wx.DLG_SZE(self.pnl2, 65, cfg.DIMFONTDEFAULT),wx.ALIGN_RIGHT )
        #self.totale.SetFont(self.font)
        self.sc2 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.sc3 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))        
        self.prezzo2 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.prezzo1 = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.nriga = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.rigadoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 275,37))
        self.vUM = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 5,37))                    
        self.vMERCE = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 5,52))                                                         
        self.codmerc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))   
        self.costo_ag = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))    
        self.annodoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))          
        self.tipodoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.datadoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.numdoc = wx.TextCtrl(self.pnl2, -1, "", 
              wx.DLG_PNT(self.pnl2, 285,137))  
        self.ok = wx.Button(self.pnl1, Nid, cfg.vcok, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))      
        self.new = wx.Button(self.pnl1, Nid, cfg.vcnew, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))      
        self.oktestata = wx.Button(self.pnl1, Nid, cfg.vcconf, 
              wx.DLG_PNT(self.pnl, 275,30), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))              
        self.inte = wx.Button(self.pnl1, Nid, cfg.vcint, 
              wx.DLG_PNT(self.pnl, 275,45), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.canc = wx.Button(self.pnl1, Nid, cfg.vccanc, 
              wx.DLG_PNT(self.pnl, 275,45), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.modi = wx.Button(self.pnl1, Nid, cfg.vcmodi, 
              wx.DLG_PNT(self.pnl, 275,60), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.dele = wx.Button(self.pnl1, Nid, cfg.vcdele, 
              wx.DLG_PNT(self.pnl, 275,60),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.stampa = wx.Button(self.pnl1, Nid, cfg.vcstampa, 
              wx.DLG_PNT(self.pnl, 275,75),
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.newr = wx.Button(self.pnl2, Nid, cfg.vcnewr, 
              wx.DLG_PNT(self.pnl2, 5,160),
              wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))      
        self.okart = wx.Button(self.pnl2, Nid, cfg.vcokr, 
              wx.DLG_PNT(self.pnl2, 67,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))
        self.modir = wx.Button(self.pnl2, Nid, cfg.vcmodir,
              wx.DLG_PNT(self.pnl2, 67,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeL1H,cfg.btnSzeV))
        self.intr = wx.Button(self.pnl2, Nid, cfg.vcintr, 
              wx.DLG_PNT(self.pnl2, 130,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        self.delr = wx.Button(self.pnl2, Nid, cfg.vcdeler, 
              wx.DLG_PNT(self.pnl2, 182,160), 
              wx.DLG_SZE(self.pnl,cfg.btnSzeLH,cfg.btnSzeV))
        #self.SetFont(self.font)
        
        for x in self.pnl.GetChildren(): x.SetFont(self.font)
        for x in self.pnl1.GetChildren(): x.SetFont(self.font)
        for x in self.pnl2.GetChildren(): x.SetFont(self.font)

        
        #box_sizer = wx.BoxSizer(wx.VERTICAL)
       	#box_sizer.Add(self.pnl, 0, wx.EXPAND|wx.ALL,0)
        #self.SetAutoLayout(1)
        #self.SetSizer(box_sizer)
        #box_sizer.Fit(self)
        
        box = wx.GridSizer(1, 1)
        box.Add(self.pnl, 0, wx.ALIGN_CENTER|wx.ALL,10)           
        self.SetSizer(box)
        box.Fit(self)

        self.delr.Bind(wx.EVT_BUTTON, self.DelRow)
        self.dele.Bind(wx.EVT_BUTTON, self.CntrDele)        
        self.oktestata.Bind(wx.EVT_BUTTON, self.OkTestata)
        self.canc.Bind(wx.EVT_BUTTON, self.Close)  
        self.okart.Bind(wx.EVT_BUTTON, self.OkRow)
        self.modi.Bind(wx.EVT_BUTTON, self.Modi)
        self.modir.Bind(wx.EVT_BUTTON, self.ModiRow)
        self.inte.Bind(wx.EVT_BUTTON, self.IntTestata)
        self.intr.Bind(wx.EVT_BUTTON, self.IntRow)
        self.newr.Bind(wx.EVT_BUTTON, self.NewRow)
        self.new.Bind(wx.EVT_BUTTON, self.New)
        self.ok.Bind(wx.EVT_BUTTON, self.Save)
        self.stampa.Bind(wx.EVT_BUTTON, self.Stampa)
        self.lc.Bind(wx.EVT_LEFT_DCLICK, self.ModiRow)
        self.lc.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct) #occhio forse self.lc
        # < diegom 
        # commentato perche richiama l'evento 2 volte ad ogni click su riga
        #self.lc.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlct) #occhio forse self.lc
        # > diegom  
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) #occhio forse self.lc


        #self.pnl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.LstSlct) #occhio forse self.lc
        #self.pnl.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.LstSlct) #occhio forse self.lc
        #self.pnl.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.LstAct) #occhio forse self.lc
        self.qt.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        self.sc1.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        self.costo_un.Bind(wx.EVT_TEXT_ENTER, self.OkRow)
        self.cragsoc1.Bind(wx.EVT_BUTTON, self.FndAnag)
        self.ccodart.Bind(wx.EVT_BUTTON, self.FndCodArt)
        self.cCAUMA.Bind(wx.EVT_BUTTON, self.FndTABGEN)
        self.cALIVA.Bind(wx.EVT_BUTTON, self.FndSelALIVA)
        self.vALIVA.Bind(wx.EVT_TEXT_ENTER, self.FndSelALIVA)
        self.ccodbar.Bind(wx.EVT_BUTTON, self.SelCodBar)
        self.codbar.Bind(wx.EVT_TEXT_ENTER, self.FndCodBar)
        self.codart.Bind(wx.EVT_TEXT_ENTER, self.FndCodArt)
        self.ragsoc1.Bind(wx.EVT_TEXT_ENTER, self.FndAnag)
        self.ragsoc1.Bind(wx.EVT_CHAR, self.EvtChar)
        self.cnum_mov.Bind(wx.EVT_BUTTON, self.FndMov)
        self.num_mov.Bind(wx.EVT_TEXT_ENTER, self.FndMov)
        self.datamov.Bind(wx.EVT_TEXT_ENTER, self.CntData)
        self.vCAUMA.Bind(wx.EVT_TEXT_ENTER, self.FndTABGEN)
        self.descriz.Bind(wx.EVT_KILL_FOCUS, self.FndCodArt)
        #self.descriz.Bind(wx.EVT_KILL_FOCUS, self.KillFcs_des)
        self.num_doc.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_num_doc)
        self.data_doc.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_data_doc)      
        self.num_mov.Bind(wx.EVT_CHAR, self.EvtChar)
        self.CFM.Bind(wx.EVT_TEXT_ENTER, self.KillFcs_CFM)        
        self.Bind(wx.EVT_CLOSE, self.Close)
        self.CFM.Bind(wx.EVT_COMBOBOX, self.SelCFM)
        self.Start(self)
        
    def Start(self, evt): 
        self.totriga.Enable(False)
        self.CAMBIO.Enable(False)
        self.rigadoc.Enable(False)
        self.CAMBIO.Show(False)
        self.rigadoc.Show(False)
        self.anno.Enable(False)
        self.vdatamov.Show(False)
        self.vCAUMA.Enable(False)
        self.dCAUMA.Enable(False)
        self.cCAUMA.Enable(False)
        self.cod_mag.Enable(False)
        self.dcod_mag.Enable(False)
        self.ccod_mag.Enable(False)
        self.num_doc.Enable(False)
        self.data_doc.Enable(False)
        self.cdatadoc.Enable(False)        
        self.vCFM.Show(False)
        self.CFM.Enable(False)
        self.codcf.Enable(False)
        self.ccodcf.Enable(False)        
        self.ragsoc1.Enable(False)
        self.cragsoc1.Enable(False)
        self.ragsoc2.Enable(False)
        self.vDIV.Enable(False)
        self.vDIV.Show(False)
        self.vDIV.SetValue("EU")
        self.lst.SetValue("1")
        self.lst.Enable(False)
        self.clst.Enable(False)
        self.vCAUMA.SetValue('')
        self.dCAUMA.SetValue('')        
        self.cod_mag.SetValue('01')
        self.dcod_mag.SetValue(_('Magazzino Centrale'))
        self.campo1.Enable(False)
        self.campo1.Show(False)
        self.campo1.SetValue("")
        self.campo2.Enable(False)
        self.campo2.Show(False)
        self.campo2.SetValue("")
        self.sc2.Show(False)
        self.sc3.Show(False)
        self.nriga.Show(False)
        self.vUM.Show(False)
        self.vMERCE.Show(False)
        self.prezzo1.Show(False)
        self.prezzo2.Show(False)
        self.importo.Enable(False)
        self.importo.Show(False)        
        self.DelAnagTxt(self)
        self.DelArtTxt(self)
        self.OffAnagTxt(self)
        self.OffArtTxt(self)
        self.data = self.datacon 
        self.datamov.SetValue(self.data)
        self.data_doc.SetValue(self.data)
        self.datamov.Enable(True)
        self.num_mov.Enable(True)
        self.num_mov.SetFocus()
        self.cnum_mov.Enable(True)
        self.codmerc.Enable(False)
        self.qt.Enable(False)
        self.costo_ag.Enable(False)
        self.annodoc.Enable(False)        
        self.tipodoc.Enable(False)
        self.datadoc.Enable(False)
        self.numdoc.Enable(False)
        self.codmerc.Show(False)
        self.costo_ag.Show(False)
        self.annodoc.Show(False)        
        self.tipodoc.Show(False)
        self.datadoc.Show(False)
        self.numdoc.Show(False)
        self.lc.ClearAll()
        self.lc.InsertColumn(0, _("Codice"))
        self.lc.InsertColumn(1, _("Descrizione"))
        self.lc.InsertColumn(2, _("Q.ta`"))
        self.lc.InsertColumn(3, _("Prezzo"))
        self.lc.InsertColumn(4, _("Sc%"))
        self.lc.InsertColumn(5, _("Importo"))
        self.lc.InsertColumn(6, _("Iva"))
        self.lc.InsertColumn(7, _("UM"))
        self.lc.InsertColumn(8, _("Mis"))
        self.lc.InsertColumn(9, _("n riga"))
        self.lc.InsertColumn(10, "")
        self.lc.InsertColumn(11, "")
        self.lc.InsertColumn(12, "")
        self.lc.InsertColumn(13, "")
        self.lc.InsertColumn(14, "")
        self.lc.InsertColumn(15, "")
        self.lc.InsertColumn(16, "")
        self.lc.InsertColumn(17, "")
        self.lc.InsertColumn(18, "")
        self.lc.InsertColumn(19, "")
        self.lc.InsertColumn(20, "")
        self.lc.InsertColumn(21, "")
        self.lc.InsertColumn(22, "")
        self.lc.InsertColumn(23, "")
        self.lc.InsertColumn(24, "")
        self.lc.SetColumnWidth(0, wx.DLG_SZE(self.pnl,  60,-1).width)
        self.lc.SetColumnWidth(1, wx.DLG_SZE(self.pnl, 100,-1).width)
        self.lc.SetColumnWidth(2, wx.DLG_SZE(self.pnl, 27,-1).width)
        self.lc.SetColumnWidth(3, wx.DLG_SZE(self.pnl, 50,-1).width)
        self.lc.SetColumnWidth(4, wx.DLG_SZE(self.pnl,  25,-1).width)
        self.lc.SetColumnWidth(5, wx.DLG_SZE(self.pnl,  50,-1).width)
        self.lc.SetColumnWidth(6, wx.DLG_SZE(self.pnl,  25,-1).width)
        self.lc.SetColumnWidth(7, wx.DLG_SZE(self.pnl, 20,-1).width)
        self.lc.SetColumnWidth(8, wx.DLG_SZE(self.pnl, 20,-1).width)
        self.lc.SetColumnWidth(9, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(10, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(11, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(12, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(13, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(14, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(15, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(16, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(17, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(18, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(19, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(20, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(21, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(22, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(23, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.SetColumnWidth(24, wx.DLG_SZE(self.pnl, 0,-1).width)
        self.lc.Enable(False)
        self.stampa.Enable(True)
        self.ok.Show(False)
        self.oktestata.Show(False)
        self.canc.Show(True)
        self.new.Enable(True)
        self.new.Show(True)
        self.modi.Show(True)
        self.modi.Enable(False)
        self.dele.Show(False)
        self.dele.Enable(False)        
        self.inte.Show(False)
        self.newr.Enable(False)
        self.okart.Enable(False)
        self.modir.Enable(False)
        self.intr.Enable(False)
        self.delr.Enable(False)
        self.ccodart.Enable(False)      
        self.lcodcf.SetLabel(_(" Cod. Cliente :"))
        if self.ccodbar.GetValue()==0:
            self.codart.Show(True)
            self.codbar.Show(False)            
        else:
            self.codart.Show(False) 
            self.codbar.Show(True)
        self.UM.SetValue(_("PZ"))
        self.vALIVA.SetValue("20")
        self.dALIVA.SetValue(_("Aliquota 20%"))
        self.sCAUMA = 'C'
        if (self.tcpart=="C"):self.lcodcf.SetLabel(_(" Cod. Cliente :"))
        self.vCFM.SetValue("C")
        self.sCFM = ""
        self.SelCOMBO(self)
        self.cntr = ""
        self.cntr_row = ""
        self.row = 0
        if (self.rec!=""):
            self.num_mov.SetValue(self.rec)
	self.ntbk.SetFocus() 
	self.ntbk.SetSelection(0)
        
    def SelCodBar(self, evt):
        if self.ccodbar.GetValue()==0 :
            self.ccodbar.SetToggle(False)
            self.codart.Show(True)
            self.codbar.Show(False)
            self.lcod.SetLabel(_("Codice:"))
            self.codart.SetFocus()
            self.codbar.SetValue('')
        else:
            self.ccodbar.SetToggle(True)
            self.codart.Show(False)
            self.codbar.Show(True)
            self.lcod.SetLabel(_("BarCod:"))
            self.codbar.SetFocus()
            self.codart.SetValue('')

    def FndTABGEN(self, evt):
        val = self.vCAUMA.GetValue()
        cod =  "CAUMA"
        cnt_rec = 0
        sql = """ select * from tabgen 
                  where cod = "%s" and valore like "%s" """
        valueSql = cod,"%" + val + "%"
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            print "FndTABGEN Error %s" % (msg)
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.dCAUMA.SetValue(row[2])
            self.CFM.SetFocus()
        elif (cnt_rec>1):
            try:
	        import srctabg
            except :
	        pass
            try:
                import base.srctabg
            except :
                pass
            control = ['Ricerca Causale',self.vCAUMA,self.dCAUMA,self.FndTABGEN,'CAUMA']     
            win = srctabg.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

    def FndALIVA(self, evt):
        val = self.vALIVA.GetValue()
        cod =  "ALIVA"
        cnt_rec = 0
        sql = """ select * from tabgen 
                  where cod = "%s" and valore like "%s" """
        valueSql = cod,"%" + val + "%"
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","FndALIVA Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.dALIVA.SetValue(row[2])
            self.qt.SetFocus()
        elif (cnt_rec>1):
            try:
	        import srctabg
            except :
	        pass
            try:
                import base.srctabg
            except :
                pass
            control = ['Ricerca Cod. IVA',self.vALIVA,self.dALIVA,self.FndSelALIVA,'ALIVA']     
            win = srctabg.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)

    def FndSelALIVA(self, evt):
        val = self.vALIVA.GetValue()
        cod =  "ALIVA"
        cnt_rec = 0
        sql = """ select * from tabgen 
                  where cod = "%s" and valore = "%s" """
        valueSql = cod, val
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","FndSelALIVA Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==1 and cnt_rec<2):
            self.dALIVA.SetValue(row[2])
            self.qt.SetFocus()
        else:self.FndALIVA(self)

    def IntTestata(self, evt):
        if(self.lc.GetItemCount()!=0 or self.codcf.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgint, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
            if dlg.ShowModal()==wx.ID_YES:
                self.rec = ""
                self.Start(self)
            else:
                dlg.Destroy()
        else:
            self.rec = ""
            self.Start(self)

    def NewTxt(self, evt):
        self.OnAnagTxt(self)
        self.num_mov.Enable(False)
        self.cnum_mov.Enable(False)
        self.datamov.Enable(True)
        self.datamov.SetFocus()
        self.new.Show(False)
        self.ok.Show(False)
        self.oktestata.Show(True)
        self.canc.Show(False)
        self.inte.Show(True)
        self.modi.Enable(False)

    def ModiTxt(self, evt):
        self.OnAnagTxt(self)
        self.cntr = "modi"       
        self.num_mov.Enable(False)
        self.cnum_mov.Enable(False)
        self.datamov.Enable(True)
        self.datamov.SetFocus()
        self.modi.Enable(False)
        self.modi.Show(False)
        self.dele.Show(True)
        self.new.Show(False)
        self.oktestata.Show(True)
     

    def KillFcs_num_doc(self, evt):  
        self.data_doc.SetFocus()
        
    def KillFcs_data_doc(self, evt):  
        self.oktestata.SetFocus()
        
    def KillFcs_CFM(self, evt):  
        if self.vCFM.GetValue()=="M" :self.num_doc.SetFocus()
        else: self.ragsoc1.SetFocus()
    
    def CntvsData(self, evt):
        if (self.cntr=="new" or self.cntr=="modi"):
            cnt_gma = 0

            if vsdata != "":
                gma = vsdata.split('/')
                try:
                    if (gma[0].isdigit()!= True):
                        self.Message(cfg.msgdatano ,self.ttl)
                    elif (gma[1].isdigit()!= True):
                        self.Message(cfg.msgdatano ,self.ttl)
                    elif (gma[2].isdigit()!= True):
                        self.Message(cfg.msgdatano ,self.ttl)
                except:
                    self.Message(cfg.msgdatano ,self.ttl)
                
                if len(gma)==3:
                    gg = int(gma[0])
                    mm = int(gma[1])
                    aa = int(gma[2])
                    if gg > 0 and gg < 31:
                        cnt_gma+=1
                        if mm>=0 and mm<=12:
                            cnt_gma+=1
                            if aa<=int(self.annoc) :
                                cnt_gma+=1
                    if cnt_gma!=3: self.Message(cfg.msgdatano ,self.ttl)
                    if cnt_gma==3: self.ragsoc1.SetFocus()
            else:self.ragsoc1.SetFocus()

    def CntData(self, evt):
        if (self.cntr=="new" or self.cntr=="modi"):    
            datamov = self.datamov.GetValue().strip()
            cnt_gma = 0
            gma = datamov.split('/')
            try:
                if (gma[0].isdigit()!= True):
                    self.Message(cfg.msgdatano ,self.ttl)
                elif (gma[1].isdigit()!= True):
                    self.Message(cfg.msgdatano ,self.ttl)
                elif (gma[2].isdigit()!= True):
                    self.Message(cfg.msgdatano ,self.ttl)
            except:
                self.Message(cfg.msgdatano ,self.ttl)
            if len(gma)==3:
                gg = int(gma[0])
                mm = int(gma[1])
                aa = int(gma[2])
                if gg > 0 and gg<=31:
                    cnt_gma+=1
                    if mm>=0 and mm<=12:
                        cnt_gma+=1
                        if aa==int(self.annoc):
                            cnt_gma+=1
                            vdatamov = self.vdatamov.GetValue()

                            vgma  = vdatamov.split('/')
                            vgg = int(vgma[0])
                            vmm = int(vgma[1])
                            vaa = int(vgma[2])
                            vdata  = int(vgma[2] + vgma[1] + vgma[0])
                            data = int(gma[2] + gma[1] + gma[0])
                            self.vCAUMA.SetFocus()

                            if data < vdata :
                                dlg = wx.MessageDialog(self,cfg.msgdatault ,self.ttl, 
                                      wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
                                if dlg.ShowModal()==wx.ID_YES:
                                    self.vdatamov.SetValue(self.datamov.GetValue())
                                    self.datamov.Enable(False)
                                    dlg.Destroy()
                                else:
                                    self.datamov.SetFocus()
                                    dlg.Destroy()
                            else:
                                self.vdatamov.SetValue(self.datamov.GetValue())
                                self.datamov.Enable(False)
                if cnt_gma==2 and aa <> int(self.annoc):
                    self.Message(cfg.msgdataes + self.annoc,self.ttl)            
                elif cnt_gma!=3 : self.Message(cfg.msgdatano ,self.ttl)
           
    def EvtChar(self, evt):
        evt_char = evt.GetKeyCode()
        if (evt_char==27 and self.cntr==""):self.canc.SetFocus()
        if (evt_char==27 and self.cntr!=""):self.inte.SetFocus()
        evt.Skip()
        
    def OffAnagTxt(self, evt):
        self.CFM.Enable(False)
        self.vCAUMA.Enable(False)
        self.cCAUMA.Enable(False)
        self.num_mov.Enable(False)
        self.cnum_mov.Enable(False)
        self.datamov.Enable(False)
        self.ragsoc1.Enable(False)
        self.cragsoc1.Enable(False)
        self.num_doc.Enable(False)
        self.data_doc.Enable(False)
       
    def OnAnagTxt(self ,evt):
        self.CFM.Enable(True)
        self.cCAUMA.Enable(True)
        self.vCAUMA.Enable(True)
        self.cCAUMA.Enable(True)
        self.ragsoc1.Enable(True)
        self.cragsoc1.Enable(True)
        self.num_doc.Enable(True)
        self.data_doc.Enable(True)

    def DelAnagTxt(self, evt):
        self.num_mov.SetValue('')
        self.vdatamov.SetValue('')
        self.datamov.SetValue('')
        self.codcf.SetValue('')
        self.ragsoc1.SetValue('')
        self.ragsoc2.SetValue('')
        self.sc2.SetValue('0,00')
        self.vALIVA.SetValue("20")
        self.dALIVA.SetValue(_("Aliquota 20%"))
        self.costo_ag.SetValue('0,00')
        self.totale.SetValue('0,00')
        self.totriga.SetValue('0,00')
        self.vCAUMA.SetValue('')
        self.dCAUMA.SetValue('')
        self.num_doc.SetValue('')
        self.data_doc.SetValue('')
        
    def SelCOMBO(self, evt):
        vCFM = self.vCFM.GetValue()
        self.CFM.Clear()
        for item in cfg.vcCFM:
            if (item[:1]==vCFM):self.sCFM = item  
            self.CFM.Append(item, item[:1])      
        cntCFM = 0
        cntCFM = self.CFM.FindString(self.sCFM)
        self.CFM.Select(cntCFM)

    def SelCFM(self, evt):
        self.Sel(evt)
        self.vCFM.SetValue(self.cb_val)
        if self.vCFM.GetValue()=="F": self.lcodcf.SetLabel(_(" Cod. Fornit. :"))
        if self.vCFM.GetValue()=="C": self.lcodcf.SetLabel(_(" Cod. Cliente :"))
        if self.vCFM.GetValue()=="M":
            self.lcodcf.SetLabel(_(" Cod. Magaz.  :"))
            self.lragsoc1.SetLabel(_(" Magazzino :"))
            self.ragsoc1.SetValue(_('Magazzino Centrale'))
            self.datadoc.SetValue('')
            self.codcf.SetValue('01')
            self.ragsoc1.Enable(False)
            self.lragsoc2.Show(False)
            self.ragsoc2.Show(False)
            self.cragsoc1.Show(False)
        else:
            self.lragsoc2.Show(True)
            self.ragsoc2.Show(True)
            self.cragsoc1.Show(True)
            self.lragsoc1.SetLabel(_("Rag. Sociale1 ( Cognome ) :"))
            self.ragsoc1.SetValue('')
            self.codcf.SetValue('')
            self.ragsoc1.Enable(True)

    def Sel(self, evt):
        cb = evt.GetEventObject()
        self.cb_val = cb.GetClientData(cb.GetSelection())
        self.cb_str =  evt.GetString()
        evt.Skip()
        
    def SetFcs(self, evt):
        evt.Skip()

    def KillFcs_des(self, evt):
        if self.codart.GetValue()=='':
            self.descriz.SetValue(self.descriz.GetValue().upper())  
        
    def getColTxt(self, index, col):
        item = self.lc.GetItem(index, col)
        return item.GetText()

    def LstSlct(self, evt):      
        self.currentItem = evt.m_itemIndex
        self.codart.SetValue(self.lc.GetItemText(self.currentItem))
        self.descriz.SetValue(self.getColTxt(self.currentItem, 1))
        self.qt.SetValue(self.getColTxt(self.currentItem, 2))
        self.costo_un.SetValue(self.getColTxt(self.currentItem, 3))
        self.sc1.SetValue(self.getColTxt(self.currentItem, 4))
        self.importo.SetValue(self.getColTxt(self.currentItem, 5))
        self.totriga.SetValue(self.getColTxt(self.currentItem, 5))
        self.vALIVA.SetValue(self.getColTxt(self.currentItem, 6))
        self.UM.SetValue(self.getColTxt(self.currentItem, 7))
        self.mis.SetValue(self.getColTxt(self.currentItem, 8))
        self.nriga.SetValue(self.getColTxt(self.currentItem, 9))
        self.codbar.SetValue(self.getColTxt(self.currentItem, 10))
        self.codmerc.SetValue(self.getColTxt(self.currentItem, 11))
        self.costo_ag.SetValue(self.getColTxt(self.currentItem, 12))
        self.sc2.SetValue(self.getColTxt(self.currentItem, 13))
        self.sc3.SetValue(self.getColTxt(self.currentItem, 14))
        self.lst.SetValue(self.getColTxt(self.currentItem, 15))
        self.vDIV.SetValue(self.getColTxt(self.currentItem, 16))
        self.CAMBIO.SetValue(self.getColTxt(self.currentItem, 17))
        self.rigadoc.SetValue(self.getColTxt(self.currentItem, 18))
        self.annodoc.SetValue(self.getColTxt(self.currentItem, 19))
        self.tipodoc.SetValue(self.getColTxt(self.currentItem, 20))
        self.datadoc.SetValue(self.getColTxt(self.currentItem, 21))
        self.numdoc.SetValue(self.getColTxt(self.currentItem, 22))
        self.campo1.SetValue(self.getColTxt(self.currentItem, 23))
        self.campo2.SetValue(self.getColTxt(self.currentItem, 24))
        self.row = self.currentItem
        self.SelRow(self)

    def LstAct(self, evt):
        self.SelRow(self)
        self.currentItem = evt.m_itemIndex

    def FndSelAnag(self, evt):
        row = evt
        self.codcf.SetValue(str(row[1]))
        self.ragsoc1.SetValue(str(row[3]).title())
        self.ragsoc2.SetValue(str(row[4]).title())
        self.__MDI__.CnvVM(row[30])
        if(self.__MDI__.val==""):self.__MDI__.val = "0"
        self.sc1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVM(row[31])
        self.sc2.SetValue(self.__MDI__.val)
        self.num_doc.SetFocus()
           
    def FndSelMov(self, evt):
        row = evt
        self.anno.SetValue(str(row[0]))
        self.num_mov.SetValue(str(row[1]))
        self.vdatamov.SetValue(str(row[2]))
        self.datamov.SetValue(str(row[2]))
        self.vCAUMA.SetValue(str(row[3]))
        self.cod_mag.SetValue(str(row[4]))
        self.vCFM.SetValue(str(row[5]))
        self.codcf.SetValue(str(row[6]))
        self.num_doc.SetValue(str(row[28]))
        self.data_doc.SetValue(str(row[27]))
        self.FndCodCF(self)
        self.FndTABGEN(self)
        self.SelCOMBO(self)
        self.FndMovCorpo(self)
        self.num_mov.Enable(False)
        self.datamov.Enable(False)
        self.new.Enable(False)
        self.canc.Show(False)
        self.inte.Show(True)        
        self.modi.Enable(True)
        self.modi.SetFocus()
        
    def FndMov(self, evt):
        num_mov = self.num_mov.GetValue()
        if num_mov=="" :
            self.Message(cfg.msgass + " --> " + str(self.tbl), self.ttl)
        else:
            cnt_rec = 0       
            anno = self.anno.GetValue()
            vCAUMA = self.vCAUMA.GetValue()
            sql = """ select * from movmag 
                      where num_mov = "%s" and anno = "%s" """
            valueSql = int(num_mov),anno
            try:
                cr = self.CnAz.cursor ()
                cr.execute(sql % valueSql)
                rows = cr.fetchall()
                for row in rows:
                    cnt_rec+=1
            except StandardError, msg:
                self.__MDI__.MsgErr("movmag","FndMov Error %s " % (msg))
            self.CnAz.commit()
            if (cnt_rec==0):self.Message(cfg.msgass + " --> " + self.tbl,self.ttl)
            else : self.FndSelMov(row)  
                                        
    def FndMovCorpo(self, evt):
        rowlc = 0
        cnt_rec = 0
        num_mov = self.num_mov.GetValue()
        anno = self.anno.GetValue()
        sql = """ select * from movmag
                  where num_mov = "%s" and anno = "%s"
                  order by num_rig desc """
        valueSql = int(num_mov), anno
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows: 
                for rowlc in range(1):
                    row_lc = self.lc.GetItemCount()  
                    codart = row[8]
                    #if codart=='' or codart==None or codart==Null: codart = ''
                    if codart=='' or codart==None: codart = ''
                    self.__MDI__.CnvVMQT(row[14])
                    qt = self.__MDI__.val
                    self.__MDI__.CnvVMPZ(row[15])
                    costo_un = self.__MDI__.val
                    self.__MDI__.CnvVM(row[21])
                    sc1 = self.__MDI__.val
                    if (sc1==""):sc1 = "0,0"
                    self.__MDI__.CnvVM(row[22])
                    sc2 = self.__MDI__.val
                    self.__MDI__.CnvVM(row[23])
                    sc3 = self.__MDI__.val
                    self.__MDI__.CnvVM(row[17])
                    tot_riga = self.__MDI__.val
                    self.lc.InsertStringItem(rowlc, codart)
                    self.lc.SetStringItem(rowlc, 1, row[11])
                    self.lc.SetStringItem(rowlc, 2, qt)
                    self.lc.SetStringItem(rowlc, 3, costo_un)
                    self.lc.SetStringItem(rowlc, 4, sc1)
                    self.lc.SetStringItem(rowlc, 5, tot_riga)
                    self.lc.SetStringItem(rowlc, 6, row[18])
                    self.lc.SetStringItem(rowlc, 7, row[12])        
                    self.lc.SetStringItem(rowlc, 8, str(row[13]))
                    self.lc.SetStringItem(rowlc, 9, str(row[7]))
                    self.lc.SetStringItem(rowlc, 10, str(row[9]))
                    self.lc.SetStringItem(rowlc, 11, str(row[10]))
                    self.lc.SetStringItem(rowlc, 12, str(row[16]))
                    self.lc.SetStringItem(rowlc, 13, sc2)
                    self.lc.SetStringItem(rowlc, 14, sc3)                    
                    self.lc.SetStringItem(rowlc, 15, str(row[24]))
                    self.lc.SetStringItem(rowlc, 16, str(row[19]))        
                    self.lc.SetStringItem(rowlc, 17, str(row[20]))
                    self.lc.SetStringItem(rowlc, 18, str(row[29]))
                    self.lc.SetStringItem(rowlc, 19, str(row[25]))
                    self.lc.SetStringItem(rowlc, 20, str(row[26]))
                    self.lc.SetStringItem(rowlc, 21, str(row[27]))
                    self.lc.SetStringItem(rowlc, 22, str(row[28]))
                    self.lc.SetStringItem(rowlc, 23, str(row[30]))
                    self.lc.SetStringItem(rowlc, 24, str(row[31]))
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","FndMovCorpo Error %s " % (msg))
        self.CnAz.commit()
        self.CalcTotale(self)
       
    def Modi(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgmodi_doc, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.ModiTxt(self)
            dlg.Destroy()
        else:
            self.cntr = ""
            dlg.Destroy()

    def CntrDele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgnodele_doc, self.ttl,
                        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_EXCLAMATION)
        if dlg.ShowModal()==wx.ID_YES:
            self.Dele(self)
        else:
            self.cntr = ""
            dlg.Destroy()
            
    def Dele(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdele_doc,self.ttl,
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.cntr = ""
            vCAUMA = self.vCAUMA.GetValue()
            vanno = self.anno.GetValue()
            vnum_mov = self.num_mov.GetValue()
            valueSql = vCAUMA,vanno,int(vnum_mov)
            try:
                cr = self.CnAz.cursor()
                sql = """ delete from movmag 
                          where cauma = "%s" anno = "%s" num_mov = "%" """                    
                cr.execute(sql % valueSql)
            except StandardError, msg:
                self.__MDI__.MsgErr("movmag","Dele Error %s " % (msg))
            self.CnAz.commit()
            self.Start(self)
            dlg.Destroy()
        else:
            self.cntr = ""
            dlg.Destroy()

    def OkTestata(self, evt):
        if (self.codcf.GetValue()==""):
            self.Message(cfg.msgnocod,self.ttl)
            self.codcf.SetFocus()
        else:
            self.ragsoc1.Enable(False)
            self.cragsoc1.Enable(False)
            self.lc.SetBackgroundColour(wx.Colour(255, 255, 255))
            self.lc.Enable(True)
            if (self.cntr=="new" or self.cntr=="modi"):
                self.OffAnagTxt(self)
                self.oktestata.Show(False)
                self.new.Show(False)
                self.ok.Show(True)
                self.ok.Enable(True)
                self.ntbk.SetSelection(1)
                self.newr.Enable(True)
                self.newr.SetFocus()

    def FndCodCF(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue().upper()
        cod = self.codcf.GetValue()
	if cod=='' or cod=='None' or cod=='Null': cod = '0'
        self.tcpart = str(self.vCFM.GetValue())
        sql = """ select * from anag where cod = "%s" and t_cpart = "%s" """
        valueSql = int(cod), self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            #print  " FndCodCF %s " % rows
            for row in rows:
                cnt_rec+=1  
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","FndCodCF Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==0 and self.tcpart!="M"):self.Message(cfg.msgdatono,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)
        if  self.tcpart=="F": self.lcodcf.SetLabel(_(" Cod. Fornit. :"))
        if  self.tcpart=="C": self.lcodcf.SetLabel(_(" Cod. Cliente :"))
        if self.tcpart=="M":
            self.lcodcf.SetLabel(_(" Cod. Magaz.  :"))
            self.lragsoc1.SetLabel(_(" Magazzino :"))
            self.ragsoc1.SetValue(_('Magazzino Centrale'))
            self.datadoc.SetValue('')
            self.codcf.SetValue('01')
            self.ragsoc1.Enable(False)
            self.lragsoc2.Show(False)
            self.ragsoc2.Show(False)
            self.cragsoc1.Show(False)
        else:
            self.lragsoc2.Show(True)
            self.ragsoc2.Show(True)
            self.cragsoc1.Show(True)
            self.lragsoc1.SetLabel(_("Rag. Sociale1 ( Cognome ) :"))
        
    def FndAnag(self, evt):
        cnt_rec = 0
        val = self.ragsoc1.GetValue()
        cod = self.codcf.GetValue()
        self.tcpart = self.vCFM.GetValue()
        sql = """ select * from anag 
                       where rag_soc1 like "%s" and t_cpart = "%s" """
        valueSql = "%" + val.title() + "%", self.tcpart
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)           
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","FndAnag Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelAnag(row)
        elif (cnt_rec>1):
            try:
	        import srcanag
            except :
	        pass
            try:
                import base.srcanag
            except :
                pass
            control = [self.tcpart,self.codcf,self.ragsoc1,self.FndCodCF]               
            win = srcanag.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
        else:
            self.num_doc.SetFocus()

    def OffArtTxt(self, evt):
        self.codart.Enable(False)
        self.codbar.Enable(False)
        self.ccodart.Enable(False)
        self.ccodbar.Enable(False)
        self.descriz.Enable(False)
        self.cdescriz.Enable(False)
        self.UM.Enable(False)
        self.mis.Enable(False)
        self.qt.Enable(False)
        self.costo_un.Enable(False)
        self.sc1.Enable(False)
        self.vALIVA.Enable(False)
        self.cALIVA.Enable(False)
        self.dALIVA.Enable(False)
        self.totale.Enable(False)
        self.UM.Enable(False)
        self.vMERCE.Enable(False)
        self.modir.Enable(False)
        self.okart.Enable(False)
        self.modir.Show(True)
        self.okart.Show(False)
        self.intr.Enable(False)
        self.delr.Enable(False)
        self.newr.Enable(True)
        self.newr.SetFocus()

    def OffArtTxtAll(self, evt):
        self.lc.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.lc.Enable(True)        
        self.codart.Enable(False)
        self.ccodart.Enable(False)
        self.codbar.Enable(False)
        self.ccodbar.Enable(False)
        self.descriz.Enable(False)
        self.cdescriz.Enable(False)
        self.UM.Enable(False)
        self.nriga.Enable(False)
        self.totale.Enable(False)
        self.UM.Enable(False)
        self.vMERCE.Enable(False)
        
    def OnArtTxt(self, evt):
        self.lc.SetBackgroundColour(self.color)
        self.lc.Enable(False)
        self.codart.Enable(True)
        self.ccodart.Enable(True)
        self.codbar.Enable(True)
        self.ccodbar.Enable(True)
        self.descriz.Enable(True)
        self.cdescriz.Enable(True)
        self.UM.Enable(True)
        self.mis.Enable(True)
        self.costo_un.Enable(True)
        self.sc1.Enable(True)
        self.qt.Enable(True)
        self.vALIVA.Enable(True)
        self.cALIVA.Enable(True)
              
    def NewRow(self, evt):
        self.OnArtTxt(self)
        self.DelArtTxt(self)
        self.cntr_row = "new"
        if self.ccodbar.GetValue()==0:self.codart.SetFocus()
        else:self.codbar.SetFocus()
        self.newr.Enable(False)
        self.intr.Enable(True)
        self.modir.Enable(False)
        self.okart.Enable(True)
        self.modir.Show(False)
        self.okart.Show(True)
        
    def ModiRow(self, evt):
        self.OnArtTxt(self)   
        self.cntr_row = "modi"
        self.qt.SetFocus()
        self.delr.Enable(True)
        self.cntr_row = ""
        self.modir.Show(False)
        self.modir.Enable(False)
        self.okart.Show(True)
        self.okart.Enable(True)
        
    def DelArtTxt(self, evt):
        self.codart.SetValue('')
        self.codbar.SetValue('')
        self.descriz.SetValue('')
        self.UM.SetValue('')
        self.costo_un.SetValue('')
        self.importo.SetValue('')
        self.qt.SetValue('')
        self.costo_ag.SetValue('0,00')
        self.vALIVA.SetValue('20')
        self.dALIVA.SetValue(_("Aliquota 20%"))

    def CalcTotale(self,evt):
        tot_riga = 0
        for x in range(self.lc.GetItemCount()):
            # < diegom corretto colonna 5 invece che 17
            self.__MDI__.CnvPM(self.getColTxt(x, 5))
            tot_riga_row = self.__MDI__.val
            #print tot_riga_row                 
            if tot_riga_row!=0 and tot_riga_row!="0" and tot_riga_row!="":tot_riga+=tot_riga_row
        self.__MDI__.CnvVM(tot_riga)
        self.totale.SetValue(self.__MDI__.val)
        
    def SelRow(self,evt):
        self.intr.Enable(True)
        self.modir.Enable(True)
        self.newr.Enable(False)      

    def IntRow(self,evt):
        self.OffArtTxt(self)
        self.DelArtTxt(self)
        self.codart.Show(True)
        self.lc.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.lc.Enable(True) 
        
    def DelRow(self, evt):
        dlg = wx.MessageDialog(self, cfg.msgdelrow, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_YES:
            self.lc.DeleteItem(self.row)
            self.IntRow(self)
            self.CalcTotale(self)  
            self.newr.SetFocus()
            dlg.Destroy()
        else:
            dlg.Destroy()
        
    def RmpRow(self, evt):
        self.lc.InsertStringItem(self.row, self.codart.GetValue())
        self.lc.SetStringItem(self.row, 1, self.descriz.GetValue())
        self.lc.SetStringItem(self.row, 2, self.qt.GetValue())
        self.lc.SetStringItem(self.row, 3, self.costo_un.GetValue())
        self.lc.SetStringItem(self.row, 4, self.sc1.GetValue())
        self.lc.SetStringItem(self.row, 5, self.importo.GetValue())
        self.lc.SetStringItem(self.row, 6, self.vALIVA.GetValue())
        self.lc.SetStringItem(self.row, 7, self.UM.GetValue())        
        self.lc.SetStringItem(self.row, 8, self.mis.GetValue())
        self.lc.SetStringItem(self.row, 9, self.nriga.GetValue())
        self.lc.SetStringItem(self.row, 10, self.codbar.GetValue())
        self.lc.SetStringItem(self.row, 11, self.codmerc.GetValue())
        self.lc.SetStringItem(self.row, 12, self.costo_ag.GetValue())
        self.lc.SetStringItem(self.row, 13, self.sc2.GetValue())
        self.lc.SetStringItem(self.row, 14, self.sc3.GetValue())
        self.lc.SetStringItem(self.row, 15, self.lst.GetValue())
        self.lc.SetStringItem(self.row, 16, self.vDIV.GetValue())        
        self.lc.SetStringItem(self.row, 17, self.CAMBIO.GetValue())
        self.lc.SetStringItem(self.row, 18, self.rigadoc.GetValue())
        self.lc.SetStringItem(self.row, 19, self.annodoc.GetValue())
        self.lc.SetStringItem(self.row, 20, self.tipodoc.GetValue())
        self.lc.SetStringItem(self.row, 21, self.datadoc.GetValue())
        self.lc.SetStringItem(self.row, 22, self.numdoc.GetValue())
        self.lc.SetStringItem(self.row, 23, self.campo1.GetValue())
        self.lc.SetStringItem(self.row, 24, self.campo2.GetValue())

    def OkRow(self, evt):
        cnt_val = 0
        valcosto_un = self.costo_un.GetValue().replace(".","")
        valcosto_un = valcosto_un.replace(",","")
        valcosto_un = valcosto_un.replace("-","") 
        valcosto_un = valcosto_un.replace("-","") 
        if (valcosto_un!="" and valcosto_un.isdigit()==True):
            self.__MDI__.CnvPMPZ(self.costo_un.GetValue())
            vcosto_un = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgprezno,self.ttl)
            self.costo_un.SetFocus()
        sc1 = self.sc1.GetValue().replace(",","")  
        if (sc1!="" and sc1.isdigit()==True):
            self.__MDI__.CnvPM(self.sc1.GetValue())
            vsc1 = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgscno,self.ttl)
            self.sc1.SetFocus()
        qt = self.qt.GetValue().replace(",","") 
        if (qt!="" and qt.isdigit()==True):
            self.__MDI__.CnvPMQT(self.qt.GetValue())
            vqt = self.__MDI__.val
            cnt_val+=1
        else:
            self.Message(cfg.msgqtno,self.ttl)
            self.qt.SetFocus()
        if (cnt_val==3):
            tot_riga = (vcosto_un*vqt)-(vcosto_un*vqt*vsc1/100)
            self.__MDI__.CnvVM(tot_riga)
            self.importo.SetValue(self.__MDI__.val)
            self.totriga.SetValue(self.importo.GetValue())
            self.OffArtTxt(self)
            if ( self.cntr_row=="new"):
                self.row = self.lc.GetItemCount()
                nriga  = self.row + 1
                self.nriga.SetValue(str(nriga*10))
                self.RmpRow(self)
            if ( self.cntr_row==""):
                self.RmpRow(self)
                self.lc.DeleteItem(self.row + 1)
                self.lc.SetItemState(self.row-1, wx.LIST_STATE_SELECTED,
                      wx.LIST_STATE_SELECTED)
            self.CalcTotale(self)
            self.newr.Enable(True)
            self.newr.SetFocus()
            self.modir.Enable(False)
            self.okart.Enable(False)
            self.cntr_row = ""

    def FndSelArt(self, evt):
        row = evt
        self.codart.SetValue(str(row[0]))
        self.descriz.SetValue(row[2])
        self.UM.SetValue(str(row[3]))
        self.mis.SetValue(str(row[4]))         
        self.__MDI__.CnvVMPZ(row[5])
        self.prezzo1.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVMPZ(row[6])
        self.prezzo2.SetValue(self.__MDI__.val)
        self.__MDI__.CnvVMPZ(row[7])
        self.costo_un.SetValue(self.__MDI__.val)
        if self.costo_un.GetValue()=='' : self.costo_un.SetValue('0')
        self.codbar.SetValue(str(row[1]))          
        self.vALIVA.SetValue(str(row[11]))
        self.vMERCE.SetValue(str(row[8]))
        self.OffArtTxtAll(self)
        self.vALIVA.SetFocus()

    def FndCodArt(self, evt):
        cnt_rec = 0
        cod = self.codart.GetValue().upper()
        sql = """ select * from articoli where cod like "%s" """
        valueSql = "%" + cod + "%"
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","FndCodArt Error %s " % (msg)) 
        self.CnAz.commit()
        #if (cnt_rec>=1000): self.Message(cfg.msgfnd + str(cnt_rec) ,self.ttl)
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2):self.FndSelArt(row)     
        elif (cnt_rec>1):
            try:
	        import srcart
            except :
	        pass
            try:
                import base.srcart
            except :
                pass
            control = [self.tblart,self.codart,self.descriz,self.FndArt]
            win = srcart.create(self,control) 
            win.Centre(wx.BOTH)
            win.Show(True)
            
    def FndCodBar(self, evt):
        cnt_rec = 0
        cod = self.codbar.GetValue()
        sql = """ select * from articoli where codbar = "%s" """
        valueSql = codbar
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            #print  " FndCodBar %s " % rows
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","FndCodBar Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatono,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelArt(row)


    def FndArt(self, evt):
        cnt_rec = 0
        descriz = self.descriz.GetValue().upper()
        cod = self.codart.GetValue().upper()
        sql = """ select * from articoli where cod like "%s" """        
        if cod!="": valueSql = "%" + cod + "%"
        else: valueSql = "%" + descriz + "%"
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            rows = cr.fetchall()
            for row in rows:
                cnt_rec+=1
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","FndArt Error %s " % (msg))
        self.CnAz.commit()
        if (cnt_rec==0):self.Message(cfg.msgdatonull,self.ttl)
        elif (cnt_rec==1 and cnt_rec<2): self.FndSelArt(row)
      
    def FndArtSel(self, evt):
        self.okart.Enable(True)
        self.okart.SetFocus()

#    def Stampa(self, evt):
        #evt.Skip()
        #CAUMA = self.vCAUMA.GetValue()
        #anno = self.anno.GetValue()
        #num_mov = self.num_mov.GetValue()


    def Stampa(self, evt):   
        anno=self.annoc 
        num_mov = self.num_mov.GetValue()
        tipo_doc='lstmovmag'
        import skprint
        skprint.stampaDoc(
              conn = self.CnAz ,  
              tipo = tipo_doc,
              parametriSql = (anno,num_mov),
              datiazienda = self.dzDatiAzienda,
              anteprima = True )



    def New(self, evt):
        self.NewTxt(self)
        self.cntr = "new"
        registro = "R1"
        anno = self.anno.GetValue()
        chiave = "RMAG"   
        sql = """ select * from libriaz
                  where chiave = "%s" and anno = "%s" and registro = "%s" """  
        valueSql = chiave, anno, registro
        try:
            cr = self.CnAz.cursor ()
            cr.execute(sql % valueSql)
            while (1):
                row = cr.fetchone()
                #print row
                if row==None:
                    break
                if (row[3]==None) : self.num_mov.SetValue('1')
                if (row[3] != None) : self.num_mov.SetValue(str(int(row[3]) + 1))
                if (row[16]==None) : self.vdatamov.SetValue(self.data)
                if (row[16] != None) : self.vdatamov.SetValue(row[16])
        except StandardError, msg:
            self.__MDI__.MsgErr("movmag","New Error %s " % (msg))  
        self.CnAz.commit()
        num_mov = int(self.num_mov.GetValue())
        self.datamov.SetValue(self.vdatamov.GetValue())
        self.data_doc.SetValue(self.vdatamov.GetValue())
        self.vCAUMA.SetFocus()

                    
    def Message(self, qst, ttl):
        dlg = wx.MessageDialog(self, qst, ttl,
                              wx.OK | wx.ICON_EXCLAMATION)
        if dlg.ShowModal()==wx.ID_OK:
            dlg.Destroy()
                        
    def Close(self, evt):
        if (self.ragsoc2.GetValue()!="" or self.ragsoc1.GetValue()!=""):
            dlg = wx.MessageDialog(self, cfg.msgesci, self.ttl,
                              wx.YES_NO | wx.NO_DEFAULT |wx.ICON_QUESTION)
            if dlg.ShowModal()==wx.ID_YES:
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
            
    def Save(self, evt):
        if(self.lc.GetItemCount()!=0 and self.codcf.GetValue()!=""):
            vcntr = self.cntr
            self.cntr = ""
            valcntr = vcntr
            vanno = self.anno.GetValue()
            vnum_mov = int(self.num_mov.GetValue())            
            vdatamov = self.datamov.GetValue()
            valCAUMA = self.vCAUMA.GetValue()
            chiave = "RMAG"
            registro = "R1"
            vcod_mag = 1 
            vcodcf = self.codcf.GetValue()
            vnum_doc = self.num_doc.GetValue()  
            vdatadoc = self.datadoc.GetValue()
            vtipodoc = ""
            vrigadoc = ""
            vannodoc = ""
            vdiv = self.vDIV.GetValue()
            valCFM = self.vCFM.GetValue()              
            vcampo1 = "" 
            vcampo2 = "" 
            valueSql = vnum_mov, vanno
            if(vcntr=="modi"):
                try:
                    cr = self.CnAz.cursor()
                    sql = """ delete from movmag 
                              where num_mov = "%s" and anno = "%s" """                   
                    cr.execute(sql % valueSql)
                except StandardError, msg:
                    self.__MDI__.MsgErr("movmag","Save dele Error %s " % (msg)) 
        	self.CnAz.commit()
                vcntr = "new"       
            if(vcntr=="new"):
                nrow = self.lc.GetItemCount() 
                for row in range(nrow):
                    vcod_mag = 1
                    vcodart = self.getColTxt(row, 0).upper()
                    vdescriz = self.getColTxt(row, 1).upper()
                    vqt = self.getColTxt(row, 2)
                    self.__MDI__.CnvPMQT(vqt)
                    vqt = float(self.__MDI__.val)   
                    vcosto_un = self.getColTxt(row,3)
                    self.__MDI__.CnvPMPZ(vcosto_un)
                    vcosto_un = self.__MDI__.val
                    vsc1 = self.getColTxt(row, 4)
                    self.__MDI__.CnvPM(vsc1)
                    vsc1 = self.__MDI__.val 
                    vimporto = self.getColTxt(row, 5)
                    self.__MDI__.CnvPMPZ(vimporto)
                    vimporto = self.__MDI__.val
                    valALIVA = self.getColTxt(row, 6)
                    vUM = self.getColTxt(row, 7).upper()
                    if vUM=='':vUM = '--'
                    vmis = self.getColTxt(row, 8)
                    vnriga = int(self.getColTxt(row, 9))    
                    vcodbar = self.getColTxt(row, 10)
                    vMERCE = self.getColTxt(row, 11)              
                    vcosto_ag = self.getColTxt(row, 12)
                    self.__MDI__.CnvPMPZ(vcosto_ag)
                    vcosto_ag = (self.__MDI__.val)
                    vsc2 = 0 
                    vsc3 = 0 
                    vlst = 1 
                    valDIV = "EU" 
                    vCAMBIO = 0 
                    vrigadoc = self.getColTxt(row, 18)
                    if vrigadoc=="":vrigadoc = 0
                    vannodoc = self.getColTxt(row, 19)                
                    vtipodoc = self.getColTxt(row, 20)
                    vdatadoc = self.data_doc.GetValue() 
                    vnumdoc = self.num_doc.GetValue() 
                    vcampo1 = self.getColTxt(row,23)
                    vcampo2 = self.getColTxt(row, 24)
                    vm0 = vanno,int(vnum_mov),vdatamov
                    vm1 = valCAUMA, int(vcod_mag), valCFM, vcodcf,\
                          int(vnriga),vcodart,vcodbar,vMERCE
                    vm2 = vdescriz,vUM,vmis,vqt,float(vcosto_un),\
                          float(vcosto_ag)
                    vm3 = float(vimporto),valALIVA,valDIV,vCAMBIO,\
                          float(vsc1),vsc2,vsc3
                    vm4 = vlst,vannodoc,vtipodoc,vdatadoc,vnumdoc,\
                          int(vrigadoc)
                    vm5 = vcampo1, vcampo2
                    valueSql = vm0 + vm1 + vm2 + vm3 + vm4 + vm5
                    try:
                        cr = self.CnAz.cursor()
                        sql = """ INSERT INTO movmag
                                  VALUES("%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                         "%s","%s","%s","%s","%s","%s","%s",
                                          "%s","%s","%s","%s","%s","%s","%s",
                                          "%s","%s","%s","%s")"""
                        cr.execute(sql % valueSql)  
        	    except StandardError, msg:
                        self.__MDI__.MsgErr("movmag","Save ins Error %s " % (msg))
        	    self.CnAz.commit()
                valueSql = vnum_mov, vdatamov, chiave, vanno, registro
                if valcntr == 'new' :
                    try:
                        cr = self.CnAz.cursor()
                        sql = """ update libriaz set ultnum = "%s", 
                                  udatreg = "%s" 
                                  where chiave = "%s" and anno = "%s"
                                  and registro = "%s" """                    
                        cr.execute(sql % valueSql)  
        	    except StandardError, msg:
                        self.__MDI__.MsgErr("movmag","Save Update Libriaz Error %s " % (msg))
        	    self.CnAz.commit()
            self.Start(self)
            self.stampa.SetFocus()     
        else:
            self.Message(cfg.msgass,self.ttl) 



    def is_look(self):
        if (self.cntr!="new" and self.cntr!="modi"): return False
        else : return True
        
    def data_reload(self,rec,cntrp):
        self.rec=rec
        #self.tcpart=cntrp.upper()
        self.Start(self)
