# Copy File (Command Line)
import sys
import os

def CopyFile(src, dest):
    if os.path.exists(src):
        f1 = open(src, "r")
        f2 = open(dest, "w")

        f2.write(f1.read())

        f1.close()
        f2.close()
        print("File copied successfully")
    else:
        print("Source file not found")

def main():
    if len(sys.argv) != 2:
        print("Usage: python Assignment_Q3.py filename")
        return

    CopyFile(sys.argv[1], "Demo.txt")

if __name__ == "__main__":
    main()