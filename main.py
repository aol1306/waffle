import window_hide
import socket

DEBUG = True

def init():
    if DEBUG == False:
        window_hide.hide_console_window()

def try_connect_and_handle():
    # connect to remote server
    # on success: pass execution to handler
    pass
        
def main_loop():
    print("Enter main loop")
    while True:
        try_connect_and_handle()
        
def main():
    init()
    main_loop()

if __name__ == "__main__":
    main()