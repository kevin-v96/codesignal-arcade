def solution(bishop, pawn):
    if ord(bishop[0]) == ord(pawn[0]):
        return False
        
    bishopElem = ord(bishop[0]) + int(bishop[1])
    pawnElem = ord(pawn[0]) + int(pawn[1])
    
    return (bishopElem + pawnElem) % 2 == 0