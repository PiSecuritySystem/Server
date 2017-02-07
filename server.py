import socket
port = 60000                 
s = socket.socket()          
#host = socket.gethostname() 
s.bind(('', port))           
s.listen(5)                  
print 'Waiting for client...'

conn, addr = s.accept()    
data_lock = True

data = conn.recv(1024)
print('Server received', repr(data))
while True:
    while data_lock:
        data = conn.recv(1024)
        print(data)
        if "exit" in data:
            conn.send('Server closing down')
            conn.close()
            data_lock = False
    s.listen(5)
    conn, addr = s.accept()
    data_lock = True
    data = conn.recv(1024)
