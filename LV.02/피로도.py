from itertools import permutations
def solution(k, dungeons):
    ret = 0
    for i in permutations(dungeons, len(dungeons)):
        cnt = 0
        tmp = k
        for need, con in i:
            if need <= tmp:
                tmp -= con
                cnt +=1
        ret = max(ret, cnt)
    return ret


# 다른방법
answer = 0
def dfs(k, cnt, dungeons, visited):
  global answer
  if cnt > answer:
    answer = cnt

  for i in range(len(dungeons)):
    if not visited[i] and k >= dungeons[i][0]:
      visited[i] = True
      dfs(k - dungeons[i][1], cnt + 1, dungeons, visited)
      visited[i] = False

def solution02(k, dungeons):
  global answer
  visited = [False] * len(dungeons)
  dfs(k, 0, dungeons, visited)
  return answer