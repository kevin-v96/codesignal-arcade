def solution(a):
    a_sorted = sorted([i for i in a if i != -1])
    
    j = 0 
    
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = a_sorted[j]
            j += 1
            
    return a