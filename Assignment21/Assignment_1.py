import threading

def IsPrime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def Prime(Data):
    print("Prime numbers are:")
    for x in Data:
        if IsPrime(x):
            print(x, end=" ")
    print("\n")

def NonPrime(Data):
    print("Non-Prime numbers are:")
    for x in Data:
        if not IsPrime(x):
            print(x, end=" ")
    print("\n")

def AcceptList():
    n = int(input("Enter number of elements: "))
    Data = []
    for i in range(n):
        value = int(input("Enter element: "))
        Data.append(value)
    return Data

def main():
    Data = AcceptList()

    t1 = threading.Thread(target=Prime, args=(Data,), name="Prime")
    t2 = threading.Thread(target=NonPrime, args=(Data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()