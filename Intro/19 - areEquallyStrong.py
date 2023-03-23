from collections import Counter

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    yourStrength = Counter([yourLeft, yourRight])
    friendStrength = Counter([friendsLeft, friendsRight])
    
    return yourStrength == friendStrength