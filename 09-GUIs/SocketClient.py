# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 23:30:15 2019

@author: GISWork
"""

import socket

socket_1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connecting to local machine port 5555
socket_1.connect(("localhost", 5555)) # Address tuple
socket_1.send(bytes("hello world", encoding="UTF-8")) 
