# 1. 기본 노드 클래스 만들기
class Node:
  def __init__(self, value):
    self.value = value;
    self.left = None;
    self.right = None;

# 2. 트리 구조 만들기
class Tree:
  def __init__(self, head):
    self.head = head;

  # 값이 현재 노드보다 작으면 왼쪽, 크면 오른쪽으로 분류한다
  def insert(self, value):
    self.current_node = self.head;
    # 데이터를 저장할 때마다 순환이 발생해야 하므로 조건을 True로 설정
    while True:
      if value < self.current_node.value:
        if self.current_node.left != None:
          self.current_node = self.current_node.left;
        else:
          self.current_node.left = Node(value);
          break;
      else:
        if self.current_node.right != None:
          self.current_node = self.current_node.right;
        else:
          self.current_node.right = Node(value);
          break;
#3. 트리 탐색
  def search(self, value):
    self.current_node = self.head;
    while self.current_node:
      if value == self.current_node.value:
        return True;
      elif value < self.current_node.value:
        self.current_node = self.current_node.left;
      else:
          self.current_node = self.current_node.right;
    return False;
#4. 삭제
  def delete(self, value):
    searched = False;
    self.current_node = self.head;
    self.parent = self.head;
    while self.current_node:
      if self.current_node.value == value:
        searched = True;
        break;
      elif value < self.current_node.value:
        self.parent = self.current_node;
        self.current_node = self.current_node.left;
      else:
        self.parent = self.current_node;
        self.current_node = self.current_node.right;
    if searched == False:
      return False;

    # Case 1. 삭제할 노드가 Leaf Node
    if self.current_node.left == None and self.current_node.right == None:
      if value < self.parent.value:
        self.parent.left == None;
      else:
        self.parent.right == None;
      del self.current_node;
    # Case 2. 삭제할 노드의 브랜치가 1개
    # Case 2-1. 삭제할 노드의 브랜치가 왼쪽
    if self.current_node.left != None and self.current_node.right == None:
      if value < self.parent.value:
        self.parent.left = self.current_node.left;
      else:
        self.parent.right = self.current_node.left;
    # Case 2-2. 삭제할 노드의 브랜치가 오른쪽
    if self.current_node.left == None and self.current_node.right != None:
      if value < self.current_node.value:
        self.parent.left = self.current_node.right;
      else:
        self.parent.right = self.current_node.right;
    # Case 3. 삭제할 노드의 브랜치가 2개
    # Case 3-1. 삭제할 노드가 부모의 왼쪽에 존재
    if self.current_node.left != None and self.current_node.right != None:
      if value < self.parent.value:
        self.change_node = self.current_node.right;
        self.change_node_parent = self.current_node.right;
        while self.change_node.left != None:
          self.change_node_parent = self.change_node;
          self.change_node = self.change_node.left;
        if self.change_node.right != None:
          self.change_node_parent.left = self.change_node.right;
        else:
          self.change_node_parent.left = None;
        self.parent.left = self.change_node;
        self.change_node.right = self.current_node.right;
        self.change_node.left = self.current_node.left;
    # Case 3-2. 삭제할 노드가 부모의 오른쪽에 존재
      else:
        self.change_node = self.current_node.right;
        self.change_node_parent = self.current_node.right;
        while self.change_node.left != None:
          self.change_node_parent = self.change_node;
          self.change_node = self.change_node.left;
        if self.change_node.right != None:
          self.change_node_parent.left = self.change_node.right;
        else:
          self.change_node_parent.left = None;
        self.parent.right = self.change_node;
        self.change_node.left = self.current_node.left;
        self.change_node.right = self.current_node.right;