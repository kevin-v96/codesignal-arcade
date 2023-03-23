def solution(a):
    suma = 0
    sumb = 0
    for i in range(len(a)):
        if i % 2 == 0:
            suma += a[i]
        else:
            sumb += a[i]
        
    return [suma, sumb]