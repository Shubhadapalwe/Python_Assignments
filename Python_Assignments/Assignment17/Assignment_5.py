#Check prime or not (Return True/False)

def CheckPrime(No):
    if No <= 1:
        return False
    for i in range (2,No):
        if No % i == 0:
            return False
    return True


def main():
    No = int(input("Enter the number :"))
    if CheckPrime(No):
        print("It is prime Number :")
    else:
        print("it is not prime")

if __name__ =="__main__":
    main()