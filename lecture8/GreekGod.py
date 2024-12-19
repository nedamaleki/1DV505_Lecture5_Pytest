class GreekGod:
    def __init__(self, greek_name, roman_name):
        self.greek_name = greek_name
        self.roman_name = roman_name
        
    def __eq__(self, other):
        if not isinstance(other, GreekGod):
            return False
        return self.greek_name == other.greek_name and self.roman_name == other.roman_name
    
    def __hash__(self):
        HASH_MULTIPLIER = 31
        value = 0
        
        for c in self.greek_name:
            value = value * HASH_MULTIPLIER + ord(c)
            
        # Add a separator to ensure difference
        value = value * HASH_MULTIPLIER + ord('|')
        
        for c in self.roman_name:
            value = value * HASH_MULTIPLIER + ord(c)
            
        return value # The hash value is based on both names
    
    def __str__(self):
        return f'{self.greek_name} ({self.roman_name})'