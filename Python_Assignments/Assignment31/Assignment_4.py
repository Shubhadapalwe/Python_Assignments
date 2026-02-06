#Copy only files with given extension from dir1 → dir2
# DirectoryCopyExt.py
import sys
import os
import shutil
from MarvellousLogger import Log, GetLogFilePath
from MarvellousUtils import NormalizeExt, IsValidDirectory, EnsureDirectory, ListFilesWithExtension

def DirectoryCopyExt(src_dir: str, dest_dir: str, ext: str, log_file: str) -> int:
    ext = NormalizeExt(ext)

    if not IsValidDirectory(src_dir):
        Log(f"ERROR: Source directory invalid: {src_dir}", log_file)
        return 1

    if not dest_dir:
        Log("ERROR: Destination directory name is empty.", log_file)
        return 1

    if not ext:
        Log("ERROR: Extension is empty.", log_file)
        return 1

    EnsureDirectory(dest_dir)
    Log(f"Copying '{ext}' files from '{src_dir}' to '{dest_dir}'", log_file)

    copied = 0
    for src_path in ListFilesWithExtension(src_dir, ext):
        filename = os.path.basename(src_path)
        dst_path = os.path.join(dest_dir, filename)
        shutil.copy2(src_path, dst_path)
        Log(f"COPIED: {src_path} -> {dst_path}", log_file)
        copied += 1

    Log(f"CopyExt completed. Total files copied: {copied}", log_file)
    return 0

def main():
    log_file = GetLogFilePath()
    try:
        # Usage: DirectoryCopyExt.py "Demo" "Temp" ".exe"
        if len(sys.argv) != 4:
            Log("ERROR: Invalid arguments.", log_file)
            Log('Usage: python3 DirectoryCopyExt.py "Demo" "Temp" ".exe"', log_file)
            sys.exit(1)

        src_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        ext = sys.argv[3]

        Log("----- DirectoryCopyExt START -----", log_file)
        rc = DirectoryCopyExt(src_dir, dest_dir, ext, log_file)
        Log("----- DirectoryCopyExt END -----", log_file)

        sys.exit(rc)

    except Exception as e:
        Log(f"EXCEPTION: {e}", log_file)
        sys.exit(1)

if __name__ == "__main__":
    main()