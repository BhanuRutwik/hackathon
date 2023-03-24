# Script 5: JSON parsing
import json

json_str = '{"name": "John Smith", "age": 30, "city": "New York"}'
data = json.loads(json_str)

print(data["name"])
print(data["age"])
print(data["city"])
