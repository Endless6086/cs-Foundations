class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)        
        if self.head == None:
            self.head = new_node
            return

        current = self.head

        while current.next != None:
            current = current.next
        
        current.next = new_node

List = SinglyLinkedList()

for i in range(1,6):
    List.append(i)