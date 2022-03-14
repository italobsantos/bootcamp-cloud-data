import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFIlesAtributesW('ocultar.txt', atributo_ocultar)

if retorno:
    print('Arquivo ocultado')
else:
    print('O arquivo não foi ocultado ')