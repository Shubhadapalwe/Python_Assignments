def CheckNumber(No):
    if No > 0:
        print("this is positive number:")
    elif No < 0:
        print("This is negative number ")
    else:
        print("This is Zero")

def main():
   No = int(input("Enter the number : "))
   CheckNumber(No)
if __name__ == "__main__":
    main()