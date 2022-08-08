def somaListas(lista1, lista2):
    lista = []
    if len(lista1) != len(lista2):
        return None
    for x, y in zip(lista1, lista2):
        lista.append(x + y)
    return lista

if __name__ == '__main__':
    print(somaListas())
