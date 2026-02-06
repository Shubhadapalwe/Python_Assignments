#Find duplicate files (log only)
import sys, os
from MarvellousLogger import Log
from MarvellousUtils import IsValidDir, FileChecksum

def FindDuplicates(dirname):
    data = {}

    for file in os.listdir(dirname):
        path = os.path.join(dirname, file)
        if os.path.isfile(path):
            chk = FileChecksum(path)
            data.setdefault(chk, []).append(path)

    for k in data:
        if len(data[k]) > 1:
            for f in data[k]:
                Log(f"DUPLICATE: {f}")

def main():
    try:
        if len(sys.argv) != 2:
            Log("Usage: DirectoryDuplicate.py Demo")
            return

        folder = sys.argv[1]

        if not IsValidDir(folder):
            Log("Invalid directory")
            return

        Log("Duplicate scan started")
        FindDuplicates(folder)
        Log("Duplicate scan finished")

    except Exception as e:
        Log(str(e))

if __name__ == "__main__":
    main()