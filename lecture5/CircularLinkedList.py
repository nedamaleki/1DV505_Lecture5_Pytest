class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:  # First node
            self.head = new_node
            new_node.next = new_node  # Points to itself
        else:
            temp = self.head
            while temp.next != self.head:  # Traverse until the last node
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head  # Connect new node to the head

    def __str__(self):
        if not self.head:
            return "[]"
        
        result = []
        current = self.head
        while True:  # Traverse until we return to the head
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(result)

# Example Usage
cll = CircularLinkedList()
cll.add(1)
cll.add(2)
cll.add(3)

print(cll)  # Output: 1 -> 2 -> 3
