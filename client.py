#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Programa cliente UDP que abre un socket a un servidor."""

import socket
import sys

try:
    SERVER, PORT, METHOD, USER, EXPIRES = sys.argv[1:]
except ValueError:
    sys.exit("Debe introducir los siguientes datos: client.py ip "
             "puerto register sip_address expires_value")
SIP = ("REGISTER sip:" + USER + " SIP/2.0\r\nExpires: " + EXPIRES + "\r\n\r\n")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, int(PORT)))
    print("Enviando: " + "REGISTER sip:" + USER + " SIP/2.0" + "\r\n")
    print("Expires: " + EXPIRES + "\r\n\r\n")
    my_socket.send(bytes(SIP, 'utf-8') + b'\r\n')

    try:
        data = my_socket.recv(1024).decode('utf-8')
    except ConnectionRefusedError:
        sys.exit("No se puede conectar al servidor")
    print(data)
