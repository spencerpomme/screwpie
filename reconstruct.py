#! python3
# This script reconstruct the huge startOperation function into several samll
# functions.

def startOperation(init_url:str, pages:int=None, filename:str="TSTCSV")->list:
    """
    This function starts core process of crawler.
    """
    