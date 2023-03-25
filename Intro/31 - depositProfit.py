def solution(deposit, rate, threshold):
    year = 0
    money = deposit
    while money < threshold:
        money = money * ((100 + rate) / 100)
        year += 1
        
    return year