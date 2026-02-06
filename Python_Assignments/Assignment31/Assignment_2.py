# DirectoryRename.py
#Rename all files from ext1 → ext2
import sys
import os
from MarvellousLogger import Log, GetLogFilePath
from MarvellousUtils import NormalizeExt, IsValidDirectory, ListFilesWithExtension

def DirectoryRename(dir_name: str, old_ext: str, new_ext: str, log_file: str) -> int:
    old_ext = NormalizeExt(old_ext)
    new_ext = NormalizeExt(new_ext)

    if not IsValidDirectory(dir_name):
        Log(f"ERROR: Invalid directory: {dir_name}", log_file)
        return 1

    if not old_ext or not new_ext:
        Log("ERROR: Extensions must not be empty.", log_file)
        return 1

    Log(f"Renaming files in '{dir_name}' from '{old_ext}' to '{new_ext}'", log_file)

    renamed = 0
    for src in ListFilesWithExtension(dir_name, old_ext):
        base = os.path.splitext(src)[0]
        dst = base + new_ext

        if os.path.exists(dst):
            Log(f"SKIP (target exists): {dst}", log_file)
            continue

        os.rename(src, dst)
        Log(f"RENAMED: {src} -> {dst}", log_file)
        renamed += 1

    Log(f"Rename completed. Total renamed files: {renamed}", log_file)
    return 0

def main():
    log_file = GetLogFilePath()
    try:
        # Usage: DirectoryRename.py "Demo" ".txt" ".doc"
        if len(sys.argv) != 4:
            Log("ERROR: Invalid arguments.", log_file)
            Log('Usage: python3 DirectoryRename.py "Demo" ".txt" ".doc"', log_file)
            sys.exit(1)

        dir_name = sys.argv[1]
        old_ext = sys.argv[2]
        new_ext = sys.argv[3]

        Log("----- DirectoryRename START -----", log_file)
        rc = DirectoryRename(dir_name, old_ext, new_ext, log_file)
        Log("----- DirectoryRename END -----", log_file)

        sys.exit(rc)

    except Exception as e:
        Log(f"EXCEPTION: {e}", log_file)
        sys.exit(1)

if __name__ == "__main__":
    main()