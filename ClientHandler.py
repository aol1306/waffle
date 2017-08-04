import connection
import threading
import CommandHandler

class ClientHandler:
    def __init__(this, conn):
        this.conn = conn
        this.send_hello_message()
        this.main_loop()
        
    def send_hello_message(this):
        this.conn.send_one_string_message("hello")
        
    def main_loop(this):
        try:
            command_handler = CommandHandler.CommandHandler()
            while True:
                print("Waiting for message")
                msg = this.conn.recv_one_string_message()
                response = command_handler.handle_command(msg)
                this.conn.send_one_string_message(response)
        except TypeError:
            print("Connection closed")