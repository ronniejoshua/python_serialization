"""Example of streaming JSON"""
"""
Reference: https://docs.python.org/3/library/io.html#io.BytesIO
"""
import json
from io import BytesIO

groups = [
    {'animal': 'bee', 'group': 'swarm'},
    {'animal': 'fox', 'group': 'charm'},
    {'animal': 'whale', 'group': 'pod'},
]

# Sending side
network = BytesIO()
for message in groups:
    # Serialize the python object
    data = json.dumps(message)
    # Sockets work in byte level
    network.write(data.encode('utf-8'))
    network.write(b'\n')

# Receiving side
# Go back to start of data for reading side
# Seeks back to the beginning of the Buffer
network.seek(0)

while True:
    line = network.readline()
    # If there are no lines left
    if not line:
        break
    # De-serializes the Json String
    message = json.loads(line)
    print('got', message)
