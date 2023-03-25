def solution(address):
    email = re.search(r'[^@]+@([^@]+\.[^@]+)$', address)
    return email.group(1)