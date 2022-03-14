import os

print("#" * 60)

ip_ou_host = input('Digite o ip ou host a ser verificado: ')
print("#" * 60)

os.system('ping {} -w 4 '.format(ip_ou_host))
print("-" * 60)
