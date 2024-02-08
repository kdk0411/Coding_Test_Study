from math import factorial
def solution(n):
    num = 10
    while n < factorial(num):
        num-=1
    return num