def solution(n):
    dimensions = n
    element = 1
    matrix = [[0] * n for x in range(n)]
    while 0 < dimensions:
        i = n - dimensions
        for j in range(n - dimensions, dimensions):
            matrix[i][j] = element
            element += 1
        for i in range(n - dimensions + 1, dimensions):
            matrix[i][j] = element
            element += 1
        for j in range(dimensions - 2, n - dimensions - 1, -1):
            matrix[i][j] = element
            element += 1
        for i in range(dimensions - 2, n - dimensions, -1):
            matrix[i][j] = element
            element += 1
        dimensions -= 1
        
    return matrix
