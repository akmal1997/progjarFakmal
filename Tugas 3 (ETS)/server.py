import os
import sys
import glob
import json
import socket

def checkArg(cmd, data):
    return {'cmd' : cmd, 'data' : data}

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket berhasil dibuat"
except socket.error as err:
    print "socket gagal dengan kesalahan %s" %(err)
    sys.exit()

port = 5000

s.bind(('', port))
print "Port yang ditunjuk adalah port %s" %(port) 

def ls(c,data):
    if ('arg' not in rcvdData):
        files = glob.glob('*')
    else:
        files = os.listdir('.')

    for name in files:
        data = data + name + '   '
    data = checkArg('LS',data)
    c.sendall(json.dumps(data))

def get(c,data):
    if ('arg' not in rcvdData):
        c.sendall(json.dumps({'cmd' : 'GET','err' : 'syntax error'}))
    else:
        filename = './' + rcvdData['arg']
        if os.path.exists(filename):
            c.sendall(json.dumps({'cmd' : 'GET', 'action': 'Berhasil'}))
            with open(filename, 'rb') as f:
                for line in f:
                    c.sendall(line)
        else:
            c.sendall(json.dumps({'cmd' : 'GET','err' : 'File tidak ada'}))

def put(c,data):
    if ('err' in rcvdData):
        print rcvdData['err']
    else:
        filename = rcvdData['arg']
        with open(os.path.join('./', filename), 'wb') as f:
            while (True):       
                l = c.recv(1024)
                while (l):
                    f.write(l)
                    l = c.recv(1024)
                break    

def rm(c,data):
    if ('arg' not in rcvdData):
        c.sendall(json.dumps({'cmd' : 'RM','err' : 'syntax error'}))
    else:
        filename = './' + rcvdData['arg']
        if os.path.exists(filename):
            c.sendall(json.dumps({'cmd' : 'RM', 'action': 'Berhasil'}))
            os.remove(filename)
        else:
            c.sendall(json.dumps({'cmd' : 'RM','err' : 'File tidak ada'}))       

s.listen(5)

while True:
    c, addr = s.accept()
    data = ""
    rcvdData = c.recv(1024)
    print "Client:",rcvdData
    rcvdData = json.loads(rcvdData)
    if (rcvdData['cmd'] == 'LS'):
        ls(c,data)

    elif(rcvdData['cmd'] == 'GET'):
        get(c,data)

    elif(rcvdData['cmd'] == 'PUT'):
        put(c,data)

    elif(rcvdData['cmd'] == 'RM'):
        rm(c,data)
        
    elif(rcvdData['cmd'] == 'HELP'):
        continue

    elif(rcvdData['cmd'] == 'QUIT'):
        break

    else:
        c.sendall(json.dumps({'cmd' : 'QUIT','data' : 'Command Tidak Diketahui!'}))

    c.close()

s.close()
