import socket

#Gets private IP address
host = socket.gethostbyname(socket.gethostname())
port = 9090
HOST = ''

#TCP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(host)

