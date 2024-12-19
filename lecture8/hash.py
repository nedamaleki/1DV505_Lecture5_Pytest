def simple_hash(string):
    value = 0
    for c in string:
        #print(ord(c))
        value += ord(c)
    return value

def better_hash(string):
    HASH_MULTIPLIER = 31
    value = 0
    for c in string:
        value = value * HASH_MULTIPLIER + ord(c)
    return value

def hash_with_shift(string):
    value = 0
    for c in string:
        # equivalent to 31 * h + ord(c)
        value = ((value << 5) - value) + ord(c)
    return value

def main():
    #print(simple_hash('Darth Vader'))
    print('eat simple hash:', simple_hash('eat'))
    print('tea simple hash:', simple_hash('tea'))  
    print() 
    
    print('Ra better hash:', better_hash('Ra'))
    print('eat better hash:', better_hash('eat'))
    print('tea better hash:', better_hash('tea'))
    print() 
    
    print('Darth Vader better hash:', better_hash('Darth Vader'))
    print('Darth Vader shift hash:', hash_with_shift('Darth Vader'))
    print() 

main()