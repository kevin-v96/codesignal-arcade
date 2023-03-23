def solution(statues):
    result = list()
    sortedStats = sorted(statues)
    
    i = sortedStats[0]
    
    while i != sortedStats[-1]:
        i += 1
        
        if i not in sortedStats:
            result.append(i)
            
    return len(result)