# 1. 크루스칼
# 과정
# 1) 가중치를 기준으로 그래프 간선을 오름차순으로 정렬한다.
# 2) 가장 큰 가중치가 나올때까지 작은 가중치 간선부터 MST 간선을 더해간다.
# 3) 사이클이 발생하지 않게 간선을 더한다.

# 특정 원소가 속한 집합 찾기
def find(parent, x):
  if parent[x] == x:
    return x
  parent[x] = find(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합 찾기
def union(parent, a, b):
  rootA = find(parent, a)
  rootB = find(parent, b)

  if rootA < rootB:
    parent[rootB] = rootA
  else:
    parent[rootA] = rootB

# 노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

edge = []
result = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i
  
# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
  a, b, cost = map(int, input().split())
  # 가중치를 오름차순으로 정렬하기 위해 튜플의 첫 번째 원소를 cost로 설정
  edge.append((cost, a, b))

edge.sort()

for e in edge:
  cost, a, b = e
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find(parent, a) != find(parent, b):
    union(parent, a, b)
    result += cost

print(result)

# 2. 프림
# 과정
# 1) 시작 단계에서는 시작 정점만 MST 집합에 포함된다.
# 2) 앞에서 만들어진 MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리를 확장한다.
# -> 가장 낮은 가중치를 먼저 선택한다.
# 3) 트리가 N-1개의 간선을 가질 때 까지 반복한다.

# 1) Collections 라이브러리 defaultdict 사용
from collections import defaultdict
# key에 대한 값을 지정하지 않았을 때 빈리스트로 초기화함
list_dict = defaultdict(list)
print(list_dict['key1'])
list_dict2 = defaultdict(list)
print(list_dict2['key1'])

edges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (15, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]
from heapq import *
def prim(first_node, edges):
  mst = []
  # 해당 노드에 해당 간선을 추가
  adjacent_edges = defaultdict(list)
  for weight, node1, node2 in edges:
    adjacent_edges[node1].append((weight, node1, node2))
    adjacent_edges[node2].append((weight, node2, node1))

  # 처음 선택한 노드를 연결된 노드 집합에 삽입
  connected = set(first_node)
  # 선택된 노드에 연결된 간선을 간선 리스트에 삽입
  candidated_edge = adjacent_edges[first_node]
  # 오름 차순으로 정렬
  heapify(candidated_edge)

  while candidated_edge:
    weight, node1, node2 = heappop(candidated_edge)
    # 사이클 있는지 확인 후 연결
    if node2 not in connected:
      connected.add(node2)
    mst.append((weight, node1, node2))

    for edge in adjacent_edges[node2]:
      if edge[2] not in connected:
        heappush(candidated_edge, edge)

  return mst


from heapdict import heapdict

def prim(graph, first):
  mst = []
  keys = heapdict()
  previous = dict()
  total_weight = 0

  # 초기화
  for node in graph.keys():
    keys[node] = float('inf')
    previous[node] = None

  keys[first], previous[first] = 0, first

  while keys:
    current_node, current_key = keys.popitem()
    mst.append([previous[current_node], current_node, current_key])
    total_weight += current_key
    for adjacent, weight in graph[current_node].items():
      if adjacent in keys and weight < keys[adjacent]:
        keys[adjacent] = weight
        previous[adjacent] = current_node
    return mst, total_weight

graph = {
  'A': {'B': 7, 'D': 5},
  'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
  'C': {'B': 8, 'E': 5},
  'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
  'E': {'B': 7, 'C': 5, 'F': 8, 'G': 9},
  'F': {'D': 6, 'E': 8, 'G': 11},
  'G': {'E': 9, 'F': 11}
}

mst, total_weight = prim(graph, 'A')
print(mst)
print(total_weight)