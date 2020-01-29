from RSA import *
from os import system

carregado = False

while True:
    system('cls | clear')
    print('###   RSA   ###')
    print('1 - Carregar Valores')
    print('2 - Encriptar')
    print('3 - Decriptar')
    print('4 - Sair')

    op = input()

    if op == '1':
        system('cls | clear')
        print('1 - Carregar Valores\n\n')

        p = int(input('Valor de P: '))
        q = int(input('Valor de Q: '))

        val = []
        while True:
            aux = str(input('Insira um valor númerico ou um valor não númerico para encerrar: '))
            if not aux.isnumeric():
                break
            val.append(int(aux))
            carregado = True

        texto = RSA(p, q, val)
        input('Valores CARREGADOS!!')

    elif op == '2':
        system('cls | clear')
        print('2 - Encriptar\n\n')
        if carregado:
            texto.encriptar()
            input('Valores encriptados: ' + texto.__str__())
        else:
            input('Valores não carregados!')
        
    elif op == '3':
        system('cls | clear')
        print('3 - Decriptar\n\n')
        if carregado:
            texto.decriptar()
            input('Valores decriptados: ' + texto.__str__())
        else:
            input('Valores não carregados!')
    elif op == '4':
        break

# as validações já ocorrem internamente

# resta saber se a entrada e saida do programa
# pode ser uma lista de inteiros