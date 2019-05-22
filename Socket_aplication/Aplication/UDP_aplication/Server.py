import socket
import _thread

from pip._vendor.distlib.compat import raw_input

host = ''
porta = 4850

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado!')

socket_server.bind((host,porta))
print('Socket vinculado a porta!')

print('\nSocket executando!')

while True:
    msg_cliente, cliente = socket_server.recvfrom(2048)
    print(cliente, msg_cliente)
    mensagem = raw_input('Digite uma resposta: ').encode()
    socket_server.sendto(mensagem,cliente)


socket_server.close()