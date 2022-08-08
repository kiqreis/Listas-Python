import re

string = input('Digite seu nome e sua nota, respectivamente: ')
lista = list(map(float, re.findall(r'\d+\.\d+', string)))

print(lista)
