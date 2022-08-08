import requests
import bs4

def conta_tag(html, tipo):
    html_doc = html
    soup = bs4.BeautifulSoup(html_doc, 'html.parser')
    return len(soup.find_all(tipo))

if __name__ == '__main__':
    conta_tag()
