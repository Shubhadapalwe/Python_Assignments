import threading

def Maximum(Data):
    max_no = Data[0]
    for x in Data:
        if x > max_no:
            max_no = x
    print("Maximum element is:", max_no)

def Minimum(Data):
    min_no = Data[0]
    for x in Data:
        if x < min_no:
            min_no = x
    print("Minimum element is:", min_no)

def AcceptList():
    n = int(input("Enter number of elements: "))
    Data = []
    for i in range(n):
        value = int(input("Enter element: "))
        Data.append(value)
    return Data

def main():
    Data = AcceptList()

    t1 = threading.Thread(target=Maximum, args=(Data,), name="Thread1")
    t2 = threading.Thread(target=Minimum, args=(Data,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()