import requests
import bs4

def lista(site):
    lista = []
    html_doc = site
    soup = bs4.BeautifulSoup(html_doc, "html.parser")
    menus = soup.find_all("li")

    for menu in menus:
        lista.append(menu.text)
    return lista
if __name__ == '__main__':
    lista()
