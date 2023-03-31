def solution(score1, score2):
    if score1 > score2:
        return (score1 == 7 and (4 < score2 < 7)) or (score1 == 6 and (0 <= score2 < 5))
    else:
        return (score2 == 7 and (4 < score1 < 7)) or (score2 == 6 and (0 <= score1 < 5))