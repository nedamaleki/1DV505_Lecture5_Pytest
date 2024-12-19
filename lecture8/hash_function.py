def better_hash(string):
    HASH_MULTIPLIER = 31
    value = 0
    for c in string:
        value = value * HASH_MULTIPLIER + ord(c)
    return value

def hash_function(string, capacity):
    hash_value = better_hash(string)
    if hash_value <= 0:
        hash_value = -hash_value
    return hash_value % capacity


def main():
    capacity = 11
    egyptian = [''] * capacity # List of ten empty elements
    
    print('Ra:', hash_function('Ra', capacity))
    
    egyptian[hash_function('Ra', capacity)] = 'Ra'
    egyptian[hash_function('Amun', capacity)] = 'Amun'
    egyptian[hash_function('Osiris', capacity)] = 'Osiris'
    egyptian[hash_function('Set', capacity)] = 'Set'
    egyptian[hash_function('Anubis', capacity)] = 'Anubis'
    egyptian[hash_function('Horus', capacity)] = 'Horus'
    
    for i in range(len(egyptian)):
        print(f'God at {i} is {egyptian[i]}')
    
main()

