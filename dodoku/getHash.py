import hashlib

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