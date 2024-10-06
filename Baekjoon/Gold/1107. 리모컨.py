import sys

input = sys.stdin.readline
target_chanel = int(input())
# 단순 + or -
simple = abs(target_chanel - 100)

N = int(input())
if N > 0:
    target_num = set(input().split())
else:
    target_num = set()

click_cnt = float('inf')
for num in range(1000001):
    for digit in str(num):
        if digit in target_num:
            break
    else:
        click_cnt = min(click_cnt, len(str(num)) + abs(num - target_chanel))

sys.stdout.write(str(min(simple, click_cnt)))
