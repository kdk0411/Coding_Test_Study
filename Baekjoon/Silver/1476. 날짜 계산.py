import sys
input = sys.stdin.readline
E, S, M = map(int, input().split())

pre_E, pre_S, pre_M = 1, 1, 1
ret_year = 1

while True:
    if pre_E > 15: pre_E = 1
    if pre_S > 28: pre_S = 1
    if pre_M > 19: pre_M = 1
    if pre_E == E and pre_S == S and pre_M == M:
        sys.stdout.write(str(ret_year))
        break
    ret_year += 1
    pre_E, pre_S, pre_M = pre_E+1, pre_S+1, pre_M+1


import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())
E, S, M = E - 1, S - 1, M - 1

ret_year = 0

while True:
    if ret_year % 15 == E and ret_year % 28 == S and ret_year % 19 == M:
        sys.stdout.write(str(ret_year + 1))
        break
    ret_year += 1
