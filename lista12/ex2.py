import requests, re, bs4



def link(html):
    lista = []
    lista2 = []
    html_doc = html
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')

    for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
        lista.append(link.get('href'))
        lista2.append(link.text)
    return lista[0], lista2[0]
 

if __name__ == '__main__':
    link()
