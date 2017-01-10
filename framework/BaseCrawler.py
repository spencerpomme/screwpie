'''
This is a web crawler framework that help collecting ZHIHU & Douban data.
'''

from bs4 import BeautifulSoup
import requests
import datetime
import time
import csv
import os

# Project defined exceptions:


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
        + Set a csv file name to save the temp data
        + Gets total web pages to be scaped

    Attributes:
            base_url: The page where crawler starts crawling
            save_name: The temp save csv file name to hold collected data
            total_page: total pages to be scaped
    '''

    def __init__(self):
        '''
        Constructor, can be customized in subclasses.
        '''
        self.base_url = ""
        self.save_name = ""
        self.total_page = 0

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

    def set_total_page(self, url, mode='Test', page_num=1)->int:
        '''
        Gets total pages to be scaped in one mission.

        Specific page structure rule needs to be defined in subclass, here
        provides test features.

        Attributes:
            url: target webpage url
            mode: if mode == 'Test' then enable test feature
            page_num: defaut scape page number set to 1
        Returns: 
            An integer page number
        Raises: 
            NotImplementedError
        '''
        if mode == 'Test':
            return page_num
        else:
            raise NotImplementedError("Need to define get_total_page().")

    def create_tempfile(self, directory=None):
        '''
        Instance method that returns a pointer of a new temp file location.
        By default the saving location is current working directory.

        Args:
            directory: The location that wish to save the temp csv file
        Returns:
            An IOTextWrapper object
        Raises:
            CSVfileNameError: when the directory and self.save_name fail to
            form a legal directory location

        TODO: It may not be a good practice, which is to say, create a IO
        object and left it unclosed by just returning it. So change it in
        the future shall any problem occurs.
        '''
        if not directory:
            location = os.getcwd()
        try:
            temp_csv = open(r'%s/%s' % (directory, self.save_name))
        except Exception as e:
            print(e)
            os.remove(r'%s/%s' % (directory, self.save_name))
        return temp_csv

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
