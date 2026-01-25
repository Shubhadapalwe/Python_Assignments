# Pattern (Triangle 1..i)
#    1
#    1 2
#    1 2 3
#    1 2 3 4
#    1 2 3 4 5

def TrianglePattern(No):
    lines = [ ]
    row = " "
    for i in range(1,No + 1):
        row = row + str(i) + " "
        lines.append(row)
    return lines

def main():
    No = int(input("Enter the number :"))
    result = TrianglePattern(No)
    for line in result:
        print(line)

if __name__ == "__main__":
        main()