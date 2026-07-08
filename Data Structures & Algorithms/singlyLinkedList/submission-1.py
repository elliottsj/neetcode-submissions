class Node:
    def __init__(self, val: int, next: 'Node' | None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        node = self.head
        i = 0
        while node is not None and i < index:
            node = node.next
            i += 1
        return node.val if node is not None else -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val, None)
            return
        node = self.head
        while node is not None and node.next is not None:
            node = node.next
        node.next = Node(val, None)

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                return True
            return False
        pred = self.head
        i = 0
        while pred is not None and pred.next is not None and i < index - 1:
            pred = pred.next
            i += 1
        if pred is None or pred.next is None:
            return False
        pred.next = pred.next.next
        return True

    def getValues(self) -> List[int]:
        lst = []
        node = self.head
        while node is not None:
            lst.append(node.val)
            node = node.next
        return lst
