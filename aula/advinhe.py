import random

numero = random.randrange(1,10)
escolha = int (input('Escolha um numero de 1 á 10 '))

if numero == escolha:
    print('Voce ganhou o jogo')
    print('O numero aleatrorio é ', numero)
else:
    print('NT')
    print('O numero aleatrorio é ', numero)