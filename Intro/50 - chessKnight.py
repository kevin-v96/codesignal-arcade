from itertools import permutations

def solution(cell):
    knight_possible_moves = list(permutations([1,2,-1,-2], 2))
    knight_moves = []
    valid_moves = 0
    
    #get all knight moves
    for permutation in range(len(knight_possible_moves)):
        if sum(knight_possible_moves[permutation]) != 0:
            knight_moves.append(knight_possible_moves[permutation])
            
    #now count the valid moves according to where the knight is
    for x, y in knight_moves:
        #if the knight stays on the board after the move
        if (97 <= ord(cell[0]) + x <= 104) and (1 <= int(cell[1]) + y <= 8):
            valid_moves += 1
            
    return valid_moves