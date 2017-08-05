import connection
import threading
import time

commands = []

class ServerHandler(threading.Thread):
    def __init__(self, conn, id):
        threading.Thread.__init__(self)
        print("Thread with id", id, "has been created")
        print(len(commands), "sessions available")
        self.id = id
        self.running = True
        self.conn = conn
        
    def run(self):
        try:
            while self.running:
                self.get_and_handle_command()
        except Exception as e:
            print("Connection closed")
            print(e)
            self.conn.close()
            
    def get_and_handle_command(self):
        if commands[self.id] != "":
            msg = commands[self.id]
            self.conn.send_one_string_message(msg)
            recv = self.conn.recv_one_string_message() 
            print(recv)
            if msg == "exit":
                self.conn.close()
                self.running = False
            commands[self.id] = ""
        else:
            time.sleep(0.1)

class UI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.current_session = 0
        self.running = True
        
    def run(self):
        while self.running:
            print("Current session:", self.current_session)
            cmd = input("Enter command (session [id] to change session): ")
            if cmd.split()[0] != "session":
                commands[self.current_session] = cmd
            else:
                self.current_session = int(cmd.split()[1])
            
sock = connection.server_factory(5555)
session_counter = 0
print(sock)
ui = UI()
ui.start()
# now accept connections
while True:
    print("Waiting for client...")
    (clientsocket, address) = sock.accept()
    print("Accept ", address)
    # start with listening for message
    conn = connection.Connection(clientsocket)
    # get hello message
    conn.recv_one_string_message()
    server_handler = ServerHandler(conn, session_counter)
    commands.append("")
    session_counter += 1
    server_handler.start()