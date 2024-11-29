import pytest
from LinkedList import LinkedList

def test_empty_list_creation():
    ll = LinkedList()
    assert ll.is_empty() == True
    assert ll.get_size() == 0
    assert str(ll) == '[]'
        
#test_empty_list_creation()  -> # No Need to Call the Test Function Manually. pytest automatically discovers and runs all functions prefixed with test_.

def test_add_first_olympian_gods():
    ll = LinkedList()
    ll.add_first('Zeus')
    assert ll.get_first() == 'Zeus'
    assert ll.get_size() == 1
    ll.add_first('Poseidon')
    assert ll.get_first() == 'Poseidon'
    assert ll.get_size() == 2
    
def test_remove_first():
    ll = LinkedList()
    ll.add_first('Hades')
    ll.add_first('Poseidon')
    ll.add_first('Zeus')
    ll.remove_first()
    assert ll.get_first() == 'Poseidon'
    assert ll.get_size() == 2
    
def test_contains_and_find_methods():
    ll = LinkedList()
    gods = ['Zeus', 'Hera', 'Poseidon', 'Demeter']
    for god in gods:
        ll.add_first(god)
    assert ll.contains('Hera') == True
    assert ll.contains('Apollo') == False
    assert ll.find('Poseidon') == 1
    assert ll.find('Apollo') == -1