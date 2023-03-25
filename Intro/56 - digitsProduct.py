def solution(product):
    if product == 1:
        return 1
    if product == 0:
        return 10
        
    for i in range(4000):
        p = 1
        for j in str(i):
            p *= int(j)
        if p == product:
            return i
    
    return -1