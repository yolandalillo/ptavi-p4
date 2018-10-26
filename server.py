#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegistrerHandler(socketserver.DatagramRequestHandler):
    """
        SIP server class
    """
    dic = {}

    def handle(self):
        """
        handle method of the server class
        (all requests will be handled by this method)
        """
        datos = self.rfile.read().decode('utf-8')
        print(datos)




        self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")
        print(self.client_address)
        for line in self.rfile:
            if line.decode('utf-8')[:8] == 'REGISTER':
                print("El cliente nos envia:", line.decode('utf-8'))
                user = line.decode('utf-8')[13:-10]
                self.dic['DIRECCION'] = user
                self.dic['IP'] = self.client_address[0]
        print(self.dic)


if __name__ == "__main__":
    # Listens at localhost ('') port 6001
    # and calls the EchoHandler class to manage the request
    try:
        PORT = int(sys.argv[1])
    except IndexError:
        sys.exit("Debe introducir: server.py port_number")

    serv = socketserver.UDPServer(('', PORT), SIPRegistrerHandler)
    print("Lanzando servidor UDP de SIP...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
