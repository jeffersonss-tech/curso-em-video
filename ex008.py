m = float(input('uma distancia em metros:'))
km = m / 1000
cm = m * 100

print('{:.2f}km'.format(km))
print(f'{m} metro(s) é igual a {cm:.0f} cm(s)')
