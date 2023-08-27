import socket
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
BUFFER_SIZE = int(os.getenv("BUFFER_SIZE"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server is listening at port {PORT}.")
    client_socket, client_address = server_socket.accept()
    with client_socket:
        print(f"{client_address} just connected to the server!")
        while True:
            data_received = client_socket.recv(BUFFER_SIZE)
            if not data_received:
                print(f"{client_address} just disconnected from the server!")
                break
            client_socket.sendall(data_received)
