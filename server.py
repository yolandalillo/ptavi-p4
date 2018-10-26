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
            line = self.rfile.read()  # Leyendo lo que envia el cliente.
            line_client = line.decode('utf-8').split()
            if not line:
                break  # Termina el bucle
            else:
                print("Petición recibida \r\n")

            if line_client[0] == 'REGISTER':
                # Guardamos dirección e IP en nuestro diccionario.
                direccion = line_client[1].split(':')
                expires = int(line_client[4])
                time_actual = int(time.time())
                time_actual_str = time.strftime('%Y-%m-%d %H:%M:%S',
                                                time.gmtime(time_actual))
                time_exp = int(expires + time_actual)
                time_exp_string = time.strftime('%Y-%m-%d %H:%M:%S',
                                                time.gmtime(time_exp))
                lista = []
                for cliente in dic:

                    if time_actual_str >= dic[cliente][1]:
                        lista.append(cliente)

                dic[direccion[1]] = self.client_address[0]
                print("SIP/2.0 200 OK\r\n")
                self.wfile.write(b"SIP/2.0 200 OK" + b'\r\n\r\n')
                if line_client[4] == '0':
                    print("Borramos el diccionario")
                    del dic[direccion[1]]
                    print(dic)
                else:
                    print(dic, time_exp_string)
            self.register2json()

    def register2json(self):
        with open('registered.json', 'w') as archivo_json:
            json.dump(dic, archivo_json, sort_keys=True,
                      indent=4, separators=(',', ': '))


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
