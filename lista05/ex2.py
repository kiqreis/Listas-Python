matriz = []

numLinha = int(input('Digite o número de linhas: '))
numColuna = int(input('Digite o número de colunas: '))

for i in range(numLinha):
    linha = []
    for j in range(numColuna):
        valores = int(input('Digite um valor: '))
        linha.append(valores)
    matriz.append(linha)
#print(matriz)

transposta = list(map(list, zip(*matriz)))
print(transposta)

