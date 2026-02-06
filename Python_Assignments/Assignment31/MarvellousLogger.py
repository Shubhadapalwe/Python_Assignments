# MarvellousLogger.py
import os
from datetime import datetime

def GetLogFilePath(log_dir: str = "Logs", log_name: str = "Automation.log") -> str:
    os.makedirs(log_dir, exist_ok=True)
    return os.path.join(log_dir, log_name)

def Log(message: str, log_file: str = None) -> None:
    if log_file is None:
        log_file = GetLogFilePath()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}\n"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line)