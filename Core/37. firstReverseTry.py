def solution(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    a, *b, c = arr
    return [c] + b + [a]