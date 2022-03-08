# Criando erros personalizados


class Error(Exception):
    pass


class InputError(Error):

    def __init__(self,message):
        self.message = message


while True:
    try:
        x = int(input('Entre com um número de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10.')
        elif x < 0:
            raise InputError('Nota não pode ser negativa.')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)