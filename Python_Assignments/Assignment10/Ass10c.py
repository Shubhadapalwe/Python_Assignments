def Factorial(No):
    Fct = 1
    for i in range(1,No +1):
        Fct = Fct * i 
    print("Factorial of given number is :",Fct)
No = int(input("Enter the number for computing the factorial:  "))
Factorial(No)     