class Node:
    def __init__(self,key=None,data=None):
        self.key = key
        self.data = data


class MinHeap:
    def __init__(self, sorted_array = []):
        self.heap = [Node()]
        for key, data in sorted_array:
            self.heap.append(Node(key, data))

    def heapify(self, i=1):
        left = 2*i
        right = 2*i + 1
        smallest = i
        if left < len(self.heap) and self.heap[left].key < self.heap[smallest].key:
            smallest = left
        if right < len(self.heap) and self.heap[right].key < self.heap[smallest].key:
            smallest = right
        if smallest != i:
            temp = self.heap[smallest]
            self.heap[smallest] = self.heap[i]
            self.heap[i] = temp
            self.heapify(smallest)
     
    def read_min(self):
        return self.heap[1]
    
    def replace_min(self, key, data):
        minimum = self.heap[1]
        self.heap[1] = Node(key, data)
        self.heapify()
        return minimum
    
    def remove_min(self):
        minimum = self.heap[1]
        self.heap = [self.heap[0]] + self.heap[2:len(self.heap)]
        self.heapify()
        return minimum

sorted_matrix = [[1,5,10,15,20],[2,6,11,16,21],[3,7,12,17,22], [4,8,13,18,23]]
k = 5
min_heap = MinHeap(zip(sorted_matrix[0], [(0,i) for i in range(len(sorted_matrix[0]))]))
for i in range(k):
    current_min = min_heap.read_min()
    if current_min.data[0]+1 < len(sorted_matrix):
        next_input_key = sorted_matrix[current_min.data[0]+1][current_min.data[1]]
        next_input_data = (current_min.data[0]+1, current_min.data[1])
        min_heap.replace_min(next_input_key, next_input_data)
    else:
        min_heap.remove_min()
print(current_min.key)
