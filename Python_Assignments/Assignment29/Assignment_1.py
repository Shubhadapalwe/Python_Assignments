# Check File Exists in Current Directory
import os

def CheckFileExists(fname):
    return os.path.exists(fname)

def main():
    name = input("Enter file name: ")

    if CheckFileExists(name):
        print("File exists")
    else:
        print("File does not exist")

if __name__ == "__main__":
    main()