import sys

INF = sys.maxsize()

V = 4
graph = [
  [0, 2, INF, 4],
  [2, 0, INF, 5],
  [3, INF, 0, INF],
  [INF, 2, 1, 0]
]
def Floyd_Warshall():
  dist = [[INF] * V for i in range(V)]

  for i in range(V):
    for j in range(V):
      dist[i][j] = graph[i][j]

  for i in range(V):
    for j in range(V):
      for k in range(V):
        if dist[j][k] > dist[i][j] + dist[j][i]:
          dist[j][k] = dist[i][j] + dist[j][i]

  return dist

dist = Floyd_Warshall()

for i in range(V):
  for j in range(V):
    print(dist[i][j], end='')
  print(s)