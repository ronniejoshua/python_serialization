"""Generate metric in JSON"""
import json
from datetime import datetime

from base_modules.so_metric import metric


def default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return obj


data = json.dumps(metric, default=default, indent=4)
print(data)
