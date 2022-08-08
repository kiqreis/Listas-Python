from sympy import *


def distancia(obj1, obj2):
    inter = intersection(obj1, obj2)
    if not inter:
        return None
    elif len(intersection(obj1, obj2)) <= 1:
        return 0
    elif len(intersection(obj1, obj2)) > 1:
        return float(inter[0].distance(inter[1]))

if __name__ == '__main__':
    distancia()
