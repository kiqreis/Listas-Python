n = int(input(''))
d = int(input(''))
k = 1

print('EXTRA:')
for i in range(1, n + 1):
    if i % d == 0:
        print(i, end=', ')
