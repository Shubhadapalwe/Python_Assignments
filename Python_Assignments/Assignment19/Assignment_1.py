def AcceptList():
    n = int(input("Enter number of elements: "))
    Data = []
    for i in range(n):
        value = int(input("Enter element: "))
        Data.append(value)
    return Data

def Addition(Data):
    total = 0
    for x in Data:
        total = total + x
    return total

def main():
    Data = AcceptList()
    result = Addition(Data)
    print("Addition is:", result)

if __name__ == "__main__":
    main()