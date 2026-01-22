#Lambda: check odd number
CheckOdd = lambda No :  No % 2 != 0
No = int(input("Enter the number :"))
print("Number is odd :",CheckOdd(No))