import json

dictionary = '{"nome": "Gabriel","idade":36}'
json_file = json.loads(dictionary)
print(json_file)
