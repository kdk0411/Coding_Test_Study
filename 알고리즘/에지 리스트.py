V = 7
edge = [(1, 2), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 2), (3, 4), (3, 4), (4, 2), (4, 3), (4, 5), (4, 6), (5, 1), (5, 2), (5, 4), (6, 4)]

agj_list = [[] for _ in range(V)]

# 간선(에지)리스트 방향 그래프
for u, v in edge:
  agj_list[u].append(v)

# 간선(에지)리스트 무방향 그래프
for u, v in edge:
  agj_list[u].append(v)
  agj_list[v].append(u)