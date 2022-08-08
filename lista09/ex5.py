def troca(x, n):
    num = bin(x & ((~0 << n) -1))
    return int(num, 2)

if __name__ == '__main__':
    troca()
