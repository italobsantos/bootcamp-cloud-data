# Função lambda forma de escrever uma função anonima(Não precisa de nome) de uma linha

# Lambda 1º variaveis de entrada : operação a ser retornada

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['gato', 'cachorro', 'coelho']
print(contador_letras(lista_animais))

soma  = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5,4))
print(subtracao(3,2))

# Criando uma calculadora com lambda

calculadora = {
    'soma': lambda a, b: a + b,
    'subtração': lambda a, b: a - b,
    'multiplicação': lambda a, b: a * b,
    'divisão': lambda a, b: a / b,
}
soma = calculadora['soma']
print(soma(2,3))