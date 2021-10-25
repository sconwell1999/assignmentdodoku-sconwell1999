import re
from dodoku.getHash import getHash
import random
import ast

def _insert(parms):
    result = {}
    if not parms.hasKey('cell'):
        result = {'status':'error: Missing cell value'}
        return result
    result['grid'] = ast.literal_eval(parms['grid'])
    if not parms['integrity'] in getHash(result['grid']):
        result = {'status': 'error: Integrity mismatch'}
        return result
    try:
        if int(parms['value']) > 9 or int(parms['value']) < 1:
            raise ValueError
    except ValueError:
        result = {'status': 'error: Invalid value'}
        return result
    pattern = r"R(.*?)C(\d+)"
    row = int(re.search(pattern, parms['cell'], re.IGNORECASE).group(1))
    column= int(re.search(pattern, parms['cell'], re.IGNORECASE).group(2))
    #insert value
    if row < 7 and column < 10:
        if result['grid'][(row-1)*9 + (column - 1)] >= 0:
            result['grid'][(row-1)*9 + (column - 1)] = int(parms['value'])
        else: 
            result = {'status': 'error: Immutable cell'}
            return result
    elif row > 6 and row < 10 and column < 16:
        if result['grid'][54 + (row-7)*15 + (column - 1)] >= 0:
            result['grid'][54 + (row-7)*15 + (column - 1)] = int(parms['value'])
        else: 
            result = {'status': 'error: Immutable cell'}
            return result
    elif row > 9 and row < 16 and column > 6 and column < 16:
        if result['grid'][99 + (row-10)*9 + (column - 7)] >= 0:
            result['grid'][99 + (row-10)*9 + (column - 7)] = int(parms['value'])
        else: 
            result = {'status': 'error: Immutable cell'}
            return result
    else:
        result = {'status':'error: Invalid cell'}   
        return result
    if not(columnValuesCheck(result['grid'], column) and rowValuesCheck(result['grid'], row) and subGridValuesCheck(result['grid'], row, column)):
        result['status'] = 'warning'
    else:
        result['status'] = 'ok'   
    #check for valid numbers
    r = random.randint(0,56)
    result['integrity'] = getHash(result['grid'])[r:r+8]
    return result

def columnValuesCheck(grid, column):
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
            
    if len(values) == 15:        
        return len(values[0:9]) == len(set(values[0:9])) and len(values[6:16]) == len(set(values[6:16]))
    return len(values) == len(set(values))

def rowValuesCheck(grid, row):
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
            
    if len(values) == 15:
        return len(values[0:9]) == len(set(values[0:9])) and len(values[6:16]) == len(set(values[6:16]))
    return len(values) == len(set(values))

def subGridValuesCheck(grid, row, column):
    values = []
    startRow = row - row % 3
    startColumn = column - column % 3
    if row in range(1,7):
        for i in range(3):
            for j in range(3):
                values.append(grid[(startRow-1+i)*9+startColumn+j])
    if row in range(7,10):
        for i in range(3):
            for j in range(3):
                values.append(grid[(startRow-1+i)*15+startColumn+j])
    if row in range(10,16):
        for i in range(3):
            for j in range(3):
                values.append(grid[(startRow-1+i)*9+startColumn+j])
    return len(values) == len(set(values))
    
