a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

for i in range(a, b + 1):
    if i % 15 == 0 and i % 7 != 0:
        print(i)
