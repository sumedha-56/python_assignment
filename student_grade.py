students={}
while True:
    print("1. Add Student")
    print("2. Change grade")
    print("3. View grade")

    choice=int(input("Enter choice"))
    if choice==1:
        name=input("Enter student name")
        grade=input("Enter student grade")
        students[name]=grade
        print ("Student added")
    elif choice==2:
        name=input("Enter student name")
        if name in students:
            grade=input("Enter new grade")
            students[name]=grade
            print("Grade updated")
        else:
            print("Student not found")
    elif choice==3:
        for name, grade in students.items():
            print(name, ":", grade)
    else:
        print("Invalid choice")
        break
