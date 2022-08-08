import re

texto = input('Diga seu nome, idade, cidade e estado: ')
nomeSobrenome = re.search(r'[A-Z]\w+\s[A-Z]\w+\s[A-Z]\w+|[A-Z]\w+\s[A-Z]\w+|[A-Z]\w+\s\w+\s[A-Z]\w+|[A-Z]\w+', texto).group()
idade = re.search(r'\d+', texto).group()
#Cidade-BR | São Cidade-BR
cidEstado = re.search(r'[A-Z]\w+\s[de|da|das]+\s[de|da|das]+\s[A-Z]\w+\-[A-Z]{2}|[de|da]+\s[A-Z]\w+\-[A-Z]{2}|[de|da]+\s[A-Z]\w+\s[de|da]+\s[A-Z]\w+\-[A-Z]{2}|[A-Z]\w+\s[A-Z]\w+\-[A-Z]{2}|[A-Z]\w+\-[A-Z]{2}|[A-Z]\w+\s\w+\s[A-Z]\w+\-[A-Z]{2}', texto).group()
estado = re.search(r'[A-Z]{2}', texto).group()
re.sub(r'\-[A-Z]{2}', '', cidEstado)
f = list()
f.append(nomeSobrenome)
f.append(int(idade))
f.append(re.sub(r'\-[A-Z]{2}', '', cidEstado))
f.append(estado)
print(tuple(f))
