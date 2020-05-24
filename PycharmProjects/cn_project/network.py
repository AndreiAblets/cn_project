import socket
import pickle


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET refers to the address family ipv4.
        self.server = "192.168.0.105"                                   #The SOCK_STREAM means connection oriented TCP protocol.
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):

        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(512))
        except:
            print('error')

    def send(self, data):

        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(512))
        except EOFError as e:
            print(e)

