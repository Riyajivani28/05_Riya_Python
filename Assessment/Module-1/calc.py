def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 75:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 35:
        return "Pass"
    else:
        return "Fail"


while True:

    print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
    print("1. Check Student Grade")
    print("2. Exit")

    choice = input("Enter your choice : ")

    if choice == "1":

        name = input("Enter student name : ")
        mark = int(input("Enter student marks : "))

        grade = calculate_grade(mark)

        print("\n----- RESULT -----")
        print("Student Name :", name)
        print("Marks :", mark)
        print("Grade :", grade)

    elif choice == "2":
        print("Program Closed Successfully")
        break

    else:
        print("Invalid Choice! Please try again.")