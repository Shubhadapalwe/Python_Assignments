class Circle:
    PI = 3.14     

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius:", self.Radius)
        print("Area:", self.Area)
        print("Circumference:", self.Circumference)


def main():
    Obj = Circle()

    Obj.Accept()
    Obj.CalculateArea()
    Obj.CalculateCircumference()
    Obj.Display()


if __name__ == "__main__":
    main()