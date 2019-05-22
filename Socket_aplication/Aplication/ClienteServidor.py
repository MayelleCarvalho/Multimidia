import socket
import sys
from _thread import *

HOST = '127.0.0.1'
PORT = 50500

# para UDO USAR: socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket criado!')

## associando o socket com a porta e o host informado
try:
    socket_server.bind((HOST, PORT))
except socket.error as msg:
    print('Erro no bind. Código: ' +str(msg[0]) + 'Mensagem: ' +msg[1])
    sys.exit()

print('Socket ligado!')

socket_server.listen(10)
print('Socket sendo escutado!!!')

def cliente_thread(conn):

    mensagem = 'Você está conectado '
    msg_codificada = mensagem.encode()
    conn.send(msg_codificada)

    while True:

        dado = conn.recv(1024)
        reply = 'ok...' + dado.decode()
        if not dado:
            break

        conn.sendall(reply.encode())

    conn.close()

while 1:

    conn, addr = socket_server.accept()
    print('Conectado com o endereço: ' + addr[0] + ':' + str(addr[1]))

    start_new_thread(cliente_thread,(conn,))

socket_server.close()
