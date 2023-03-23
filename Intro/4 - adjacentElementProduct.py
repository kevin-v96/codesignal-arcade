def solution(inputArray):
    largestProduct = -1000000
    for i in range(len(inputArray) - 1):
        product = inputArray[i] * inputArray[i + 1]
        if product > largestProduct:
            largestProduct = product
            
    return largestProduct