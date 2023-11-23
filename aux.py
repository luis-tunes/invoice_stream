import json

with open('key.json', 'r') as f:
    data = json.load(f)

json_str = json.dumps(data)
print(json_str)