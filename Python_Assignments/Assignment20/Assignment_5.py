import threading

def Display1to50():
    print("Thread1:")
    for i in range(1, 51):
        print(i, end=" ")
    print("\n")

def Display50to1():
    print("Thread2:")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("\n")

def main():
    t1 = threading.Thread(target=Display1to50, name="Thread1")
    t2 = threading.Thread(target=Display50to1, name="Thread2")

    t1.start()
    t1.join()     

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()