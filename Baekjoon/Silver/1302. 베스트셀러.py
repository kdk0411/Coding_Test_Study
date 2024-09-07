# Solve 1
import heapq
import sys

# num = int(input())
num = int(sys.stdin.readline())
pq = []

for _ in range(num):
	# x = int(input())
	x = int(sys.stdin.readline())
	if x:
		heapq.heappush(pq, (abs(x), x))
	else:
		print(heapq.heappop(pq)[1] if pq else 0)

# Solve 2
d = dict()

for _ in range(int(input())):
	book = input()
	if book in d:
		d[book] += 1
	else:
		d[book] = 1

m = max(d.values())
arr = []
for k, v in d.items():
	if v==m:
		arr.append(k)

print(sorted(arr)[0])