import scipy.integrate as integrate

def integral(funcao, ini = 0, fim = 1):
    resultado = integrate.quad(funcao, ini, fim)
    return resultado[0]


if __name__ == '__main__':
    integral()
