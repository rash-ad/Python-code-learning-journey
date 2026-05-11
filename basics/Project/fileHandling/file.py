print("Welcome to the File Handling Program!")
file_name = input("Enter the name of the file you want to create (with extension): ")
try:
    with open(file_name, 'w') as file:
        print("File created successfully!")
        while True:
            content = input("Enter content to write to the file (or type 'done' or 'd' to finish): ")
            if content.lower() == 'done' or content.lower() == 'd':
                break
            file.write(content + '\n')
            print("Content added successfully!")
    print("\nFile writing completed!")
except Exception as e:
    print("An error occurred while handling the file:", e)
print("\nThank you for using the File Handling Program!")