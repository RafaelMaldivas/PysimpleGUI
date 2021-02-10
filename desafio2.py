import random


while True:
    x = random.randint(0, 10)
    try:
        n = int(input('Chute um valor entre 0 e 10'))

        if n == x:
            print('\033[31m Parabéns Você Acertou!! \033[m!!')
            break
        elif n > x:
            print('\033[32mChute um número menor !\033[m')
        elif n < x:
            print('\033[32mChute um número maior !\033[m')
        if n > 10:
            print('\033[34mValor deve ser abaixo de 10!\033[m')
        if n < 0:
            print('\033[34mValor deve ser maior que zero!\033[m')
    except ValueError:
        print('\033[33m - Você deve digitar apenas números\033[m')
        pass