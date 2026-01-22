# Lambda: minimum of two numbers
Minimum = lambda No1,No2 : No2 if No1 > No2 else No1

No1= int(input("Enter the 1st number :"))
No2= int(input("Enter the 2nd number :"))
print("The maximum number is. :",Minimum(No1,No2))