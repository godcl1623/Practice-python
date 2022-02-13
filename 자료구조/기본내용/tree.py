'''
# 트리 구조
Node, Branch를 이용해 사이클을 이루지 않도록 구성한 데이터 구조
  - Root Node: 트리 맨 위의 노드
  - Level: 최상위 노드 기준 Level 0을 시작으로 하위 Branch로 연결된 노드의 깊이
  - Leaf Node: Child Node가 하나도 없는 노드
  - Depth: 트리에서 Node가 가질 수 있는 최대 Level
  - 이진 트리: 최대 Branch가 2인 트리
    - 가장 많이 쓰이는 유형
    - 탐색에서 많이 사용
  - 이진 탐색 트리: 이진 트리 + 추가 조건 필요
    - 왼쪽 노드: 기준 노드보다 작은 값 보유
    - 오른쪽 노드: 기준 노드보다 큰 값 보유
'''
'''
# 이진 탐색 트리 구성 방법
  트리의 기본 형태는 노드 양 옆으로 다른 노드와 연결된 브랜치 2개가 존재하는 형태
  -> 더블 링크드 리스트와 비슷한 원리 적용 가능
  ※ 주의사항
    - 루트 노드는 초기화 시점부터 브랜치를 갖는게 아니라, 데이터를 저장할 때마다 브랜치가 생기며 노드가 연결되는 방식임
      => 링크드 리스트와 달리 left, right을 파라미터로 전달할 필요도 없고, 기본값을 파라미터에 지정할 필요도 없음
'''
# 1. 기본 노드 클래스 만들기
class Node:
  def __init__(self, value):
    self.value = value;
    self.left = None;
    self.right = None;

# 2. 이진 탐색 트리 구조 만들기
# 이미 존재하는 루트 노드에서 어느 브랜치로 나뉠지 판단을 한 후 데이터를 저장하므로, self.head에 새 Node 인스턴스를 만들지 않음
class Tree:
  def __init__(self, head):
    self.head = head;

  # 값이 현재 노드보다 작으면 왼쪽, 크면 오른쪽으로 분류한다
  def insert(self, value):
    self.current_node = self.head;
    # 데이터를 저장할 때마다 순환이 발생해야 하므로 조건을 True로 설정
    while True:
      # 추가하려는 값이 현재 노드의 값보다 작은 경우 -> 왼쪽으로 분류함
      if value < self.current_node.value:
        # 현재 노드의 왼쪽에 이미 노드가 존재하는 경우 -> 현재 노드를 현재 노드의 왼쪽 노드로 바꿔 루프를 재개
        if self.current_node.left != None:
          self.current_node = self.current_node.left;
        # 현재 노드의 왼쪽에 별도 노드가 존재하지 않는 경우 -> 현재 노드의 왼쪽 브랜치에 새 노드 인스턴스를 생성하고 루프 종료
        else:
          self.current_node.left = Node(value);
          break;
      # 추가하려는 값이 현재 노드의 값보다 큰 경우 -> 오른족으로 분류함(이하 작은 경우 참조)
      else:
        if self.current_node.right != None:
          self.current_node = self.current_node.right;
        else:
          self.current_node.right = Node(value);
          break;
#3. 트리 탐색
  def search(self, value):
    # 순회 시작점 설정
    self.current_node = self.head;
    # 노드가 존재하는 동안 반복문 실행
    while self.current_node:
      # 현재 노드의 값이 검색하려는 값과 일치하는 경우, True를 반환하며 루프 종료
      if value == self.current_node.value:
        return True;
      # 현재 노드 값이 검색값보다 큰 경우, 현재 노드를 현재 노드의 왼쪽 노드로 바꾼 후 루프 재개
      elif value < self.current_node.value:
        self.current_node = self.current_node.left;
      # 현재 노드 값이 검색값보다 작은 경우, 현재 노드를 현재 노드의 오른쪽 노드로 바꾼 후 루프 재개
      else:
          self.current_node = self.current_node.right;
    # 검색하려는 값이 트리에 저장되지 않은 경우 False 반환
    return False;
#4. 삭제
  def delete(self, value):
    # 트리를 순회하며 삭제하려는 값을 찾았는지 여부 기록
    searched = False;
    # 루프 시작점 설정
    self.current_node = self.head;
    # 노드를 삭제할 때 해당 노드의 부모 노드에서 삭제하는 방식을 사용하므로, 부모 노드 미리 설정. 단, 루트 노드는 부모 노드가 없으므로, 일단 부모 노드를 루트 노드로 설정.
    self.parent = self.head;
    # Case 0. 삭제하려는 값이 트리에 존재하는지 먼저 확인
    # 노드가 존재하는 동안 반복문 실행
    while self.current_node:
      # 삭제하려는 값이 현재 노드의 값과 일치 -> 검색 여부 플래그의 값을 True로 바꾼 후 루프 종료
      if self.current_node.value == value:
        searched = True;
        break;
      # 이하, 검색하려는 값이 현재 노드 값보다 작거나 큰 경우, 부모 노드를 현재 노드로, 현재 노드는 현재 노드의 왼쪽 혹은 오른쪽 노드로 갱신하며 루프를 이어나간다.
      elif value < self.current_node.value:
        self.parent = self.current_node;
        self.current_node = self.current_node.left;
      else:
        self.parent = self.current_node;
        self.current_node = self.current_node.right;
    # 검색하려는 값이 트리에 존재하지 않을 경우(= 여전히 검색 플래그가 False인 경우), False를 반환하고 루프 종료
    if searched == False:
      return False;
    ### 검색 이후 삭제 기능
    # Case 1. 삭제할 노드가 Leaf Node
    if self.current_node.left == None and self.current_node.right == None:
      # 검색 값이 부모 노드의 값보다 작은 경우, 부모 노드의 왼쪽 브랜치를 삭제
      if value < self.parent.value:
        self.parent.left == None;
      # 검색 값이 부모 노드 값보다 큰 경우, 부모 노드의 오른쪽 브랜치 삭제
      else:
        self.parent.right == None;
      # 현재 노드 삭제
      del self.current_node;
    # Case 2. 삭제할 노드의 브랜치가 1개
    # Case 2-1. 삭제할 노드의 브랜치가 왼쪽
    if self.current_node.left != None and self.current_node.right == None:
      # 삭제하려는 값이 부모 노드 값보다 작으면 '현재 노드를 삭제한 후' 부모의 왼쪽 노드를 현재 노드의 왼쪽으로, 클 경우 부모 오른쪽 - 현재 오른쪽 노드를 연결한다.
      if value < self.parent.value:
        self.parent.left = self.current_node.left;
      else:
        self.parent.right = self.current_node.left;
    # Case 2-2. 삭제할 노드의 브랜치가 오른쪽 - 2-1 참조
    if self.current_node.left == None and self.current_node.right != None:
      if value < self.current_node.value:
        self.parent.left = self.current_node.right;
      else:
        self.parent.right = self.current_node.right;
    # Case 3. 삭제할 노드의 브랜치가 2개
    '''
    # 삭제할 노드의 브랜치가 2개인 경우, 다음 2가지 전략을 사용 가능
      1. 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 삭제할 노드의 Parent Node가 가리키도록 설정 -> 채택
        (1) 삭제할 노드가 부모 노드의 왼쪽 + 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 자식 노드가 없음
        (2) 삭제할 노드가 부모 노드의 왼쪽 + 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 가진 노드의 오른쪽에 자식 노드가 있음
      2. 삭제할 노드의 왼쪽 자식 중 가장 큰 값을 삭제할 노드의 Parent Node가 가리키도록 설정
    '''
    # Case 3-1. 삭제할 노드가 부모의 왼쪽에 존재
    if self.current_node.left != None and self.current_node.right != None:
      if value < self.parent.value:
        # 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 찾기 위해 순회 지점 설정 - 변경할 노드 = 삭제할 노드의 오른쪽 노드, 변경할 노드의 부모 = 일단 변경할 노드와 같게 처리
        self.change_node = self.current_node.right;
        self.change_node_parent = self.current_node.right;
        # 변경할 노드의 왼쪽 노드가 존재하지 않을 때까지 루프 = 오른쪽 노드 중 가장 작은 값 찾기
        while self.change_node.left != None:
          # 현재 change_node를 change_node_parent로, 현재 change_node의 왼쪽 노드(= 값이 작은 자식 노드)를 현재 change_node로 설정
          self.change_node_parent = self.change_node;
          self.change_node = self.change_node.left;
        # 가장 값이 작은 노드의 오른쪽에 노드가 존재할 경우
        if self.change_node.right != None:
          # change_node_parent의 왼쪽 브랜치에 change_node의 오른쪽 노드를 연결함
          self.change_node_parent.left = self.change_node.right;
        # 가장 값이 작은 노드의 오른쪽에 노드가 없을 경우
        else:
          # change_node_parent의 왼쪽 브랜치에 연결될 노드가 없으므로 None으로 설정
          self.change_node_parent.left = None;
        ### 찾은 노드(= change_node)를 삭제하려는 노드 자리로 변경하는 코드
        # 삭제 노드의 부모 노드의 왼쪽 브랜치에 찾은 노드 연결
        self.parent.left = self.change_node;
        # change_node의 오른쪽, 왼쪽 각각 업데이트
        self.change_node.right = self.current_node.right;
        self.change_node.left = self.current_node.left;
    # Case 3-2. 삭제할 노드가 부모의 오른쪽에 존재
      else:
        # 삭제할 노드의 오른쪽 노드 중 가장 작은 값을 찾기 위한 루프 시작점 설정
        self.change_node = self.current_node.right;
        self.change_node_parent = self.current_node.right;
        # 변경할 노드의 왼쪽 노드가 존재하지 않을 때까지 루프 반복(= 오른쪽 노드 중 최솟값 찾을 때까지 반복)
        while self.change_node.left != None:
          # 현재 change_node를 change_node_parent로 업데이트
          self.change_node_parent = self.change_node;
          # 현재 change_node의 왼쪽 노드를 change_node로 업데이트
          self.change_node = self.change_node.left;
        # 반복문 끝 = 가장 값이 작은 노드 발견
        # change_node의 오른쪽 노드가 비어있지 않은 경우
        if self.change_node.right != None:
          # change_node_parent의 왼쪽 노드를 change_node의 오른쪽 노드로 변경
          self.change_node_parent.left = self.change_node.right;
        # change_node의 오른쪽 노드가 비어있는 경우 change_node_parent의 왼쪽 노드를 비워둠
        else:
          self.change_node_parent.left = None;
        ### 찾은 노드(= change_node)를 삭제하려는 노드 자리로 올림
        # 삭제 노드의 부모 노드의 오른쪽 브랜치에 change_node 위치
        self.parent.right = self.change_node;
        # change_node의 왼쪽, 오른쪽을 삭제하려는 노드(= current_node)의 왼쪽, 오른쪽으로 각각 연결
        self.change_node.left = self.current_node.left;
        self.change_node.right = self.current_node.right;

'''
# 루트 노드는 Node 클래스를 이용해 따로 생성한 후
tree_head = Node(1)
# (이진 탐색) 트리의 새 인스턴스로 위 루트 노드를 추가함
BST = Tree(tree_head)
'''