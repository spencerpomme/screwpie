'''
This module is a component of web crawler framework that help collecting 
ZHIHU & Douban data.

Pipeline manages different data storing strategies of the crawler.
'''

import os
import csv

class SaveToCSV(object):
    '''
    This class defines data storing strategies for the crawler.
    '''

    def __init__(self, name, location=None):
        '''
        Initialize file/database name.
        Arguments:
                name: csv file name. This name is garuanteed to be legal since
                      it was tested by BaseCrawler._is_legal_file_name method.
        '''
        self.name = name
        if not location:
            self.location = os.getcwd()
        else:
            self.location = location
        self.csv_file = self.create_file()

    def __repr__(self):
        '''
        Representation format of this object.
        '''
        return 'Pipeline Object:'
               '[csv file: %s] at "%s"' % (self.name, self.location)

    def create_file(self):
        '''
        Instance method that returns a pointer of a new file location.
        By default the saving location is current working directory.

        Returns:
                An IOTextWrapper object
        Raises:
                CSVfileNameError: when the directory and self.save_name fail to
                form a legal directory location

        TODO: It may not be a good practice, which is to say, create a IO
        object and left it unclosed by just returning it. So change it in
        the future shall any problem occurs.
        '''
        try:
            file_ptr = open(r'%s/%s' % (self.location, self.name))
        except Exception as e:
            print(e)
            os.remove(r'%s/%s' % (self.location, self.name))
        else:
            return file_ptr

    def close_file(self):
        '''
        Close the opened csv file.
        '''
        self.csv_file.close()

    def write_data(self, data_row: list):
        '''
        Write data in the csv file.

        Arguments:
                data_row: a list of field data extracted from webpage, returned
                          by DGStructure object instance method get_row_data()
        '''
        writer = csv.writer(self.csv_file)
        writer.writerow(data_row)




        