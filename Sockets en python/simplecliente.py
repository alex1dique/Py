#!/usr/bin/python          


import socket               # Importar el modulo socket 

s = socket.socket()         # Crea un   objeto socket 
host = socket.gethostname() # Obtener el nombre de la maquina 
port = 12345                # Reserva  este puerto para la conexion.

s.connect((host, port))		#Establece conexion 
print s.recv(1024)
s.close                     # Close the socket when done
