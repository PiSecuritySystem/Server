import socket 
import thread

clients = []

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
            print 'Client', index, '>>', msg
    clientsocket.close()

s = socket.socket()       
port = 60000              
print 'Server started!'
print 'Waiting for clients...'
s.bind(('', port))        
s.listen(5)                

while True:
   c, addr = s.accept()    
   clients.append(addr[1])
   thread.start_new_thread(on_new_client,(c,addr,len(clients)))
s.close()
