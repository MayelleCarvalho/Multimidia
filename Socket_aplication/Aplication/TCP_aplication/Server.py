import socket
import _thread

# host = ''
# porta = 2523
#
# def conectado(con, cliente):
#     print('Conectado por', cliente)
#
#     while True:
#         msg = con.recv(1024)
#         if not msg: break
#         print(cliente, msg)
#
#     print ('Finalizando conexao do cliente', cliente)
#     con.close()
#     _thread.exit()
#
# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print('Socket criado!')
#
# socket_server.bind((host,porta))
# print('Socket vinculado a porta!')
#
# socket_server.listen(1)
# print('Socket executando!')
#
# while True:
#     con, cliente = socket_server.accept()
#     _thread.start_new_thread(conectado, tuple([con, cliente]))
#
# socket_server.close()
#

#####teste

host = ''
porta = 2523


def conectado(con, cliente):
    print('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, msg)

    print ('Finalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()



socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket criado!')

socket_server.bind((host,porta))
print('Socket vinculado a porta!')

socket_server.listen(5)
print('Socket executando!')

while True:
    cliente, endereco = socket_server.accept()
    _thread.start_new_thread(conectado, tuple([cliente, endereco]))

socket_server.close()