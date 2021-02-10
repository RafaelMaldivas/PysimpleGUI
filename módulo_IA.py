import random
from time import sleep
respostas = ['Porque viver é amar !', 'Porque estamos vivos !',
             'Porque a vida é assim mesmo !', 'Agora vc me pegou !', 'Porque a vida ás vezes não tem sentido !', 'O brasileiro precisa ser estudado !']
perguntas = ['Você quer fazer outra pergunta?[s/n]', 'Posso te fazer uma pergunta?[s/n]', 'Você já sentiu isso?[s/n]', 'Você gosta de ler?[s/n]']
reação = ['Tá certo !', 'Faz assim então !', 'Vamos Prosseguir !', 'Só sei que nada sei', 'E se você ...', 'Foda tudo isso!']


def pergunta ():
    Pergunta = input(' - Me faça uma pergunta ?').strip().lower()
    return Pergunta


def analisador (Pergunta):
    for p in Pergunta:
        if 'porque' in Pergunta:
            escolhe = random.randint(0,(len(respostas)-1))
            reage = random.randint(0, (len(reação)-1))
            print(' . . . Pensando ! ! ')
            sleep(2)
            print(' . . Pensando ! !')
            sleep(2)
            print(respostas[escolhe])
            sleep(0.8)
            print(reação[reage])
        elif 'quantos' in Pergunta:
            print("Quantos for necessário!")

        elif 'é' in Pergunta:
            print('Eu não você é?')
            print('Seu troxão !!')

        elif 'onde' in Pergunta:
            print('Na puta que o pariu !!')
        break


def gerador_de_pergunta():
    escolha = random.randint(0, 3)
    perg1 = input(perguntas[escolha]).strip().lower()
    if perg1 == 's':
        print(' Pensando aqui ...')
        sleep(2)
        if 'uma' in perguntas[escolha]:
            print('Porque você é tão feio?')
            print('Meu Deus, Criatura!!!')
        if 'outra' in perguntas[escolha]:
            print('Só não abusa hein !!!')
        if 'sentiu' in perguntas[escolha]:
            print('Você gosta de sentir né? Safadão!!!')
        if 'ler' in perguntas[escolha]:
            print('Muito bom, só não pode ter votado no Bolsonaro ! ! !')
    else:
        if perg1 == 'n':
            print('Então ..')
            print('Vai se foder!!!')
            return False


