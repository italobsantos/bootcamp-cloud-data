# Aula06 Conjuntos e Subconjunto (chave-valor)

# Não repete os elementos
conjunto1 = {1, 2, 3, 4}
print("Conjunto 1 : {}".format(conjunto1))

conjunto2 = {4, 5, 6, 7}
print("Conjunto 2 : {}".format(conjunto2))


#
# conjunto.add(6)
#
# conjunto.discard(4)
#
# print(type(conjunto))
# print(conjunto)

# União de conjuntos (Pega todos os elementos)

conjunto_uniao = conjunto1.union(conjunto2)

print("União: {}".format(conjunto_uniao))

# Intersecção dos conjuntos (Pega os termos iguais)

conjunto_interseccao = conjunto1.intersection(conjunto2)
print("Intersecção: {}".format(conjunto_interseccao))

# Diferença de conjuntos (Pega os termos que tem em um dos conjuntos mas não no outro)

conjunto_diferenca1 = conjunto1.difference(conjunto2)
print("Diferença entre 1 e 2: {}".format(conjunto_diferenca1))

conjunto_diferenca2 = conjunto2.difference(conjunto1)
print("Diferença entre 2 e 1: {}".format(conjunto_diferenca2))

# Diferença Simetrica (Tudo que tem em ambos conjuntos que não é igual em ambos)

conujnto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferença Simetrica entre 1 e 2: {}".format(conujnto_diff_simetrica))

# Subconjunto

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5, 6}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print("A é subconjunto de B: {}".format(conjunto_subset))


conjunto_superset = conjunto_b.issuperset(conjunto_a)
print("B é superconjunto de A: {}".format(conjunto_superset))

# Converter uma lista para um conjunto

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)

conjunto_animais = set(lista)
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)
