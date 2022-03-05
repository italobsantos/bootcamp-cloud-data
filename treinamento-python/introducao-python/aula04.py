# Aula 04 laços de repetição for/while

# Verifica se o número é primo
# a = int(input("Entre com o número: "))
#
# div = 0
# for x in range(1,a+1):
#     resto = a % x
#
#     print(x,resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print("O número é primo")
# else:
#     print("O número não é primo")


# Verifica quais são os número primos até um valor x informado pelo usuario

# x = int(input("Digite o número: "))
#
# for num in range(x + 1):
#     div = 0
#     for x in range(1, x + 1):
#         resto = num % x
#
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# Bloco de repetição while. Verificando se as notas são validas

nota_a = int(input("Entre com a nota do primeiro bimestre: "))

while nota_a > 10:
    nota_a = int(input("Nota invalida. Entre com a nota do primeiro bimestre: "))

nota_b = int(input("Entre com a nota do segundo bimestre: "))

while nota_b > 10:
    nota_b = int(input("Nota invalida. Entre com a nota do segundo bimestre: "))

nota_c = int(input("Entre com a nota do terceiro bimestre: "))

while nota_c > 10:
    nota_c = int(input("Nota invalida. Entre com a nota do terceiro bimestre: "))

nota_d = int(input("Entre com a nota do quarto bimestre: "))

while nota_d > 10:
    nota_d = int(input("Nota invalida. Entre com a nota do quarto bimestre: "))

media = (nota_a + nota_b + nota_c + nota_d)/4

print("A média final do aluno é: {}".format(media))

print("Fim do programa!!!")