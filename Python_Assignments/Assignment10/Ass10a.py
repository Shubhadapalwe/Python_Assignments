# multiplication table of given number

def Table(No):
    for i in range(1,11):
        print(No * i)
No = int(input("Enter the number :"))
Table(No)