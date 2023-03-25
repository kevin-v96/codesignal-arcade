from collections import Counter

gridCounter = Counter([1,2,3,4,5,6,7,8,9])

def checkLocalGrid(grid, i, j):            
    localElems = []
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            localElems.append(grid[x][y])
    
    if Counter(localElems) != gridCounter:
        return False
        
    return True
    
def solution(grid):
    for x in range(9):
        rowElems = []
        for y in range(9):
            rowElems.append(grid[x][y])
            if x % 3 == 0 and y % 3 == 0 and not checkLocalGrid(grid, x, y):
                return False
        if Counter(rowElems) != gridCounter:
            return False
            
    for y in range(9):
        colElems = []
        for x in range(9):
            colElems.append(grid[x][y])
        if Counter(colElems) != gridCounter:
            return False
                
    return True