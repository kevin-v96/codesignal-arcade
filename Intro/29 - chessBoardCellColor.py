def solution(cell1, cell2):
    cell1num = ord(cell1[0]) + int(cell1[1])
    cell2num = ord(cell2[0]) + int(cell2[1])
    
    return (cell1num + cell2num) % 2 == 0