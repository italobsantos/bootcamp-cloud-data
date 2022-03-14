# Faz ping em diversos ips

import os
import time


with open ('hosts.txt','r') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verificando o ip: ',ip)
        print('-' * 60)
        os.system('ping {} -w 2'.format(ip))
        print('-' * 60)
        time.sleep(5)