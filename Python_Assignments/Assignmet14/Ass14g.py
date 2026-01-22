# Lambda: divisible by 5
DivisibleBy5 = lambda No : No % 5 == 0
No = int(input("Enter the number :"))
print("Given number is divisible by 5 :",DivisibleBy5(No))