import pytest
from CircularLinkedList import CircularLinkedList

def test_circular_traversal():
    cll = CircularLinkedList()
    cll.add(1)
    cll.add(2)
    cll.add(3)
    nodes = []
    current = cll.head
    for _ in range(4):  # Traverse 4 times (to test looping)
        nodes.append(current.data)
        current = current.next
    assert nodes == [1, 2, 3, 1]
