class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def desc(self):
        if self.head == None:
            print('현재 저장된 자료가 없습니다')
            return
        else:
            node = self.head
            while node.next:
                print(node.data)
                node = node.next
            print(node.data)
            return

    def headSearch(self, find):
        if self.head == None:
            print('현재 저장된 자료가 없습니다')
            return
        else:
            node = self.head
            while node.next:
                if node.data == find:
                    print(node)
                    return
                    # return node
                else:
                    node = node.next
            if node.data == find:
                print(node)
                return
                # return node
            else:
                print('찾는 자료가 없습니다')
                return

    def tailSearch(self, find):
        if self.head == None:
            print('현재 저장된 자료가 없습니다')
        else:
            node = self.tail
            while node.prev:
                if node.data == find:
                    print(node)
                    return
                else:
                    node = node.prev
            if node.data == find:
                print(node)
                return
            else:
                print('찾는 자료가 없습니다')
                return

    def remove(self, find):
        if self.head == None:
            print('현재 저장된 자료가 없습니다')
            return
        if self.head.data == find:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            del temp
            return
        elif self.tail.data == find:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            del temp
            return
        else:
            node = self.head
            while node.next:
                if node.next.data == find:
                    temp = node.next
                    node.next = temp.next
                    node.next.prev = node
                    del temp
                    return
                else:
                    node = node.next

dlink = NodeMgmt(0)
for index in range(1, 10):
    dlink.add(index)
dlink.remove(9)
dlink.desc()
print(dlink.tail.next)