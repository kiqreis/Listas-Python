n = int(input('Digite um número: '))
k = 0

print('EXTRA:')
while True:
    if k < n:
        print(k, end=', ')
        k += 1
    elif k == n:
        print(k)
        break
