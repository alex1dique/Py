#!/usr/bin/python          

import socket                 # Importar el modulo socket 

s = socket.socket()          # Crea un   objeto socket 
host = socket.gethostname()  # Obtener el nombre de la maquina 
port = 12345                # Reserva  este puerto para la conexion.
s.bind((host, port))        # enlace al puerto

s.listen(5)                 # Esperando la conexion del cliente
while True:
   c, addr = s.accept()     # Establece  la conexion del cliente
   print 'conectado desde', addr
   c.send('Gracias por conectarse....')  # Envia un mensaje al cliente
   c.close()                # Cierra la conexion
