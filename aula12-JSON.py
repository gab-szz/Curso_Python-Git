############
#   JSON   #
############
import json

# Converter Json em Dicionário
json_file = '{"nome": "Gabriel","idade":36}'
dictionary = json.loads(json_file)
print(dictionary)

# Converter Dicionário em Json
new_json = json.dumps(dictionary)
print(type(new_json))
