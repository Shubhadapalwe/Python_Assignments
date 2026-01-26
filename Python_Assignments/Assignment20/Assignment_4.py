import threading

def CountSmall(Str):
    count = 0
    for ch in Str:
        if ch.islower():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Small letters count:", count)
    print()

def CountCapital(Str):
    count = 0
    for ch in Str:
        if ch.isupper():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Capital letters count:", count)
    print()

def CountDigits(Str):
    count = 0
    for ch in Str:
        if ch.isdigit():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Digits count:", count)
    print()

def main():
    Str = input("Enter string: ")

    t1 = threading.Thread(target=CountSmall, args=(Str,), name="Small")
    t2 = threading.Thread(target=CountCapital, args=(Str,), name="Capital")
    t3 = threading.Thread(target=CountDigits, args=(Str,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()