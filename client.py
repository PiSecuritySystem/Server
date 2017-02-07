# client.py

import socket                   # Import socket module
import signal

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.
s.connect(("152.10.193.79", port))
s.send("Hello server!")

while True:
    testVar = raw_input("-> ")
    s.send(testVar)
    if "exit" in testVar:
        break

s.close()


def signal_handler(signal, frame):
    s.send('exit')
    s.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
#with open('received_file', 'wb') as f:
#    print 'file opened'
#    while True:
#        print('receiving data...')
#        data = s.recv(1024)
#        print('data=%s', (data))
#        if not data:
#            break
#        # write data to a file
#        f.write(data)

#f.close()
#print('Successfully get the file')
#s.close()
#print('connection closed')
