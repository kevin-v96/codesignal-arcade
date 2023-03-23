def solution(year):
    century = int(year / 100)
    if year % 100 != 0:
        century = century + 1
    return century