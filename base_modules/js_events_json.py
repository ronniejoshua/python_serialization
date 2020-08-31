"""Basic usage of JSON"""
import json
from base_modules.js_events import event

# Converts a Python object into a JSON string
data = json.dumps(event)
print('serialized:', data)
print('data type:', type(data))

# Serialize(JSON String) to bytes, dict keys must be str
data_bytes = data.encode('utf-8')
print('data_bytes:', data_bytes)
print('data_bytes type:', type(data_bytes))

# Indented
print('serialized indented:', json.dumps(event, indent=4))

# Convert the JSON String document into the Python dictionary
event_str = json.loads(data)
print('equal:', event_str == event)

# Can convert (json string converted to bytes) to Python Dictionary
event_bytes = json.loads(data_bytes)
print('equal (bytes):', event_bytes == event)

# Working with files
with open('js_event.json', 'w') as out:
    json.dump(event, out)

with open('js_event.json') as fp:
    event_file = json.load(fp)

print('equal (file):', event_file == event)
