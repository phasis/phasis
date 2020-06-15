#!/usr/bin/env python
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
import cfg

 
def create(parent,cnt):
    return Calcolatrice (parent,cnt)

class Calcolatrice(wx.Frame):
    def __init__(self, prnt, cnt ):
        wx.Frame.__init__(self, id = wx.NewId(), name='',
              parent=prnt, pos=wx.Point(0, 0), size=wx.DefaultSize,  
              style=wx.MINIMIZE_BOX | wx.STAY_ON_TOP | wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU|wx.FRAME_EX_METAL,
              #style=wx.DEFAULT_FRAME_STYLE, 
              title=cnt[0])
        self.SetIcon(wx.Icon(cfg.path_img + "null.ico", wx.BITMAP_TYPE_ICO))
        self.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
        self.Center(wx.BOTH) 
        self.AggMenu = cnt[3]
        self.IDMENU = cnt[4]
        self.__MDI__=wx.GetApp().GetPhasisMdi()
        
        self.SetClientSize(wx.Size(465, 260))       
        
        self.Bind(wx.EVT_ACTIVATE,self.OnActiv)
        
        self.panel=wx.Panel(self,-1)

        self.btn1 = wx.Button(parent=self.panel, id=-1, label='1', name='btn1',
               pos=wx.Point(16, 145), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn1, self.btn1)

        self.btn2 = wx.Button(parent=self.panel, id=-1, label='2', name='btn2',
               pos=wx.Point(64, 145), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn2, self.btn2)
        
        self.btn3 = wx.Button(parent=self.panel, id=-1, label='3', name='btn3',
               pos=wx.Point(112, 145), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn3, self.btn3)
 
        self.btn4 = wx.Button(parent=self.panel, id=-1, label='4', name='btn4',
               pos=wx.Point(16, 105), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn4, self.btn4)

        self.btn5 = wx.Button(parent=self.panel, id=-1, label='5', name='btn5',
               pos=wx.Point(64, 105), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn5, self.btn5)

        self.btn6 = wx.Button(parent=self.panel, id=-1, label='6', name='btn6',
               pos=wx.Point(112, 105), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn6, self.btn6)

        self.btn7 = wx.Button(parent=self.panel, id=-1, label='7', name='btn7',
               pos=wx.Point(16, 65), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn7, self.btn7)
 
        self.btn8 = wx.Button(parent=self.panel, id=-1, label='8', name='btn8',
               pos=wx.Point(64, 65), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn8, self.btn8)
 
        self.btn9 = wx.Button(parent=self.panel, id=-1, label='9', name='btn9',
               pos=wx.Point(112, 65), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn9, self.btn9)

        self.btn0 = wx.Button(parent=self.panel, id=-1, label='0', name='btn0',
               pos=wx.Point(16, 185), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtn0, self.btn0)
 
        self.btnDot = wx.Button(parent=self.panel, id=-1, label='.', name='btnDot',
               pos=wx.Point(64, 185), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtnDot, self.btnDot)

        self.btnEqual = wx.Button(parent=self.panel, id=-1, label='=',
              name='btnEqual',  pos=wx.Point(112, 185),
              size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtnEqual, self.btnEqual)

        self.edit = wx.TextCtrl(parent=self.panel, id=-1, name='edit', 
                                pos=wx.Point(16, 16), size=wx.Size(232, 34), 
                                style=wx.TE_PROCESS_TAB|wx.TE_PROCESS_ENTER|wx.TE_RIGHT, value='0')

        #self.edit = wx.StaticText(parent=self.panel, id=-1, name='edit', 
        #                        pos=wx.Point(16, 16), size=wx.Size(232, 34), 
        #                        style=wx.ALIGN_RIGHT|wx.ST_NO_AUTORESIZE)
        
        self.edit.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL, False))
     
        self.story = wx.TextCtrl(parent=self.panel, id=-1, name='story', 
                                pos=wx.Point(260, 16), size=wx.Size(190, 193), 
                                style=wx.TE_PROCESS_TAB|wx.TE_RIGHT|wx.TE_MULTILINE|wx.TE_READONLY, value='')
        
        self.story.SetFont(wx.Font(10, wx.TELETYPE, wx.NORMAL, wx.NORMAL, False))
        
        self.descri=wx.StaticText(parent=self.panel, id=-1, name='decimali', 
                    pos=wx.Point(265, 227), size=wx.Size(180, 20),
                    style=wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
        self.descri.SetFont(wx.Font(10, wx.TELETYPE, wx.NORMAL, wx.NORMAL, False))
        
        #self.descri.SetBackgroundColour('White')
        #wx.StaticBox(parent=self.panel, id=-1, name='box', 
        #            pos=wx.Point(260, 210), size=wx.Size(192, 40),
        #            style=0)
                

        self.edit.Bind(wx.EVT_CHAR, self.EvtChar)
        #self.edit.Bind(wx.EVT_TEXT, self.EvtText)
        
        self.story.Bind(wx.EVT_CHAR, self.EvtChar)
        #stile=wx.TextAttr()
        #stile.SetAlignment(wx.TEXT_ALIGNMENT_RIGHT)
        #self.story.SetDefaultStyle(stile);

        #self.story.SetAlignment(wx.TEXT_ALIGNMENT_RIGHT)
        #self.panel.SetFocusIgnoringChildren()
        self.Bind(wx.EVT_CHAR, self.EvtChar)
        #self.edit.SetEvtHandlerEnabled(False)
        #self.story.SetEvtHandlerEnabled(False)
        #self.SetEvtHandlerEnabled(False)
        
        #self.story.Bind(wx.EVT_KILL_FOCUS, self.OnActiv)

        #self.edit.Enable(False)
        #self.story.Enable(False)
        
        self.edit.SetBackgroundColour("yellow")
 
        self.btnPlus = wx.Button(parent=self.panel, id=-1, label='+',
              name='btnPlus',  pos=wx.Point(160, 65), size=wx.Size(32,
              32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtnPlus, self.btnPlus)

        self.btnMinus = wx.Button(parent=self.panel, id=-1, label='-',
              name='btnMinus',  pos=wx.Point(160, 105),
              size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtnMinus, self.btnMinus)

        self.btnMulti = wx.Button(parent=self.panel, id=-1, label='*',
              name='btnMulti',  pos=wx.Point(160, 145),
              size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtnMulti, self.btnMulti)

        self.btnDiv = wx.Button(parent=self.panel, id=-1, label='/', name='btnDiv',
               pos=wx.Point(160, 185), size=wx.Size(32, 32), style=0)
        self.Bind(wx.EVT_BUTTON,  self.OnBtnDiv, self.btnDiv)
        
        self.btnClear = wx.Button(parent=self.panel, id=-1, label='&Clr',
              name='btnClear',  pos=wx.Point(208, 65),
              size=wx.Size(40, 32), style=0)
        self.btnClear.SetToolTipString(_('Clear'))
        self.Bind(wx.EVT_BUTTON, self.OnBtnClear, self.btnClear)

        self.btnClose = wx.Button(parent=self.panel, id=-1, label='&Off',
              name='btnClose',  pos=wx.Point(208, 105),
              size=wx.Size(40, 32), style=0)
        self.btnClose.SetToolTipString(_('Close'))
        self.Bind(wx.EVT_BUTTON, self.OnBtnClose, self.btnClose)
        self.Bind(wx.EVT_CLOSE, self.OnBtnClose)
        
        self.btnBack = wx.Button(parent=self.panel, id=-1, label='<-',
              name='btnBack',  pos=wx.Point(208, 145),
              size=wx.Size(40, 32), style=0)
        self.Bind(wx.EVT_BUTTON, self.OnBtnBack, self.btnBack)

        self.btnPiumeno = wx.Button(parent=self.panel, id=-1, label='+/-', name='btnPiumeno',
               pos=wx.Point(208, 185), size=wx.Size(40, 32), style=0)
        self.Bind(wx.EVT_BUTTON,  self.OnBtnPiumeno, self.btnPiumeno)



        self.btnRnd0 = wx.Button(parent=self.panel, id=-1, label=_('var'), name='btnRnd0',
               pos=wx.Point(16, 225), size=wx.Size(55, 30), style=0)
        self.btnRnd0.SetToolTipString(_('decimali variabili'))
        self.Bind(wx.EVT_BUTTON, self.OnBtnRnd0, self.btnRnd0)
        
        self.btnRnd1 = wx.Button(parent=self.panel, id=-1, label=_('2 dec'), name='btnRnd1',
               pos=wx.Point(75, 225), size=wx.Size(55, 30), style=0)
        self.btnRnd1.SetToolTipString(_('2 decimali'))
        self.Bind(wx.EVT_BUTTON, self.OnBtnRnd1, self.btnRnd1)

        self.btnRnd2 = wx.Button(parent=self.panel, id=-1, label=_('3 dec'),
              name='btnRnd2',  pos=wx.Point(134, 225),
              size=wx.Size(55, 30), style=0)
        self.btnRnd2.SetToolTipString(_('3 decimali'))
        self.Bind(wx.EVT_BUTTON, self.OnBtnRnd2, self.btnRnd2)

        self.btnRnd3 = wx.Button(parent=self.panel, id=-1, label=_('4 dec'), name='btnRnd3',
               pos=wx.Point(193, 225), size=wx.Size(55, 30), style=0)
        self.btnRnd3.SetToolTipString(_('4 decimali'))
        self.Bind(wx.EVT_BUTTON,  self.OnBtnRnd3, self.btnRnd3)

        self.btnRnd0.SetFont(wx.Font(10, wx.TELETYPE, wx.NORMAL, wx.NORMAL, False)) #.Refresh(True)
        self.btnRnd1.SetFont(wx.Font(10, wx.TELETYPE, wx.NORMAL, wx.NORMAL, False)) #.Refresh(True)
        self.btnRnd2.SetFont(wx.Font(10, wx.TELETYPE, wx.NORMAL, wx.NORMAL, False)) #.Refresh(True)
        self.btnRnd3.SetFont(wx.Font(10, wx.TELETYPE, wx.NORMAL, wx.NORMAL, False)) #.Refresh(True)

        #self.Bind(wx.EVT_SET_FOCUS,self.SetFocus)

        self.maxdec=8  #NUMERO MASSIMO DI DECIMALI INSERIBILI
        self.maxint=9  #NUMERO MASSIMO DI CIFRE INTERE
        self.maxcifre=11 #LUNGHEZZA MASSIMA DEL NUMERO
        self.primo=False
        self.precris='0'
        self.precope=''
        self.num='0'
        self.arro=-1 #ARROTONDAMENTO DI DEFAULT -1=VARIABILE
        self.Rnd(self.arro)
        #self.SetFocus()
        self.FocusEdit()
        accell=wx.AcceleratorTable(self.__MDI__.accellentry)
        self.SetAcceleratorTable(accell)
        self.Bind(wx.EVT_MENU, self.OnMenu)
        
    def OnMenu(self, event):
        #ID = event.GetId()
        #if ID == DAFRAMEATAB : self.__MDI__.trasfotab(self)
        event.Skip()
    

    def EvtChar(self, evt):
        evt_char = evt.GetKeyCode()
        if 325 < evt_char < 336 : evt_char=evt_char-278
        elif 390 < evt_char < 397 : evt_char=evt_char-349
        elif evt_char==390 : evt_char=61
        elif evt_char==372 : evt_char=13
        #util.alert(self,"Codice:"+str(evt_char))
        if evt_char<255:
            key=chr(evt_char)
            if evt_char==wx.WXK_ESCAPE: self.OnBtnClear(self)
            elif key in ['0','1','2','3','4','5','6','7','8','9']: self.val(key) 
            elif key in ['+','-','/','*']: self.ope(key)
            elif key in ['.',',']: self.OnBtnDot(None)
            elif key in ['='] or evt_char==wx.WXK_RETURN: self.OnBtnEqual(None)
            elif evt_char==wx.WXK_BACK: self.OnBtnBack(None)
            elif evt_char==wx.WXK_DELETE: self.OnBtnCanc(None)
            elif evt_char==wx.WXK_TAB: self.FocusEdit()
            else: pass #self.edit.SetValue(self.Aggiorna())
        else: pass #self.edit.SetValue(self.Aggiorna())
    
    def EvtText(self, evt):
        self.edit.SetValue(self.Aggiorna())
        self.FocusEdit()
        
    def val(self,numero):
        if self.primo==False or self.num=='0': 
            self.num=''
            self.primo=True
        self.num=self.num+numero
        self.edit.SetValue(self.Aggiorna(True))
        self.FocusEdit()

    def ope(self,operazione):
        if self.primo==True or self.precope=='':
            self.num=self.Sistema(self.num)
            self.story.AppendText(self.Aggiorna()+' '+operazione+'\n')
            if self.precope=='': 
                self.precris=self.num[:]
                self.precope=operazione[:]
            else:
                if float(self.num)==0.0 and self.precope=='/':
                    self.story.AppendText(_('Errore div 0')+'\n\n')
                    self.num='0'
                    self.precris='0'
                    self.precope=''
                else:
                    self.num=self.Calcola(self.precris,self.precope,self.num)
                    self.num=self.Sistema(self.num)
                    #METTERE CONTROLLO 'e' PER MAX NUMERO SE SI VUOLE GESTIRE
                    self.precris=self.num[:]                
                    self.precope=operazione[:]
            self.primo=False
            self.edit.SetValue(self.Aggiorna())
        self.FocusEdit()


    def OnBtnBack(self, evt):
        if self.primo==False: 
            self.num='0'
        else: 
            self.num=self.num[:-1]
            lung=len(self.num)
            if lung==0 or (lung==1 and self.num[0]=='-'): self.num='0'
        self.edit.SetValue(self.Aggiorna())
        self.FocusEdit()
        
    def OnBtnPiumeno(self, evt):
        if self.precope=='' or self.primo==True:
            if self.num != '0':
                if self.num[0]=='-': self.num=self.num[1:]
                else:
                    self.num='-'+self.num    
                self.edit.SetValue(self.Aggiorna())
        self.FocusEdit()

    def OnBtn0(self, evt):
        self.val('0')
 
    def OnBtn1(self, evt):
        self.val('1')
 
    def OnBtn2(self, evt):
        self.val('2')
 
    def OnBtn3(self, evt):
        self.val('3')
 
    def OnBtn4(self, evt):
        self.val('4')
        
    def OnBtn5(self, evt):
        self.val('5')
 
    def OnBtn6(self, evt):
        self.val('6')
 
    def OnBtn7(self, evt):
        self.val('7')
 
    def OnBtn8(self, evt):
        self.val('8')
 
    def OnBtn9(self, evt):
        self.val('9')
        
    def OnBtnRnd0(self, evt):
        self.Rnd(-1)
 
    def OnBtnRnd1(self, evt):
        self.Rnd(2)
 
    def OnBtnRnd2(self, evt):
        self.Rnd(3)
 
    def OnBtnRnd3(self, evt):
        self.Rnd(4)
 
    def OnBtnDot(self, evt):
        if ('.' not in self.num) and self.primo==True:
            self.num=self.num+'.'
            self.edit.SetValue(self.Aggiorna())
        self.FocusEdit()
 
    def OnBtnEqual(self, evt):
        if self.precope!='' and self.primo==True:
            self.num=self.Sistema(self.num)
            self.story.AppendText(self.Aggiorna()+' =\n')          
            if float(self.num)==0.0 and self.precope=='/':
                txt=_('Errore div 0')
                self.num='0'
                self.edit.SetValue('0')
            else:
                self.num=self.Calcola(self.precris,self.precope,self.num)
                self.num=self.Sistema(self.num)
                #METTERE CONTROLLO 'e' PER MAX NUMERO SE SI VUOLE GESTIRE
                txt=self.Aggiorna()
                self.edit.SetValue(txt)
            lung=len(txt)            
            self.story.AppendText('-'*lung+'  \n')
            self.story.AppendText(txt+'  \n')
            self.story.AppendText('\n')           
            self.precope=''
            self.primo=False
        self.FocusEdit()
 
    def OnBtnPlus(self, evt):
        self.ope('+')
 
    def OnBtnMinus(self, evt):
        self.ope('-')
 
    def OnBtnMulti(self, evt):
        self.ope('*')
 
    def OnBtnDiv(self, evt):
        self.ope('/')
 
    def OnBtnClear(self, evt):
        self.num='0'
        self.edit.SetValue('0')
        if self.precope!='': self.story.AppendText(_('-calcolo canc-')+'\n\n')
        else: self.story.SetValue('')
        self.precris='0'
        self.primo=False
        self.precope=''
        self.FocusEdit()
        
    def OnBtnCanc(self,evt):
        self.num='0'
        self.edit.SetValue('0')
        self.primo=False
        self.FocusEdit()
        
    def OnActiv(self,evt):
        self.FocusEdit()
        evt.Skip()
    
    def Rnd(self,rnd):
        if self.arro==-1: self.btnRnd0.Enable(True)
        elif self.arro==2: self.btnRnd1.Enable(True)
        elif self.arro==3: self.btnRnd2.Enable(True)
        elif self.arro==4: self.btnRnd3.Enable(True)
        if rnd==-1: 
            self.btnRnd0.Enable(False)
            self.descri.SetLabel(_("Decimali variabili"))
        elif rnd==2: 
            self.btnRnd1.Enable(False)
            self.descri.SetLabel(_("2 decimali fissi"))
        elif rnd==3: 
            self.btnRnd2.Enable(False)
            self.descri.SetLabel(_("3 decimali fissi"))
        elif rnd==4: 
            self.btnRnd3.Enable(False)
            self.descri.SetLabel(_("4 decimali fissi"))
        self.arro=rnd
        self.OnBtnClear(None)
    
    def FocusEdit(self):
        self.edit.SetFocus()
        self.edit.SetInsertionPointEnd()
        #self.SetFocus()

    def Calcola(self,txt1,ope,txt2):
        if '.' in txt1: num1=float(txt1)
        else: num1=int(txt1)
        if '.' in txt2 or ope=='/': num2=float(txt2)
        else: num2=int(txt2)
        if ope=='+': ris=num1+num2
        elif ope=='-': ris=num1-num2
        elif ope=='/': ris=num1/num2
        elif ope=='*': ris=num1*num2
        return str(ris) #"%f" % ris
    
    def Sistema(self,txt):
        if '.' in txt:
            num=float(txt)
            if self.arro>=0: num=round(num,self.arro)
            else: num=round(num,self.maxdec)
        else: num=int(txt)
        txt=str(num)  # "%f" % num
        lista=txt.split('.')
        if len(lista)>1 : lung=len(lista[1][:])
        else: lung=0       
        if self.arro<=0 and lung==1 and txt[-1:]=='0': txt=txt[:-2]
        if self.arro>0:
            if lung==0: txt=txt[:]+'.'
            txt=txt[:]+('0'*(self.arro-lung))        
        return txt
    
    def Aggiorna(self,inse=False):
        lista=self.num.split('.')
        txt=lista[0][:]
        lung=len(txt)
        if txt[0]=='-': lung=lung-1
        if len(lista)>1 : 
            txt2=lista[1][:]
            lung2=len(txt2)
            if inse==True and (lung2>self.maxdec or (lung+lung2)>self.maxcifre):
                txt2=txt2[:-1]
                self.num=self.num[:-1]
            txt2=','+txt2[:]
        else:
            txt2=''
            if inse==True and (lung>self.maxint or lung>self.maxcifre):
                txt=txt[:-1]
                self.num=self.num[:-1]
                lung=lung-1
        lung=(lung-1)/3
        i=0
        j=3
        while i<lung:
            txt=txt[:-j]+'.'+txt[-j:]
            i=i+1
            j=j+4 
        txt=txt[:]+txt2[:]
        
        return txt 

    def OnBtnClose(self, evt):
        self.__MDI__.CloseTabObj(self)
        #self.Destroy()
        
    def OnSetFocus(self,evt):
        self.FocusEdit()
        #evt.Skip()
