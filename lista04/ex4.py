lista = []

while True:
    n = input('Digite i, r ou s: ')
    if n == 's':
        break
    if n == 'i':
        lista.insert(0, int(input('Insira um valor: ')))
    elif n == 'r':
        print(lista.pop(0))
