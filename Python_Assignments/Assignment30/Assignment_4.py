# Copy File Contents
import os

def CopyFile(src, dest):
    if not os.path.exists(src):
        print("Source file not found")
        return

    f1 = open(src, "r")
    data = f1.read()
    f1.close()

    f2 = open(dest, "w")
    f2.write(data)
    f2.close()

    print("File copied successfully")

def main():
    src = input("Enter source file: ")
    dest = input("Enter destination file: ")

    CopyFile(src, dest)

if __name__ == "__main__":
    main()