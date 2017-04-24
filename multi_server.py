#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import thread

clients = []


from Crypto.Cipher import AES

def do_decrypt(ciphertext):
    obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
    message = obj2.decrypt(ciphertext)
    return message


def on_new_client(clientsocket,addr,index):
    print clients
    while True:
        try:
            msg = clientsocket.recv(1024)
            if not msg: break
        except socket.error, e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                sleep(1)
                print 'No data available'
                continue
            else:
                print e
                sys.exit(1)
        else: 
            print 'Client', index, '>>', do_decrypt(msg)
    clientsocket.close()

s = socket.socket()         # Create a socket object
port = 60000                # Reserve a port for your service.
print 'Server started!'
print 'Waiting for clients...'
s.bind(('', port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.

while True:
   c, addr = s.accept()     # Establish connection with client.
   clients.append(addr[1])
   thread.start_new_thread(on_new_client,(c,addr,len(clients)))
s.close()
