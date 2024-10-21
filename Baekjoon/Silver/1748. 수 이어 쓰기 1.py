import sys
input = sys.stdin.readline
N = int(input())

length = 0
digit = 1
current = 1

while current <= N:
	end = min(N, current * 10 - 1)  # i=1 일때 cur = 9 -> i=2 일때 cur = 99
	length += (end - current + 1) * digit  # 개수 * 자릿수
	current *= 10
	digit += 1

sys.stdout.write(str(length))
