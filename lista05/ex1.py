matrizA = []
matrizB = []
matrizC = []
numLinha = int(input('Digite o número de linhas: '))
numColuna = int(input('Digite o número de colunas: '))



for i in range(numLinha):
    linha = []
    for j in range(numColuna):
        valores = int(input('Digite um valor: '))
        linha.append(valores)
    matrizA.append(linha)
#print(matrizA)

for l in range(numLinha):
    linha = []
    for m in range(numColuna):
        valores = int(input('Digite um valor: '))
        linha.append(valores)
    matrizB.append(linha)
#print(matrizB)

for i in range(numLinha):
    linha = [0]*numColuna
    matrizC.append(linha)
    for j in range(numColuna):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
        print(matrizC[i][j], end=' ')
    print()
