import re
s = input('Digite uma string: ')
n = int(input('Digite um número: '))
x = input('Digite um caractere: ')
if n < len(s):
    print(re.sub(r'\w$', x, s))
else:
    s = s + x
    print(s)
