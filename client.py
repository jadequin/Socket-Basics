import socket             

class Client():
    def __init__(self, host, port):    
        self.host = host # ip address of the communicating device
        self.port = port # 1227 or maybe 2712


    def sendMsg(self, msg):    
        self.s = socket.socket()   
        try:        
            self.s.connect((self.host, self.port))
            self.s.send(msg.encode('utf-8'))
            self.s.close()
        except:
            print("Couldn't reach server")



# how to use for example (just send messages with the client instance to a server)
client = Client('172.24.36.253', 2712) ### <--- CHANGE YOUR IP ADDRESS HERE
while True:
    msg = input('Type in your message: ')
    client.sendMsg(msg)