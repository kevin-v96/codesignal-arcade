def solution(a, b):
    string = ''
    for i in range(a, b + 1):
        string += format(i, '08b')
    return sum(list(map(int, string)))