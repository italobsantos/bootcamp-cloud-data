# Métodos funções e classes

# Função é tudo que retorna valor método não

# Declaração de métodos


# def soma(a, b):
#     return a + b
#
#
# print(soma(1, 2))
# print(soma(4, 5))

# Definição de classe


class Calculadora:

    # O método init não pode ficar vazio ele é o inicializador da classe

    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def divisao(self):
        return self.a / self.b

    def multiplicacao(self):
        return self.a * self.b


calculadora = Calculadora(1, 2)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())

