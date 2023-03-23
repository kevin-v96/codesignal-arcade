def getSum(n):
    
    list_of_number = list(map(int, n.strip()))
    return sum(list_of_number)

def solution(n):
    strn = str(n)
    halfLen = int(len(strn)/2)
    tick1 = strn[:halfLen]
    tick2 = strn[halfLen:]
    
    return getSum(tick1) == getSum(tick2)