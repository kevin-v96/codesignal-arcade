def solution(commands):
    count = 0
    smartStudent = 0
    dumbStudent = 0
    
    for c in commands:
        if c == 'L' or c == 'R':
            smartStudent -= 1
            dumbStudent += 1
        elif c == 'A':
            smartStudent += 2
            dumbStudent += 2
    
        #modulo them to keep them in check
        if smartStudent < 0:
            smartStudent += 4
        else:
            smartStudent %= 4
            
        if dumbStudent < 0:
            dumbStudent += 4
        else:
            dumbStudent %= 4
            
        if smartStudent == dumbStudent:
            count += 1
        
    return count