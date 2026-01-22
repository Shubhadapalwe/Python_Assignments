#Accept two numbers and print addition, subtraction, multiplication, division
def calculate_operations(No1,No2):
    addition = No1 + No2
    subtraction = No1 - No2
    multiplication = No1 * No2
    divison = No1 / No2 
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", divison)
No1 = int(input("Enter first number: "))
No2 = int(input("Enter second number: "))
calculate_operations(No1,No2)