#Two threads Even and Odd (first 10 numbers)
import threading
def DisplayEven():
    print("Even Thread :")
    for i in range(2,21,2):
        print(i, end =" ")
    print("\n")

def DisplayOdd():
    print("Odd Thread :")
    for i in range (1,20,2):
        print(i, end = " ")
    print("\n")

def main():
    t1 = threading.Thread(target=DisplayEven, name = "Even")
    t2 = threading.Thread(target=DisplayOdd, name = "odd")
 
    t1.start()
    t2.start()

    t1.join()
    t2.join()

print("Exit main: ")

if __name__ == "__main__":
    main()
