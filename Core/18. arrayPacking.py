def solution(a):
    string = ''
    #go through the array from the back and add a '08b' representation of the number to the 
    #string
    for i in range(len(a), 0, -1):
        string += format(a[i - 1], '08b')
    #at the end, return the decimal representation
    return int(string, 2)