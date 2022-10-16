import socket

#Gets private IP address
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9090

#TCP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()

