def evalExpression(sign, a, b, c):
    return eval(f'a{sign}b==c')

def solution(a, b, c):
    signs = ['+', '-', '*', '/']
    
    for sign in signs:
        if evalExpression(sign, a, b, c):
            return True
            
    return False