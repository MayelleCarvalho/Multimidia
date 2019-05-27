# import socket
# from pip._vendor.distlib.compat import raw_input
#
# host_server = '127.0.0.1'
# porta_server = 4850
#
# socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# socket_cliente.connect((host_server, porta_server))
# print('Conectado ao servidor')
#
# mensagem = raw_input('Digite uma msg: ')
#
# while mensagem != '27':
#     socket_cliente.sendto(mensagem.encode(), ((host_server, porta_server)))
#     mensagem_server = socket_cliente.recvfrom(2048)
#     print(mensagem_server)
#     mensagem = raw_input('Digite uma msg: ')
#
# socket_cliente.close()


##teste:

import math
import os
import socket
import time

from pip._vendor.distlib.compat import raw_input

host_server = '127.0.0.1'
porta_server = 3020

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket_cliente.connect((host_server, porta_server))
print('Conectado ao servidor')

nome_arquivo = input('Informe um arquivo: ')
arquivo = open(nome_arquivo,'rb')

conteudo = arquivo.read(1024)

qtd_envio = math.ceil(os.path.getsize(nome_arquivo) / 1024)

# socket_cliente.sendto('Arquivo sendo enviado, informações: %d  partes' + str(qtd_envio).encode('utf-8'), ((host_server, porta_server)))
socket_cliente.sendto(str(qtd_envio).encode('utf-8'), ((host_server, porta_server)))

cont = 1
tempo_espera = 0.000
while conteudo:
    time.sleep(tempo_espera)
    tempo_espera +=10

    socket_cliente.sendto(conteudo, ((host_server, porta_server)))
    print('Enviado parte %d de %d partes: ' % (cont, qtd_envio))
    # envio de próxima parte de byte
    conteudo = arquivo.read(1024)
    cont += 1

arquivo.close()
socket_cliente.close()