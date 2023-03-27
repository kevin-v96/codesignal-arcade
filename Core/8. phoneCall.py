def solution(min1, min2_10, min11, s):
    totalDuration = 0
    
    if s >= min1:
        s -= min1
        totalDuration +=1
    else:
        return totalDuration
        
    if s >= 9 * min2_10:
        s -= 9 * min2_10
        totalDuration += 9
    else:
        totalDuration += s // min2_10
        return totalDuration
        
    return totalDuration + s // min11
    