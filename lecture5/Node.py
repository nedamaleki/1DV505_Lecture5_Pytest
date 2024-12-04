class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        if isinstance(self.data, str):
            return f"'{self.data}'"
        return str(self.data)

