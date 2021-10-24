import re
import dodoku.getHash as getHash
import random

def _insert(parms):
    result = {}
    pattern = r"R(.*?)C(\d+)"
    row = int(re.search(pattern, pattern['cell'], re.IGNORECASE).group(1))
    column= int(re.search(pattern, pattern['cell'], re.IGNORECASE).group(2))
    result['grid'] = parms['grid']
    #insert value
    result['grid'][54 + (row-7)*15 + (column - 1)] = int(parms['value'])
    r = random.randint(0,56)
    result['integrity'] = getHash(result['grid'])[r:r+8]
    result['status'] = 'ok'
    return result

