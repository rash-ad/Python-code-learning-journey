list = [1, 2, 3, 4, 5]
print("Welcome to the List and Loop Program!")
print("The original list is: " + str(list))
print("The length of the list is: " + str(len(list)))

print("The first element of the list is: " + str(list[0]))
print("The last element of the list is: " + str(list[-1]))
for i in range(len(list)):
    print("Element at index " + str(i) + ": " + str(list[i]))
print("\nThe list reversed is: " + str(list[::-1]))
print("\nThe list with each element squared: " + str([x ** 2 for x in list]))
print("\nThe list with only even numbers: " + str([x for x in list if x % 2 == 0]))
print("\nThe list with only odd numbers: " + str([x for x in list if x % 2 != 0]))
print("The list with each element multiplied by 10: " + str([x * 10 for x in list]))
print("\nThe list with each element divided by 2: " + str([x / 2 for x in list]))