from collections import Counter  

def solution(inputString):
    counts = Counter(inputString)
    for char in counts.keys():
        if char == 'a':
            continue
        
        currCount = counts[char]
        prevCount = counts[chr(ord(char) - 1)]
        
        if currCount > prevCount:
            return False
            
    return True
        