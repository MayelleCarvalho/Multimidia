import socket
from pip._vendor.distlib.compat import raw_input

host_server = '127.0.0.1'
porta_cliente = 5500

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.connect((host_server, porta_cliente))
print('Conectado ao servidor')
mensagem = raw_input('Digite uma msg: ')

while mensagem != '\x18':
    socket_server.send(mensagem.encode())
    mensagem = raw_input('Digite uma msg: ').encode()

socket_server.close()

##### teste

# host_server = '127.0.0.1'
# porta_cliente = 5440
#
# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# socket_server.connect((host_server, porta_cliente))
# print('Conectado ao servidor')
# mensagem = raw_input('Digite o nome do arquivo: ')
#
# while mensagem != '27':
#     socket_server.send(mensagem.encode())
#     print('arquivo enviado!')
#     resposta = socket_server.recv(2048)
#     print('Servidor: ', resposta)
#     mensagem = raw_input('Digite uma msg: ')
#
# socket_server.close()