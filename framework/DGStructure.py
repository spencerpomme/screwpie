'''
This is a web crawler framework that help collecting ZHIHU & Douban data.

DGStructure extends BaseStructure class to extract needed information in douban
group web page.
'''

from BaseStructure import BaseStructure
from bs4 import BeautifulSoup


class DGStructure(BaseStructure):
    '''
    This class decribes how to draw out douban group data.

    This douban group class has the following specific functionalities:
        + search for specific author
        TODO: 
            (1) search for specific time
            (2) search for posts containning specific keyword
            (3) search for posts which have specific length of title

    Attributes:
        Same as super class.
    '''

    def __init__(self, data_row):
        '''
        Creates a data fields.

        This initialization method overrides the method from supper class.

        Arguments:
                data_row: A bs4.element.Tag object that contains a row
                of douban group posts.
        Attributes:
                title      : 
                title_url  :
                author     :
                author_url :
                follow_num :
                time       :
        '''
        self.title = data_row.find('td', {'class': 'title'}.a.attrs['title'])
        self.title_url = data_row.find(
            "td", {"class": "title"}).a.attrs["href"]
        self.author = data_row.find("td", {"nowrap": "nowrap"}).a
        self.author_url = data_row.find(
            "td", {"nowrap": "nowrap"}).a.attrs["href"]
        self.follow_num = data_row.find(lambda tag: len(
            tag.attrs) == 2 and tag.name == "td").text
        self.time = data_row.find(
            "td", {"nowrap": "nowrap", "class": "time"}).text
        if self.follow_num == "":
            self.follow_num = "0"

    def get_row_data(self):
        pass
