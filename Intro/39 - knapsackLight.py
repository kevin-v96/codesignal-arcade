
#generic 1/0 knapsack solution with space optimization
def solution(value1, weight1, value2, weight2, maxW):
    #need weights and values arrays for the generic algorithm
    wts = [weight1, weight2]
    vals = [value1, value2]
    
    #how many items to take
    n = 2
    
    dp = [0 for i in range(maxW + 1)]
    
    #starting from 1 because first row/column has to be 0
    for i in range(1, n + 1):
        #iterate through weights backwards
        for w in range(maxW, 0, -1):
            if wts[i-1] <= w:
                dp[w] = max(dp[w], dp[w-wts[i-1]] + vals[i-1])
                
    return dp[maxW]
                