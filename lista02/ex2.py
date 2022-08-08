import turtle 

tipo = input('Digite um formato geométrico: ')
if tipo == 'quadrado':
    L = int(input('Digite o tamanho do lado: '))
    turtle.forward(L)
    turtle.right(90)
    turtle.forward(L)
    turtle.right(90)
    turtle.forward(L)
    turtle.right(90)
    turtle.forward(L)
elif tipo == 'retangulo':
    l = int(input('Digite o tamanho do lado: '))
    h = int(input('Digite a altura: '))
    if l == h:
        print('Continua sendo um quadrado...')
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(l)
    turtle.right(90)
    turtle.forward(h)
else:
    radius = int(input('Digite o tamanho do raio: '))
    turtle.circle(radius)
