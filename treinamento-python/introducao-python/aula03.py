# Aula02 blocos condicionais if/else


# Comparação entre 3 números


# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))

# if a > b and a > c:
#     print("O maior número é: {}".format(a))
# elif b > a and b > c:
#     print("O Maior número é: {}".format(b))
# else:
#     print("O Maior número é: {}".format(c))
#

# Verifica se algum dos números digitados é par

# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print("Foi digitado um número par!")
# else:
#     print("Não foi digitado um número par!")
#

#Verificar se a nota é valida

a = int(input("Nota primeiro bimestre: "))
b = int(input("Nota segundo bimestre: "))
c = int(input("Nota terceiro bimestre: "))
d = int(input("Nota quarto bimestre: "))

media = (a+ b + c + d)/4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print("Média: {}".format(media))
else:
    print("Foi informado alguma nota invalida")

print("Final do programa")