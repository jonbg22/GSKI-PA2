from array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self):
        # Pick one of these to use.
        # Stack must have the container you dont choose for Queue
        
        self.container = LinkedList()
        # self.container = ArrayDeque()

    def add(self, data):
        self.container.push_back(data)
    
    def remove(self):
        return self.container.pop_front()

    def get_size(self):
        return self.container.get_size()

    def __str__(self):
        return str(self.container)

if __name__ == "__main__":
    q = Queue()
    print(q)
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(0)
    print(q)
    print(q.remove())
    print(q)

