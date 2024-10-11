from math import factorial as fc
def solution(balls, share):
    n, m = fc(balls), fc(share)
    return n/(fc(balls-share)*m)