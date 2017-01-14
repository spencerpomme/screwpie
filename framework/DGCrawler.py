'''
This is a web crawler collecting Douban Group data.

This class extends the BaseCrawler class and adds website specific functions.
'''

from BaseCrawler import *
from DGStructure import DGStructure
from bs4 import BeautifulSoup


class DGCrawler(BaseCrawler):
    '''
    This class is a specific crawler for douban group.

    '''

    def __init__(self, base_url, save_name, total_page):
        '''
        Douban group constructor.
        Attributes:
            base_url   : The page where crawler starts crawling
            save_name  : The temp save csv file name to hold collected data
            total_page : total pages of the group post
            group_name : name of scrapping group
        '''
        BaseCrawler.__init__(self, base_url, save_name)
        self.total_page = None
        self.group_name = None
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:43.0) "
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
        Instance method gets total pages to be scaped in one mission.
        '''
        res = requests.get(self.base_url, headers=self.headers)
        psoup = BeautifulSoup(res.text, 'lxml')
        # the line below need to be validated. The needed message is in html tag
        # attribute value, the problem is how to extract it properly.
        paginator_list = psoup.select('div[class="paginator"] > span')
        if paginator_list:
            self.total_page = int(paginator_list[1]['data-total-page'])
        else:
            raise NoPageNumber

    def get_group_name(self):
        '''
        Instance method that returns group_name field.
        '''
        pass




if __name__ == '__main__':
    print(dir(BaseCrawler), end='\n\n')
    print(dir(DGCrawler))
    url = 'https://www.douban.com/group/gz020/discussion?start=0'
    test = DGCrawler()
