import socket              
import signal

s = socket.socket()         
host = socket.gethostname() 
port = 60000                
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
