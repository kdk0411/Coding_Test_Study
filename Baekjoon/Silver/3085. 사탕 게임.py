import sys

input = sys.stdin.readline

num = int(input())
game_map = [list(input()) for _ in range(num)]

def check():
	max_cnt = 1
	for i in range(num):
		cnt = 1
		for j in range(1, num):
			if game_map[i][j-1] == game_map[i][j]: # 현재와 가로 한칸 앞이 같은지
				cnt += 1
			else:
				cnt = 1
			max_cnt = max(cnt, max_cnt)
		cnt = 1
		for j in range(1, num):
			if game_map[j-1][i] == game_map[j][i]:
				cnt += 1
			else:
				cnt = 1
			max_cnt = max(cnt, max_cnt)
	return max_cnt

ret = 1
for i in range(num):
	for j in range(num-1):
		# 오른쪽 Swap
		if j+1 < num and game_map[i][j] != game_map[i][j+1]:
			game_map[i][j], game_map[i][j+1] = game_map[i][j+1], game_map[i][j]
			ret = max(ret, check())
			# 되돌리기
			game_map[i][j], game_map[i][j+1] = game_map[i][j+1], game_map[i][j]

		if i+1 < num and game_map[i][j] != game_map[i+1][j]:
			game_map[i][j], game_map[i+1][j] = game_map[i+1][j], game_map[i][j]
			ret = max(ret, check())
			# 되돌리기
			game_map[i][j], game_map[i+1][j] = game_map[i+1][j], game_map[i][j]
print(ret)