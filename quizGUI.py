import datetime
from time import sleep
import random
import PySimpleGUI as sg

sg.theme('DarkBrown')


class Quiz:
    def __init__(self):
        self.layout = [
            [sg.Text(f'{"- - - Guru Goró - - -":^30}', size=(30, 0))],
            [sg.Text(f'{"- - - Me Faça uma pergunta ! - - -":^30}', size=(30, 0))],
            [sg.Input(size=(30, 0), key='pergunta')],
            [sg.Button('    Perguntar   ', size=(15, 0))],
            [sg.Text(f'{" - Resposta - ":^30}', size=(30, 0))],
            [sg.Output(size=(40, 10))],
        ]

        self.janela = sg.Window('Guru Goró').Layout(self.layout)
        self.respostas = [
            ' - Sim, com certeza !',
            ' - Não acho que seja uma boa idéia !',
            ' - Talvez possa dar certo !',
            ' - Por que as coisas são como elas são !',
            ' - Não sei, mas você precisa encontrar uma resposta !',
            ' - Não sei se sou a pessoa mais indicada a responder isso !',
            ' - Vou te dar um dica, procura no Google !!',
            ' - Se você ler um pouco mais e estudar, talvez um dia saberá !',
            ' - Paciência meu amigo, quando menos esperar a resposta chegará',
            ' - Estava justamente pensando a mesma coisa, acredita !?',
            ' - Como já dizia um grande filófo, "Só sei que nada sei" !',
            ' - Não entendi sua pergunta, seja mais específico, na próxima !'
        ]
        self.respPorque = [
            ' - Porque as coisas são como elas são !',
            ' - Porque os seres humanos são animais muito complexos',
            ' - Porque os cientistas ainda não descobriram isso !',
            ' - Porque sim !',
            ' - Porque Deus quis !',
            ' - Porque as coisas não são mais como eram antigamente, se atualize !'
        ]
        self.respOnde = [
            ' - Onde ninguém possa te encontrar !',
            ' - Não sei, olha no GPS !',
            ' - No planeta Terra !', ' - Na natureza !',
            ' - Nos quintos dos Infernos !', ' - Onde possa ser feliz !',
            ' - Onde alguém te suporte !', ' - Melhor lugar é no litoral !',
            ' - Onde o vento faz a curva', ' - Aonde os fracos não tem vez !'
        ]
        self.respQual = [
            ' - Na hora que você crescer ! ', ' - No momento mais importante',
            ' - O que for melhor !', ' - Me desculpa, mas não sei essa !',
            ' - Que palhaçada, faz uma pergunta mais inteligenet!',
            ' - E daí, pergunta pra sua mãe !', 'Qualquer um poderia ter respondido essa !',
            ' - Nunca saberemos este mistério !', ' - Tava na ponta da língua, mas eu esqueci !'
        ]
        self.resp_e = [' - É nada, sério ?', ' - Sou o que sou !', ' - Será o que ele quiser !',
                       ' - É zueira só poder ser né?', ' - Sou muito mais que isso !', 'Eu não, mas você é que eu sei',
                       ' - Todo mundo sabe que isso é mentira !', ' - Todo mundo sabe que isso é verdade !',
                       ' - É isso mesmo, porra!!',
                       ' - É a história que as pessoas estão contando por aí !',
                       ' - É muito mimimi, pra pouca atitude !', ' - É sim, e nada vai mudar isso !',
                       ' - É sua mãe isso sim !', ' - É melhor abandonar essa idéia !',
                       ' - Isso é conspiração isso sim !!']
        self.respQuanto = [
            'Quanto vc pode pagar ?!', 'Quanto tempo for necessário !', 'Não fiz essa conta !',
            'Não faço esse tipo de cálculo !', 'Não sei, melhor comprar uma calculadora !',
            'Já estudou matemática na vida ?',
            'O quanto você conseguir !', 'Não sei, mas quanto mais, melhor !!', 'Qual era a pergunta mesmo ?',
            'Quanto você tem no bolso?',
            'O quanto menos for melhor', 'Não sei, será , 8, ou 9, ou 10, sei lá !', 'Quanta mentira !',
            'Quanta verdade !', '8', '4', 'Só sei que é um número par',
            'Só sei que é um número ímpar', 'Só pode ser um número real !', 'Só pode ser um número isso daí ! Ta ok !?'
        ]
        self.respQuem = [
            'Pergunta no posto Ipiranga !', 'Eu é que não, porque só existo no computador',
            'Isso é uma questão quem só vc poderá descobrir !',
            'Será que o google saberia essa?', 'Ser ou não ser, eis a questão', 'Quem poderia saber essa?',
            'Quem muito quer nada tem',
            'Alguém mais poderia responder essa pergunta pra você?', 'Esse alguém já morreu !',
            'Posso responder outra hora? Estou cansado !'
        ]
        self.matou = [
            'Bolsonaro', 'Famíglia Bolsonaro', 'Bolsonaro Facista', 'O presidente do país', 'O bozzo'
        ]




    def iniciar(self):

        while True:
            self.perguntar()


    def perguntar(self):
        self.button, self.values = self.janela.Read()
        print(datetime.datetime.now().time())
        pergunta = self.values['pergunta']
        print(' Pensando . . .')
        sleep(2.5)
        print(' Você perguntou:')
        print(f'"{self.values["pergunta"]}"?')
        sleep(2.5)
        print('-Minha Resposta é:')
        sleep(2.5)
        if 'porque' in pergunta or 'por que' in pergunta:
            random.shuffle(self.respPorque)
            print(random.choice(self.respPorque))
        elif 'matar' in pergunta or 'matou' in pergunta:
            random.shuffle(self.matou)
            print(random.choice(self.matou))
        elif 'onde' in pergunta or 'aonde' in pergunta:
            random.shuffle(self.respOnde)
            print(random.choice(self.respOnde))
        elif 'quem' in pergunta:
            random.shuffle(self.respQuem)
            print(random.choice(self.respQuem))
        elif 'qual' in pergunta or 'quais' in pergunta:
            random.shuffle(self.respQual)
            print(random.choice(self.respQual))
        elif 'é' in pergunta or 'sou' in pergunta:
            random.shuffle(self.resp_e)
            print(random.choice(self.resp_e))
        elif 'quanto' in pergunta or 'quantos' in pergunta:
            random.shuffle(self.respQuanto)
            print(random.choice(self.respQuanto))
        else:
            random.shuffle(self.respostas)
            print(random.choice(self.respostas))

teste = Quiz()
teste.iniciar()