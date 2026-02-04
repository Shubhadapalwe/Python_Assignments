# Count Words in File
import os

def CountWords(fname):
    if not os.path.exists(fname):
        return -1

    f = open(fname, "r")
    data = f.read()
    f.close()

    words = data.split()
    return len(words)

def main():
    filename = input("Enter file name: ")

    result = CountWords(filename)

    if result == -1:
        print("File not found")
    else:
        print("Total words:", result)

if __name__ == "__main__":
    main()