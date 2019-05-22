import socket
import _thread

host = ''
porta = 5232

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado!')

socket_server.bind((host,porta))
print('Socket vinculado a porta!')

print('\nSocket executando!')

while True:
    msg, cliente = socket_server.recvfrom(1024)
    print(cliente, msg)

socket_server.close()