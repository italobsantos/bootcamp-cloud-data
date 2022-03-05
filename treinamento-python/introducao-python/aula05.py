# Aula05 listas e tuplas

# É possível adidionar mais de um tipo, mas não é recomendado
lista = [1, 3, 5, 7]

lista_animal = ["cachorro", "gato", "elefante"]

# print(lista,"\n")
# print(lista_animal[1])
#
# for x in lista_animal:
#     print(x)

#Somar elementos da lista

# soma = 0
# for x in lista:
#     soma += x
#
# print(soma)
#
# print(sum(lista))

# Máximo e minimo de uma lista

# print(max(lista))
# print(min(lista))
#
# print(max(lista_animal))
# print(min(lista_animal),"\n")

# Verifica a existencia de um termo na lista

# if 'lobo' in lista_animal:
#     print("O elemento lobo está na lista")
# else:
#     print("O elemento lobo não está na lista")

# Operações com lista

# nova_lista = lista_animal * 3
# print(nova_lista)

# Adiciona novo item na lista

# lista_animal.append('lobo')
# print(lista_animal)

# Retira item da lista
#
# lista_animal.pop() # retira o ultimo elemento
# print(lista_animal)
#
# lista_animal.pop(0)
# print(lista_animal)

# Retira o item passando o nome do elemento

# lista_animal.remove('gato')
# print(lista_animal)

# Ordenar a lista
# lista.sort()
# lista_animal.sort()
#
# print(lista)
# print(lista_animal)

# Inverter a lista

# lista_animal.reverse()
# print(lista_animal)

# Tuplas são imutaveis

tupla = (1, 2, 3, 4, 5, 6)
# print(tupla[2])

# tupla[0] = 5 não é possível alterar o valor

# Verifica o tamanho
#
# print(len(tupla))
#
# print(len(lista_animal))
#

# Converter lista <-> tupla

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))

lista_numerica = list(tupla)
print(type(lista_numerica))