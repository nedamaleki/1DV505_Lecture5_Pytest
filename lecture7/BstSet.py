class BstSet:
    
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = BstNode(val, None, None)
        else:
            self.root.add(val)

    def search(self, val):
        if self.root is None:
            return False
        else:
            return self.root.contains(val)

    def __str__(self):   
        txt = "{ "
        if self.root is not None:
            txt += self.root.to_string()
        return txt + "}"
    
    # Inside class BstSet
    def dot(self):
        if self.root is None:
            return "No nodes ==> no markup"
        else:
            dot_text = "graph BST {\n"
            # Parent is None for root
            dot_text += self.root.dot(None) # None as parent
            dot_text += "}"
            return dot_text


class BstNode:
    def __init__(self, value, left, right):
        self.value = value  # Value to store in node
        self.left = left  # Left child (a node)
        self.right = right  # Right child (a node)

    def add(self, val):
        if val < self.value:  # Go left
            if self.left is None:  # Empty slot, add new left child
                self.left = BstNode(val, None, None)
            else:
                self.left.add(val)  # Recursive call on left child
        elif val > self.value:  # Go right
            if self.right is None:  # Empty slot, add new right child
                self.right = BstNode(val, None, None)
            else:
                self.right.add(val)  # Recursive call on right child


    def to_string(self): # inorder print
        # Generate a string representation using in-order traversal
        result = ""
        if self.left is not None:
            result += self.left.to_string() + ", "  # Add left subtree
        result += str(self.value)  # Add current node
        if self.right is not None:
            result += ", " + self.right.to_string()  # Add right subtree
        return result
    
    # Inside class BstNode
    ''' def dot(self, parent):
        txt = ""
        # If the parent exists, create an edge from parent to self
        if parent is not None:
            txt += f'    "{parent}" -- "{self.value}";\n'

        # Add edges for the left child
        if self.left is not None:
            txt += self.left.dot(self.value)  # Pass current node's value as parent
        else:
            # Visualize a null left child
            txt += f'    "{self.value}" -- "null-{self.value}-L" [style=dotted];\n'

        # Add edges for the right child
        if self.right is not None:
            txt += self.right.dot(self.value)  # Pass current node's value as parent
        else:
            # Visualize a null right child
            txt += f'    "{self.value}" -- "null-{self.value}-R" [style=dotted];\n'

        return txt
        '''
    
    def dot(self, parent):
        txt = ""
        if parent is not None:
            # Create an edge from parent to current node
            txt += f'    "{parent}" -- "{self.value}";\n'

        # Add invisible left child for alignment if left is missing
        if self.left is None:
            txt += f'    L{self.value} [style=invis, width=0, label=" "];\n'
            txt += f'    "{self.value}" -- L{self.value} [style=invis, width=0, label=" "];\n'
        else:
            txt += self.left.dot(self.value)

        # Add invisible right child for alignment if right is missing
        if self.right is None:
            txt += f'    R{self.value} [style=invis, width=0, label=" "];\n'
            txt += f'    "{self.value}" -- R{self.value} [style=invis, width=0, label=" "];\n'
        else:
            txt += self.right.dot(self.value)

        return txt

