from itertools import groupby

def solution(s):
    encoding = ''
    for key, group in groupby(s):
        l = len(list(group))
        if l == 1:
            encoding += key
        else:
            encoding += str(l) + key
            
    return encoding