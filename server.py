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
class MyFrame2(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self,title = u"Server Socket Python", size = wx.Size( 500,400 ), *args, **kwargs)
        
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
        self.SetSizer( fgSizer1 )
        self.Layout()
        self.Centre( wx.BOTH )
		
        self.Panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.TAB_TRAVERSAL )
        self.text = wx.TextCtrl(self.Panel, wx.ID_ANY,  wx.EmptyString,wx.DefaultPosition, wx.Size( 300,270 ),style=wx.TE_MULTILINE)
        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.text, 1, wx.ALL | wx.EXPAND, 5)
        fgSizer1.Add( self.Panel, 1, wx.EXPAND |wx.ALL, 5 )
        self.Panel.SetSizerAndFit(self.sizer)  
        
      
        self.Show()

        self.thread = threading.Thread(target=self.Server)
        self.thread.start()
        
        # Connect Events
        self.btnEnviar.Bind( wx.EVT_BUTTON, self.Enviar )
		
    
    def Enviar( self, event ):
		self.port =int(self.txt_Puerto.GetValue())
		self.ip=str(self.txt_IpServer.GetValue())
		#self.client.close()	
		#self.client.connect((self.ip, self.port))
		#def sendSocketMessage(message):
		"""Send a message to a socket"""
		try:
			#port = random.randint(1025,36000)
			self.message=self.txt_Mensaje.GetValue()			
			if self.message=='salir':
				self.Close()
			else:
				self.client.send(self.message)
			
				self.txt_Mensaje.SetValue("")
		except Exception, msg:
			print msg	
			
     
    def Print(self, text):
        wx.CallAfter(self.text.AppendText, text + "\n")

    def Server(self):
        self.Print("Puerto: {}".format(port))
		#instanciamos un objeto para trabajar con el socket
        self.tcpServer = socket(AF_INET , SOCK_STREAM)
        #Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
        # addr es una tupla que definimos anteriormente con el host y puerto
        self.tcpServer.bind(addr)
        #Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
		#El numero de conexiones entrantes que vamos a aceptar
        self.tcpServer.listen(5)
        try:
            while True:
                self.Print("Esperando la conexion...")
                #Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este 
				#devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
                tcpClient, caddr = self.tcpServer.accept()
                self.Print("Conectado desde {}".format(caddr))

                while True:
					#Recibimos el mensaje, con el metodo recv recibimos datos 
					# y como parametro  la cantidad de bytes para recibir 
                    data = tcpClient.recv(bufsiz)
                    if not data:
                        break
                    tcpClient.send('[%s]\nData\n%s' % (ctime(), data))
                    self.Print(data)
                tcpClient.close()

        except KeyboardInterrupt:
            tcpServer.close()

	def __del__(self):
		self.tcpServer.close()
		self.Close()
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



