from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('O Carro do piloto {} percorreu {} km \n'.format(piloto, trajeto))



if __name__ == '__main__':

    #carro1(10)
    #carro2(20)

    t_carro1 = Thread(target=carro, args=[10, 'Carlos'])
    t_carro2 = Thread(target=carro, args=[20, 'João'])

    t_carro1.start()
    t_carro2.start()