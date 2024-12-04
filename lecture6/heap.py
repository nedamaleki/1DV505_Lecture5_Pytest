class Heap:
    def __init__(self):
        # Store heap elements in a list
        self.data = []

    def is_empty(self):
        # Return True if the heap has no elements
        return len(self.data) == 0

    def add(self, value):
        # Add a new value to the heap
        self.data.append(value)  # Add to the end
        self._bubble_up(len(self.data) - 1)  # Restore heap property

    def pull(self):
        # Remove and return the root (largest element)
        if self.is_empty():
            raise IndexError("Pull from empty heap")
        
        root = self.data[0]
        # Move the last element to the root and remove it
        self.data[0] = self.data.pop()
        
        # Restore heap property by bubbling down the new root
        if not self.is_empty():
            self._bubble_down(0)
        
        return root

    def _bubble_up(self, index):
        # Move a node up until the heap property is restored
        parent_index = (index - 1) // 2  # Parent's index
        while index > 0 and self.data[index] > self.data[parent_index]:
            # Swap with parent if current node is greater
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            index = parent_index  # Move up
            parent_index = (index - 1) // 2

    def _bubble_down(self, index):
        # Move a node down until the heap property is restored
        largest = index
        left_child = 2 * index + 1  # Left child's index
        right_child = 2 * index + 2  # Right child's index

        # Check if the left child is larger than the current node
        if left_child < len(self.data) and self.data[left_child] > self.data[largest]:
            largest = left_child

        # Check if the right child is larger than the largest so far
        if right_child < len(self.data) and self.data[right_child] > self.data[largest]:
            largest = right_child

        # If the largest is not the current node, swap and continue
        if largest != index:
            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            self._bubble_down(largest)
