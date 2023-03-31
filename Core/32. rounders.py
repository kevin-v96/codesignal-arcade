def solution(n):
    strn = str(n)
    carry = 0
    string = ''
    for i in range(len(strn) - 1, 0, -1):
        curr = int(strn[i]) + carry
        string += '0'
        if curr >= 5:
            carry = 1
        else:
            carry = 0
    string = str(int(strn[0]) + carry) + string
    return int(string)
                