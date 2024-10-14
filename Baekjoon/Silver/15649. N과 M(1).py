import sys


def dfs():
	if len(array) == M:
		print(' '.join(map(str, array)))
		return
	for i in range(1, N + 1):
		if visited[i]:
			continue
		visited[i] = True
		array.append(i)
		dfs()
		array.pop()
		visited[i] = False


input = sys.stdin.readline
N, M = map(int, input().split())
array = []
visited = [False] * (N + 1)

dfs()
