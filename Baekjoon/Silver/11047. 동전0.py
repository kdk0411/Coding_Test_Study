# Solve 1
import sys
n, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]
cnt = n-1

ret = 0

while k:
	if coins[cnt] <= k:
		ret += k // coins[cnt]
		k %= coins[cnt]
	cnt -= 1

print(ret)

# Solve 2s
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = n - 1
ret = 0
while k > 0 and cnt >= 0:
	if coins[cnt] <= k:
		ret += k // coins[cnt]
		k %= coins[cnt]
	cnt -= 1

print(ret)