from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_first(self, data):
        new_node = Node(data)  # initially this new node’s next pointer is None.
        new_node.next = self.head  # This sets the new node’s next to point to the current first node (self.head).
        self.head = new_node # The head is updated to the new_node, making it the new first node.
        self.size += 1
        
    def get_first(self):
        if self.head is None:
            raise ValueError("List is empty")
        return self.head.data
    
    def remove_first(self):
        if self.size == 0:
            raise ValueError("List is empty")
        self.head = self.head.next  # Move head to the next node
        self.size -= 1  # Decrease the size of the list
        
    def __str__(self):
        if self.size == 0:
            return '[]'
        result = []
        current = self.head
        while current:
            result.append(str(current))
            current = current.next
        return f"[{' -> '.join(result)}]"
    
    def is_empty(self):
        return self.head is None
    
    def get_size(self):
        return self.size
    
    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def find(self, data):
        pos = 0
        current = self.head
        while current:
            if current.data == data:
                return pos
            current = current.next
            pos += 1
        return -1
