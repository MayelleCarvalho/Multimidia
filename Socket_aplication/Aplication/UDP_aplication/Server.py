import socket
from pip._vendor.distlib.compat import raw_input

host = ''
porta = 4850

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado!')

socket_server.bind((host,porta))
print('Socket vinculado a porta!')

print('\nSocket aguardando requisição...')

while True:
    #recebe msg do cliente:
    msg_cliente, cliente = socket_server.recvfrom(2048)
    print(cliente, msg_cliente.decode())

    #envio de resposta ao cliente:
    mensagem = raw_input('Digite uma resposta: ')
    socket_server.sendto(mensagem.encode(),cliente)


socket_server.close()