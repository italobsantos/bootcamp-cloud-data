import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as ex:
        print('A conexão falhou.')
        print('Erro: {}'.format(ex))
        sys.exit()

    print("Socket criado com sucesso!")

    host_alvo = input("Digite o Host ou Ip a ser conectado: ")
    porta_alvo = int(input("Digite a Porta a ser conectada: "))

    try:
        s.connect((host_alvo, porta_alvo))
        print('Cliente TCP conectado com sucesso no Hosta Alvo: {} e na Porta: {}'.format(host_alvo,porta_alvo))
        s.shutdown(2)

    except socket.error as ex:
        print("A conexão falhou.")
        print("Erro: {}".format(ex))
        sys.exit()


if __name__ == '__main__':

    main()