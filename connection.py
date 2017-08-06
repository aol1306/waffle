import socket
import struct

def make_client_connection():
    sock = client_factory("127.0.0.1", 5555)
    return Connection(sock)

def client_factory(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Connected")
    return s
    
def server_factory(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", port))
    s.listen(5)
    return s

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return buf
        buf += newbuf
        count -= len(newbuf)
    return buf

class Connection:
    def __init__(self, sock):
        self.sock = sock

    def send_one_string_message(self, str):
        self.send_one_message(str.encode("utf-8"))
        
    def recv_one_string_message(self):
        return self.recv_one_message().decode("utf-8")
        
    def send_one_message(self, data):
        length = len(data)
        self.sock.sendall(struct.pack('!I', length))
        self.sock.sendall(data)
        
    def recv_one_message(self):
        lengthbuf = recvall(self.sock, 4)
        length, = struct.unpack('!I', lengthbuf)
        return recvall(self.sock, length)
        
    def close(self):
        self.sock.close()