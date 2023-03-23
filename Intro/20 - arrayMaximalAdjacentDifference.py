def solution(inputArray):
    max = -100
    for i in range(1, len(inputArray)):
        diff = abs(inputArray[i] - inputArray[i-1])
        if diff > max:
            max = diff
    
    return max