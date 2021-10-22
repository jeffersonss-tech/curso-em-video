menu = int(input('digite 1 para converter de real para dolar, ou digite 2 para converter dolar para real'))
if menu == 1:
    real = float(input('digite um valor em reais:'))
dolar = real / 5.46

if real == 1:
    print(f'{real:.2f} real vale {dolar:.2f}R$ dolares')

    while dolar == 1:
        print(f'{real} reais valem {real}R$ dolar')
    else:
        print(f'{real} reais valem {dolar:.2f} dolares')
else:
    pass

while menu == 2:
    dolar2 = float(input('digite um valor em dolar:'))
real2 = dolar / 5.46

if real == 1:
    print(f'{dolar2:.2f} real vale {real2:.2f}R$ dolares')

    while dolar == 1:
        print(f'{dolar2} reais valem {real2}R$ real2')
    else:
        print(f'{dolar2} reais valem {real2:.2f} dolares')