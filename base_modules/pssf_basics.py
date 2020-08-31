"""Basic pickle exmaple"""
import pickle
from base_modules.pssf_moves import move1, move2, move3, move4

print(f'move1 = {move1}')

# serialize. data is of type "bytes:
data = pickle.dumps(move1)
print(f'data (from move1) = {data}')

# de-serialize
move1d = pickle.loads(data)
print(f'move1d (from data) = {move1d}')

# serialize to file
# open a file with .pkl extension and write as binary
with open('move1.pkl', 'wb') as out:
    pickle.dump(move1, out)

# de-serialize from file
# read a file as binary with .pkl extension

with open('move1.pkl', 'rb') as fp:
    move1f = pickle.load(fp)

print(f'move1f (from file) = {move1f}')

# You can save only one object with pickle, to serialize several objects place
# them in a container (e.g. list, dict, set ...)

dance = [move1, move2, move3, move4]

with open('dance.pkl', 'wb') as out:
    pickle.dump(dance, out)

# Load all from file
with open('dance.pkl', 'rb') as fp:
    file_dance = pickle.load(fp)

for move in file_dance:
    print(f'{move.limb} {move.action}')
