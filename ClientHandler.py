import connection
import threading
import subprocess

class ClientHandler:
    def __init__(self, conn):
        self.conn = conn
        self.state = "normal"
        self.send_hello_message()
        self.main_loop()
        
    def send_hello_message(self):
        self.conn.send_one_string_message("hello")
        
    def main_loop(self):
        try:
            while True:
                print("Waiting for message")
                msg = self.conn.recv_one_string_message()
                response = self.create_response(msg)
                self.conn.send_one_string_message(response)
        except TypeError as e:
            print("Connection closed")
            print(e)
            
    def create_response(self, message):
        if self.state == "normal":    
            return self.handle_normal_command(message)
        elif self.state == "shell":
            return self.handle_shell_command(message)
            
    def handle_normal_command(self, command):
        print("Handling normal command", command)
        if command == "exit":
            exit()
        if command == "shell":
            self.state = "shell"
            print("state: shell")
            return "Switched to shell"
        else:
            return "Unknown command"
            
    def handle_shell_command(self, command):
        print("Handling shell command", command)
        if command == "exit":
            self.state = "normal"
            print("state: normal")
            return "exit"
        else:
            result = str(subprocess.getoutput(command))
            return result