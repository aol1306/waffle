import connection

def main_loop(conn):
    try:
        while True:
            msg = input("> ")
            conn.send_one_string_message(msg)
            recv = conn.recv_one_string_message() 
            print(recv)
            if msg == "exit":
                conn.close()
                break
    except:
        print("Connection closed")
        conn.close()
        
sock = connection.server_factory(5555)
print(sock)
# now accept connections
while True:
    print("Waiting for client...")
    (clientsocket, address) = sock.accept()
    print("Accept ", address)
    # start with listening for message
    conn = connection.Connection(clientsocket)
    # get hello message
    conn.recv_one_string_message()
    main_loop(conn)