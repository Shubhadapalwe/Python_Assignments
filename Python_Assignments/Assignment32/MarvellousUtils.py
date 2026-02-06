import os
import hashlib

def IsValidDir(path):
    return os.path.exists(path) and os.path.isdir(path)

def FileChecksum(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            h.update(data)
    return h.hexdigest()