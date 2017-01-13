'''
This is a web crawler collecting Douban Group data.

This class extends the BaseCrawler class and adds website specific functions.
'''

from BaseCrawler import BaseCrawler
from DGStructure import DGStructure

class DGCrawler(BaseCrawler):
    '''
    This class is a specific crawler for douban group.
    
    '''
    def __init__(self):
        pass

if __name__ == '__main__":
    print(dir(BaseCrawler))
    print(dir(DGStructure))
