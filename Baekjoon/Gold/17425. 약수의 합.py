import sys
input = sys.stdin.readline
MAX = 1000000
# dp[i]는 i의 약수들의 합이다.
dp = [1] * (MAX + 1) # 1은 모든 수의 약수이기 때문에 cnt가 1인 상태로 시작
# s[i]는 1~i 까지의 약수들의 합의 누적값이다.
s = [0] * (MAX + 1)

# 약수의 합 구하기(DP)
for i in range(2, MAX + 1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i # i의 배수(i * j)에 대한 처리이다. 각 i*j의 수에 i값을 더해준다.
        j += 1 # 한칸씩 전진

# 누적합 구하기 (S)
for i in range(1, MAX + 1):
    s[i] = s[i - 1] + dp[i]

T = int(input())
ret = []
# 미리 구해놓은 누적합(S)를 사용해서 입력된 값 N에 적합한 누적합을 도출한다.
for _ in range(T):
    N = int(input())
    ret.append(s[N])

sys.stdout.write('\n'.join(map(str, ret)) + '\n')
