'''
This is a web crawler framework that help collecting ZHIHU & Douban data.

DGStructure extends BaseStructure class to extract needed information in douban
group web page.
'''

from BaseStructure import BaseStructure

class DGStructure(BaseStructure):
    '''
    This class decribes how to draw out douban group data.

    This douban group class has the following specific functionalities:
        + search for specific author
        TODO: 
            (1) search for specific time
            (2) search for posts containning specific keyword
            (3) search for posts which have specific length of title

    Attributes:
        Same as super class.
    '''

    def set_total_page():
        pass
