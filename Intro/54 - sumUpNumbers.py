def solution(inputString):
    number_strings = re.findall(r'\d+', inputString)
    
    return sum(map(int, number_strings))