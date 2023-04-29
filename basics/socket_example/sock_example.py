import socket

# The function returns a list of 5-tuples
print("getaddrinfo example")
results = socket.getaddrinfo("google.com", 443)
for result in results:
    print(f"IP: {result[4][0]}")

# Get the fully qualified domain name
print("getfqdn example")
print(socket.getfqdn("8.8.8.8"))
print(socket.getfqdn())

# Get the IP, does not support IPv6
print("gethostbyname example")
print(socket.gethostbyname("google.com"))

# Returns machine hostname where python is running
print("gethostname example")
print(socket.gethostname())

# Returns a tuple with 3 attributes
# ('dns.google', ['8.8.8.8.in-addr.arpa'], ['8.8.8.8'])
print("gethostbyaddr example")
print(socket.gethostbyaddr("8.8.8.8"))