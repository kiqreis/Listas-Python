dic = dict()

while True:
    nome = input('Insira seu nome: ')
    if nome == 's':
        break
    idade = int(input('Insira sua idade: '))
    if nome not in dic.keys():
        dic.update({nome: idade})


print(dic)
