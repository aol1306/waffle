import connection
import threading

class ClientHandler:
    def __init__(this, conn):
        this.conn = conn
        this.send_hello_message()
        this.main_loop()
        
    def send_hello_message(this):
        this.conn.send_one_string_message("hello")
        
    def main_loop(this):
        try:
            while True:
                print("Waiting for message")
                print("Got message: ", this.conn.recv_one_string_message())
                this.conn.send_one_string_message("ACK")
        except TypeError:
            print("Connection closed")