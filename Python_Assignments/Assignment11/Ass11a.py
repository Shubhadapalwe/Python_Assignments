def CheckPrime(No):
    if No <= 1:
        print("Not Prime Number")
        return

    for i in range(2, No):
        if No % i == 0:
            print("Not Prime Number")
            return

    print("Prime Number")

No = int(input("Enter the number: "))
CheckPrime(No)