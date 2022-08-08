menor = float('inf')
while True:
    n = input('Digite um número: ')
    if n == 's':
        break
    else:
        n = int(n)
        if n < menor:
            menor = n
print(menor)
