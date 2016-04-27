import bs4
import requests

url = 'http://www.douban.com/group/kaopulove/discussion?start=0'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, 'lxml')

def getGroupName(soup: bs4.BeautifulSoup) -> str:
    """
    This function is a part of the scroup application, retriving
    group name from the topic table page.
    """
    groupname = soup.select('div > div > div[class="info"]\
                            > div[class="title"] > a')[0].getText()
    return groupname

name = getGroupName(soup)
print(name)

    
