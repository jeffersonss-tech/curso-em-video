salario = float(input('qual e o salario?'))
if salario <= 2000:
    almento = salario + (salario * 10) / 100
    print(f'quem ganha {salario}R$ ganhara {almento}')

else:
    aumento = salario + (salario * 5) / 100
    print(f'quem ganha {salario}R$ ganhara {aumento}RS')
