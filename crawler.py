import requests

from bs4 import BeautifulSoup


def nits_spider():
    url = 'http://nits123.github.io'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('h1'):
        print(link.string)

    div = soup.find('nav')

    for link in div.find_all('a'):

        href = 'http://nits123.github.io' + link.get('href')
        print('Links are \n', href)
        if href =='http://nits123.github.io/blog':
            get_inside_link(href)


def get_inside_link(link):

    url = link
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    ul = soup.find('ul', {'class': 'posts'})
    print(ul)


nits_spider()
