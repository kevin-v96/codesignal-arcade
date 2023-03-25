def solution(upSpeed, downSpeed, desiredHeight):
    height = 0
    day = 1
    while height + upSpeed < desiredHeight:
        day += 1
        height = height + upSpeed - downSpeed
    
    return day