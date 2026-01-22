#Accept marks and display grade
def DisplayGrade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

marks = int(input("Enter marks: "))
DisplayGrade(marks)