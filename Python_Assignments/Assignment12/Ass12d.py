#Accept one number and print that many numbers starting from 1
def PrintFromStarting(No):
    for i in range (1,No+1):
        print(i)
No = int(input("Enter the number :"))
PrintFromStarting(No)