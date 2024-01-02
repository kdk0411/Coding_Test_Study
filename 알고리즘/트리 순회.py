# 전위 순회
def preorder(self, n):
  if n != None:
    print(n.item, '', end='') # 노드 방문
    if n.left:
      self.preodrer(n.left)
    if n.right:
      self.preodrer(n.right)

# 후위 순회
def postorder(self, n):
  if n != None:
    if n.left:
      self.postorder(n.left)
    if n.right:
      self.postorder(n.right)
    print(n.item, '', end='') # 노드 방문

# 중위 순회
def inorder(self, n):
  if n!= None:
    if n.left:
      self.inorder(n.left)
      print(n.item, '', end='') # 노드 방문
  if n.right:
    self.inorder(n.right)

# 레벨 순회
def levelorder(self, n):
  q = []
  q.append(n)
  while q:
    t = q.pop(0)
    print(t.item, '', end='')
    if t.left != None:
      q.append(t.left)
    if t.right != None:
      q.append(t.right)