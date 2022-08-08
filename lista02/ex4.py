a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o valor de c: '))

delta = b**2 - 4*a*c
raizDelta = delta ** 0.5
x1 = (- b - raizDelta) / 2*a
x2 = (- b + raizDelta) / 2*a

if a != 0:
    if delta > 0:
        print(f'As raízes são {x1} e {x2}')
    elif delta == 0:
        print(f'A raiz é {x1}')
    else:
        print('Nenhuma raiz')
elif a == 0:
    print(f'Riz da função afim é {-c/b}')
