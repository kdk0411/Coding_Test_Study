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

# 특정 숫자 n의 제곱근 즉 루트(n)의 값으로 n을 나누면 해당 숫자가 소수인지 아닌지 알 수 있다.
# ex1) 루트 15는 약 3.xx이다. 이것을 3으로 Int화 시켜 3으로 15를 나누면 나누어 지기 때문에 15는 소수가 아니게 되는것이다.
# ex2) 루트 17은 약 4.xx이다. 이것을 4로 Int화 시켜 4로 17을 나누면 나누어 지지 않기 떄문에 17은 소수가 아니라는것을 알 수 있다.