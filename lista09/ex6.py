def msb(n):
    lista = []
    binario = bin(n)
    for i in binario:
        lista.append(i)
    lista.reverse()
    return int(''.join(lista).rfind('1'))

if __name__ == '__main__':
    msb()
