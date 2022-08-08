num = int(input('Digite um número: '))
fat = 1

for num in range(num, 0, -1):
    fat *= num
print(fat)
