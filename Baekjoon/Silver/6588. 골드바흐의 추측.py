import math
import sys
input = sys.stdin.readline

max_num = 1000001
num_list = [1 for _ in range(max_num)]

for i in range(2, int(math.sqrt(max_num)) + 1):
	if num_list[i]:
		for j in range(2*i, max_num, i):
			num_list[j] = 0

while True:
	n = int(input())

	if n == 0:
		break

	for i in range(n-3, 2, -2):
		if num_list[i] == True and num_list[n-i] == True:
			print(f"{n} = {n-i} + {i}")
			break
	else:
		print('"Goldbach\'s conjecture is wrong."')
