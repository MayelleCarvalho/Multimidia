import socket

from pip._vendor.distlib.compat import raw_input

host_server = '127.0.0.1'
porta_cliente = 2523

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.connect((host_server, porta_cliente))
print('Conectado ao servidor')
mensagem = raw_input('Digite uma msg: ')

while mensagem != '\x18':
    socket_server.send(mensagem.encode())
    mensagem = raw_input('Digite uma msg: ').encode()

socket_server.close()