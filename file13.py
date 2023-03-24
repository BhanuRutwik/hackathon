# Script 8: Dictionary manipulation
person = {"name": "John Smith", "age": 30, "city": "New York"}
person["occupation"] = "Programmer"

for key, value in person.items():
    print("{}: {}".format(key, value))
