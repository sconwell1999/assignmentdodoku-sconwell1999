import hashlib
import random

def _create(parms):
    result = {'grid':'', 'integrity':'', 'status':''}

    if parms['op'] == 'create' and 'level' in parms:
        result['status'] = 'ok'
    
    if parms['level'] == '2':
        result['grid'] = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,
                       0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,
                       0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,
                       0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,
                       -9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0
                       ,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]
    r = random.randint(0,56)
    result['integrity'] = getHash(result['grid'])[r,r+8]
        
    return result

def getHash(grid):
    #convert to column-major string
    cm_string = ''
    for i in range(0,6):
        for x in range(i,i+46,9):
            cm_string += str(grid[x])
        for x in range(i+54,i+85,15):
            cm_string += str(grid[x])
    for i in range(0,3):
        for x in range(i+6,i+52,9):
            cm_string += str(grid[x])
        for x in range(i+60,i+91,15):
            cm_string += str(grid[x])
        for x in range(i+99,i+145,9):
            cm_string += str(grid[x])
    for i in range(0,6):
        for x in range(i+63,i+94,15):
            cm_string += str(grid[x])
        for x in range(i+102,i+148,9):
            cm_string += str(grid[x])
    
    theHash = hashlib.sha256()
    theHash.update(cm_string.encode())
    theHashDigest = theHash.hexdigest()
    return theHashDigest
    
    