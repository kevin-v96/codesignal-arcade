def solution(n):
    return [2 ** match.start() for occurence, match in enumerate(re.finditer(r'0',format(n, '0b')[::-1])) if occurence == 1][0]


def solution(n):
    return ~(n | (n + 1)) & ((n | (n + 1)) + 1)