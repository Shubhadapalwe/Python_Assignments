#Threads EvenList & OddList (sum of even/odd elements)
import threading

def AcceptList():
    n = int(input("Enter number of elements: "))
    Data = []
    for i in range(n):
        value = int(input("Enter element: "))
        Data.append(value)
    return Data

def EvenList(Data):
    total = 0
    for x in Data:
        if x % 2 == 0:
            total += x
    print("Sum of even elements:", total)

def OddList(Data):
    total = 0
    for x in Data:
        if x % 2 != 0:
            total += x
    print("Sum of odd elements:", total)

def main():
    Data = AcceptList()

    t1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()