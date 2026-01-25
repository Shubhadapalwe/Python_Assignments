# Lambda: Power of two (square)
# Input: 4 → 16, 6 -> 64

Power = lambda No: 2 ** No

def main():
    No = int(input("enter the number :"))
    print("Output ",Power(No))

if __name__ == "__main__":
    main()