import numpy as np

def soma(m1 = np.random.rand(2, 2), m2 = np.random.rand(2, 2)):
    try:
        return m1 + m2
    except ValueError:
        raise ValueError('Tamanhos incosistentes')
       
      
if __name__ == '__main__':
    soma()
