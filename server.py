import socket
from threading import Thread

class Server(Thread):
    def __init__(self, incomingData, host, port):
        self.incomingData = incomingData
        self.host = host    # your own ip address
        self.port = port    # 2712 or maybe 1227

        Thread.__init__(self)
        Thread.start(self)


    def run(self):
        print('Server started')
        s = socket.socket()

        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        s.bind((self.host, self.port))

        s.listen(5)
        while True:
            c, addr = s.accept() #loop freezes here and waits for new inputs
            #print ('Got connection from',addr)
            msg = c.recv(1024).decode('utf-8')
            self.incomingData(msg) #trigger the function from outside
            c.close()

# how to use for example (attach a function to the instance of the class)
def incomingData(s):
    print(s)

Server(incomingData, '172.24.36.253', 2712) ### <--- CHANGE YOUR IP ADDRESS HERE