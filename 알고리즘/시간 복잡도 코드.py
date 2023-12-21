import random

findNumber = random.randrange(1, 101)

for i in range(1, 101):
  if i == findNumber:
    print(i)
    break


# ex 1 연산 횟수 = N
N = 100000
cnt = 1
for i in range(N):
  print("연산 횟수" + str(cnt))
  cnt += 1


# ex 2 연산 횟수 = 3N
N = 100000
cnt = 1
for i in range(N):
  print("연산 횟수" + str(cnt))
  cnt += 1
for i in range(N):
  print("연산 횟수" + str(cnt))
  cnt += 1
for i in range(N):
  print("연산 횟수" + str(cnt))
  cnt += 1

# ex 3 연산 횟수 = N^2
N = 100000
cnt = 1
for i in range(N):
  for j in range(N):
    print("연산 횟수" + str(cnt))
    cnt += 1