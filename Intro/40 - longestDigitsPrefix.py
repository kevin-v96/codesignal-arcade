def solution(inputString):
    match = re.match(r'^(\d*)\w*', inputString)
    return match.group(1)