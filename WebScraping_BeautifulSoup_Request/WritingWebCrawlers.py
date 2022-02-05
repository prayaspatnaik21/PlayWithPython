import urllib.request
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global Page
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    requestUrl = urllib.request.Request('https://bloggingfordevs.com/cpp-blogs/',None,headers)
    html = urllib.request.urlopen(requestUrl)
    
    bs = BeautifulSoup(html,'lxml')
    # print(bs.prettify())

    try:
        print(bs.h1.get_text())

    except AttributeError as e:
        print(e)
        print("This page is missing something Continuing")

getLinks('')