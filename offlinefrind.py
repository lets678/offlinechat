import socket

HOST = input("enter friend ip:") # Your tab's IP address
PORT = 12345          # The same unique port number used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print('Connected to server')

while True:
    data = client_socket.recv(1024)
    print('Friend:', data.decode('utf-8'))
    message = input('You: ')
    client_socket.send(message.encode('utf-8'))
