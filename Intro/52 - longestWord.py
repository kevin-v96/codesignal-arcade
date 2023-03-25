def solution(text):
    matches = re.findall(r'[A-Za-z]+', text)
    
    return max(matches, key = len)