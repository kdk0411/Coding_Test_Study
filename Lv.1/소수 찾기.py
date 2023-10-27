import math
def solution(n):
    cnt = 0
    for i in range(1, n+1):
        bl = True
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j == 0:
                bl = False
                break
        if bl is True:
            cnt += 1
    return cnt-1