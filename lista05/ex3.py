lista = []


while True:
    n = input('Digite um número: ')
    if n == 's':
        break
    lista.append(int(n))
print(lista)

linhas = int(input('Digite um número de linhas: '))
colunas = int(input('Digite um número de colunas: '))

if len(lista) == linhas * colunas:
    matriz = []
    for i in range(linhas):
        lista_temp = []
        for j in range(colunas):
            lista_temp.append(lista[i * colunas + j])
        matriz.append(lista_temp)
        print(*matriz[i], sep = ' ')
else:
    print('IMPOSSIVEL')
