lista = []

while True:
    n = input('Digite um número: ')
    if n == 's':
        break
    lista.append(int(n))
    
print(any(lista.count(elemento) > 1 for elemento in lista))
