def AcceptList():
    n = int(input("Enter number of elements: "))
    Data = []
    for i in range(n):
        value = int(input("Enter element: "))
        Data.append(value)
    return Data

def Minimum(Data):
    min_no = Data[0]
    for x in Data:
        if x < min_no:
            min_no = x
    return min_no

def main():
    Data = AcceptList()
    result = Minimum(Data)
    print("Minimum number is:", result)

if __name__ == "__main__":
    main()