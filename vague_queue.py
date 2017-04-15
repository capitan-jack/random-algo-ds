        
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
