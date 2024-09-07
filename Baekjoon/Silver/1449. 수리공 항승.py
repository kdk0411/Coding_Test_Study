# Solve 1
N, K = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort()
start = ls[0]
cnt = 1

for location in ls[1:]:
	if location in range(start, start+K):
		continue
	else:
		start = location
		cnt += 1

print(cnt)

# Solve 2
N, K = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort()
end = ls[0] + K - 1
cnt = 1

for location in ls[1:]:
	if location > end + 0.5:
		end = location + K - 1
		cnt += 1

print(cnt)