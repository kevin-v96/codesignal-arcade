def solution(candlesNumber, makeNew):
    total = 0
    leftovers = 0
    
    while candlesNumber:
        total += candlesNumber
        leftovers += candlesNumber
        candlesNumber = leftovers // makeNew
        leftovers %= makeNew
        
    return total