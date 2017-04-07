'''This is a basic implementation of trie datastructure. 
Tries are generally used for implementing contacts book, similar to ones in phone.
Below Trie implementation has methods to add and find strings. 
Since this is a simple implementation, it assumes all add calls are made with distinct strings.
There is also boilerplate code for user input if this is run from CMD/Terminal.

input format is number of commands and then 'add' or 'find' command in seperate lines.
'''

'''receiving input for number of commands'''
n = int(input().strip())

'''Class for each trie node. using dict to store links, might be better to use fixed size array of length 26.
entry variable to denote if this node forms the end of a word present in the Trie.'''
class Node:
    def __init__(self):
        self.links = dict()
        self.entry = False


class Trie:
    def __init__(self):
        self.__root = Node()

    def add(self, string):
        root = self.__root
        for i in range(len(string)):
            if string[i] in root.links:
                root = root.links[string[i]]
            else:
                root.links[string[i]] = Node()
                root = root.links[string[i]]
        root.entry = True
    
    def find(self, string):
        root = self.__root
        for i in range(len(string)):
            if string[i] in root.links:
                root = root.links[string[i]]
            else:
                return False
        return root.entry

'''receive n inputs in seperate lines
ex:-
add test
add tester
find test
---output---True
find testing
---output---False
'''
contacts = Trie()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        contacts.add(contact)
    else:
        print(contacts.find(contact))
