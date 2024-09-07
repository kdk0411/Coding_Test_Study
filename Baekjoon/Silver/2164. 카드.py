# Solve 1
num = int(input())
cards = [i+1 for i in range(num)]

for i in range(len(cards)):
	if len(cards) > 1:
		break
	if i%2==0:
		cards = cards[1:] + cards[0]
	else:
		cards = cards[1:]

print(cards[0])

# Solve 2
from collections import deque

num = int(input())
cards = deque(range(1, num+1))

while len(cards) > 1:
	cards.popleft()
	cards.append(cards.popleft())

print(cards[0])

# Solve 3
num = int(input())

arr = []
for i in range(1, num+1):
	arr.append(i)

while len(arr) > 1:
	arr.pop(0)
	arr.append(arr.pop(0))

print(arr.pop())