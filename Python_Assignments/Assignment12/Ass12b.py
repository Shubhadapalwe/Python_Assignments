#Accept one number and print its factors
def print_factors(No):
    for i in range(1,No+1):
        if (No % i == 0):
            print(i)
No = int(input("Enter number: "))
print_factors(No)