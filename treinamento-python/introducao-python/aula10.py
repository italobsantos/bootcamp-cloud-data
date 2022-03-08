# Manipulação de data e hora

from datetime import date, time, datetime,timedelta

data_atual = date.today() # Formato date
data_atual_str = data_atual.strftime('%d/%m/%y') # Formato String

#print(data_atual.strftime('%d/%m/%y'))
#print(data_atual.strftime('%A %B %Y'))


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)


def trabalhando_com_date_time():

    # Retorna a data e o horario atual
    data_atual = datetime.now()

    # Formas de formatar a saída do datetime
    # print(data_atual)
    # print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    # print(data_atual.strftime('%c'))
    # print(data_atual.day)
    # print(data_atual.month)
    # print(data_atual.year)

    # Formas de reescrever o dia da semana para portugues
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

    # Criar uma data com o datetime
    data_criada = datetime(2020, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))

    # Converter uma string data para o tipo datetime
    data_string = '01/01/2020'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)

    # Operações com Data
    nova_data = data_convertida - timedelta(days=365, hours=2,minutes=15)
    print(nova_data)


if __name__ == '__main__':

    trabalhando_com_date_time()