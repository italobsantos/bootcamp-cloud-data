# Tratamento de exceções


lista = [1, 10]
arquivo = open('teste_aula09.txt', 'r')
try:
    divisao = 10 / 1
    texto = arquivo.read()
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero.')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmetica.')
except IndexError:
    print('Erro ao acessar um indice inválido da lista.')
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não acontece uma exceção')
finally:
    print('Sempre executa com ou sem exceção.')
    arquivo.close()
