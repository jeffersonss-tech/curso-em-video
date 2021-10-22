preço = float(input('digite um valor:'))
desconto = int(input('digite a porcentagem do desconto:'))
novo = preço -(preço * desconto) / 100

print(f'o novo valor do produto com {desconto}% off será {novo:.2f}.')