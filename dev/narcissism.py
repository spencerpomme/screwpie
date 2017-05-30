'''
This module is for entertainment only.
'''

class FollowerScanner(object):
    '''
    This class provides basic functionalities to get to know your followers
    '''
    def __init__(self, home_url:str, cookies:str):
        '''
        Creates a new FollowerScanner instance
        Args:
            home_url: homepage url of the user in string
            cookies : the cookies of the user in string
        Returns:
            No returns
        Raises:
            TypeError: An error occurrs when home_url or cookies are not string
        '''
        self.home = home_url
        self.cookies = cookies
