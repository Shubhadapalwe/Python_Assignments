# Sum of digits
def SumDigit(No):
    sum = 0
    while No != 0:
        digit = No % 10
        
        sum = sum + digit
        No = No //10
    print("Addition of digits :",sum)
No = int(input("ENter the number: "))
SumDigit(No)    
    