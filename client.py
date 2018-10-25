#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
LINE = sys.argv[3:]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto

try:
    SERVER, PORT, METHOD, USER, EXVAL = sys.argv[1:]
except ValueError:
    sys.exit("Debe introducir los siguientes datos: client.py ip "
             "puerto register sip_address expires_value")
REG = ("REGISTER sip:" + USER + " SIP/2.0\r\nExpires: " + EXVAL + "\r\n\r\n")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, int(PORT)))
    my_socket.send(bytes(REG, 'utf-8') + b'\r\n')

    try:
        data = my_socket.recv(1024).decode('utf-8')
    except ConnectionRefusedError:
        sys.exit("NO se puede conectar al servidor")
    print(data)
