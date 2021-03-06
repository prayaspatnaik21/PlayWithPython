from bs4 import BeautifulSoup
import requests

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

# match = soup.find('div',class_='article')
# print(match)

for article in soup.find_all('div',class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()