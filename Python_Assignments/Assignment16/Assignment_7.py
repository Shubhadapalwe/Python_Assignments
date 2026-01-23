def DivisibleBy5(No):
    if No % 5 ==0:
        return True
    else:
        return False
def main():
    No = int(input("Enter the number :"))
    print(DivisibleBy5(No))
   
if __name__ == "__main__":
    main()