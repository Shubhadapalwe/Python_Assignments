# Addition of N natural numbers

def SumOfNaturalNumbers(No):
    Sum = 0
    for i in range(0,No + 1):
        Sum = Sum + i
    print("the summation of given number is :",Sum)
No = int(input("Enter the number for addition : "))
SumOfNaturalNumbers(No  )