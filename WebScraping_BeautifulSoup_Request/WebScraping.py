from bs4 import BeautifulSoup
import requests
import csv

#Request.get gives the response object
source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

csv_file = open('cms_scrape.csv','w')

csv_writer = csv.writer(csv_file)

#print(soup.prettify())
csv_writer.writerow(['Headline','Summary','VideoLink'])

for article in soup.find_all('article'):

    headline = article.h2.a.text
    print(headline)

    Summary = article.find('div',class_='entry-content').p.text
    try:
        vidSrc = article.find('iframe',class_='youtube-player')['src']

        vidId = vidSrc.split('/')[4]
        vidId = vidId.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vidId}'
    except Exception as e:
        yt_link = None

    print(yt_link)

    print()

    csv_writer.writerow([headline,Summary,yt_link])


csv_file.close()