class Node:
  def __init__(self,item):
    self.item = item
    self.left = None
    self.right = None

class BinaryTree():
  def __init__(self):
    self.root = None

# 각 노드 생성
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

# 각 노드를 엮기 위해 BinaryTree 생성
tree = BinaryTree()
tree.root = n1
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8