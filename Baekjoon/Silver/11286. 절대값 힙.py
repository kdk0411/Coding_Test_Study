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
import heapq
import sys

input = sys.stdin.readline
min_heap = [] # 양수
max_heap = [] # 음수

for _ in range(int(input())):
	x = int(input())
	if x:
		if x>0:
			heapq.heappush(min_heap, x)
		else:
			heapq.heappush(max_heap, -x)
	else:
		if min_heap:
			if max_heap:
				if min_heap[0] < abs(-max_heap[0]): # max_heap[0]과 같음
					print(heapq.heappop(min_heap))
				else:
					print(-heapq.heappop(max_heap))
			else:
				print(heapq.heappop(min_heap))
		else:
			if max_heap:
				print(-heapq.heappop(max_heap))
			else:
				print(0)