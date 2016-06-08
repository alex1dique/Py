import wx
from socket import *
from time import ctime
import random
import threading
import serial
# definir el puerto por el cual se recibiran las peticiones
port=8080
#Definimos el host,Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
host = ''
#definimos una tupla con los datos del host y el puerto
addr = (host, port)
#definimos en la variable  la cantidad de bytes para recibir desde un cliente
bufsiz = 1024
#definimos el puerto para conexion del arduino
serialport='/dev/ttyACM0'
#definimos la velocidad de transmision en baudios
baud= 9600
#establecemos la conexion al arduino
arduino = serial.Serial(serialport,baud) 
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

        tcpServer = socket(AF_INET , SOCK_STREAM)
        tcpServer.bind(addr)
        tcpServer.listen(5)
        try:
            while True:
                self.Print("Esperando la conexion...")
                tcpClient, caddr = tcpServer.accept()
                self.Print("Conectado desde {}".format(caddr))

                while True:
                    data = tcpClient.recv(bufsiz)
                    if not data:
                        break
                    #escribimos datos al arduino a traves del puerto serie    
                    arduino.write(data)      
                    tcpClient.send('[%s]\nData\n%s' % (ctime(), data))
                    self.Print(data)
                tcpClient.close()

        except KeyboardInterrupt:
            tcpServer.close()

	def __del__(self):
		#cerramos las conexiones del socket, del arduino y el form
		self.tcpServer.close()
		self.arduino.close()
		self.Close()
app = wx.App(False)
win = MainWindow(None)
app.MainLoop()
