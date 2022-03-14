import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado com sucesso.')

host = 'localhost'

porta = 5432

# Ligação entre cliente servidor entre o host e porta
s.bind((host, porta))

mensagem = '\nServidor : Olá cliente !!!!'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)



