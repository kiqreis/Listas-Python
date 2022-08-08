def menor(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    posicao = [j for j, pos in enumerate(lista) if pos == min]
    return min, posicao

if __name__ == '__main__':
    print(menor())
