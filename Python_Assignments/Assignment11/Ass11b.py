def CountDigits(No):
    count = 0
    while No != 0:
        No = No // 10
        count = count + 1
    print("Count of digits is:", count)

No = int(input("Enter the number: "))
CountDigits(No)