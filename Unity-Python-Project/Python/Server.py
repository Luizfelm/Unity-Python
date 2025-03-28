import socket

# Define server host and port
HOST = '127.0.0.1'  # Localhost address
PORT = 5005         # Port to listen on

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the specified host and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen()
print("Waiting for connection...")

# Accept a connection from a client
conn, addr = server_socket.accept()
print(f"Connected to {addr}")  # Log the client's address

try:
    # Main loop to send messages to the client
    while True:
        # Prompt the user to enter a message to send to the Unity client
        message = input("Enter message for Unity: ")
        
        # Send the message to the client, appending a newline character
        conn.sendall((message + "\n").encode())
except KeyboardInterrupt:
    # Handle graceful shutdown on keyboard interrupt (Ctrl+C)
    print("Closing connection.")
    conn.close()  # Close the client connection
    server_socket.close()  # Close the server socket