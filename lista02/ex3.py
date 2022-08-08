massa = float(input('Digite sua massa: '))
altura = float(input('Digite sua altura: '))


if massa / altura ** 2 < 18.5:
    print('Baixo peso')
elif massa / altura ** 2 >= 18.5 and massa / altura ** 2 < 25:
    print('Peso adequado')
elif massa / altura ** 2 >= 25 and massa / altura ** 2 < 30:
    print('Sobrepeso')
else:
    print('Obesidade')
    
