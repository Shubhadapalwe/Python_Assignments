# Pattern (Input: 5)
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

def Pattern(No):
    lines = []
    for i in range(No,0,-1):
        lines.append("* " * i)
    return lines
def main():
    No = int(input("ENter the count: "))
    result = Pattern(No)
    for line in result:
        print(line)

if __name__ == "__main__":
    main()