lista = []
def bit(x, n):
    binario = bin(x)
    for i in binario:
        lista.append(i)
    lista.reverse()
    return int(lista[n])

if __name__ == '__main__':
    bit()
