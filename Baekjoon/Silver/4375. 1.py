import sys

for line in sys.stdin:
	divisor = int(line.strip())
	cnt = 1
	current_number = 1

	while current_number % divisor != 0:
		current_number = current_number * 10 + 1
		cnt += 1

	print(cnt)