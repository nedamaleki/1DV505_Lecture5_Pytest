class HashTableIterator:
    def __init__(self, table):
        self._table = table
        self._bucket_index = 0
        self._element_index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while self._bucket_index < len(self._table):
            current_bucket = self._table[self._bucket_index]
            
            if self._element_index < len(current_bucket):
                element = current_bucket[self._element_index]
                self._element_index += 1
                return element
            
            self._bucket_index += 1
            self._element_index = 0
            
        raise StopIteration