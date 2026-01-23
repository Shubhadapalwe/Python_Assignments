def Add(No1,No2):
    return No1 + No2

def main():
    Num1 = int(input("Enter the 1st number :"))
    Num2 = int(input("Enter the 1st number :"))

    Ans = Add(Num1,Num2)
    print("The Addition is :",Ans)

if __name__ == "__main__":
    main()