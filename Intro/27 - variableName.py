def solution(name):
    if re.match(r"^[A-Za-z_]\w*$", name):
        return True
    else:
        return False