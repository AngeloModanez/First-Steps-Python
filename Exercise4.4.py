name = input('Digite o nome do lutador: ')
weight = float(input('Digite o peso do lutador: '))

if weight < 52:
    category = ''
elif weight < 65:
    category = 'Pena'
elif weight < 72:
    category = 'Leve'
elif weight < 79:
    category = 'Ligeiro'
elif weight < 86:
    category = 'Meio-Médio'
elif weight < 93:
    category = 'Médio'
elif weight < 100:
    category = 'Meio-Pesado'
else:
    category = 'Pesado'

if category != '':
    print(f'\nO lutador {name} pesa {weight:.2f}kg e se enquadra na categoria {category}')
else:
    print(f'\nPeso invalido: {weight}')
