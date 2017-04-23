
class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None


def check_palindrome_ll(head, root):
    if root == None:
        return True
    comp_val = None
    if root.next == None:
        comp_val = 1
    else:
        comp_val = check_palindrome_ll(head, root.next)
    if not comp_val == None:
        ptr = head
        for i in range(1,comp_val):
            ptr = ptr.next
        if ptr.data == root.data:
            return comp_val + 1
        else:
            return None


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print(check_palindrome_ll(head, head))
