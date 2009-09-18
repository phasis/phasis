# Project       Phasis
#
# Description
# Gestionale Aziendale Open Source Phasis (R)
#
#*  Copyright (C) 2003, 2004, 2005, 2006  Phasis - http://www.phasis.it/
#   Author: Massimo Gerardi <m.gerardi@mgsoft.it>
#   Via Michele Rosi 184 - Aranova (Roma)
#   00050 Aranova (Roma) - Italy
#   tel. +39 06 6674756 - fax +39 06 6674756
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   www.phasis.it - info@phasis.it 
#

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



