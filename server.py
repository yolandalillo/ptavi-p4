#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de SIP en UDP simple
"""

import socketserver
import sys
import json
import time

class SIPRegistrerHandler(socketserver.DatagramRequestHandler):
    """
        SIP server class
    """

    def handle(self):

        while 1:
            #Leyendo lo que envia el cliente.
            line = self.rfile.read()
            line_client = line.decode('utf-8').split()
            if not line:
                break #Termina el bucle
            else:
                print("Petición recibida \r\n")

            if line_client[0] == 'REGISTER':
                #Guardamos dirección e IP en nuestro diccionario.
                direccion = line_client[1].split(':')
                dic[direccion[1]] = self.client_address[0]
                print("SIP/2.0 200 OK\r\n")
                self.wfile.write(b"SIP/2.0 200 OK" + b'\r\n\r\n')
                if line_client[4] == '0':
                    print("Borramos del diccionario")
                    del dic[direccion[1]]
                else:
                    print(dic)

if __name__ == "__main__":

    dic = {}
    try:
        PORT = int(sys.argv[1])
    except IndexError:
        sys.exit("Debe introducir: server.py port_number")
    """Creamos UDP en el puerto que indicamos utilizando la clase."""
    serv = socketserver.UDPServer(('', PORT), SIPRegistrerHandler)
    print("Iniciando servidor... \r\n")
    try:
        """Creamos el servidor"""
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
