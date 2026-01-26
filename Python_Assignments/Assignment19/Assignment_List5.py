import MarvellousNum

def AcceptList():
    n = int(input("Enter number of elements: "))
    Data = []
    for i in range(n):
        value = int(input("Enter element: "))
        Data.append(value)
    return Data

def ListPrime(Data):
    total = 0
    for x in Data:
        if MarvellousNum.ChkPrime(x):
            total = total + x
    return total

def main():
    Data = AcceptList()
    result = ListPrime(Data)
    print("Addition of prime numbers is:", result)

if __name__ == "__main__":
    main()