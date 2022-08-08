from Crypto.Hash import SHA256
import pandas as pd

def salva(dados):
    df = pd.DataFrame.from_dict(dados)
    j = df.to_json()
    h = df.to_html()
    l = df.to_latex()
    j, h, l = SHA256.new()
    return j.hexdigest(), h.hexdigest(), l.hexdigest()

if __name__ == '__main__':
    salva()
