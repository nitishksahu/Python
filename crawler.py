import requests

from bs4 import BeautifulSoup


def nits_spider():
    url = 'http://nits123.github.io'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('h1'):
        print(link.string)

    for link in soup.findAll('li'):
        print(link.string)


nits_spider()
