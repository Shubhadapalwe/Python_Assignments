def ReverseNumber(No):
    rev = 0
    while No != 0:
        digit = No % 10
        rev = (rev * 10) + digit
        No = No // 10
    print("Reverse number is:", rev)

No = int(input("Enter the number: "))
ReverseNumber(No)