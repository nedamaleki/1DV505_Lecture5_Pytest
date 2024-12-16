from graphviz import Digraph

class BstNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, val):
        if val < self.value:
            if self.left is None:
                self.left = BstNode(val)
            else:
                self.left.add(val)
        elif val > self.value:
            if self.right is None:
                self.right = BstNode(val)
            else:
                self.right.add(val)

    def generate_dot(self, graph=None):
        if graph is None:
            graph = Digraph(comment='BinarySearchTree')

        # Add this node to the graph
        graph.node(str(self.value), str(self.value))

        # Add left child to the graph if it exists
        if self.left:
            graph.node(str(self.left.value), str(self.left.value))
            graph.edge(str(self.value), str(self.left.value))
            self.left.generate_dot(graph)

        # Add right child to the graph if it exists
        if self.right:
            graph.node(str(self.right.value), str(self.right.value))
            graph.edge(str(self.value), str(self.right.value))
            self.right.generate_dot(graph)

        return graph


class BstSet:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = BstNode(val)
        else:
            self.root.add(val)

    def print_tree(self):
        if self.root:
            graph = self.root.generate_dot()
            graph.render(filename='bst_tree', format='png', view=True)  # Saves and opens the image
        else:
            print("The tree is empty.")

# Main function to run the program
def main():
    lst = [59, 70, 81, 23, 62, 25, 74, 60, 68, 53]
    print("Input list:", lst)
    bst = BstSet()  # Create empty BST
    for n in lst:
        bst.add(n)  # Add values to tree
    bst.print_tree()  # Visualize the tree

main()
