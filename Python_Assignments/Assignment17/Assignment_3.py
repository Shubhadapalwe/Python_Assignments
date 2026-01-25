def factorial(No):
    fact = 1
    for i in range (1,No + 1):
        fact = fact * i
    return fact

def main():
    No = int(input("Enter number : "))
    print("Factorial is : ",factorial(No))
if __name__ == "__main__":
    main()