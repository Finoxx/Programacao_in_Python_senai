import random

perguntas = [
    'O que é o que é? Quanto mais se tira, maior fica?',
    'Por que o livro foi ao médico?',
    'O que é o que é que tem dentes, mas não morde?',
    'Por que o computador foi preso?',
    'O que é o que é que cai em pé e corre deitado?',
    'O que é um pontinho vermelho no jardim?',
    'O que o tomate foi fazer no banco?',
    'O que é o que é que tem asa, mas não voa, e canta sem ter boca?',
    'Por que o lápis se deu mal na prova?',
    'O que é o que é que quanto mais quente fica, mais frio deixa o ambiente?'

]
respostas = [ 'Um buraco!', 'Porque ele estava com muitas “histórias” pra contar!', 'O pente!', 'Porque ele executou um programa!', ' A chuva!', 'Uma formiga com batom!', 'Tirar extrato!', 'O ventilador!', 'Porque estava sem ponta!', 'O ar-condicionado!'

]

pergunta_escolhida = random.choice(perguntas)
print(pergunta_escolhida)

escolha = int(input(f'''

0 = {respostas[0]}
1 = {respostas[1]}
2 = {respostas[2]}
3 = {respostas[3]}
4 = {respostas[4]}
5 = {respostas[5]}
6 = {respostas[6]}
7 = {respostas[7]}
8 = {respostas[8]}
9 = {respostas[9]}

'''))

indice_pergunta = perguntas.index(pergunta_escolhida)


if indice_pergunta == escolha:
    print('Acertou em cheio ')
    print('Voce ganhou um 🌽🌽')
else:
    print('ERROU FEIO')
    print('Voce tem que pagar um kkkk')

