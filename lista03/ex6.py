num = float(input('Digite um número: '))
i = 2*3*5*7*11*13
while i <= num:
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0 and i % 11 == 0 and i % 13 == 0:
        print(i)
    i += 1
