import sys

input = sys.stdin.readline
L, C = map(int, input().split())
diction = list(map(str, input().split()))
diction.sort()
vowel = ['a', 'e', 'i', 'o', 'u']


def check_ward(list):
	v_cnt, c_cnt = 0, 0
	for i in list:
		if i in vowel:
			v_cnt += 1
		else:
			c_cnt += 1
	if v_cnt >= 1 and c_cnt >= 2:
		return True
	return False


def backtracking(list):
	if len(list) == L:
		if check_ward(list):
			print("".join(list))
			return

	for i in range(len(list), C):
		if list[-1] < diction[i]:
			list.append(diction[i])
			backtracking(list)
			list.pop()


for i in range(C - L + 1):
	ls = [diction[i]]
	backtracking(ls)
