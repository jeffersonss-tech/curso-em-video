velocidade = int(input('qual é a sua velocidade?'))

if velocidade > 60:
    multa = (velocidade - 60) * 7
    print(f'VOCÊ FOI MULTADO EM {multa}R$ POR EXCESSO DE VELOCIDADE')
else:
    print('VOCÊ NÃO FOI MULTADO, DIRIJA COM CUIDADO')
