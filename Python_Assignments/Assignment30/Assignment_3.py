# Display File Line by Line
import os

def DisplayFile(fname):
    if not os.path.exists(fname):
        print("File not found")
        return

    f = open(fname, "r")

    for line in f:
        print(line, end="")

    f.close()

def main():
    filename = input("Enter file name: ")
    DisplayFile(filename)

if __name__ == "__main__":
    main()