segundos = int(input('Segundos: '))

anos = segundos // (24 * 360 * 3600)
segundos = segundos % (24 * 360 * 3600)
meses = segundos // (24 * 30 * 3600)
segundos = segundos % (24 * 30 * 3600)
dias = segundos // (24 * 3600)
segundos = segundos % (24 * 3600)
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60 
segundos = segundos

if anos > 0:
    print(f'{anos} anos')
if meses > 0:
    print(f'{meses} meses')
if dias > 0:
    print(f'{dias} dias')
if horas > 0:
    print(f'{horas} horas')
if minutos > 0:
    print(f'{minutos} minutos')
if segundos > 0:
    print(f'{segundos} segundos')
    
