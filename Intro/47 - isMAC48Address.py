def solution(inputString):
    mac = re.match(r'^([\dA-F]{2}-){5}[\dA-F]{2}$', inputString)
    
    return bool(mac)