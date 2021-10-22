import random
from time import sleep
print('-=- ' * 10)
print('               JOGO DE ADIVINHAÇÃO')
print('-=- ' * 10, '\n')

com = random.randint(1, 5)
jogador = int(input('tente adivinhar o numero que o computador pensou, entre 1 e 5:'))
print('PROCESSANDO...')
sleep(2)

if jogador == com:
    print('PARABENS!\nVOCÊ ACERTOU')
else:
    print('VOCÊ ERROU!')
print(f'pensei no numero {com}')


