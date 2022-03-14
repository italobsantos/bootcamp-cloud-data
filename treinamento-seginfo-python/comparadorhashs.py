import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print("Os arquivos são diferentes.")
    print('O hash do arquivo a.txt é: {}', hash1.hexdigest())
    print('O hash do arquivo b.txt é: {}', hash2.hexdigest())

else:
    print("Os arquivos são iguais")
    print('O hash do arquivo a.txt é: {}', hash1.hexdigest())
    print('O hash do arquivo b.txt é: {}', hash2.hexdigest())
