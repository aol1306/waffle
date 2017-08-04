import connection

sock = connection.server_factory(5555)
print(sock)
# now accept connections

def main_loop(conn):
    try:
        while True:
            msg = input("> ")
            conn.send_one_string_message(msg)
            print("Got: ", conn.recv_one_string_message())
    except:
        print("Connection closed")
        conn.close()

while True:
    print("Waiting for client...")
    (clientsocket, address) = sock.accept()
    print("Accept ", address)
    # start with listening for message
    conn = connection.Connection(clientsocket)
    # get hello message
    print("Got: ", conn.recv_one_string_message())
    main_loop(conn)