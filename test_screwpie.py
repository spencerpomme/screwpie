from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.douban.com/group/kaopulove/discussion?start=0"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")
table = soup.findAll()