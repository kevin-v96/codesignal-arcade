def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])
    squares = []
    square_count = 0
    
    for i in range(rows - 1):
        for j in range(cols - 1):
            square_2x2 = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
            if square_2x2 not in squares:
                squares.append(square_2x2)
                square_count += 1
                
    return square_count