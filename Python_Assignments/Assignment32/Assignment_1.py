#Display checksum of all files
import sys, os
from MarvellousLogger import Log
from MarvellousUtils import IsValidDir, FileChecksum

def DirectoryChecksum(dirname):
    for file in os.listdir(dirname):
        path = os.path.join(dirname, file)
        if os.path.isfile(path):
            checksum = FileChecksum(path)
            Log(f"{file} : {checksum}")

def main():
    try:
        if len(sys.argv) != 2:
            Log("Usage: DirectoryChecksum.py Demo")
            return

        folder = sys.argv[1]

        if not IsValidDir(folder):
            Log("Invalid directory")
            return

        Log("Checksum started")
        DirectoryChecksum(folder)
        Log("Checksum finished")

    except Exception as e:
        Log(str(e))

if __name__ == "__main__":
    main()