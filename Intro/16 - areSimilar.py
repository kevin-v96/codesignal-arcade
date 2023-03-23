def solution(a, b):
    checkA = []
    checkB = []
    count = 0
    
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            checkA.append(a[i])
            checkB.append(b[i])
            
    if count == 0:
        return True
    elif count == 2:
        return set(checkA) == set(checkB)
    else:
        return False