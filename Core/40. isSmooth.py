def solution(arr):
    length = len(arr)
    middle = arr[length // 2] if length % 2 != 0 else arr[length // 2] + arr[length // 2 - 1]
    return arr[0] == middle == arr[-1]