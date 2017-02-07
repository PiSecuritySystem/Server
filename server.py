import socket
port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
#host = socket.gethostname()     # Get local machine name
s.bind(('', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
print 'Server listening....'

conn, addr = s.accept()     # Establish connection with client.
data_lock = True

print 'Got connection from', addr
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
