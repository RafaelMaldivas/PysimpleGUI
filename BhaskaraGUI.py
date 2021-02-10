import PySimpleGUI as sg
import math

sg.theme('DarkBrown')

class Bhaskara:
    def __init__(self):
        self.layout = [
            [sg.Text('Digite o termo A', size=(20, 0)), sg.Input(size=(5, 0), key='A')],
            [sg.Text('Digite o termo B', size=(20, 0)), sg.Input(size=(5, 0), key='B')],
            [sg.Text('Digite o termo C', size=(20, 0)), sg.Input(size=(5, 0), key='C')],
            [sg.Button('Processar Dados', size=(25, 0))],
            [sg.Text(' - - - Resultado - - - ', size=(25, 0))],
            [sg.Output(size=(25, 10))]
        ]

        self.janela = sg.Window('Fórmula de Bháskara').Layout(self.layout)

    def iniciar(self):
        while True:
            self.buttons, self.values = self.janela.Read()
            self.processamento()

    def processamento(self):
        TermoA = float(self.values['A'])
        TermoB = float(self.values['B'])
        TermoC = float(self.values['C'])

        bhaskarapos =float((-TermoB + math.sqrt((math.pow(TermoB, 2))-(4*TermoA*TermoC)))/(2*TermoA))
        bhaskaraneg =float((-TermoB - math.sqrt((math.pow(TermoB, 2))-(4*TermoA*TermoC)))/(2*TermoA))

        print(f' - BhasKara = termo positivo : {bhaskarapos:.1f}\n - Bhaskara = termo negativo : {bhaskaraneg}')

bhaskara = Bhaskara()
bhaskara.iniciar()
