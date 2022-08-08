conj1 = set()
conj2 = set()

while True:
    n = input('Digite um número: ')
    if n == 's':
        break
    conj1.add(int(n))

#print(conj1)
while True:
    m = input('Digite um número: ')
    if m == 's':
        break
    conj2.add(int(m))
#print(conj2)

result = sorted(conj1 & conj2)
print(list(result))
