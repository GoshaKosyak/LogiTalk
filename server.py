import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(("localhost",5000))
socket_server.setblocking(True)
socket_server.listen(1)
print("Підключився клієнт ")

conn, adress = socket_server.accept()

data = conn.recv(1024).decode()
conn.send(f"{data}, {adress}".encode())
conn.close()
socket_server.close()