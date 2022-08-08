compra = float(input('Valor da compra: R$'))
valorPago = float(input('Valor pago: R$'))
troco = valorPago - compra
dimDisponivel = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
print(f'Troco: R${troco}\n')


for i in dimDisponivel:
    contador = 0
    while troco >= i:
        contador += 1
        troco -= i
    print(f'{contador} de R$ {i:.2f}')
