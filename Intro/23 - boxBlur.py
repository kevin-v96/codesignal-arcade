def blurredPixel(matrix, i, j):
    summ = 0
    for row in range(i - 1, i + 2):
        for col in range(j - 1, j + 2):
            summ += matrix[row][col]
    mean = summ // 9
    return mean

def solution(image):
    blurredImage = []
    rows, cols = len(image), len(image[0])
    
    for row in range(1, rows - 1):
        output = []
        for col in range(1, cols - 1):
            output.append(blurredPixel(image, row, col))
        blurredImage.append(output)
        
    return blurredImage