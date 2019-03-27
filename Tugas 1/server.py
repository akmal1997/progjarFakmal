import socket
import sys

#TCP_IP Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost',10000)
print>>sys.stderr, 'starting up port on %s port %s' % server_address
s.bind(server_address)
s.listen(1)
while True:
    print >> sys.stderr, 'waiting for a connection'
    connection, client_address = s.accept()
    print >> sys.stderr, 'connection from', client_address

    while True:
        data = connection.recv(32)
        print>>sys.stderr, 'received "%s"' % data
        if data:
            print >> sys.stderr, 'sending data to the client'
            connection.sendall('-->'+data)
        else:
            print >> sys.stderr, 'no more data from', client_address
            break
        connection.close()
