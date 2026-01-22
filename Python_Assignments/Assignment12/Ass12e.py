#Accept one number and print that many numbers in reverse order
def PrintReverse(No):
    for i in range (No,0,-1):
        print(i)
No = int(input("Enter the number :"))
PrintReverse(No)