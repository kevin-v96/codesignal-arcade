def solution(young, beautiful, loved):
    if young and beautiful:
        return not loved
    elif loved:
        return not(young and beautiful)
    else:
        return loved