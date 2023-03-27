def solution(divisor, bound):
    N = bound
    while N > 0:
        if N % divisor == 0:
            return N
        N -= 1