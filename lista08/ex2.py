def soma(x, y):
    try:
        x + y
        return x + y
    except:
        return None

def subt(x, y):
    try:
        x - y
        return x - y
    except:
        return None


def mult(x, y):
    try:
        x * y
        return x * y
    except:
        return None

def divi(x, y):
    try:
        x / y
        return x / y
    except:
        return None



if __name__ == '__main__':
    print(soma())
    print(subt())
    print(mult())
    print(divi())
