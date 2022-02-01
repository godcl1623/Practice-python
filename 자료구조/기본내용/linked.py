# 1. 링크드 리스트 - 데이터와 다음 노드의 주소를 담는 노드끼리 연결된 형태
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Lnk:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def search(self, item):
        if self.head == '':
            print('No data in the list')
            return False
        else:
            node = self.head
            while node:
                if node.data == item:
                    return node
                else:
                    node = node.next
            return False

    def remove(self, search):
        if self.head == '':
            print('No data to delete')
            return False
        elif self.head.data == search:
            temp = self.head
            self.head = self.head.next
            del temp
            return True
        else:
            node = self.head
            while node.next:
                if node.next.data == search:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return True
                else:
                    node = node.next
            return False

# 2. 더블 링크드 리스트 - 링크드 리스트와 달리 양방향으로 이동 가능
class DNode:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLnk:
    def __init__(self, data):
        self.head = DNode(data)
        self.tail = self.head

    def add(self, data):
        if self.head == '':
            self.head = DNode(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            newNode = DNode(data)
            node.next = newNode
            newNode.prev = node
            self.tail = newNode

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def htotSearch(self, search):
        if self.head == '':
            print('No data in the list')
            return False
        else:
            node = self.head
            while node:
                if node.data == search:
                    return node
                else:
                    node = node.next
            return False

    def ttohSearch(self, search):
        if self.head == '':
            print('No data in the list')
            return False
        else:
            node = self.tail
            while node:
                if node.data == search:
                    return node
                else:
                    node = node.prev
            return False

    def insert_after(self, search, data):
        if self.head == '':
            print('No data in the list')
            return False
        else:
            node = self.head
            while node:
                if node.data == search:
                    newNode = DNode(data)
                    oldNext = node.next
                    node.next = newNode
                    newNode.prev = node
                    newNode.next = oldNext
                    if oldNext != None:
                        oldNext.prev = newNode
                    else:
                        self.tail = newNode
                    return True
                else:
                    node = node.next
            return False

    def insert_before(self, search, data):
        if self.head == '':
            print('No data in the list')
            return False
        else:
            node = self.tail
            while node:
                if node.data == search:
                    newNode = DNode(data)
                    oldPrev = node.prev
                    node.prev = newNode
                    newNode.next = node
                    newNode.prev = oldPrev
                    if oldPrev != None:
                        oldPrev.next = newNode
                    else:
                        self.head = newNode
                    return True
                else:
                    node = node.prev
            return False
