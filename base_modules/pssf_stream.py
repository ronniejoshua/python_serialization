"""Streaming pickle example"""
import pickle
from socket import socketpair
from base_modules.pssf_moves import move1, move2, move3, move4

"""
Resources:
https://docs.python.org/3/library/socket.html
https://www.youtube.com/watch?v=T0rYSFPAR0A
"""

# Creates two connected sockets
ws, rs = socketpair()

# For every socket create a file
w, r = ws.makefile('wb'), rs.makefile('rb')

# Serialize - Dump the moves to write socket
pickle.dump(move1, w)
pickle.dump(move2, w)
pickle.dump(move3, w)
pickle.dump(move4, w)

# Flushing the data written/dumped data to the receiving socket
w.flush()

# De-serialize
for _ in range(4):
    # loads data from the read file
    move = pickle.load(r)
    print(f'{move.limb} {move.action}')
