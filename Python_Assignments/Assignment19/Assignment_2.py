def AcceptList():
    n = int(input("Enter number of elements: "))
    Data = []
    for i in range(n):
        value = int(input("Enter element: "))
        Data.append(value)
    return Data

def Maximum(Data):
    max_no = Data[0]
    for x in Data:
        if x > max_no:
            max_no = x
    return max_no

def main():
    Data = AcceptList()
    result = Maximum(Data)
    print("Maximum number is:", result)

if __name__ == "__main__":
    main()