from collections import Counter

def solution(inputString):
    count = Counter(inputString)
    singletons = 0
    for key in count:
        if count[key] % 2 != 0:
            singletons += 1
    
    if singletons <= 1:
        return True
    else:
        return False