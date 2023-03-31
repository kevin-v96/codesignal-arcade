def solution(n, l, r):
    ways = 0
    seen = set()
    for i in range(l, r + 1):
        rest = n - i
        if l <= rest <= r and (rest, i) not in seen:
            seen.add((i, rest))
            ways += 1
    return ways
