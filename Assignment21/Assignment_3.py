import threading

counter = 0
lock = threading.Lock()

def Increase():
    global counter
    for i in range(100000):
        lock.acquire()
        counter += 1
        lock.release()

def main():
    t1 = threading.Thread(target=Increase)
    t2 = threading.Thread(target=Increase)
    t3 = threading.Thread(target=Increase)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final value of counter is:", counter)

if __name__ == "__main__":
    main()