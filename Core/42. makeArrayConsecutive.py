def solution(statues):
    sortedStatues = sorted(statues)
    count = 0
    for i in range(1, len(statues)):
        count += sortedStatues[i] - sortedStatues[i-1] - 1
    return count