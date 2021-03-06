import hashlib
import random
import dodoku.getHash as getHash

def _create(parms):
    result = {'grid':'', 'integrity':'', 'status':'ok'}
    
    if 'level' in parms.keys():
        if parms['level'] == '1' or parms['level'] == '':
            result['grid'] = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,
                              -1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,
                              -2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,
                              0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,
                              -6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,
                              -5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1] 
        elif parms['level'] == '2':
            result['grid'] = [0,-6,0,0,0,0,0,-5,-9,-9,-3,0,-4,-8,0,0,0,0,0,0,0,0,0,-7,-3,
                           0,0,0,-5,0,0,-1,0,0,-4,-6,0,0,0,0,0,-6,0,-9,0,0,-8,-1,-2,0,
                           0,0,0,0,0,0,0,0,-7,0,0,0,0,0,0,0,0,-5,0,-8,0,-4,0,0,-1,0,0,
                           0,-7,0,0,-6,0,-2,0,-9,0,0,0,0,0,0,0,0,-5,0,0,0,0,0,0,0,0,0,
                           -9,-5,-3,0,0,-7,0,-4,0,0,0,0,0,-5,-8,0,0,-1,0,0,-9,0,0,0
                           ,-2,-1,0,0,0,0,0,0,0,0,0,-9,-8,0,-6,-1,-6,-1,0,0,0,0,0,-7,0]
        elif parms['level'] == '3':
            result['grid'] = [0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,
                        -7,0,-8,-9,0,-9,0,0,-5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,
                        -3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,-7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,
                        -9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,-6,-5,0,0,0,-7,-3,0,-5,
                        -9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0]
        else:
            result = {'status':'error:Invalid level input'}
            return result
    else:
        result['grid'] = [0,-2,0,0,-1,0,0,-4,0,-8,0,-1,-9,0,0,0,0,-5,0,0,0,0,-3,0,0,
                              -1,0,0,-3,0,0,0,0,-4,0,-6,-5,0,-9,0,0,0,0,0,-7,0,0,0,0,0,0,
                              -2,-8,0,-2,0,0,-6,0,0,0,0,0,0,-1,-4,0,-6,0,0,0,-6,0,0,-3,0,
                              0,0,-2,0,0,-1,0,-9,0,-4,0,-5,-7,0,0,0,0,0,0,-7,0,0,-5,0,0,
                              -6,0,0,0,0,-9,0,-2,0,0,0,0,0,-4,0,-8,-7,0,-9,0,0,0,0,0,0,0,
                              -5,0,0,-9,0,0,0,0,-4,0,0,-6,0,-3,-9,0,0,0,-6,0,0,-5,0,0,-3,-1]
    r = random.randint(0,56)
    result['integrity'] = getHash(result['grid'])[r:r+8]
        
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
    
    