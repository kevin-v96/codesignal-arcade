def solution(arr):
    length = len(arr)
    middle = arr[length // 2] if length % 2 != 0 else arr[length // 2] + arr[length // 2 - 1]
    
    if length % 2 == 0:
        return arr[:length // 2 - 1] + [middle] + arr[length // 2 + 1:]
    else:
        arr[length // 2] = middle
        return arr