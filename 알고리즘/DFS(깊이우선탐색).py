graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# 1. 리스트
def DFS_List(graph, start_node):
  need_visited, visited = list(), list()
  need_visited.append(start_node)

  while need_visited:
    node = need_visited.pop()

    if node not in visited:
      visited.append(node)
      need_visited.extend(graph[node])

  return visited
DFS_List(graph, 'A')

# 2. deque
def DFS_deque(graph, start_node):
  from collections import deque

  visited = []
  need_visited = deque()

  need_visited.append(start_node)

  while need_visited:
    node = need_visited.pop()

    if node not in visited:
      visited.append(node)
      need_visited.extend(graph[node])

  return visited
DFS_deque(graph, 'A')

# 3. 재귀함수
def DFS_Re(graph, start, visited = []):
  visited.append(start)
  for node in graph[start]:
    if node not in visited:
      DFS_Re(graph, node, visited)
  return visited
DFS_Re(graph, 'A')