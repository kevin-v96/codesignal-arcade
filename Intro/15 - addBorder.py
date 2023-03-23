def solution(picture):
    rows, cols = len(picture), len(picture[0])
    top = '*' * (cols + 2)
    
    for i in range(rows):
        picture[i] = '*' + picture[i] + '*'
        
    return([top] + picture + [top])