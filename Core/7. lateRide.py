def solution(n):
    hours = n // 60 
    minutes = n % 60
    return sum(map(int, list(str(hours) + str(minutes))))