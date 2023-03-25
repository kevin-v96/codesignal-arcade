def solution(code):
    string = ''
    for i in range(0, len(code), 8):
        curr = chr(int(code[i:i+8], 2))
        string += curr
        
    return string
        