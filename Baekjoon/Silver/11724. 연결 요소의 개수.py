import sys

sys.setrecursionlimit(10**6) # 재귀 횟수 증가
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[0] * N for _ in range(N)]

for _ in range(M):
	a, b = map(lambda x:x-1, map(int, input().split()))
	adj[a][b] = adj[b][a] = 1

ret = 0
check = [False] * N

def dfs(now):
	for nxt in range(N):
		# 현재 간선에서 다음으로 갈 수 있다면
		if adj[now][nxt] and not check[nxt]:
			check[nxt] = True
			dfs(nxt)


for i in range(N):
	if not check[i]:
		ret += 1
		check[i] = True
		dfs(i)

print(ret)