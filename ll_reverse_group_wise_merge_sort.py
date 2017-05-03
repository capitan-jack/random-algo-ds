class Node:
    def __init__(self, data, doubly=False):
        self.next = None
        self.data = data
        if doubly:
            self.prev = None


class LL:
    def __init__(self, doubly=False):
        self.root = None
        self.doubly = doubly

    def append(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            root = self.root
            while root.next != None:
                root = root.next
            root.next = Node(data)
    
    def merge_alternating(self, other):
        to_insert = other.root
        insert_after = self.root
        while to_insert != None and insert_after.next != None:
            next_to_insert = to_insert.next
            to_insert.next = insert_after.next
            insert_after.next = to_insert
            insert_after = insert_after.next.next
            to_insert = next_to_insert
        if insert_after.next == None:
            insert_after.next = to_insert
    
    def traverse(self, root=None):
        if root==None:
            root = self.root
        if root.next == None:
            print(root.data)
        else:
            print(root.data)
            self.traverse(root.next)
    
    def reverse_in_groups(self, root=None, k=2):
        if root == None:
            root = self.root
        aux = []
        iterator = root
        for i in range(1,k):
            if iterator == None:
                return
            aux.append(iterator.data)
            iterator = iterator.next
        aux.append(iterator.data)
        iterator = root
        for i in range(len(aux)-1, -1,-1):
            iterator.data = aux[i]
            iterator = iterator.next
        if iterator != None:
            self.reverse_in_groups(iterator, k)
    
    def left_right_merge(self, left, right):
        add_to = left
        add_from = right
        if add_to.data > add_from.data:
            add_to = right
            add_from = left
        root = add_to
        while add_from != None:
            if add_to.next != None and add_to.next.data < add_from.data:
                add_to = add_to.next
            else:
                temp = add_from.next
                add_from.next = add_to.next
                add_to.next = add_from
                add_from = temp
                add_to = add_to.next 
        return root
    
    def _merge_sort(self, root):
        if root.next == None:
            return root
        slow = root
        fast = root
        prev = None
        while fast.next != None and fast.next.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        second_half = slow
        if prev != None:
            prev.next = None
        else:
            second_half = slow.next
            slow.next = None
        left = self._merge_sort(root)
        right = self._merge_sort(second_half)
        merged = self.left_right_merge(left, right)
        return merged
        
    def merge_sort(self):
        r = self._merge_sort(self.root)
        self.root = r
        
ll_1 = LL()
ll_1.append(1)
ll_1.append(3)
ll_1.append(5)
ll_1.append(7)
ll_1.append(9)
ll_1.append(11)
ll_1.append(13)

ll_2 = LL()
ll_2.append(1+1)
ll_2.append(3+1)
ll_2.append(5+1)
ll_2.append(7+1)
ll_2.append(9+1)
ll_2.append(11+1)
ll_2.append(13+1)

ll_1.merge_alternating(ll_2)
ll_1.traverse()
print("------")
ll_1.reverse_in_groups(None,4)
ll_1.traverse()
print("------")
ll_1.merge_sort()
ll_1.traverse()
