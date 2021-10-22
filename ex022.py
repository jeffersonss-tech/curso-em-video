nome = str(input('digite seu nome completo:')).strip()

print(f'convertido para maiusculo: {nome.upper()}')
print(f'convertido para minusculo: {nome.lower()}')
print('seu nome tem {} letras' .format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras' .format(nome.find(' ')))