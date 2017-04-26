class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            root = self.head
            while root.next != None:
                root = root.next
            root.next = Node(data)

    def traverse(self):
        root = self.head
        while root != None:
            print(root.data)
            root = root.next
    
    def pair_wise_swap(self):
        root = self.head
        while root != None and root.next != None:
            temp = root.data
            root.data = root.next.data
            root.next.data = temp
            root = root.next.next

            
list = LList()
list.append(1)
list.append(11)
list.append(111)
list.append(1111)
list.append(11111)
list.append(111111)

list.traverse()
list.pair_wise_swap()
list.traverse()
