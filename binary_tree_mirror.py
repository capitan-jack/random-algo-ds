class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''to support level order traversal to insert level wise left to right'''       
class Queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, data):
        self.data = self.data + [data]
    
    def dequeue(self):
        if len(self.data) > 0:
            dequed = self.data[0]
            self.data = self.data[1:len(self.data)]
            return dequed
        return None
    
    def size(self):
        return len(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def insert_level_wise(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        que = Queue()
        que.enqueue(self.root)
        found_parent = None
        while que.size() > 0 and found_parent == None:
            dequed = que.dequeue()
            if dequed.left != None and dequed.right != None:
                que.enqueue(dequed.left)
                que.enqueue(dequed.right)
            else:
                found_parent = dequed
        if found_parent.left == None:
            found_parent.left = Node(data)
        else:
            found_parent.right = Node(data)
        
    def traverse_in_order(self):
        self._traverse_in_order(self.root)
    
    def _traverse_in_order(self, root):
        if root != None:
            self._traverse_in_order(root.left)
            print(root.data)
            self._traverse_in_order(root.right)
    
    def mirror_tree(self):
        self._mirror_tree(self.root)
    
    def _mirror_tree(self, root):
        if root == None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self._mirror_tree(root.left)
        self._mirror_tree(root.right)
    
    def is_mirror(self):
        if self.root == None:
            return True
        return self._is_mirror(self.root.left, self.root.right)
    
    def _is_mirror(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return True
        return node1.data == node2.data and\
    self._is_mirror(node1.left, node2.right) and\
    self._is_mirror(node1.right, node2.left)
