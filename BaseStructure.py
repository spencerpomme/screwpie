'''
This is a web crawler collecting ZHIHU & Douban data.

BaseStructure is an empty class that to be customized for specific websites.
'''

class BaseStructure(object):
    '''
    This class creates basic html page structure analysis object.

    '''
    def __init__(self):
        '''
        Creates a data field.
        '''
        self.fields = []

    def __repr__(self):
        '''
        Representation of the structure.

        Returns:
            a human readable list of data fields from the web page.
        '''
        if not self.fields:
            raise NotImplementedError("To be implemented in sub class.")
        else:
            

