from datetime import datetime
import socket

address = ("localhost", 6789)
max_size = 4096

print(f"Starting the server at: {datetime.now()}")
print(f"Waiting for a client to send data.")
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(address)
data, client = server.recvfrom(max_size)
print(f"{datetime.now()}: {client} said: {data}")
server.sendto(b"Are you talking?", client)
server.close()