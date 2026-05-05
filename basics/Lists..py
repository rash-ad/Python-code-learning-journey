
fruits = ["apple", "banana", "cherry"]
print(fruits)
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)
numbers = [10, 20, 30, 40, 50]
print("numbers: " + str(numbers))

print("First index: " + str(numbers[0]))  # Output: 10
print("Third index: " + str(numbers[2]))  # Output: 30
print("Fifth index: " + str(numbers[4]))  # Output: 50
if "banana" in fruits:
    print("Banana is in the list!")
else:
    print("Banana is not in the list.")
fruits.append("orange")
fruits.insert(1, "grape")
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange']

print("Last index: " + str(fruits[-1]))  # Output: orange
print("Second index: " + str(fruits[1]))  # Output: grape
