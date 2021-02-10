import random
import PySimpleGUI as sg
from time import sleep

sg.theme('DarkBlue')


class jogo_da_velha:

    def __init__(self):
        self.layout = [
            [sg.Text(' - - - Jogo da Velha - - -', size=(30, 0))],
            [sg.Text(' << VocÊ é o Jogador -X- >>', size=(30, 0))],
            [sg.Text(' - Tabuleiro do Jogo -', size=(30, 0))],
            [sg.Text('  [ 0 ] [ 1 ] [ 2 ]\n  [ 3 ] [ 4 ] [ 5 ]\n  [ 6 ] [ 7 ] [ 8 ]')],
            [sg.Text('\n - Digite a casa onde quer jogar', size=(20, 0)), sg.Input(size=(3, 0), key='casa')],
            [sg.Button('Marcar Casa', size=(20, 0))],
            [sg.Text(' - - - Movimentos - - -', size=(20, 0))],
            [sg.Output(size=(30, 30))]
        ]

        self.janela = sg.Window('Jogo da Velha', layout=self.layout)

        self.tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.jogador1 = 'X'
        self.jogador2 = 'O'
        self.pontos = 0
        self.empate = []

    def inicio(self):
        self.Button, self.values = self.janela.Read()
        while True:
            self.tabuleitoprint()
            self.logica_do_jogo()
            self.horizontal()
            self.diagonal()
            self.vertical()
            self.empata()
            self.jogada2()

    def tabuleitoprint(self):
        print(f'Pontos : {self.pontos}')
        for i in range(0, 9, 3):
            print(f' [ {self.tabuleiro[i]} ]    [ {self.tabuleiro[i + 1]} ]   [ {self.tabuleiro[i + 2]} ]')

    def logica_do_jogo(self):
        while True:
            casa1 = int(self.values['casa'])  # int(input(' - Digite o número onde deseja marcar : '))

            if 0 <= casa1 <= 8:
                if self.jogador1 == self.tabuleiro[casa1] or self.jogador2 == self.tabuleiro[casa1]:
                    print('Número Inválido!!')
                else:
                    self.tabuleiro[casa1] = self.jogador1
                    self.empate.append(casa1)
                    break
            else:
                print(' - - Número Inválido - - ')

    def jogada2(self):
        print('Computador pensando ...')
        sleep(2)
        while True:
            casa2 = random.randint(0, 8)
            if self.jogador1 == self.tabuleiro[casa2] or self.jogador2 == self.tabuleiro[casa2]:
                print('Jogador O - pensando ...')
            else:
                self.tabuleiro[casa2] = self.jogador2
                self.empate.append(casa2)
                break

    def empata(self):
        if len(self.empate) == 10:
            print('Jogo Empatado')
            self.continuar()

    def horizontal(self):
        for i in range(0, 9, 3):
            if self.tabuleiro[i] == self.tabuleiro[i + 1] == self.tabuleiro[i + 2]:
                print(f' - O Jogador {self.tabuleiro[i]} Venceu')
                if self.tabuleiro[i] == self.jogador1:
                    self.pontos += 1
                else:
                    self.pontos -= 1
                self.continuar()

    def vertical(self):
        for i in range(3):
            if self.tabuleiro[i] == self.tabuleiro[i + 3] == self.tabuleiro[i + 6]:
                print(f' - O Jogador {self.tabuleiro[i]} Venceu')
                if self.tabuleiro[i] == self.jogador1:
                    self.pontos += 1
                else:
                    self.pontos -= 1
                self.continuar()

    def diagonal(self):
        for i in range(3):
            if self.tabuleiro[0 + i] == self.tabuleiro[4] == self.tabuleiro[8 - i]:
                print(f' - O jogador {self.tabuleiro[i]} Venceu')
                if self.tabuleiro[i] == self.jogador1:
                    self.pontos += 1
                else:
                    self.pontos -= 1
                self.continuar()

    def continuar(self):
        while True:
            cont = input('Deseja jogar novamente [s/n]')[0].lower()
            if cont not in 'sn':
                cont = input('Deseja jogar novamente [s/n]')[0].lower()
            elif cont == 's':
                self.empate.clear()
                self.tabuleiro.clear()
                for i in range(9):
                    self.tabuleiro.append(i)
                self.inicio()

            elif cont == 'n':
                print('FIM DE JOGO !!')
                exit()


jogovelha = jogo_da_velha()
jogovelha.inicio()
