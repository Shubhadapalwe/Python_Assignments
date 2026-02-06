# Delete duplicates + log + execution time
import sys, os, time
from MarvellousLogger import Log
from MarvellousUtils import IsValidDir, FileChecksum

def RemoveDuplicates(dirname):
    data = {}

    for file in os.listdir(dirname):
        path = os.path.join(dirname, file)
        if os.path.isfile(path):
            chk = FileChecksum(path)
            data.setdefault(chk, []).append(path)

    for k in data:
        for f in data[k][1:]:
            os.remove(f)
            Log(f"REMOVED: {f}")

def main():
    try:
        start = time.time()

        if len(sys.argv) != 2:
            Log("Usage: DirectoryDuplicateRemovalTime.py Demo")
            return

        folder = sys.argv[1]

        if not IsValidDir(folder):
            Log("Invalid directory")
            return

        Log("Timed duplicate removal started")
        RemoveDuplicates(folder)

        end = time.time()
        Log(f"Execution time: {end-start:.2f} seconds")

    except Exception as e:
        Log(str(e))

if __name__ == "__main__":
    main()