# Addition of digits (Input: 5187934 → Output: 37)
import math

def CountDigits(No):
    No = abs(No)
    if No == 0:
        return 1
    return int(math.log10(No)) + 1

def SumDigits(No):
    No = abs(No)
    total = 0
    while No != 0:
        total = total + (No % 10)
        No = No // 10
    return total

def main():
    No = int(input("Enter number: "))

    digit_count = CountDigits(No)
    digit_sum = SumDigits(No)

    print("Count of digits is:", digit_count)
    print("Addition of digits is:", digit_sum)

if __name__ == "__main__":
    main()