import ast

def interpreta(string):
    try:
        return ast.literal_eval(string)
    except Exception:
        raise Exception('Tipo desconhecido')

if __name__ == '__main__':
    interpreta()
