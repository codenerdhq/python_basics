import socket
from datetime import datetime

server_addr = ("localhost", 6789)
max_buffer = 4096

print(f"Client starts at: {datetime.now()}" )
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello!!!", server_addr)
data, server = client.recvfrom(max_buffer)
print(f"{datetime.now()}: {server} said: {data}")
client.close()