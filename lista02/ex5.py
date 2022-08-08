import math

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

print()
ari = (n1 + n2 + n3) / 3
geo = (n1*n2*n3)**(1/3)
qua = math.sqrt((n1**2 + n2**2 + n3**2)/3)
har = 3/(1/n1 + 1/n2 + 1/n3)



if n1 and n2 and n3 > 0:
    if ari < geo and ari < qua and ari < har:
        print(f'Menor: {ari}')
    elif geo < ari and geo < qua and geo < har:
        print(f'Menor: {geo}')
    elif qua < ari and qua < geo and qua < har:
        print(f'Menor: {qua}')
    elif har < ari and har < geo and har < qua:
        print(f'Menor: {har}')

if n1 and n2 and n3 > 0:
    if ari > geo and ari > qua and ari > har:
        print(f'Maior: {ari}')
    elif geo > ari and geo > qua and geo > har:
        print(f'Maior: {geo}')
    elif qua > ari and qua > geo and qua > har:
        print(f'Maior: {qua}')
    elif har > ari and har > geo and har > qua:
        print(f'Maior: {har}')
