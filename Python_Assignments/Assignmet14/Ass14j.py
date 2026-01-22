# Lambda: largest among three numbers
Largest = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)

No1 = int(input("Enter first number: "))
No2 = int(input("Enter second number: "))
No3 = int(input("Enter third number: "))
print("Largest number is:", Largest(No1, No2, No3))