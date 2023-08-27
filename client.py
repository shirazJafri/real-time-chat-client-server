import socket
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
BUFFER_SIZE = int(os.getenv("BUFFER_SIZE"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(b"Hello World!")
    received_data = client_socket.recv(BUFFER_SIZE)

print(f"Message from the server: {received_data}")
