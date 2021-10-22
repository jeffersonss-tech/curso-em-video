n1 = float(input('primeira nota:'))
n2 = float(input('segunda nota:'))
m = (n1 + n2) / 2
print(f'a média foi {m:.1f}')

if m >= 6:
    print('APROVADO!')

else:
    print('REPROVADO!')

