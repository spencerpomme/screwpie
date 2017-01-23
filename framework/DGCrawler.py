'''
This is a web crawler collecting Douban Group data.

This class extends the BaseCrawler class and adds website specific functions.
'''

from BaseCrawler import *
from DGStructure import DGStructure
from Pipeline import SaveToCSV
from bs4 import BeautifulSoup
from progressbar import ProgressBar
import requests
import time


class DGCrawler(BaseCrawler):
    '''
    This class is a specific crawler for douban group.

    '''
    post_per_page = 25  # There are 25 posts per group page in douban group

    def __init__(self, base_url, save_name=None):
        '''
        Douban group constructor.
        Attributes:
            base_url   : The page where crawler starts crawling
            save_name  : The temp save csv file name to hold collected data
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
        self.targets = ()
        if not save_name:
            self.set_group_name()
            save_name = self.get_group_name() + '.csv'

        if not BaseCrawler._is_legal_file_name(save_name):
            raise CSVfileNameError

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

    def run(self, pages=None, target=None):
        '''
        The main function of the crawler.
        Arguments:
                pages : Number of pages to be downloaded, default to None;
                target: Note down target author while running through required
                        number of pages if applicable, default to None.
                        Is a tuple of str. 
        '''
        if not pages:
            self.set_total_page()
            pages = self.get_total_page()

        save_file = SaveToCSV(self.save_name)
        if target is not None and isinstance(target, tuple):
            target_file = self.set_targets(target)
        bar = ProgressBar(max_value=pages, redirect_stdout=True)
        for page in range(pages):
            print("Crawling page %d ..." % (page + 1))
            current_url = self.base_url + str(DGCrawler.post_per_page * page)
            time.sleep(0.5)
            try:
                for line in self.parse_page(current_url):
                    save_file.write_data(line)
                    if self.targets and DGCrawler._has_targets(line):
                        target_file.write_data(line)
            except Exception as e:
                print('There is a problem:', e)
                print('Waiting 10 seconds to recover...')
                time.sleep(10)
                page -= 1
                continue
            bar.update(page+1)
            
        save_file.close_file()

    def parse_page(self, current_page: str):
        '''
        This method uses imported DGStructure class to get fields list of 
        current page.
        Attributes:
                current_page: url
        Yields:
                a list, one line data of the group topics
        '''
        res = requests.get(current_page)
        soup = BeautifulSoup(res.text, 'lxml')
        table = soup.findAll('table', {'class': 'olt'})
        rows = list(table)[0].findAll("tr", {"class": "", "id": ""})
        if not len(rows):
            print("Empty page or something wrong on %s" % current_page)
            return None
        for row in rows:
            data_row = DGStructure(row)
            yield data_row.get_line_data()

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
        res = requests.get(self.base_url + '0', headers=self.headers)
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
        Instance method that gets group name of the group.
        Usually only need to be called once at the beginning per run.
        '''
        res = requests.get(self.base_url + '0', headers=self.headers)
        soup = BeautifulSoup(res.text, 'lxml')
        sidebar_soup = soup.select('div[class="side-reg"]')[0]
        self.group_name = sidebar_soup.select('div[class="title"]')[0].a.text

    def set_targets(self, targets: tuple):
        '''
        Instance method that sets target authors. Garuantees the targets tuple
        contains valid target string.

        Attributes:
                targets: a tuple of str names
        Returns:
                An SaveToCSV object
        '''
        if targets:
            for target in targets:
                if not isinstance(target, str):
                    raise InvalidTargets
            self.targets = targets
            return SaveToCSV('target_histroy.csv')

    def _has_targets(line)->bool:
        '''
        Class method

        Costumized functionality for douban group. To detect whether an author
        is in current group.

        Attributes:
                line: current line of post in the group
        '''
        if not self.targets:
            raise Exception('Need to set targets first!')
        if line:
            try:
                if line[2] in self.targets:
                    return True
                else:
                    return False
            except Exception as e:
                print(e)
                print(line)
                raise e

'''
Temporary test code:
[date: 2017.1.20][status: working]
'''
if __name__ == '__main__':

    base_url = 'https://www.douban.com/group/GuangZhoulove/discussion?start='
    test = DGCrawler(base_url)
    test.run()
