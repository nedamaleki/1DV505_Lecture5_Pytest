import random as rnd
from BstSet import BstSet  


def main():
    # Create a random list of integers
    lst = [rnd.randint(1, 100) for _ in range(10)]
    print(f"Input list: {lst}")

    # Create an empty Binary Search Tree
    bst = BstSet()

    # Add values to the BST
    for n in lst:
        bst.add(n)

    # Display the BST as a string (in-order traversal)
    print("Binary Search Tree created!")
    print(bst)

    # Generate DOT representation and save to file
    dot_representation = bst.dot()
    with open("tree.dot", "w") as f:
        f.write(dot_representation)
    print("DOT file 'tree.dot' created. Use Graphviz to visualize.")
    

    # Optionally, render DOT to PNG if Graphviz is installed
    try:
        import subprocess
        subprocess.run(["dot", "-Tpng", "tree.dot", "-o", "tree.png"], check=True)
        print("Tree visualization saved as 'tree.png'.")
    except FileNotFoundError:
        print("Graphviz 'dot' command not found. Please install Graphviz to visualize the tree.")
    except Exception as e:
        print(f"An error occurred during visualization: {e}")


main()
