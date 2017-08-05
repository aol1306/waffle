import connection
import threading

class ServerHandler(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.running = True
        self.conn = conn
        
    def run(self):
        try:
            while self.running:
                msg = input("> ")
                self.conn.send_one_string_message(msg)
                recv = self.conn.recv_one_string_message() 
                print(recv)
                if msg == "exit":
                    self.conn.close()
                    self.running = False
        except:
            print("Connection closed")
            self.conn.close()
        
sock = connection.server_factory(5555)
print(sock)
# now accept connections
while True:
    print("Waiting for client...")
    (clientsocket, address) = sock.accept()
    print("Accept ", address)
    # start with listening for message
    conn = connection.Connection(clientsocket)
    # get hello message
    conn.recv_one_string_message()
    server_handler = ServerHandler(conn)
    server_handler.start()