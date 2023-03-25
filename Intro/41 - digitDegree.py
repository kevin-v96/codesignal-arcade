def isSingleDigit(n):
    return n // 10 == 0

def solution(n):
    degree = 0
    
    digits = n
    while not isSingleDigit(digits):
        degree += 1
        sumOfDigits = sum(map(lambda x: int(x), list(str(digits))))
        digits = sumOfDigits
        
    return degree