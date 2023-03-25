def solution(st):
    for i in range(len(st)):
        substring = st[i:len(st)]
        if substring[::-1] == substring:
            missing = st[:i]
            return st + missing[::-1]
            
    return st