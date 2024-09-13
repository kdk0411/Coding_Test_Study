import sys
num = int(sys.stdin.readline())
ls = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in ls:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                cnt += 1
            break
print(cnt)