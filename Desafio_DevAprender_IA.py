import módulo_IA

while True:
    print(' - - Pergunte ao Guru Goró - - ')
    módulo_IA.pergunta()
    módulo_IA.analisador(módulo_IA.pergunta())
    módulo_IA.gerador_de_pergunta()
    if módulo_IA.gerador_de_pergunta() == False:
        break