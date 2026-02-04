# Search a Word in File
import os

def SearchWord(fname, word):
    if not os.path.exists(fname):
        return -1

    f = open(fname, "r")
    data = f.read()
    f.close()

    # check word presence
    if word in data:
        return True
    else:
        return False


def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    result = SearchWord(filename, word)

    if result == -1:
        print("File not found")
    elif result:
        print("Word found")
    else:
        print("Word not found")


if __name__ == "__main__":
    main()