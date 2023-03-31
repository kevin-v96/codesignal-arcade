def solution(k):
    y = 0
    r = 0
    odd = True
    for m in range(1, k + 1):
        if odd:
            y += m * m
        else:
            r += m * m
        odd = not odd
    return r - y
            
