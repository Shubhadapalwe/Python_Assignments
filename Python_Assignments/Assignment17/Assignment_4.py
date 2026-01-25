#Return addition of factors (Input: 12 -> 16)
def AdditionOfFactors(No):
    total = 0
    for i in range(1,No):
        if No % i == 0:
            total = total + i
    return total
def main():
    No = int(input("Enter the number :"))
    print("The addition of FActors are :",AdditionOfFactors(No))

if __name__ == "__main__":
    main()