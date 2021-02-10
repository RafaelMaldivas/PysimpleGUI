

tela = TelaPython()
tela.iniciar()
import PySimpleGUI as sg

sg.theme('DarkBrown')


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome', size=(8, 0)), sg.Input(size=(20, 0), key='nome')],
            [sg.Text('Idade', size=(8, 0)), sg.Input(size=(20, 0), key='idade')],
            [sg.Text('Peso', size=(8, 0)), sg.Input(size=(20, 0), key='peso')],
            [sg.Text('Altura', size=(8, 0)), sg.Input(size=(20, 0), key='altura')],
            [sg.Text('Sexo:'), sg.Radio('Masculino', 'sexo', key='Masculino'),
             sg.Radio('Feminino', 'sexo', key='Feminino')],
            [sg.Text('Qual o melhor navegador?')],
            [sg.Checkbox('Crome', key='crome'), sg.Checkbox('Mozilla', key='mozilla'),
             sg.Checkbox('Explorer', key='explorer')],
            [sg.Button('Enviar', size=(25, 0))],
            [sg.Slider(range=(0, 100), default_value=8, orientation='h', size=(15, 25), key='velocidade')],
            [sg.Text(' - Resultado da Análise - ')],
            [sg.Output(size=(30, 20))]
        ]
        self.janela = sg.Window('Dados do Usuário').layout(layout)

    def iniciar(self):
        while True:
            self.definições()

    def definições(self):
        self.button, self.values = self.janela.Read()
        nome = self.values['nome']
        idade = int(self.values['idade'])
        masculino = self.values['Masculino']
        feminino = self.values['Feminino']
        google = self.values['crome']
        linux = self.values['mozilla']
        micro = self.values['explorer']
        imc = float(self.values['peso']) / (float(self.values['altura']) * float(self.values['altura']))
        velocidade = float(self.values['velocidade'])
        print('-' * 30)
        print(f'Nome : {nome.capitalize()}')
        print(f'Idade : {idade} anos')
        if masculino:
            print('Sexo :  Masculino')
        elif feminino:
            print('Sexo : Feminino')
        print(f'Resultado IMC = {imc:.2f}')
        if google:
            print(f'Navegador do Google ')
        elif linux:
            print(f'Navegador Linux')
        elif micro:
            print(f'Navegador da Microsoft')
        print(f'Velocidade = {velocidade} Km/h')
        print('-' * 30)
