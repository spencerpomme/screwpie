'''
This is a web crawler collecting Douban Group data.

This class extends the BaseCrawler class and adds website specific functions.
'''

from BaseCrawler import *
from DGStructure import DGStructure
from Pipeline import SaveToCSV
from bs4 import BeautifulSoup
import requests


class DGCrawler(BaseCrawler):
    '''
    This class is a specific crawler for douban group.

    '''

    def __init__(self, base_url, save_name, page):
        '''
        Douban group constructor.
        Attributes:
            base_url   : The page where crawler starts crawling
            save_name  : The temp save csv file name to hold collected data
            save_page  : How many pages do you want to get
            group_name : Name of scrapping group
        '''
        BaseCrawler.__init__(self, base_url, save_name)
        self.total_page = None
        self.group_name = None
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0;"
                        "WOW64; rv:43.0) "
                        "Gecko/20100101 Firefox/43.0",
                        "Connection": "keep-alive"
                        }

    def __repr__(self):
        '''
        Representation method of douban group class.
        '''
        info = ('[DGCrawler Object]'
                '[base_url: %s]'
                '[save_name: %s]'
                '[total_page: %s'
                '[group_name: %s') % (self.base_url, self.save_name,
                                      self.total_page, self.group_name)
        return info

    def parse_data(self, current_page)->list:
        '''
        This method uses imported DGStructure class to get fields list of 
        current page.
        Attributes:
                current_page: 
        '''
        res = requests.get(current_page)
        soup = BeautifulSoup(res.text, 'lxml')
        table = soup.findAll('table', {'class': 'olt'})
        rows = list(table)[0].findAll("tr", {"class": "", "id": ""})
        for row in rows:
            data_row = DGStructure(row)
        

    def get_total_page(self):
        '''
        Instance method returns total_page field.
        '''
        if self.total_page:
            return self.total_page
        else:
            raise NoPageNumber

    def set_total_page(self):
        '''
        Instance method gets total pages to be scaped.
        Usually only need to be called once at the beginning per run.
        '''
        res = requests.get(self.base_url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'lxml')
        # the line below need to be validated. Needed message is in html tag
        # attribute value, the problem is how to extract it properly.
        paginator_list = soup.select('div[class="paginator"] > span')
        if paginator_list:
            self.total_page = int(paginator_list[1]['data-total-page'])
        else:
            raise NoPageNumber

    def get_group_name(self):
        '''
        Instance method that returns group_name field.
        '''
        if self.group_name:
            return self.group_name
        else:
            raise Exception('Group name yet set.')

    def set_group_name(self):
        '''
        Instance method gets group name of the group.
        Usually only need to be called once at the beginning per run.
        '''
        res = requests.get(self.base_url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'lxml')
        sidebar_soup = soup.select('div[class="side-reg"]')[0]
        self.group_name = sidebar_soup.select('div[class="title"]')[0].a.text

    def has_author(self, author: str, field):
        pass


'''
Temporary test code:
[date: 2017.1.19][status: working]
'''
if __name__ == '__main__':
    # print(dir(BaseCrawler), end='\n\n')
    # print(dir(DGCrawler))
    url = 'https://www.douban.com/group/18297/discussion?start=0'
    test = DGCrawler(url, "test.csv", 1)
    test.set_group_name()
    print(type(test.get_group_name()))
    try:
        print(test.get_group_name())
    except:
        print(test.get_group_name().encode('utf8'))
    test.set_total_page()
    print(test.get_total_page())
