#print all even numbers till given number 
def PrintEvenNumber(No):
    for i in range(0,No + 1):
        if i % 2 == 0:
            print(i)
No = int(input("Enter the number for compute :"))
PrintEvenNumber(No)

