import math
lista = []
lista2 = []

while True:
    n = input('Digite um número: ')
    if n == 's':
        break
    n = int(n)
    lista.append(n)

fs = int(input('Digite 1 (fatorial) ou 2 (raíz quadrada): '))
for i in range(len(lista)):
    if fs == 1:
        lista[i] = math.factorial(lista[i])
        lista2.append(int(lista[i]))
    elif fs == 2:
        lista[i] = math.sqrt(lista[i])
        lista2.append(int(lista[i]))
print(lista2)
