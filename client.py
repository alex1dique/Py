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

import wx
#importamos el modulo socket
from socket import *
from time import ctime
import random
import threading
#import serial

# definir el puerto por el cual se recibiran las peticiones
port=8080
#Definimos el host,Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
host = ''
#definimos una tupla con los datos del host y el puerto
addr = (host, port)
#definimos en la variable  la cantidad de bytes para recibir desde un cliente
bufsiz = 1024
########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 487,521 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer3 = wx.FlexGridSizer( 0, 1, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Enviar mensajes con Sockets a traves de Python", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer4.SetMinSize( wx.Size( 800,800 ) ) 
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"IP Server:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.txt_IpServer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,30 ), 0 )
		fgSizer4.Add( self.txt_IpServer, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Puerto:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.txt_Puerto = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,30 ), 0 )
		fgSizer4.Add( self.txt_Puerto, 0, wx.ALL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.btnConectar = wx.Button( self, wx.ID_ANY, u"Conectar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnConectar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Mensaje:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer4.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.txt_Mensaje = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,30 ), 0 )
		fgSizer4.Add( self.txt_Mensaje, 0, wx.ALL, 5 )
		
		self.btnEnviar = wx.Button( self, wx.ID_ANY, u"Enviar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.btnEnviar, 0, wx.ALL, 5 )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.Panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,270 ), wx.TAB_TRAVERSAL )
		self.text = wx.TextCtrl(self.Panel, wx.ID_ANY,  wx.EmptyString,wx.DefaultPosition, wx.Size( 300,270 ),style=wx.TE_MULTILINE)
		self.sizer = wx.BoxSizer()
		self.sizer.Add(self.text, 1, wx.ALL | wx.EXPAND, 5)
		fgSizer4.Add( self.Panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnConectar.Bind( wx.EVT_BUTTON, self.Conectar )
		self.btnEnviar.Bind( wx.EVT_BUTTON, self.Enviar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Conectar( self, event ):
		event.Skip()
	
	def Enviar( self, event ):
		event.Skip()
	def Print(self, text):
		wx.CallAfter(self.text.AppendText, text + "\n")


	
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



