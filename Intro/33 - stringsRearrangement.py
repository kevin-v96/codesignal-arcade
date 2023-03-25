from itertools import permutations as p

def solution(inputArray):
    #get all the permutations of the input array
    permutation_list = list(p(inputArray))
    for permutation in range(len(permutation_list)):
        #number of strings with single differences between them
        count_single_diffs = 0
        for word in range(len(permutation_list[0]) - 1):
            #number of differences between two strings
            count_diffs = 0
            for letter in range(len(permutation_list[0][0])):
                #are this string and the next only different by one letter?
                if permutation_list[permutation][word][letter] != permutation_list[permutation][word + 1][letter]:
                    count_diffs += 1
            if count_diffs == 1:
                count_single_diffs += 1
        #if the number of strings in this permutation that only differ by one letter with the consecutive string is the same as the number of all strings, return True
        if count_single_diffs >= len(permutation_list[0]) - 1:
            return True
    return False