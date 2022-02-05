from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getData(url):
    try:
        htmlData = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    
    try:
        bs = BeautifulSoup(htmlData.read(),'lxml')
        title = bs.h1
    except AttributeError as e:
        print(e)
        return None
    
    return title
        
Data = getData('http://www.pythonscraping.com/pages/page1.html')

if Data == None:
    print("Data cannot be found")
else:
    print(Data)