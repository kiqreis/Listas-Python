memoria = dict()

def fibonacci(n):
    if n not in memoria:
        if n < 3:
            memoria[n] = 1
        else:
            memoria[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memoria[n]
  
if __name__ == '__main__':
  print(fibonacci())
