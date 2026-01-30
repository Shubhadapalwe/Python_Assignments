class Numbers:
    def __init__(self, no):
        self.Value = no

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, int(self.Value / 2) + 1):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors of", self.Value, "are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total

    def ChkPerfect(self):
        return self.SumFactors() == self.Value


def main():
    no1 = int(input("Enter number: "))
    obj1 = Numbers(no1)

    print("\nPrime Check:", obj1.ChkPrime())
    print("Perfect Check:", obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of Factors:", obj1.SumFactors())

    # Second object (multiple objects requirement)
    no2 = int(input("\nEnter another number: "))
    obj2 = Numbers(no2)

    print("\nPrime Check:", obj2.ChkPrime())
    print("Perfect Check:", obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of Factors:", obj2.SumFactors())


if __name__ == "__main__":
    main()