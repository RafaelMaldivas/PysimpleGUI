#como criar e modificar arquivos
'''

'r' -> usado para ler algo
'w' -> usado para escrever algo
'r+' -> usado para ler e escrever algo
'a' -> usado para acrescentar algo

'''

nomes = ['Rafael', 'Maria Beatriz', 'Renann', 'Sachê']
#usado para acrescentar informações ao arquivo txt
'''with open('nomes.txt', 'a') as arquivo:
    for i, n in enumerate(nomes):
        arquivo.write(f'nome{i} :' + str(n) + '\n')
        

#usado para escrever informações ao arquivo
'''
with open('nomes.txt','w') as arquivo:
    for i, n in enumerate(nomes):
        arquivo.write(f'nome{i} :' + str(n) + '\n')

#usado para ler informações em um arquivo

with open('nomes.txt', 'r+') as arquivo:
    arquivo.write('Paulo')
    for n in arquivo:
        print(f'{n}')


