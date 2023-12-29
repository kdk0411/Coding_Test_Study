V, E = 6, 8
edge = [0, 1, 0, 2, 0, 5, 0, 6, 4, 3, 5, 3, 5, 4, 6, 4]

adj_list = [[] for _ in range(V+1)]

# 방향 그래프
for i in range(E):
  num1, num2 = edge[2*i], edge[2*i+1]
  adj_list[num1].append(num2)

# 무방향 그래프
for i in range(E):
  num1, num2 = edge[2*i], edge[2*i+1]
  adj_list[num1].append(num2)
  adj_list[num2].append(num1)