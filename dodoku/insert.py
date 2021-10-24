import re
from dodoku.getHash import getHash
import random

def _insert(parms):
    result = {}
    if not parms['integrity'] in getHash(parms['grid']):
        result = {'status': 'error: Integrity mismatch'}
        return result
    pattern = r"R(.*?)C(\d+)"
    row = int(re.search(pattern, parms['cell'], re.IGNORECASE).group(1))
    column= int(re.search(pattern, parms['cell'], re.IGNORECASE).group(2))
    result['grid'] = parms['grid']
    #insert value
    if row < 7 and column < 10:
        result['grid'][(row-1)*9 + (column - 1)] = int(parms['value'])
    elif row < 10 and column < 16:
        result['grid'][54 + (row-7)*15 + (column - 1)] = int(parms['value'])
    elif row < 16 and column < 16:
        result['grid'][99 + (row-10)*9 + (column - 7)] = int(parms['value'])
        
    r = random.randint(0,56)
    result['integrity'] = getHash(result['grid'])[r:r+8]
    result['status'] = 'ok'
    return result

