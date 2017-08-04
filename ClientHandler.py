import connection
import threading
import CommandHandler

class ClientHandler:
    def __init__(self, conn):
        self.conn = conn
        self.send_hello_message()
        self.main_loop()
        
    def send_hello_message(self):
        self.conn.send_one_string_message("hello")
        
    def main_loop(self):
        try:
            command_handler = CommandHandler.CommandHandler()
            while True:
                print("Waiting for message")
                msg = self.conn.recv_one_string_message()
                response = command_handler.handle_command(msg)
                self.conn.send_one_string_message(response)
        except TypeError:
            print("Connection closed")
            
    def get_response(self):
        pass