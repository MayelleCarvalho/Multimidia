# import socket
# from pip._vendor.distlib.compat import raw_input
#
# host = ''
# porta = 4801
#
# socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# print('Socket criado!')
#
# socket_server.bind((host,porta))
# print('Socket vinculado a porta!')
#
# print('\nSocket aguardando requisição...')
#
# while True:
#     #recebe msg do cliente:
#     msg_cliente, cliente = socket_server.recvfrom(2048)
#     print(cliente, msg_cliente.decode())
#
#     #envio de resposta ao cliente:
#     mensagem = raw_input('Digite uma resposta: ')
#     socket_server.sendto(mensagem.encode(),cliente)
#
#
# socket_server.close()


## teste:


import socket
import time

from pip._vendor.distlib.compat import raw_input

host = ''
porta = 3020

cont = 1
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado!')

socket_server.bind((host,porta))
print('Socket vinculado a porta!\nSocket aguardando conexão de cliente...')

while True:
    #recebe informação do arquivo do cliente:
    conteudo_cliente, endereco_cliente = socket_server.recvfrom(1024)
    print('Conectado à Cliente: ', endereco_cliente)

    qtd_envio = 0
    qtd_recebido = 0
    #controla a quantidade de partes do arquivo enviado:
    if conteudo_cliente != None:
        qtd_envio = int(conteudo_cliente)
        print('Arquivo possui %d  partes' % (qtd_envio))
    else:
        print('Quantidade de partes não foi enviado ou enviado com erro')
        break

    # nome_arquivo = 'arquivo00'+str(cont)+'.txt'
    arquivo = open('arquivo_00'+str(cont)+'.txt', 'wb')
    while True:
        #inicio de recebimento do conteudo do arquivo
        inicio = time.time() * 1000
        conteudo_cliente, endereco_cliente = socket_server.recvfrom(1024)
        fim = time.time() * 1000
        latencia = fim - inicio
        velocidade = 1000 / latencia * 1024

        if conteudo_cliente != None:
            #escreve o conteudo no arquivo criado:
            arquivo.write(conteudo_cliente)
            qtd_recebido += 1
            print('Recebido %d de %d partes' %(qtd_recebido, qtd_envio))
            print('Latência: %.3f' +latencia,'\n Velocidade: %.2f KB/s ' % (velocidade/1000))

        if qtd_recebido == qtd_envio :
            arquivo.close()
            cont += 1
            print('Arquivo recebido com sucesso!')
            break

socket_server.close()

