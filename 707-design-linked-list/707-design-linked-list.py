class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

class MyLinkedList:

    def __init__(self):
        self.head = None
        
        
        print("Initialized", self)
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size():
            return -1

        if self.head is None:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        current = self.head
        if current is None:
            self.head = Node(val)
            return
        while current.next is not None:
            current = current.next
        current.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size():
            return

        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        node = Node(val)
        node.next = current.next
        current.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size():
            return

        current = self.head
        if index == 0:
            self.head = current.next
            return
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next
        
    
    def isValid(self, index):
        return 0 <= index <= self.size()
    
    def size(self):
        i = 0
        current = self.head
        while current:
            i += 1
            current = current.next
        return i
    
    def __str__(self):
        an = ""
        current = self.head
        while current:
            an += str(current.val) + " "
            current = current.next
        return an
    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)