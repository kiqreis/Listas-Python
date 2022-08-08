lista = []

a = int(input('Digite um número inteiro: '))
b = int(input('Digite um número inteiro: '))
m = int(input('Digite um número inteiro: '))

if a > b:
    for i in range(b, a + 1):
        if i % m == 0:
            lista.append(i)
elif b > a:
    for k in range(a, b + 1):
        if k % m == 0:
            lista.append(k)

print(sorted(lista))
