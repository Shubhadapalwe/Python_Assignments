# Pattern (Input: 5)
def NumberPattern(No):
    lines = []
    for i in range(No):
        line = " "
        for j in range(1,No + 1):
            line += str(j) + " "
        lines.append(line)
    return lines


        
def main():
    No = int(input("enter the number for print pattern"))
    result = NumberPattern(No)
    for line in result:
        print(line)
  
if __name__ == "__main__":
    main()