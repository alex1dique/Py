#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from socket import *
from time import ctime
import random
import threading
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ,*args, **kwargs ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.txt_Enviar = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 350,30 ), 0 )
		fgSizer1.Add( self.txt_Enviar, 0, wx.ALL, 5 )
		
		self.btnEnviar = wx.Button( self, wx.ID_ANY, u"Enviar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnEnviar, 0, wx.ALL, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.Panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.TAB_TRAVERSAL )
		self.text = wx.TextCtrl(self.Panel, style=wx.TE_MULTILINE)
		self.sizer = wx.BoxSizer()
		self.sizer.Add(self.text, 1, wx.ALL | wx.EXPAND, 5)
		fgSizer1.Add( self.Panel, 1, wx.EXPAND |wx.ALL, 5 )
		self.Panel.SetSizerAndFit(self.sizer)  
		self.Show()
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnEnviar.Bind( wx.EVT_BUTTON, self.Enviar )
		
		
	
	def Print(self, text):
		wx.CallAfter(self.text.AppendText, text + "\n")
	
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Enviar( self, event ):
		event.Skip()
	
	
########################################################################
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame2(None)
        self.SetTopWindow(frame)
        frame.Show()
        return 1

# end of class MyApp




def main():
	
	return 0

if __name__ == '__main__':
	app = MyApp(0)
	app.MainLoop()

