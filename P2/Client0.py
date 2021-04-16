import socket

class Client:
    def __init__(self, ip,port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK")
    def advanced_ping(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, sel.port))
