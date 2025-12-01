import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #file handle that does not have data associated with it yet
mysock.connect(('data.pr4e.org', 80)) #function, #tuple
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #send http command
mysock.send(cmd)

while True:
    data = mysock.recv(512) #receive up to 512 characters
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()
