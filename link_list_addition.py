'''using linked list for digit wise representaion of integer and adding two linked list
    input: 1 2 2 3 4 5 5 6 7
           2 3 4 5 5
    output 1->2->2->3->6->9->0->2->2'''

class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self, array_in_order=None):
        self.root = Node()
        if array_in_order != None:
            for i in range(len(array_in_order)):
                self.append(array_in_order[i])

    def append(self,data):
        root = self.root
        while root.next != None:
            root = root.next
        if root.data == None:
            root.data = data
        else:
            root.next = Node(data)
       
    def prepend(self, data):
        if self.root.data == None:
            self.root.data = data
        else:
            root = Node(data)
            root.next = self.root
            self.root = root
    
    def convert_to_int(self):
        num = 0
        root = self.root
        while root.next != None:
            num = num*10
            num = num + int(root.data)
            root = root.next
        if root.data != None:
            num = num*10
            num = num + int(root.data)
        return num
    
    def traverse(self):
        root = self.root
        str_format = ""
        while root.next != None:
            str_format += str(root.data) + "->"
            root = root.next
        print(str_format + str(root.data))


def to_digit_array(num):
    if num==0:
        return [0]
    num_digits = []
    while num>0:
        num_digits = [num%10] + num_digits
        num = int(num/10)
    return num_digits


def add_2_linked_lists(list1, list2):
    value = list1.convert_to_int()
    value += list2.convert_to_int()
    list3 = LinkedList(to_digit_array(value))
    return list3


array1 = list(map(int,input().strip().split(' ')))
array2 = list(map(int,input().strip().split(' ')))

l_list_1 = LinkedList(array1)
l_list_2 = LinkedList(array2)
l_list_3 = add_2_linked_lists(l_list_1, l_list_2)
l_list_3.traverse()
