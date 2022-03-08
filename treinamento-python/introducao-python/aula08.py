# Modulos e funções anonimas

# Importa o arquivo aula_7 completo
import aula07_televisão

televisão = aula07_televisão.Televisao()

print(televisão.ligada)

# Importa somente a classe Televisão da aula07_televisão

from aula07_televisão import Televisao

televisão = Televisao()

televisão.power()
print(televisão.ligada)

# Importando uma função de um modulo

from aula08_contador_palavras import contador_letras

lista_animal = ['cachorro', 'gato', 'galo', 'elefante']

print(contador_letras(lista_animal))

