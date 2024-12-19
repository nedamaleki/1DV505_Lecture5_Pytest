
from HashTableIterator import HashTableIterator


class Hash_table:
    
    def __init__(self, initial_size = 11):
        self._size = initial_size
        self._count = 0
        self._table = []
        
        for i in range(initial_size):
            self._table.append([])
            
    def better_hash(self, string):
        HASH_MULTIPLIER = 31
        value = 0
        for c in string:
            value = value * HASH_MULTIPLIER + ord(c)
            
        return value
    
    def hash_function(self, key):
        #hash_value = self.better_hash(string)  #before we have considered only string but now it is object
        hash_value = key.__hash__()  #hash(key)  
        
        if hash_value <= 0:
            hash_value = -hash_value
            
        return hash_value % self._size
    
    def _rehash(self):
        old_values = []
        for bucket in self._table:
            for item in bucket:
                old_values.append(item)
                
        self._size = self._size * 2
        self._count = 0
        
        self._table = []
        for i in range(self._size):
            self._table.append([])
            
        for value in old_values:
            self.add(value)
    
    def contains(self, key):
        position = self.hash_function(key)
        return key in self._table[position]
    
    def add(self, key):
        if self._count / self._size > 0.75:
            self._rehash()

        position = self.hash_function(key)
        
        if not self.contains(key):
            self._table[position].append(key)
            self._count += 1
            
    def remove(self, key):
        if not self.contains(key):
            return False
        
        position = self.hash_function(key)
        self._table[position].remove(key)
        self._count -= 1
        return True
        
    def __str__(self):
        result = ''
        for i in range(self._size):
            result += f'[{i}]: '
            bucket = self._table[i]
            
            if not bucket:
                result += 'None'
            else:
                for item in bucket:
                    result += str(item) + ' -> '
                    
            result += '\n'
        
        return result
    
    def __iter__(self):
        return HashTableIterator(self._table)