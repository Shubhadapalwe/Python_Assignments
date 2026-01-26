import threading

def SumList(Data, Result):
    total = 0
    for x in Data:
        total += x
    Result["sum"] = total

def ProductList(Data, Result):
    product = 1
    for x in Data:
        product *= x
    Result["product"] = product

def AcceptList():
    n = int(input("Enter number of elements: "))
    Data = []
    for i in range(n):
        value = int(input("Enter element: "))
        Data.append(value)
    return Data

def main():
    Data = AcceptList()

    Result = {}

    t1 = threading.Thread(target=SumList, args=(Data, Result), name="SumThread")
    t2 = threading.Thread(target=ProductList, args=(Data, Result), name="ProductThread")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of elements:", Result["sum"])
    print("Product of elements:", Result["product"])

if __name__ == "__main__":
    main()