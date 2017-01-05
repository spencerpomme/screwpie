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

    This base class has the following basic functionalities:
        + Set base url to start crawling;
        + Set a csv file name to save the temp data;
        + Provide test crawling run, i.e. no saving data just print out;
        + Provide a data structure reader to set SQL format;

    Attributes:
            baseURL: The page where crawler starts crawling.
            saveName: The temp save csv file name to hold collected data.
    '''

    def __init__(self):
        '''
        Constructor, can be customized in subclasses.
        '''
        self.base_url = ""
        self.save_name = ""


    def set_base_url(self, url:str):
        '''
        Instance method that sets base url of the crawler.
        '''
        if _is_legal_url(url):
            self.base_url = url
        else:
            raise WrongURL


    def set_save_name(self, name:str):
        '''
        Instance method that sets file name of temp csv file to hold data.
        '''
        if _is_legal_file_name(name):
            self.save_name = name
        else:
            raise CSVfileNameError


    def create_tempfile(self, directory=None):
        '''
        Instance method that returns a pointer of a new temp file location.
        By default the saving location is current working directory.

        Args:
            directory: The location that wish to save the temp csv file.
        Returns:
            An IOTextWrapper object.
        Raises:
            CSVfileNameError: when the directory and self.save_name fail to
            form a legal directory location.

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
