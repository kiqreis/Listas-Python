import magic

def tipo_arquivo(arquivo):
    return magic.from_file(arquivo, mime=True)

if __name__ == '__main__':
    tipo_arquivo()
