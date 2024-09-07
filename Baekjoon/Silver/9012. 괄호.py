num = int(input())
for _ in range(num):
	stack = []
	isVPS = True
	for i in input():
		if i == '(':
			stack.append(i)
		else:
			if stack:
				stack.pop()
			else:
				isVPS = False
				break
	if stack:
		isVPS = False

	print("YES" if isVPS else "NO")