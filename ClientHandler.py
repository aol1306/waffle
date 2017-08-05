import connection
import threading
import subprocess

class ClientHandler:
    def __init__(self, conn):
        self.conn = conn
        self.running = True
        self.send_hello_message()
        self.run()
        
    def send_hello_message(self):
        self.conn.send_one_string_message("hello")
        
    def run(self):
        try:
            while self.running:
                print("Waiting for message")
                msg = self.conn.recv_one_string_message()
                response = self.create_response(msg)
                self.conn.send_one_string_message(response)
        except TypeError as e:
            print("Connection closed")
            print(e)
            
    def create_response(self, message):
        return self.handle_command(message)
            
    def handle_command(self, command):
        print("Handling command", command)
        if command == "exit":
            self.running = False
            return("ACK")
        if command == "shell":
            return "Will spawn shell session, not implemented yet"
        else:
            return "Unknown command"