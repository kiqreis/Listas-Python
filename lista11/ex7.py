import os

def local(programa):
    return os.path.dirname(programa)

if __name__ == '__main__':
    local()
