import connection
import threading
import time

commands = []

class ServerHandler(threading.Thread):
    def __init__(self, conn, id):
        threading.Thread.__init__(self)
        print("Thread with id", id, "has been created")
        print(len(commands)+1, "sessions available")
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
        self.help()
        
    def run(self):
        while self.running:
            time.sleep(0.2)
            cmd = input(str(self.current_session)+"> ")
            self.handle_cmd(cmd)
                
    def handle_cmd(self, cmd):
        cmd_splitted = cmd.split()
        if len(cmd_splitted) > 0 and cmd_splitted[0] == "session":
            self.current_session = int(cmd_splitted[1])
        else:
            try:
                commands[self.current_session] = cmd
            except IndexError:
                print("Invalid session", self.current_session)
    
    def help(self):
        print("session [id] to change session")
            
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
    print("Conn type:",conn.recv_one_string_message())
    server_handler = ServerHandler(conn, session_counter)
    commands.append("")
    session_counter += 1
    server_handler.start()