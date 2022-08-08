def leia(nome):
    with open(nome, 'r') as f:
        n = f.read()
        f.close()
        return n

    
if __name__ == '__main__':
    print(leia())
