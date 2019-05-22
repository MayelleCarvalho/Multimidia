import socket
from pip._vendor.distlib.compat import raw_input

host_server = '127.0.0.1'
porta_server = 4850

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_cliente.connect((host_server, porta_server))
print('Conectado ao servidor')
mensagem = raw_input('Digite uma msg: ')

while mensagem != '\x18':
    socket_cliente.sendto(mensagem.encode(), ((host_server, porta_server)))
    mensagem_server, server = socket_cliente.recvfrom(2048)
    print(mensagem_server)
    mensagem = raw_input('Digite uma msg: ').encode()

socket_cliente.close()