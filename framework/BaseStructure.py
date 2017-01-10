'''
This is a web crawler framework that help collecting ZHIHU & Douban data.

BaseStructure is an base class that to be customized for specific websites.
'''


class BaseStructure(object):
    '''
    This class creates basic html page structure analysis object.

    This base class has the following basic functionalities:
        + Sets a list of data fields concerned in a certain webpage

    Attributes:
            fields: The page where crawler starts crawling

    '''

    def __init__(self):
        '''
        Creates a data field and total page number.
        '''
        self.fields = []

    def __repr__(self):
        '''
        Representation of the structure.

        Returns:
            a human readable list of data fields from the web page
        '''
        if not self.fields:
            raise NotImplementedError("To be implemented in subclass.")
        else:
            return self.fields

    def set_fields(self, url):
        '''
        Set field rules to scape data from page using bs4.
        To be defined in subclass.

        Returns
        '''
        raise NotImplementedError("Define scaping rule for specific websites.")
