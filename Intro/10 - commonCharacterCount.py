from collections import Counter

def solution(s1, s2):
    s1count = Counter(s1)
    s2count = Counter(s2)
    
    return sum((s1count & s2count).values())