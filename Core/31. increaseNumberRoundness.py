def solution(n):
    strn = str(n)
    rightmostEncountered = False
    for i in range(len(strn) - 1, -1, -1):
        if strn[i] != '0' and not rightmostEncountered:
            rightmostEncountered = True
        elif strn[i] == '0' and rightmostEncountered:
            return True
    return False