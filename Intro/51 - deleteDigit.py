def solution(n):
    max_number = 1e-8
    number_list = list(str(n))
    for i in range(len(number_list)):
        new_number = int(''.join(number_list[:i] + number_list[i+1:]))
        if new_number > max_number:
            max_number = new_number
    
    return max_number