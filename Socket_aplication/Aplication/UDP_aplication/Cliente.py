import socket
from pip._vendor.distlib.compat import raw_input

host_server = '127.0.0.1'
porta_server = 5232

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_server.connect((host_server,porta_server))
print('Conectado ao servidor')
mensagem = raw_input('Digite uma msg: ')

while mensagem != '\x18':
    socket_server.sendto(mensagem.encode(),((host_server,porta_server)))
    mensagem = raw_input('Digite uma msg: ').encode()

socket_server.close()