"""namedtuple example"""
from collections import namedtuple

"""
namedtuple() Factory Function for Tuples with Named Fields. Named tuples assign meaning to 
each position in a tuple and allow for more readable, self-documenting code. They can be 
used wherever regular tuples are used, and they add the ability to access fields by name 
instead of position index.
"""
Player = namedtuple('Player', 'id name keys')

# Example
if __name__ == '__main__':
    p1 = Player(1, 'Parzival', {'copper', 'jade'})
    print(repr(p1))
