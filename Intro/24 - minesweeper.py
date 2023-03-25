def neighbour_squares(matrix, i, j, rows, cols):
    return sum(matrix[x][y] for x in range(i - 1, i + 2) if 0 <= x < rows
                            for y in range(j - 1, j + 2) if 0 <= y < cols
                            if x != i or y != j)

def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    return [[neighbour_squares(matrix, i, j, rows, cols) for j in range(cols)] for i in range(rows)]
