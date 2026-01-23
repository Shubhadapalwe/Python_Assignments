def PrintStar(No):
    for i in range(No):
        print("*",end = " ")
def main():
    No = int(input("Enter the number of star you want :"))
    PrintStar(No)
if __name__ =="__main__":
    main()