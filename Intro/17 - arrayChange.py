def solution(inputArray):
    start = inputArray[0]
    count = 0
    for i in inputArray[1:]:
        if i <= start:
            count += start - i + 1
            start += 1
        else:
            start = i
    return count