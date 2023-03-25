def solution(inputArray, k):
    #fixed-length sliding window starting from the next k elements
    start = 0
    end = start + k
    currSum = 0
    #calculate the initial sum
    for i in range(end):
        currSum += inputArray[i]
        
    maxSum = currSum
    
    #now iterate through the loop again but with DP, removing the last element and adding the first
    while end < len(inputArray):
        currSum = currSum - inputArray[start] + inputArray[end]
        if currSum > maxSum:
            maxSum = currSum
        start += 1
        end += 1
        
    return maxSum