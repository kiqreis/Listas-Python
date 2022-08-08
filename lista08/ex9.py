def map(lista, funcao):
    num = []
    for i in lista:
        num.append(funcao(i))
    return num

if __name__ == '__main__':
    print(map())
