import json 
import os 

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convert Python dictionary to JSON string
json_data = json.dumps(data)
print(json_data)

# Write JSON data to a file
fileJSON = os.path.basename(__file__)[:-3]+".json"
with open(fileJSON, 'w') as file:
    json.dump(data, file)
