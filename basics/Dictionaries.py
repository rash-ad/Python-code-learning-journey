dict = {"name": "John", "age": 30, "city": "New York"}


print(dict)  
print("Name: " + dict["name"])  
print("Age: " + str(dict["age"]))  
print("City: " + dict["city"])  
dict["age"] = 31
print("Updated Age: " + str(dict["age"]))  
dict["country"] = "USA"
print(dict)

if "name" in dict:
    print("Name is in the dictionary!")
else:
    print("Name is not in the dictionary.")

del dict["city"]
print(dict)

print("Keys: " + str(dict.keys()))  
print("Values: " + str(dict.values()))  
print("Items: " + str(dict.items()))

for key, value in dict.items():
    print(key + ": " + str(value))


print("Length of dictionary: " + str(len(dict)))
dict.clear()
