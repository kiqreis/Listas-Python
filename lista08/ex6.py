def fatorial(n):
    if n == 0:
        return 1 
    return n * fatorial(n - 1)

if __name__ == '__main__':
    print(fatorial())
