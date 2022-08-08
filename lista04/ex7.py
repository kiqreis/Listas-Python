lista1 = []
lista2 = []

while True:
    n1 = input('Digite um número: ')
    if n1 == 's':
        break
    n1 = int(n1)
    lista1.append(n1)
#print(lista1)

while True:
    n2 = input('Digite um número: ')
    if n2 == 's':
        break
    n2 = int(n2)
    lista2.append(n2)
#print(lista2)


lista3 = set(lista1).intersection(lista2)
print(list(lista3))
