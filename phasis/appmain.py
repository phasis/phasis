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



'''
import wx
import cfg
import mdi
#import  thread

      
class PhApp(wx.App):
    def OnInit(self):

        # visualizza lo splash screen per 3 secondi
        
        bmp = wx.Image(cfg.path_img+"splash.png").ConvertToBitmap()
        wx.SplashScreen(bmp,
                        wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
                        3000, None, -1)
        wx.Yield()
        
        # crea la finestra principale del programma e poi esegui selaz
        
        win = mdi.create()
        self.SetPhasisMdi(win)
        win.Show(True)
        #thread.start_new_thread(self.Run, ())
        win.Selaz()
        return True

    def GetPhasisMdi(self):
        return self.__mdi
    
    def SetPhasisMdi(self,mdi):
        self.__mdi=mdi



def main():
    app = PhApp(False)
    app.MainLoop()

'''




import wx
import mdi
import cfg

class PhSplash(wx.SplashScreen):
    def __init__(self):  
        bmp = wx.Image(cfg.path_img+"splash.png").ConvertToBitmap()
        wx.SplashScreen.__init__(self, bmp,
                                 wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
                                 3000, None, -1)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.fcwin = wx.FutureCall(1000, self.ShowWin)

    def OnClose(self, evt):

        evt.Skip()
        self.Hide()
        if self.fcwin.IsRunning():
            self.fcwin.Stop()
            self.ShowWin()


    def ShowWin(self):
        #if self.fcwin.IsRunning():
        #    self.Raise()

        win = mdi.create()
        wx.GetApp().SetPhasisMdi(win)
        #win.Selaz()
        win.Show(True)
        #win.Selaz()
        
        if self.fcwin.IsRunning():
            self.Raise()
        win.Selaz()
        #self.Raise()
        
class PhApp(wx.App):
    def OnInit(self):
        self.__mdi=None
        splash = PhSplash()
        splash.Show()
        #self.SetTopWindow(self.GetPhasisMdi())
        #self.__mdi.Selaz()
        return True
    #poi vediamo meglio
    def GetPhasisMdi(self):
        return self.__mdi
    def SetPhasisMdi(self,mdi):
        self.__mdi=mdi

def main():
    app = PhApp(False)
    #wx.GetApp().__mdi.Selaz()
    app.MainLoop()








'''


class PhApp(wx.App):
    def OnInit(self):

        # visualizza lo splash screen per 3 secondi
        bmp = wx.Image(cfg.path_img+"splash.png").ConvertToBitmap()
        wx.SplashScreen(bmp,
                        wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,
                        3000, None, -1)
        wx.Yield()
        
        # crea la finestra principale del programma e poi esegui il modulo selaz
        
        #self.__mdi=None
        win = mdi.create()
        self.__mdi=win
        #wx.GetApp().SetPhasisMdi(win)
        win.Show(True)
        win.Selaz()
        return True
    
    #poi vediamo meglio
    def GetPhasisMdi(self):
        return self.__mdi
    
    def SetPhasisMdi(self,mdi):
        self.__mdi=mdi  

def main():
    app = PhApp(False)
    app.MainLoop()

'''



