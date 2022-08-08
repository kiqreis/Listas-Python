import ast 
dic = ast.literal_eval(input('Insira um dicionário: '))
valores = list(dic.values()) 
resultado = []
metade = len(valores) // 2
valores.sort()
if not len(valores) % 2:
        resultado.append((valores[metade - 1] + valores[metade]) / 2)
else:
    resultado.append(valores[metade])
print(*resultado)
