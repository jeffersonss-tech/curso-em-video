distancia = int(input('distancia:'))
if distancia >= 200:
    valor = distancia * 0.19
    print(f'voce vai pagar {valor}R$')
else:
    valor = distancia * 0.2
    print(f'voce vai pagar {valor:.2f}R$')
