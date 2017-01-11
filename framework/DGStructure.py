'''
This is a web crawler framework that help collecting ZHIHU & Douban data.

DGStructure extends BaseStructure class to extract needed information in douban
group web page.
'''

from BaseStructure import BaseStructure
from bs4 import BeautifulSoup
from types import MethodType


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
                title      : title of the post in the table
                title_url  : url links to the post page
                author     : author of the post
                author_url : url links to the author's homepage
                follow_num : reply number of the post
                time       : last reply time of the post
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

    def get_row_data(self)->list:
        '''
        This method return a list of all Attributes aquired from douban group.
        '''
        attrs = [i for i in dir(self) if not i.startswith('__')
                 and not isinstance(i, MethodType)]
        assert len(attrs) == 6
        return attrs
