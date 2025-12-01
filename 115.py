#Networked Programs

#Sockets in Python

#Python has built-in support for TCP Sockets

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#data.pr4e.org -- Host
#80 -- Port

"""
http://www.dr-chuck.com/page1.htm
http:// -- protocol
www.dr-chuck.com -- host
page1.htm -- document
"""