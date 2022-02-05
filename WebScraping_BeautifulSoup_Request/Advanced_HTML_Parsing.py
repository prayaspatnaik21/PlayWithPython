from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
"""
Accessing Attributes - myTag.attrs

Regular Expression - images = bs.find_all('img',
{'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})

Dealing  with Children

for child in bs.find('table',{'id':'giftList'}).children

Dealing with Siblings

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings

Dealing with Parent

bs.find('img',
{'src':'../img/gifts/img1.jpg'})
.parent.previous_sibling.get_text()
    
"""

def getData(url):
    try:
        htmlData = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    
    try:
        bs = BeautifulSoup(htmlData.read(),'lxml')
        title = bs.h1
        nameList = bs.findAll('span',{'class':'green'})

        for name in nameList:
            print(name.get_text())
    except AttributeError as e:
        print(e)
        return None
    
    return title
        
Data = getData('https://pythonscraping.com/pages/warandpeace.html')

if Data == None:
    print("Data cannot be found")
else:
    print(Data)


