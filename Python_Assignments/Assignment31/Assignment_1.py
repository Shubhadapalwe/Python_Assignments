# DirectoryFileSearch.py
#Display all files with given extension

import sys
import os
from MarvellousLogger import Log
from MarvellousUtils import NormalizeExt, IsValidDirectory, ListFilesWithExtension

def DirectoryFileSearch(dir_name: str, ext: str, log_file: str) -> int:
    ext = NormalizeExt(ext)

    if not IsValidDirectory(dir_name):
        Log(f"ERROR: Invalid directory: {dir_name}", log_file)
        return 1

    if not ext:
        Log("ERROR: Empty extension provided.", log_file)
        return 1

    Log(f"Searching files in '{dir_name}' with extension '{ext}'", log_file)

    count = 0
    for file_path in ListFilesWithExtension(dir_name, ext):
        Log(f"FOUND: {file_path}", log_file)
        count += 1

    Log(f"Search completed. Total matched files: {count}", log_file)
    return 0

def main():
    log_file = None
    try:
        # Usage: DirectoryFileSearch.py "Demo" ".txt"
        if len(sys.argv) != 3:
            from MarvellousLogger import GetLogFilePath
            log_file = GetLogFilePath()
            Log("ERROR: Invalid arguments.", log_file)
            Log('Usage: python3 DirectoryFileSearch.py "Demo" ".txt"', log_file)
            sys.exit(1)

        dir_name = sys.argv[1]
        ext = sys.argv[2]

        from MarvellousLogger import GetLogFilePath
        log_file = GetLogFilePath()
        Log("----- DirectoryFileSearch START -----", log_file)

        rc = DirectoryFileSearch(dir_name, ext, log_file)

        Log("----- DirectoryFileSearch END -----", log_file)
        sys.exit(rc)

    except Exception as e:
        if log_file is None:
            from MarvellousLogger import GetLogFilePath
            log_file = GetLogFilePath()
        Log(f"EXCEPTION: {e}", log_file)
        sys.exit(1)

if __name__ == "__main__":
    main()