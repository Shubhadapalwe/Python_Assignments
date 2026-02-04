# Compare Two Files (Command Line)
import sys
import os

def CompareFiles(f1, f2):
    if not os.path.exists(f1) or not os.path.exists(f2):
        return False

    file1 = open(f1, "r")
    file2 = open(f2, "r")

    result = file1.read() == file2.read()

    file1.close()
    file2.close()

    return result

def main():
    if len(sys.argv) != 3:
        print("Usage: python Assignment_Q4.py file1 file2")
        return

    if CompareFiles(sys.argv[1], sys.argv[2]):
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()