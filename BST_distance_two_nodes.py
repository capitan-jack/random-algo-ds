class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
    
    def _insert(self, root, data):
        if data<root.data:
            if root.left == None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right == None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)
    
    def _find_depth(self, root, data, current_depth):
        if root.data == data:
            return current_depth
        elif root.data < data:
            return self._find_depth(root.right, data, current_depth+1)
        else:
            return self._find_depth(root.left, data, current_depth+1)
    
    def find_distace(self, data1, data2):
        return self._find_path_length(self.root, min(data1, data2), max(data1, data2))
    
    def _find_path_length(self, root, data1, data2):
        if root.data < data1 and root.data < data2:
            return self._find_path_length(root.right, data1, data2)
        elif root.data > data1 and root.data > data2:
            return self._find_path_length(root.left, data1, data2)
        else:
            if root.data == data1:
                return self._find_depth(root.right, data2, 1)
            elif root.data == data2:
                return self._find_depth(root.left, data1, 1)
            else:
                return self._find_depth(root.left, data1, 1)+\
            self._find_depth(root.right, data2, 1) + 1

bst = BST()
bst.insert(20)
bst.insert(12)
bst.insert(32)
bst.insert(4)
bst.insert(9)
bst.insert(17)
bst.insert(14)
bst.insert(24)
bst.insert(41)
bst.insert(1)

print(bst.find_distace(12, 4))
