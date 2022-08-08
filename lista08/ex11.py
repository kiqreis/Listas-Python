def sum(lista):
    if not lista:
        return 0
    if isinstance(lista[0], list):
        soma = sum(lista[0])
    else:
        soma = lista[0]
    return soma + sum(lista[1:])

if __name__ == '__main__':
    print(sum())
