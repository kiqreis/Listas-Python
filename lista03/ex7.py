n = int(input('Digite um número: '))

for i in range(2, n):
    j = 2
    primo = True
    while j < i:
        if i % j == 0:
            primo = False
            break
        j = j + 1
    if primo:
        print(i)
