
txt1 = input('Digite o nome do arquivo: ')
txt2 = input('Digite o nome do arquivo: ')
txt3 = input('Digite o nome do arquivo: ')

lista = []
with open(f'{txt1}', 'r+') as f:
    data = f.readlines()
    for i in range(len(data)):
        if data[i] != -1:
            lista.append(data[i].rstrip('\n'))
        else:
            lista.append(data[i])
    #print(f.read())
#print(lista)
lista2 = []
with open(f'{txt2}', 'r+') as f1:
    data2 = f1.readlines()
    for i in range(len(data2)):
        if data2[i] != -1:
            lista2.append(data2[i].rstrip('\n'))
        else:
            lista2.append(lista + data2[i])
    #print(f1.read())
#print(lista2)
lista3 = lista + lista2
with open(f'{txt3}', 'w+') as f2:
    result = sorted(set(lista3))
    for x in result:
        f2.write(x + '\n')
'''with open(f'{txt3}') as f2:
    print(f2.read())'''
