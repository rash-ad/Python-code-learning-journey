print("welcome to Error Handling")
try:
    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")
    print("The list has only", len(my_list), "elements.")
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The specified file was not found.")
    print("Please check the file name and try again.")
    print("Hint: Make sure the file exists in the current directory.")

