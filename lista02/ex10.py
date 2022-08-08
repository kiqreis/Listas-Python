dia = int (input ('Digite o dia: '))
mes = int (input ('Digite o mês: '))
ano = int (input ('Digite o ano: '))
if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 0 or (mes == 2 and dia > 28) or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia == 31):
    print ('Não existe')
else:
    print ('Existe')
