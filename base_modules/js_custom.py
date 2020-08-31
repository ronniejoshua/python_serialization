"""Example serializing custom types"""
from datetime import datetime
from base_modules.js_events import _event
import json


def default(obj):
    """
    Encode datetime to string in YYYY-MM-DDTHH:MM:SS format (RFC3339)
    """
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj


def pairs_hook(pairs):
    """Convert the "time" key to datetime"""
    obj = {}
    for key, value in pairs:
        if key == 'time':
            # Python >= 3.7
            # convert from a string to date time object
            # this is called deserialize
            value = datetime.fromisoformat(value)
        obj[key] = value
    return obj


if __name__ == '__main__':
    serialized = json.dumps(_event, default=default)
    print(serialized)

    deserialized = json.loads(serialized, object_pairs_hook=pairs_hook)
    print(deserialized)
