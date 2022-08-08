lista = []

while True:
    n = input('Digite um número: ')
    if n == 's':
        break
    lista.append(int(n))
#print(lista)

x = int(input('Digite um número x: '))
if x in lista:
    lista.remove(x)

lista_temp = []
for i in lista:
    lista_temp.append(i)

lista = sorted(set(lista_temp))
print(*lista, sep='\n')
