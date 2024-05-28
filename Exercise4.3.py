print('Digite dois números e veja qual é o maior')
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundi número: '))

if number1 < number2:
    print(f'{number1} < {number2}')
elif number1 > number2:
    print(f'{number1} > {number2}')
else:
    print(f'Os números são iguais: {number1} == {number2}')
