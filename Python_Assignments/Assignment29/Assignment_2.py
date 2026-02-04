#Display File Contents
import os

def DisplayFile(fname):
    if os.path.exists(fname):
        f = open(fname, "r")
        print(f.read())
        f.close()
    else:
        print("File not found")

def main():
    name = input("Enter file name: ")
    DisplayFile(name)

if __name__ == "__main__":
    main()