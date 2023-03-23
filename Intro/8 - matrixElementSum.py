def solution(matrix):
    r, c = len(matrix), len(matrix[0])

    totalSum = 0
    for col in range(c):
        for row in range(r):
            if matrix[row][col] == 0:
                break
            
            totalSum += matrix[row][col]
    
    return totalSum