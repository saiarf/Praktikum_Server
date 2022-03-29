#!usr/bin/python 
from ast import arg
import socket, sys 

def server(host, port): 
    s = socket.socket() 
    s.bind((host, port)) 
    s.listen(1) 
    print('Menunggu Client....') 
    print('{:<12}: {:}'.format('SERVER IP',s.getsockname()[0]))  	
    print('{:<12}: {:}'.format('SERVER PORT',s.getsockname()[1]))   	
    while True:
        c, addr = s.accept() 
        msg = '{}'.format(c.recv(1024).decode())
        if msg:
            print('dari CLIENT: ', msg)
            c.send('{}'.format(msg).encode())

def client(server_ip, server_port): 
    while True: 
        s = socket.socket() 
        s.connect((server_ip, server_port))   	 	
        pesan=input(">>: ")   	 	
        if pesan == 'q': 
            break
        
        s.send(pesan.encode())
        msg = 'dari SERVER: {}'.format(s.recv(1024).decode())
        print(msg)
        s.close()

# petunjuk : 
help= "’’’"
# python3 praktikum3_npm_cs.py [server/client] [IP] [Port] 
# contoh perintah : sebagai SERVER 
# python3 praktikum3_npm_cs.py server 192.168.2.24 3344 
# python3 praktikum3_npm_cs.py server - 3344 
 
# contoh perintah : sebagai CLIENT 	
# python3 praktikum3_npm_cs.py client 192.168.2.24 3344 
#"’’’" 
 
# default host and port 
def_host = '0.0.0.0' 
args = sys.argv[1:]

if len(args) == 3:
    if args[0] == 'server':
        if args[1] == "-":
            server(def_host, int(args[2]))
        if args[1] != "-":
            server(args[1], int(args[2]))

    if args[0] == 'client':
        client(args[1], int(args[2]))
    if args[0] != 'client' and args[0] != 'server':
        print(help)
else:
    print(help)