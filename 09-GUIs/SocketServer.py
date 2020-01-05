# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 23:28:48 2019

@author: GISWork
"""

import socket

#setting up server socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#also set up on local host port 5555
serversocket.bind(('localhost', 5555))
serversocket.listen()

#reads from the socket
(socket_2, address) = serversocket.accept()

#assigns data from socket to variable
b = socket_2.recv(30)

print(str(b))
