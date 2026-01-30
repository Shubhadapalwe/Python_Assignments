class BankAccount:
    ROI = 10.5   # class variable (Rate of Interest)

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Account Balance:", self.Amount)

    def Deposit(self, value):
        if value > 0:
            self.Amount += value

    def Withdraw(self, value):
        if value > 0 and value <= self.Amount:
            self.Amount -= value
        else:
            print("Insufficient balance / invalid amount.")

    def CalculateInterest(self):
        # Simple Interest for 1 year: (P * R) / 100
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    name = input("Enter account holder name: ")
    amount = float(input("Enter initial amount: "))

    acc1 = BankAccount(name, amount)

    print("\n--- Account Details ---")
    acc1.Display()

    dep = float(input("\nEnter amount to deposit: "))
    acc1.Deposit(dep)

    wd = float(input("Enter amount to withdraw: "))
    acc1.Withdraw(wd)

    print("\n--- Updated Account Details ---")
    acc1.Display()

    interest = acc1.CalculateInterest()
    print("Interest (1 year) at ROI", BankAccount.ROI, "% is:", interest)


if __name__ == "__main__":
    main()