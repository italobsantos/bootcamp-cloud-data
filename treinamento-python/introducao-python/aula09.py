# Maniupulação de Arquivos

# Cria arquivo

import shutil


# 'w' Sobreescreve o que já existe no arquivo
def escrever_arquivo(texto):
    arquivo = open('teste_aula09.txt', 'w')
    arquivo.write(texto)
    arquivo.close()


# 'a' Adiciona uma nova infrmoção no arquivo sem paga a que já existe
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    arquivo.close()


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo)
    aluno_notas = arquivo.read()
    aluno_notas = aluno_notas.split('\n')
    lista_media = []

    for x in aluno_notas:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno: media(lista_notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/italo/Documentos/bootcamp-dio-cloud-data/treinamento-python')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/home/italo/Documentos/bootcamp-dio-cloud-data/treinamento-python')


if __name__ == "__main__":
    # escrever_arquivo("Primeira linha.\n")
    # atualizar_arquivo("Segunda linha.\n")
    # ler_arquivo('teste_aula09.txt')

    # aluno = 'Rafael,10,10,5,5\n'
    # atualizar_arquivo('notas.txt',aluno)
    #
    # aluno = 'Vinicius,10,2,9,7\n'
    # atualizar_arquivo('notas.txt',aluno)
    #
    # aluno = 'Cesar,10,2,9,7\n'
    # atualizar_arquivo('notas.txt',aluno)

    # lista_media = media_notas('notas.txt')
    # print(lista_media)

    move_arquivo('teste_aula09.txt')
