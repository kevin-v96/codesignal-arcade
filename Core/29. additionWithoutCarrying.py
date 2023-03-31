def solution(param1, param2):
    str1 = str(param1)
    str2 = str(param2)
    
    if len(str1) > len(str2):
        str2 = str2.zfill(len(str1))
    else:
        str1 = str1.zfill(len(str2))
    
    res = ''
    for i in range(len(str1)):
        res += str((int(str1[i]) + int(str2[i])) % 10)
        
    return int(res)