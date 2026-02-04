#  Count Lines in File
import os

def CountLines(fname):
    if not os.path.exists(fname):
        return -1

    f = open(fname, "r")
    lines = f.readlines()
    f.close()

    return len(lines)

def main():
    filename = input("Enter file name: ")

    result = CountLines(filename)

    if result == -1:
        print("File not found")
    else:
        print("Total lines:", result)

if __name__ == "__main__":
    main()