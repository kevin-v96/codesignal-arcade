def solution(inputString):
    parts = inputString.split('.')
    
    if len(parts) != 4:
        return False 
        
    for i in parts:
        #if there's no number
        if not i:
            return False
            
        #if there's an alphabet
        if not i.isnumeric():
            return False
            
        #if there are leading 0s
        if len(i) - len(i.lstrip('0')) != 0 and len(i) > 1:
            return False
    
    return all(map(lambda x: True if int(x) >= 0 and int(x) <= 255 else False, parts))