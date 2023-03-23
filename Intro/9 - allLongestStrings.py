def solution(inputArray):
    solns = []
    maxLen = 0
    for i in inputArray:
        if len(i) > maxLen:
            maxLen = len(i)
            solns = []
            solns.append(i)
        elif len(i) == maxLen:
            solns.append(i)
    return solns