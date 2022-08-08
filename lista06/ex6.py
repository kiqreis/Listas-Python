txt = input('Digite o nome do arquivo: ')


"""with open(f'{txt}.txt', 'w') as f:
    f.write('''teste1 a
teste2 b
teste3 c''')"""
with open(f'{txt}', 'r') as f:
    data = f.readlines()
#print(data)
lista = []
with open(f'{txt}', 'w') as f:   
    data = data[: : -1]
    for i in range(len(data)):
        if data[i] == 0:
            lista.append(data[i])
            #f.writelines(data[i])
        else:
            lista.append(data[i].rstrip('\n'))
    for x in lista:
        f.write(x + '\n')

with open(f'{txt}') as f:
    print(f.read())
