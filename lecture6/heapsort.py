#import sys # Import Heap class from folder lectures/heap
#sys.path.append("lectures/heap/")
import Heap as h

def heap_sort(lst):
    if len(lst) < 2: # Empty and singleton lists
        return lst
    
    heap = h.Heap() # A new empty heap
    for n in lst: # Add elements to heap
        heap.add(n)
        
    res = []
    while not heap.is_empty(): # Pull sorted element from heap
        res.append(heap.pull())
    return res[::-1] # In reverse to get smallest first


def main():
    # Demonstrating adding elements to the heap and pulling them one by one
    print("Heap demonstration:")
    heap = h.Heap()
    heap.add(5)
    heap.add(3)
    heap.add(10)
    heap.add(1)
    
    print(heap.pull())  # Output: 10 (largest element)
    print(heap.pull())  # Output: 5
    print(heap.pull())  # Output: 3
    print(heap.pull())  # Output: 1
    
    # Example usage of heap_sort
    print("\nHeap Sort demonstration:")
    lst = [5, 3, 10, 1, 7, 2]
    sorted_lst = heap_sort(lst)

    print("Original List:", lst)
    print("Sorted List:", sorted_lst)

main()
