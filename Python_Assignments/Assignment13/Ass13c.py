#Check whether number is Perfect or not
def CheckPerfect(No):
    sum = 0
    for i in range(1, No):
        if No % i == 0:
            sum = sum + i

    if sum == No:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

No = int(input("Enter number: "))
CheckPerfect(No)