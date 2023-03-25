def solution(names):
    dictionary = {}
    for i in range(len(names)):
        name = names[i]
        if name in dictionary:
            number = dictionary[name]
            new_name = name + '(' + str(number) + ')'
            while(new_name in dictionary):
                number += 1
                new_name = name + '(' + str(number) + ')'
            names[i] = new_name
            dictionary[name] += 1
            dictionary[new_name] = 1
        else:
            dictionary[name] = 1
            
    return names