lista = []

while (num := input('Digite um número ou "s" para encerrar: ')) != 's':
  lista.append(int(num))

m = int(input('Digite o valor de m: '))
resultante = [
  sum(num for k, num in enumerate(lista) if k % m == i)
  for i in range(m)
]

print(resultante)
