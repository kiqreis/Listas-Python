import requests
cidade = input('Digite a sua cidade: ')

c = cidade.split('-')
del c[-1]
d = ','.join(c).replace(',', '-').strip()

lista = []
for cont in range(11, 100):
    if 'cities' in requests.get(f'https://brasilapi.com.br/api/ddd/v1/{cont}').json():
        if d.upper() in requests.get(f'https://brasilapi.com.br/api/ddd/v1/{cont}').json()['cities']:
            lista.append(cont)
print(lista[0])

