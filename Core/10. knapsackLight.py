def solution(value1, weight1, value2, weight2, maxW):
    weights = [weight1, weight2]
    values = [value1, value2]
    n = len(weights)
    
    dp = [0 for x in range(maxW + 1)]
    
    for i in range(1, n + 1):
        for w in range(maxW, 0, -1):
            if weights[i-1] <= w:
                dp[w] = max(dp[w], dp[w - weights[i-1]] + values[i-1])
            
    return dp[maxW]