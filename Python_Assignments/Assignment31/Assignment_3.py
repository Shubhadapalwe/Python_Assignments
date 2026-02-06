# Copy all files from dir1 → dir2 (create dir2)
# DirectoryCopy.py
import sys
import os
import shutil
from MarvellousLogger import Log, GetLogFilePath
from MarvellousUtils import IsValidDirectory, EnsureDirectory

def DirectoryCopy(src_dir: str, dest_dir: str, log_file: str) -> int:
    if not IsValidDirectory(src_dir):
        Log(f"ERROR: Source directory invalid: {src_dir}", log_file)
        return 1

    if not dest_dir:
        Log("ERROR: Destination directory name is empty.", log_file)
        return 1

    EnsureDirectory(dest_dir)
    Log(f"Copying all files from '{src_dir}' to '{dest_dir}'", log_file)

    copied = 0
    for entry in os.listdir(src_dir):
        src_path = os.path.join(src_dir, entry)
        if os.path.isfile(src_path):
            dst_path = os.path.join(dest_dir, entry)
            shutil.copy2(src_path, dst_path)
            Log(f"COPIED: {src_path} -> {dst_path}", log_file)
            copied += 1

    Log(f"Copy completed. Total files copied: {copied}", log_file)
    return 0

def main():
    log_file = GetLogFilePath()
    try:
        # Usage: DirectoryCopy.py "Demo" "Temp"
        if len(sys.argv) != 3:
            Log("ERROR: Invalid arguments.", log_file)
            Log('Usage: python3 DirectoryCopy.py "Demo" "Temp"', log_file)
            sys.exit(1)

        src_dir = sys.argv[1]
        dest_dir = sys.argv[2]

        Log("----- DirectoryCopy START -----", log_file)
        rc = DirectoryCopy(src_dir, dest_dir, log_file)
        Log("----- DirectoryCopy END -----", log_file)

        sys.exit(rc)

    except Exception as e:
        Log(f"EXCEPTION: {e}", log_file)
        sys.exit(1)

if __name__ == "__main__":
    main()