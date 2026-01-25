def Pattern(No):
    lines = []
    for i in range (No):
        lines.append("* " * No)
    return lines
def main():
    No = int(input("Enter the number :"))
    result = Pattern(No)
    for line in result:
        print(line)
if __name__ == "__main__":
    main()