class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class LinkedList():
    def __init__(self, head = None):
        self.head = head
        self.tail = head
        self.size = 0

    def __str__(self) -> str:
        cur_node = self.head
        out = ""
        while cur_node != None:
            out += f"{cur_node.data} "
            cur_node = cur_node.next
        return out.rstrip()

    def push_front(self, data):
        self.head = Node(data,self.head)
        self.size += 1

    def pop_front(self):
        if self.head == None:
            return None
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node
    
    def push_back(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        if self.tail == None:
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_back(self):
        if self.head == None:
            return
        if self.head.next == None:
            popped_node = self.head
            self.head = None
            self.size -= 1
            return popped_node
        cur_node = self.head
        while cur_node.next.next != None:
            cur_node = cur_node.next
        popped_node = cur_node.next
        cur_node.next = None
        self.tail = cur_node
        self.size -= 1
        return popped_node

    def get_size(self):
        return self.size

if __name__ == "__main__":
    ll = LinkedList()
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_front(4)
    print(ll)
    print("Size: ",ll.get_size())
    print("Popped Back:",ll.pop_back())
    print(ll)
    print("Size: ",ll.get_size())
    print("Popped Front:",ll.pop_front())
    print(ll)
    print("Size: ",ll.get_size())

