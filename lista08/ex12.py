def min(lista):
    if len(lista) == 1:
        return lista[0]
    m = min(lista[1:])
    if m > lista[0]:
        return lista[0]
    return m

if __name__ == '__main__':
  print(min())
