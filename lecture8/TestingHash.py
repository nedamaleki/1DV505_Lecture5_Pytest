from GreekGod import GreekGod
from HashTable import Hash_table

zeus = GreekGod('Zeus', 'Jupiter')
zeus_2 = GreekGod('Zeus', 'Jupiter')
poseidon = GreekGod('Poseidon', 'Neptune')
poseidon_2 = GreekGod('Poseidon', 'Neptune')

print(f'Hash of Zeus/Jupiter: {zeus.__hash__()}')
print(f'Hash of Zeus_2: {zeus_2.__hash__()}')
print(f'Hash of Poseidon/Neptune: {poseidon.__hash__()}')
print(f'Hash of Poseidon_2: {poseidon_2.__hash__()}')

print(f'Zeus are the same', zeus == zeus_2)
print(f'Poseidons are the same', poseidon == poseidon_2)