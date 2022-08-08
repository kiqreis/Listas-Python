def ehpar(n):
    if not isinstance(n, int):
        return None 
    return n % 2 == 0

if __name__ == '__main__':
    print(ehpar())
