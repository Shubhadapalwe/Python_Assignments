def DivisibleBy(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print(" Not Divisible by 3 and 5")
no = int(input("Enter the number:"))
DivisibleBy(no)

