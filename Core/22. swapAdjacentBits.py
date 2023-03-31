def solution(n):
    #first mask has all even bits set, second has all odd bits set.
    #we AND with them and then switch the places of the bits by right and left shifting
    return 0xAAAAAAAA & n << 1 | 0x55555555 & n >> 1;
