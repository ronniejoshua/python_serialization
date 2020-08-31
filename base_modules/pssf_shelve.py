"""shelve example"""
import shelve
from base_modules.pssf_moves import move1, move2, move3, move4

"""
Resources:
https://docs.python.org/3/library/shelve.html
"""

"""
A “shelf” is a persistent, dictionary-like object. The difference with “dbm” databases is that 
the values (not the keys!) in a shelf can be essentially arbitrary Python objects — anything 
that the pickle module can handle. This includes most class instances, recursive data types, 
and objects containing lots of shared sub-objects. The keys are ordinary strings.
"""
db = shelve.open('dance.db')
db['1'] = move1
db['2'] = move2
db['3'] = move3
db['4'] = move4
db.close()

# Using context manager
with shelve.open('_dance.db') as _db:
    _db['1'] = move1
    _db['2'] = move2
    _db['3'] = move3
    _db['4'] = move4

# Go on vacation, ...

db = shelve.open('dance.db')
print(db['1'])

_db = shelve.open('_dance.db')
print(_db['1'])
