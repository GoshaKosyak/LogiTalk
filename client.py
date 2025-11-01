import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.connect(("localhost",5000))
client_name = input("Повідомлення від сервера: ")
socket_server.send(client_name.encode())

responce = socket_server.recv(1024).decode()
print(responce)
socket_server.close()