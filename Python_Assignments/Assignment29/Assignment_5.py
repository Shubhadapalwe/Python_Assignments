#Assignment29/Assignment_4.py
import os

def CountFrequency(fname, word):
    if not os.path.exists(fname):
        return -1

    f = open(fname, "r")
    data = f.read()
    f.close()

    return data.count(word)

def main():
    filename = input("Enter file name: ")
    string = input("Enter string to search: ")

    result = CountFrequency(filename, string)

    if result == -1:
        print("File not found")
    else:
        print("Frequency of", string, "is:", result)

if __name__ == "__main__":
    main()