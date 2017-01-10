'''
This is a web crawler framework that help collecting ZHIHU & Douban data.

BaseStructure is an base class that to be customized for specific websites.
'''


class BaseStructure(object):
    '''
    This class creates basic html page structure analysis object.

    This base class has the following basic functionalities:
        + Sets a list of data fields concerned in a certain webpage
        + Gets total web pages to be scaped

    Attributes:
            fields: The page where crawler starts crawling
            total_page: total pages to be scaped

    '''

    def __init__(self):
        '''
        Creates a data field and total page number.
        '''
        self.fields = []
        self.total_page = 0

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

    def set_fields(self, url):
        '''
        Set field rules to scape data from page using bs4.
        To be defined in subclass.

        Returns
        '''
        raise NotImplementedError("Define scaping rule for specific websites.")
