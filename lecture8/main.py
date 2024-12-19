from HashTable import Hash_table


def main():
    gods = Hash_table()
    
    egyptian_gods = ['Ra', 'Amun', 'Set', 'Osiris', 'Horus', 'Anubis', 'Nephthys', 'Geb', 'Shu', 'Dedun', 'Raet-Tawy', 'Sekhmet']
    
    for god in egyptian_gods:
        gods.add(god)
        
    #print(gods)  #now that we have iterator we can close this and use the for loop for gods to print the god
    
    for god in gods:
        print(god)
        
    #Output will be identical to previous program as no duplicates are allowed
    '''gods.add('Amun')
    gods.add('Geb')
    gods.add('Shu')

    print(gods)
    
    gods.remove('Osiris')
    
    print(gods)'''

main()