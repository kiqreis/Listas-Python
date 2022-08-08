n = int(input('Digite um número: '))
f1 = 0
f2 = 1

for i in range(0, n):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
print(f1)
