lista = []

while True:
    n = input('Digite um número: ')
    if n == 's':
        break
    elif type(n) == int:
        n = int(n)
        lista.append(n)
    elif type(n) == float:
        n = float(n)
        lista.append(n)
    elif type(n) == str:
        n = str(n)
        lista.append(n)
    elif type(n) == list:
        n = list(n)
        lista.append(n)
print(lista)
