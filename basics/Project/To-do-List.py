print("Welcome to the To-Do List Program!")
to_do_list = []
while True:
    task = input("Enter a task to add to your to-do list (or type 'done' or 'd' to finish): ")
    if task.lower() == 'done' or task.lower() == 'd':
        break
    to_do_list.append(task)
    print("Task added successfully!")
print("\nYour To-Do List:")
for i in range(len(to_do_list)):
    print(str(i + 1) + ". " + to_do_list[i])
    print("\nThank you for using the To-Do List Program!")

