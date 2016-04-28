from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.douban.com/group/kaopulove/discussion?start=0"
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")

# the main topic table
table = soup.findAll("table", {"class": "olt"})
# finds the total topics
total_topic_data =  soup.find("span", {"class":"thispage"}).attrs["data-total-page"]
# finds rows of the table, exclude <tr> tags that not holding valid topic data
# the "id" key is to exclude javascript at the beginning of the table rows
rows = list(table)[0].findAll("tr", {"class": "", "id": ""})


if __name__ == "__main__":

    print("---*---" * 4)

    print(rows[0])