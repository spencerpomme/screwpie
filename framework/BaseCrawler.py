'''
This module is a component of web crawler framework that help collecting 
ZHIHU & Douban data.
'''

class CSVfileNameError(Exception):

    def __str__(self):
        return 'Invalid file name, please add .csv at the end of name.'


class WrongURL(Exception):

    def __str__(self):
        return 'Invalid url input, input should be valid url of douban group.'


class NoPageNumber(Exception):

    def __str__(self):
        return 'Failed to get total group topic page numbers.'


class BaseCrawler(object):
    '''
    The base class of specific crawlers, a placeholder.

    This base class has the following basic functionalities:
        + Set base url to start crawling
        + Gets total web pages to be scaped

    Attributes:
            base_url   : The page where crawler starts crawling
            total_page : total pages of the group post
    '''

    def __init__(self, base_url, save_name):
        '''
        Constructor, can be customized in subclasses.
        '''
        self.base_url = base_url
        self.save_name = save_name
        self.total_page = None

    def set_base_url(self, url: str):
        '''
        Instance method that sets base url of the crawler.
        '''
        if _is_legal_url(url):
            self.base_url = url
        else:
            raise WrongURL

    def set_save_name(self, name: str):
        '''
        Instance method that sets file name of temp csv file to hold data.
        '''
        if _is_legal_file_name(name):
            self.save_name = name
        else:
            raise CSVfileNameError

    def set_total_page(self):
        '''
        Gets total pages to be scaped in one group.

        Specific page structure rule needs to be defined in subclass, here
        provides test features.
        '''
        raise NotImplementedError("Need to define get_total_page().")

    def _is_legal_url(url: str)->bool:
        '''
        Class method that determines whether an url is legal.
        Return True by default, need add condition in subclass.

        TODO: to be implemented using regex
        '''
        return True

    def _is_legal_file_name(name: str):
        '''
        Class method that determines whether an file name is legal.
        '''
        if name[-4:] != '.csv':
            return False
        legal_pattern = re.compile('(?<!\s)\w+.csv(?!\w+)')
        result = legal_pattern.match(name)
        if result is None:
            return False
        return True
