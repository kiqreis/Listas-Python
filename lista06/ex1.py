import re

s = input('Digite uma string: ')
c = input('Digite uma letra: ')
print(re.sub(rf'{c}', '', s))
