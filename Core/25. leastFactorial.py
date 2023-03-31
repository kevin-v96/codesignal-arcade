def solution(n):
    factorial = 1
    i = 1
    while factorial < n:
        factorial *= i
        i += 1
    return factorial