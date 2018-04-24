import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = 'https://g1.globo.com/mundo/noticia/van-atropela-pedestres-em-toronto-no-canada.ghtml'

uClient = urlopen(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
# containers = page_soup.findAll("div", {"class": "item-container"})

# container = containers[0]
# container.div
# print(container.a)

x = page_soup.findAll(text=re.compile('Canadá'))
print(x)