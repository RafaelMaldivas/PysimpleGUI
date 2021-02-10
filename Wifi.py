def criarRede():
    rede =(input('Informe o Nome da Rede :'))
    return rede

def criarSenha(rede):
    senha = input(f'Digite uma senha para a rede {rede} : ')
    return senha

def alterarSenha(senha):
    Senha = input('Digite a senha antiga :')
    if Senha == senha:
        novaSenha = input('Digite a Nova senha :')

import  time
def Conectar():
    while True:
        print('[ 1 ] Conectar')
        print('[ 2 ] Desconectar')
        print('[ 3 ] Sair')
        opc = int(input('Escolha uma opção a seguir'))
        if opc == 1:
            print('-'*20)
            time.sleep(1.5)
            print('-'*20)
            time.sleep(1.5)
            for i in range(0,4):
                print('- '*20)
                time.sleep(1.5)
                print(f'..CO..NE..CTAN...DO..')
                time.sleep(1.5)
                print('- '*20)
            print('Status - CONECTADO -')
        if opc == 2:
            print('-' * 20)
            time.sleep(1.5)
            print('-' * 20)
            time.sleep(1.5)
            for i in range(0, 4):
                print('- ' * 20)
                time.sleep(1.5)
                print(f'..DES CO NEC TAN DO..')
                time.sleep(1.5)
                print('- ' * 20)
            print('Status - Desconectado')
        if opc == 3:
            print('-' * 20)
            time.sleep(1.5)
            print(' - - Saindo - -')
            time.sleep(1.5)
            print('-' * 20)
            break
