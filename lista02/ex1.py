def total():
    numBalas = int(input('Quantidade de balas: '))
    precoBalas = float(input('Valor de cada bala: R$'))
    numCholates = int(input('Quantidade de chocolates: '))
    precoChocolate = float(input('Valor de cada chocolate: R$'))
    total = (numBalas * precoBalas) + (numCholates * precoChocolate)
    return f'O total da compra:\nR${total:.2f}'

print(total())
