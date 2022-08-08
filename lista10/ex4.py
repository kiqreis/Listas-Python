from sympy import *

def processa(expressao, var, var0 = 0):
    var = symbols('x')
    return diff(expressao, var), integrate(expressao, var), limit(expressao, var, var0)

if __name__ == '__main__':
    processa()
