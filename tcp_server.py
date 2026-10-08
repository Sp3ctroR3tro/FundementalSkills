import socket

SERVER_IP = '0.0.0.0' # Assigning an IP address that can accept connections from all network hosts.
SERVER_PORT = 1337

def main():
    # Creating the socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding the socket (must be a tuple for the bind)
    server.bind((SERVER_IP, SERVER_PORT))

    # Putting the server in a listening state allowing for up to 6 connections
    server.listen(6)
    print(f"[*] Server listenting on {SERVER_IP}:{SERVER_PORT}")

    # Accepting connections from clients
    while True:
        client, address = server.accept() # Accepting a connection from a client and returning a new socket object and the address of the client.
        with client as c_sock: # Using the socket object as a context manager to ensure it is closed after use.
            while True: # Continuously receiving data from the client until the connection is closed.
                request = c_sock.recv(1024) # Receiving data from the client in chunks of 1024 bytes.
                if not request: # If no data is received, it indicates that the client has closed the connection, so we break out of the loop.
                    break 
                print(f"Received: {request.decode('utf-8')}") # Printing the received data to the console after decoding it from bytes to a string.
                c_sock.sendall(request) # Sending the received data back to the client, effectively echoing it.

if __name__ == '__main__':
    main()