import PySimpleGUI as sg

sg.theme('DarkGreen')

class history:

    def __init__(self):
        layout = [
                    [sg.Text('-------- Bem Vindo ao Quiz História --------')],
                    [sg.Text(' - 10 perguntas nível fácil\n - 10 perguntas nível intermediário\n - 10 perguntas nível avançado',size=(35,0))],
                    [sg.Text(' - - - - - Nível Fácil - - - - - ',size=(35,0))],
                     #Questão 1
                    [sg.Text('1 - Por que o homem deixou de ser nômade e virou sedentário?',size=(35,0))],
                    [sg.Checkbox('\nPorque ele estava cansado de caçar e começou a sobreviver apenas da agricultura.','fácil',key='1A')],
                    [sg.Checkbox('\nPorque as mulheres foram caçar no lugar dos homens, pois havia uma troca.','fácil',key='1B')],
                    [sg.Checkbox('\nPorque ele procurou caçar apenas perto das cavernas.','fácil',key='1C')],
                    [sg.Checkbox('\nPorque o clima do local começou a mudar, com isso formaram desertos, e assim a caça diminuiu.','fácil',key='1D')],
                     #Questão 2
                    [sg.Text('2 - Quais armas eram utilizadas no período paleolítico?', size=(35, 0))],
                    [sg.Checkbox('\nArmas de fogo.', 'fácil', key='2A')],
                    [sg.Checkbox('\nMachados e facões.', 'fácil', key='2B')],
                    [sg.Checkbox('\nArmas feitas de pedra lascada e madeiras.', 'fácil', key='2C')],
                    [sg.Checkbox('\nArma feitas de pedras polídas.', 'fácil', key='2D')],
                     #Questão 3
                    [sg.Text('3 - Qual o nome do rio que banha o Egito?', size=(35, 0))],
                    [sg.Checkbox('\nTigre', 'fácil', key='3A')],
                    [sg.Checkbox('\nNilo', 'fácil', key='3B')],
                    [sg.Checkbox('\nEufrates', 'fácil', key='3C')],
                    [sg.Checkbox('\nHélion', 'fácil', key='3D')],
                    # Questão 4
                    [sg.Text('4 - Para que servia as pirâmides?', size=(35, 0))],
                    [sg.Checkbox('\nGuardar Comida', 'fácil', key='4A')],
                    [sg.Checkbox('\nMonumento Cultural', 'fácil', key='4B')],
                    [sg.Checkbox('\nCultos Religiosos', 'fácil', key='4C')],
                    [sg.Checkbox('\nEnterrar os faraós', 'fácil', key='4D')],
                    [sg.Text(' - - - Avalie o programa - - - ',size=(35,0))],
                    [sg.Slider(range=(0,10), default_value=8, orientation='h', size=(25,35),key='avaliação')],
                    [sg.Button('Enviar Questões',size=(35,0))],
                    [sg.Text(' - - - Resultado do Teste - - - ',size=(35,0))],
                    [sg.Output(size=(35,15))]




             ]
        self.janela = sg.Window('Quiz História Premium').layout(layout)

    def iniciar(self):
        acertos = 0
        erros = 0
        while True:
            self.button, self.values = self.janela.Read()
            A1 = self.values['1A'] #questão 1
            if A1 == True:
                acertos += 1
            else:
                erros += 1
            C2 = self.values['2C'] #questão 2
            if C2 == True:
                acertos += 1
            else:
                erros += 1
            B3 = self.values['3B']#questão 3
            if B3 == True:
                acertos += 1
            else:
                erros += 1
            D4 = self.values['4D']  # questão 4
            if D4 == True:
                acertos += 1
            else:
                erros += 1
            nota = self.values['avaliação']

            print('-'*30)
            print(' - - Resultado do Teste - -')
            print(f'Acertos : {acertos}\nErros : {erros}')

exibe = history()
exibe.iniciar()

