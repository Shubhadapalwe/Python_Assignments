import shutil
import sys
import os
import time
import schedule
import hashlib
import zipfile

# -------------------- ADDED FEATURES (Logging / Email / History / Restore / Exclude) --------------------
import smtplib
from email.message import EmailMessage

DEFAULT_IGNORE_EXTS = {".tmp", ".log", ".exe"}
DEFAULT_IGNORE_DIRS = {"Logs", "__pycache__", ".git", "MarvellousBackup"}

def EnsureLogsFolder():
    os.makedirs("Logs", exist_ok=True)
    return "Logs"

def CreateLogFile():
    LogsDir = EnsureLogsFolder()
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    LogPath = os.path.join(LogsDir, f"MarvellousDataShield_{timestamp}.log")
    return LogPath

def LogWrite(LogPath, Msg):
    # log with timestamp
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LogPath, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {Msg}\n")

def ParseIgnoreExts(ignore_exts_str):
    # "tmp,log,exe" or ".tmp,.log"
    if not ignore_exts_str:
        return set(DEFAULT_IGNORE_EXTS)

    items = [x.strip() for x in ignore_exts_str.split(",") if x.strip()]
    exts = set()
    for it in items:
        if not it.startswith("."):
            it = "." + it
        exts.add(it.lower())
    return exts.union(DEFAULT_IGNORE_EXTS)

def ShouldIgnoreFile(filename, ignore_exts):
    _, ext = os.path.splitext(filename)
    return ext.lower() in ignore_exts

def SafeZipSize(zip_name):
    try:
        return os.path.getsize(zip_name)
    except:
        return 0

def AppendHistory(date_str, files_count, zip_name, zip_size_bytes):
    LogsDir = EnsureLogsFolder()
    HistoryPath = os.path.join(LogsDir, "BackupHistory.csv")
    header_needed = not os.path.exists(HistoryPath)

    with open(HistoryPath, "a", encoding="utf-8") as f:
        if header_needed:
            f.write("DateTime,FilesCopied,ZipFileName,ZipSizeBytes\n")
        f.write(f"{date_str},{files_count},{zip_name},{zip_size_bytes}\n")

def ShowHistory():
    LogsDir = EnsureLogsFolder()
    HistoryPath = os.path.join(LogsDir, "BackupHistory.csv")

    if not os.path.exists(HistoryPath):
        print("No history found yet. Run a backup first.")
        return

    print("\n------ Backup History ------")
    with open(HistoryPath, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
    print("----------------------------\n")

def SendEmailReport(SenderEmail, SenderAppPassword, ReceiverEmail, Subject, Body, Attachments):
    """
    Attachments: list of file paths
    Note: For Gmail use App Password (not normal password).
    """
    msg = EmailMessage()
    msg["From"] = SenderEmail
    msg["To"] = ReceiverEmail
    msg["Subject"] = Subject
    msg.set_content(Body)

    for path in Attachments:
        try:
            if path and os.path.exists(path):
                with open(path, "rb") as f:
                    data = f.read()
                filename = os.path.basename(path)
                msg.add_attachment(data, maintype="application", subtype="octet-stream", filename=filename)
        except Exception as e:
            # if attachment fails, continue
            pass

    # Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SenderEmail, SenderAppPassword)
        server.send_message(msg)

def RestoreBackup(zip_file, destination):
    os.makedirs(destination, exist_ok=True)
    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall(destination)

# ------------------------------------------------------------------------------------------------------


def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder+"_" +timestamp + ".zip"

    # open the zip file
    zobj = zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED) # ZIP_DEFLATED used for compres the file

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.realpath(full_path,folder)
            zobj.write(full_path,relative)

    zobj.close()

    return zip_name


    
def Caluclate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    fobj.close()
    return hobj.hexdigest()


def BackupFiles(Source,Destination, ignore_exts=None, ignore_dirs=None, LogPath=None):
    # ADDED: ignore_exts/ignore_dirs/logging but original behavior stays if None.
    copied_files = []
    if ignore_exts is None:
        ignore_exts = set(DEFAULT_IGNORE_EXTS)
    if ignore_dirs is None:
        ignore_dirs = set(DEFAULT_IGNORE_DIRS)

    print("Creating the backup folder for backup process")
    os.makedirs(Destination,exist_ok=True)  #jar tya navach folder asel tr baher nko yeus tyala use kr

    for root,dirs,files in os.walk(Source):
        # ADDED: skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            # ADDED: skip ignored file extensions
            if ShouldIgnoreFile(file, ignore_exts):
                continue

            src_path = os.path.join(root,file) # reletive path form the folder

            relative = os.path.realpath(src_path,Source)    #relative path generate karun dee
            dest_path = os.path.join(Destination,relative)    # marvellous -> Images

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)
            #copy the files if its new/updated
            try:
                if((not os.path.exists(dest_path)) or (Caluclate_hash(src_path) != Caluclate_hash(dest_path))):

                    shutil.copy2(src_path,dest_path)
                    copied_files.append(relative)

                    # ADDED: logging copied file
                    if LogPath:
                        LogWrite(LogPath, f"Copied: {relative}")

            except Exception as e:
                if LogPath:
                    LogWrite(LogPath, f"ERROR copying {relative}: {e}")

    return copied_files

    
def MarvellousDataShieldStart(Source = "Data", ReceiverEmail=None, SenderEmail=None, SenderPass=None, IgnoreExtsStr=None): # controller
    Border = "-"*50
    
    BackupName = "MarvellousBackup"

    # ADDED: Create log file for this run
    LogPath = CreateLogFile()
    LogWrite(LogPath, Border)
    LogWrite(LogPath, f"Backup Process Started successfully at: {time.ctime()}")
    LogWrite(LogPath, f"Source Directory: {Source}")
    LogWrite(LogPath, f"Backup Directory: {BackupName}")

    # ADDED: exclusions
    ignore_exts = ParseIgnoreExts(IgnoreExtsStr)
    ignore_dirs = set(DEFAULT_IGNORE_DIRS)
    LogWrite(LogPath, f"Ignoring extensions: {sorted(list(ignore_exts))}")
    LogWrite(LogPath, f"Ignoring directories: {sorted(list(ignore_dirs))}")
    LogWrite(LogPath, Border)

    print(Border)
    print("Backup Process Started succesfully at :",time.ctime())
    print(Border)

    # ADDED: validations
    if not os.path.exists(Source):
        msg = f"ERROR: Source directory not found: {Source}"
        print(msg)
        LogWrite(LogPath, msg)
        return

    try:
        files = BackupFiles(Source,BackupName, ignore_exts=ignore_exts, ignore_dirs=ignore_dirs, LogPath=LogPath)
    except Exception as e:
        LogWrite(LogPath, f"ERROR during BackupFiles: {e}")
        return

    zip_file = ""
    try:
        zip_file = make_zip(BackupName)
    except Exception as e:
        LogWrite(LogPath, f"ERROR creating zip: {e}")

    print(Border)
    print("Backup completed succesfully")
    print("Files copied : ",len(files))
    print("Zip file gets created : ",zip_file)
    print(Border)

    # ADDED: log summary
    LogWrite(LogPath, Border)
    LogWrite(LogPath, "Backup completed successfully")
    LogWrite(LogPath, f"Files copied: {len(files)}")
    LogWrite(LogPath, f"Zip file name: {zip_file}")
    LogWrite(LogPath, Border)

    # ADDED: history
    dt = time.strftime("%Y-%m-%d %H:%M:%S")
    zip_size = SafeZipSize(zip_file)
    AppendHistory(dt, len(files), zip_file, zip_size)
    LogWrite(LogPath, f"History updated: {dt}, files={len(files)}, zip_size_bytes={zip_size}")

    # ADDED: email notification (optional)
    if ReceiverEmail and SenderEmail and SenderPass:
        try:
            subject = "Marvellous Data Shield - Backup Completed"
            body = (
                f"Backup Completed at: {dt}\n"
                f"Source: {Source}\n"
                f"Files Copied: {len(files)}\n"
                f"Zip: {zip_file} ({zip_size} bytes)\n"
                f"\nAttached: log file + zip file."
            )
            SendEmailReport(SenderEmail, SenderPass, ReceiverEmail, subject, body, [LogPath, zip_file])
            LogWrite(LogPath, f"Email sent to {ReceiverEmail}")
        except Exception as e:
            LogWrite(LogPath, f"ERROR sending email: {e}")


def main():

    Border = "-"*50
    print(Border)
    print("---- Marvellous Data sheild System -----")
    print(Border)

    # ------------------- ADDED: restore + history commands -------------------
    # Restore usage:
    # python Script.py --restore BackupZip.zip DestinationFolder
    if(len(sys.argv) >= 2):
        if(sys.argv[1] == "--restore"):
            if len(sys.argv) != 4:
                print("Usage: python Script.py --restore ZipFileName DestinationFolder")
                return
            zip_file = sys.argv[2]
            dest = sys.argv[3]
            if not os.path.exists(zip_file):
                print("Zip file not found:", zip_file)
                return
            RestoreBackup(zip_file, dest)
            print("Restore completed into:", dest)
            return

        if(sys.argv[1] == "--history"):
            ShowHistory()
            return
    # -----------------------------------------------------------------------

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This scipt is used to : ")
            print("1: takes auto backup at given time")
            print("2: Backup only new and updated files")
            print("3: Create an archive of the backup periodically")
            print("4: Maintain log file in Logs/ folder")
            print("5: Exclude file extensions (default: .tmp,.log,.exe)")
            print("6: Restore from zip (--restore)")
            print("7: Show backup history (--history)")
            print("\nOptional email mode:")
            print("python Script.py <IntervalMin> <SourceDir> <ReceiverEmail> <SenderEmail> <SenderAppPassword> [IgnoreExtsCSV]")
            print("Example IgnoreExtsCSV: tmp,log,exe,pdf")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory: Name of directory to backed up")
            print("\nWith email:")
            print("ScriptName.py TimeInterval SourceDirectory ReceiverEmail SenderEmail SenderAppPassword [IgnoreExtsCSV]")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    
    # python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])
        print(Border)

        print("Data Sheild System started succesfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    # ADDED: email + ignore exts mode (optional)
    # python Script.py 10 Data receiver@gmail.com sender@gmail.com appPassword tmp,log,exe
    elif(len(sys.argv) >= 6):
        interval = int(sys.argv[1])
        source = sys.argv[2]
        receiver = sys.argv[3]
        sender = sys.argv[4]
        sender_pass = sys.argv[5]
        ignore_exts = sys.argv[6] if len(sys.argv) >= 7 else None

        schedule.every(interval).minutes.do(
            MarvellousDataShieldStart,
            source,
            receiver,
            sender,
            sender_pass,
            ignore_exts
        )

        print(Border)
        print("Data Shield System started successfully (Email mode)")
        print("Interval (minutes):", interval)
        print("Source:", source)
        print("Receiver:", receiver)
        print("Press Ctrl + C to stop the execution")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 

    print(Border)
    print("--------- Thank you for using our script ---------")
    print(Border)
    
if __name__ == "__main__":
    main()