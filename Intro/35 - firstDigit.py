def solution(inputString):
    digit = re.match(r'^\D*(\d)', inputString)
    return digit.group(1)