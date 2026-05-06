student = {
    "name": [],
    "marks": []
}

while True:   
    name=input("Enter your  name : ")
    student["name"] .append(name)
    marks = input("Enter your marks : ")
    student["marks"] .append(marks)
    print("Student added successfully")
    for key, value in student.items():
        print(key + ": " + ", ".join(value))
    #join() means it will join the list of values into a single string with a comma and space as a separator.


    cont = input("Do you want to add another student? (yes/no): ")
    if cont.lower() != "yes" and cont.lower() != "y":
        break
    

    
 