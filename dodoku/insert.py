import re
from dodoku.getHash import getHash
import random
import ast

def _insert(parms):
    result = {}
    result['grid'] = ast.literal_eval(parms['grid'])
    if not parms['integrity'] in getHash(parms['grid']):
        result = {'status': 'error: Integrity mismatch'}
        return result
    pattern = r"R(.*?)C(\d+)"
    row = int(re.search(pattern, parms['cell'], re.IGNORECASE).group(1))
    column= int(re.search(pattern, parms['cell'], re.IGNORECASE).group(2))
    #insert value
    if row < 7 and column < 10:
        result['grid'][(row-1)*9 + (column - 1)] = int(parms['value'])
    elif row > 6 and row < 10 and column < 16:
        result['grid'][54 + (row-7)*15 + (column - 1)] = int(parms['value'])
    elif row > 9 and row < 16 and column > 6 and column < 16:
        result['grid'][99 + (row-10)*9 + (column - 7)] = int(parms['value'])
    else:
        result = {'status':'error: Invalid cell'}   
        return result
    r = random.randint(0,56)
    result['integrity'] = getHash(result['grid'])[r:r+8]
    result['status'] = 'ok'
    return result

def getColumnValues(grid, row, column):
    values = []
    if column in range(1,7):
        for x in range(0,48,9):
            values.append(grid[x+column-1])
    elif column in range(7,10):
        for x in range(0,48,9):
            values.append(grid[x+column-1])
        for x in range(54,85,15):
            values.append(grid[x+column-1])
        for x in range(99,145,9):
            values.append(grid[x+column-7])
    elif column in range(10,16):
        for x in range(63,148,9):
            values.append(grid[x+column-10])
    return values

def getRowValues(grid, row, column):
    values = []
    if row in range(1,7):
        for x in range(0,9):
            values.append(grid[(row-1)*9+x])
    elif row in range(7,10):
        for x in range(0,15):
            values.append(grid[54+(row-7)*15+x])
    elif row in range(10,16):
        for x in range(0,9):
            values.append(grid[99+(row-1)*9+x])
    return values

def getSubGridValues(grid, row, column):
    values = []
    if row in range(1,7):
        for x in range(0,3):
            return
    
