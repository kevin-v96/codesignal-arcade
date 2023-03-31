def solution(a, b, n):
    money = 0
    while n:
        money += a * b
        a += 1
        b += 1
        n -= 1
    return money

