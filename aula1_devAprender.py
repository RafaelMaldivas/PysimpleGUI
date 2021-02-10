print('-' * 20)
print('\033[32mVamos Aprender Python Porra!!!\033[m')
print('-' * 20)
from datetime import datetime

'''data_postagem = datetime.strptime(input('Quando devemos postar essa foto?'),'%d/%m/%Y')
data_agora = datetime.now()
dia_agora = datetime.now().day
mês_agora = datetime.now().month

prazo = data_postagem - data_agora
print(f'Faltam {prazo} para a postagem da foto!')
ano = int(input('Digite o ano do seu nascimento :'))
idade = datetime.now().year - ano
print(f'Você tem {idade} anos de idade')'''

'''lista_preço = [5,6,15,20,50,80,1000]
for preço in lista_preço:
    if preço == 80:
        continue
    print(f'R${preço},00')
print(f'Pulamos o R${lista_preço[5]},00')'''

'''
class carro:

    def __init__(self, fabricante, modelo, cor, ano, preço):
        self.fabricante = fabricante
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preço = preço

    def Exibir_informações(self):
        print('-' * 20)
        print(
            f'Fabricante : {self.fabricante}\nModelo : {self.modelo}\nCor : {self.cor}\nAno : {self.ano}\nPreço : R${self.preço}')
        print('-' * 20)

    def Preço(self):
        valor = float(input(f'Defina um valor para o {self.modelo}  :'))
        if valor < self.preço:
            print('O valor está abaixo da tabela FIP do carro!')
        if valor > self.preço:
            print('O valor está acima da tabela FIP do carro!')


for i in range(0, 2):
    fab = input('Digite o nome do fabricante do veículo : ')
    mod = input('Digite o modelo do veículo :')
    cor = input('Digite a cor do veículo :')
    ano = int(input('Digite o ano de fabricação do veículo :'))
    preco = float(input('Digite o preço do veículo'))
    if i == 0:
        auto1 = carro(fab, mod, cor, ano, preco)
    if i == 1:
        auto2 = carro(fab, mod, cor, ano, preco)


auto1.Exibir_informações()
auto2.Exibir_informações()
auto1.Preço()
auto2.Preço()'''

#logging
#logging serve para armazenar as informações deixadas pelo usuário
import logging
logging.basicConfig(
    filename='info.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)
logger = logging.StreamHandler()
logging.getLogger('').addHandler(logger)

logging.debug('Isso é uma mensagem nível degub !')
logging.info('Isso é uma mensagem nível informativa ! ')
logging.warning('Isso é uma mensagem nível atenção !')
logging.error('Isso é uma mensagem nível erro !')
logging.critical('Isso é uma mensagem nível crítico !')

#exception
try:
    ano_atual = int(input('Digite o ano atual :'))
except ValueError:
    print('Você deve digitar números inteiros')
