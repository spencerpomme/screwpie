'''
This is a web crawler collecting ZHIHU & Douban data.
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

    This class as a super class of further custimized classes has 5 methods:
    '''
    def __init__(self):
        '''
        fields:
            baseURL: The page where crawler starts crawling.
            saveName: The temp save csv file name to hold collected data.
        '''
        self.base_url = ""
        self.save_name = ""

    def set_base_url(self, url:str):
        '''
        Set base url of the crawler.
        '''
        if _is_legal_url(url):
            self.base_url = url
        else:
            raise WrongURL

    def set_save_name(self, name:str):
        '''Set file name of temp csv file to hold data'''
        if _is_legal_file_name(name):
            self.save_name = name
        else:
            raise CSVfileNameError

    def _is_legal_url(url:str)->bool:
        '''
        Class method that determines whether an url is legal.
        Return True by default, need add condition in subclass.
        '''
        return True

    def _is_legal_file_name(name:str):
        '''
        Class method that determines whether an file name is legal.
        '''
        if name[-4:] != '.csv':
            return False
        legal_pattern = re.compile('(?<!\s)\w+.csv(?!\w+)')
        result = legal_pattern.match(name)
        if result == None:
            return False
        return True

    def save_data_csv(self):
        '''
        Instance method 
        




