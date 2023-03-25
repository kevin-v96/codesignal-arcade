def solution(n):
    digits = [int(x) for x in str(n)]
    
    return all(map(lambda x: x % 2 == 0, digits))