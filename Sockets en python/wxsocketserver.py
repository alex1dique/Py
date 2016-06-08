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
class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.panel = wx.Panel(self)
        self.text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)

        self.sizer = wx.BoxSizer()
        self.sizer.Add(self.text, 1, wx.ALL | wx.EXPAND, 5)

        self.panel.SetSizerAndFit(self.sizer)  
        self.Show()

        self.thread = threading.Thread(target=self.Server)
        self.thread.start()

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
app = wx.App(False)
win = MainWindow(None)
app.MainLoop()
