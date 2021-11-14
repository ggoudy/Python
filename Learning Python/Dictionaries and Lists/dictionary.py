cars = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(cars)
print(cars["brand"])
print(len(cars))
print(cars["colors"])

# Get Keys method which will return a list of all keys in the dictionary
x = cars.keys()
print(x)

# Add a key to the dictionary
cars["engine"] = "4-cyl", "v6", "v8"
print(x)

# Get Values method will return a list of all the values in the dictionary
y = cars.values()
print(y)