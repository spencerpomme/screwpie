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
        Creates a data fields.
        '''
        raise NotImplementedError("Define __init__ for specific websites.")

    def __repr__(self):
        '''
        Representation of the structure.

        Returns:
            a human readable list of data fields from the web page
        '''
        return dir(self)

    def __str__(self):
        '''
        str method of the structure.

        Returns same content as __repr__ yet called by print()
        '''
        return str(dir(self))

    def set_fields(self):
        '''
        Set field rules to scape data from page using bs4.
        To be defined in subclass.
        '''
        raise NotImplementedError("Define scaping rule for specific websites.")
