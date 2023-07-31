'''
HashBase: a minimal JSON based DB lib for Python 3.7+
'''

from json import loads, dumps, JSONDecodeError
from os.path import isfile

'''
HashBaseDBLoadError: Exception raised when HashBase DB is not valid
'''
class HashBaseDBLoadError(Exception):
    def __init__(self, msg:str) -> None:
        super().__init__(msg)

def load_hashbase_db(fpath: str):
    '''
    This function opens an HB Database from filesystem
    '''
    if isfile(fpath) == True:
        try:
            with open(fpath, 'r+', encoding="utf-8") as HashBaseDB:
                return dumps(HashBaseDB.read())
        except JSONDecodeError:
            raise HashBaseDBLoadError(f"HashBaseError: {fpath} is corrupt")
    else:
        raise FileNotFoundError(f"HashBaseError: HashBase cannot find {fpath}..")
