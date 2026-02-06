import os
from datetime import datetime

def GetLogFile():
    os.makedirs("Logs", exist_ok=True)
    return os.path.join("Logs", "Automation.log")

def Log(msg):
    logfile = GetLogFile()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as f:
        f.write(f"[{time}] {msg}\n")