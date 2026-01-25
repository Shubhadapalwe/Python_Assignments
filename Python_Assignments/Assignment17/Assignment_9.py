# Count digits in number (Input: 5187934 -> Output: 7)
import math
def CountDigits(No):
    if No == 0:
        return 1
    return int(math.log10(No)) + 1

def main():
    No = int(input("Enter number :"))
    result = CountDigits(No)
    print("count of Digits is : ",result)

if __name__ == "__main__":
    main()