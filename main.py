import window_hide
import socket
import connection
import ClientHandler
import threading
import time

DEBUG = True

class MainConnectionThread(threading.Thread):
    def __init__(self):
        self.running = True
        threading.Thread.__init__(self)
        
    def run(self):
        while self.running:
            self.try_connect_and_handle()
            time.sleep(3)
            
    def try_connect_and_handle(self):
        try:
            conn = connection.make_client_connection()
            ClientHandler.ClientHandler(conn)
        except ConnectionRefusedError:
            print("Connection error. Retrying soon.")

def init():
    if DEBUG == False:
        window_hide.hide_console_window()
        
def main():
    init()
    main_connection_thread = MainConnectionThread()
    main_connection_thread.start()
    main_connection_thread.join()
    print("Main exit")

if __name__ == "__main__":
    main()