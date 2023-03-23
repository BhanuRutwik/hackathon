# Import json module using the import keyword
import json
# Open some random json file using the open() function by passing the
# filename/path as an argument to it and store it in a variable
gvn_jsonfile = open("demo.json")
# Load/get the content of the given json file using the load() function of the
# json module and store it in another variable
json_data = json.load(gvn_jsonfile)
# Print the data of the given JSON file
print("The data of the given JSON file:\n", json_data)
print()
# Get a specific value from the json file using slicing
# Printing Address details from a given JSON file
print("Printing Address details:")
print(json_data["Address"])
print()
# Printing 'geo' details in Address
print("Printing 'geo' details in Address:")
print(json_data["Address"][0]["geo"])
print()
# Printing 'lat' details in Address/geo
print("Printing 'lat' details in Address/geo:")
print(json_data["Address"][0]["geo"]["lat"])