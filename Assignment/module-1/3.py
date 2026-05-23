# Student result program using PEP 8 guidelines
# Input marks from user
s1 = int(input("Enter Python mark : "))
s2 = int(input("Enter PHP mark : "))
s3 = int(input("Enter Java mark : "))

# Calculate total marks
total_marks = s1 + s2 + s3

# Calculate percentage
percentage = total_marks / 3

# Display result
print("\nTotal Marks :", total_marks)
print("Percentage :", percentage)

# Check pass or fail using proper indentation
if s1 >= 40 and s2 >= 40 and s3 >= 40:

    # Grade calculation
    if percentage >= 80:
        print("Grade : A")

    elif percentage >= 60:
        print("Grade : B")

    elif percentage >= 50:
        print("Grade : C")

    else:
        print("Grade : D")

else:
    print("Result : Fail")